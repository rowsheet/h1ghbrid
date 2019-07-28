#-------------------------------------------------------------------------------
# Before running, you will need to export the DB credentials
# for the production DB in order to migrate it to your local
# development instance.

# export PROD_DB_HOST=<HOST>
# export PROD_DB_NAME=<NAME>
# export PROD_DB_USER=<USER>
# export PROD_DB_PORT=<PORT>
# export PROD_DB_PASS=<PASS>
#-------------------------------------------------------------------------------

# Key variable vals.

sql_dump_file=remote_dump.sql
sql_dump_min_size=1000

# Colorize for clarity.

SY='\033[0;33m' # Start yellow.
EY='\033[0m' # End yellow. 
SR='\033[0;31m' # Start red.
ER='\033[0m' # End red. 
SG='\033[0;32m' # Start green.
EG='\033[0m' # End green. 
SC='\033[0;36m' # Start cyan.
EC='\033[0m' # End cyan. 

# source the prod DB creds for this project. 
source creds/heroku_prod.sh

# Make sure all necessary variables are set.

if [ -z "$PROD_DB_HOST" ] || [ -z "$PROD_DB_NAME" ] || [ -z "$PROD_DB_USER" ] || [ -z "$PROD_DB_PORT" ] || [ -z "$PROD_DB_PASS" ]; then
	echo "\n${SR}Error:${ER} ${SC}Unable to import. Dtabase, credentials unset. See begining of this file.\n${EC}"
	echo "${SR}Aborting...\n${ER}"
 	exit 1
fi

# Dump old database.

echo "${SY}\nDumping remote database...\n${EY}"
PGPASSWORD="$PROD_DB_PASS" \
	pg_dump \
	--host=$PROD_DB_HOST \
	--port=$PROD_DB_PORT \
	--username=$PROD_DB_USER \
	--dbname=$PROD_DB_NAME \
	> $sql_dump_file

# Make sure SQL dump is legit.

actualsize=$(wc -c <"$sql_dump_file")
if ! [ $actualsize -ge $sql_dump_min_size ]; then
	echo "\n${SR}Error:${ER} ${SC}SQL Dump is too small (>$sql_dump_min_size bytes). Likeley incorrect bad sql dump and/or bad DB credentials.${EC}"
	echo "${SR}Aborting...\n${ER}"
 	exit 1
fi

# Fix the pg_owner from remote to work locally (owned by postgres).

echo "${SY}\nFixing pg_owners for local data...\n${EY}"
sed "s/$PROD_DB_USER/postgres/g" $sql_dump_file> temp.sql
mv temp.sql $sql_dump_file 

# Drop old database in case there's any stale data/schema.

echo "${SY}\nDropping old local database...\n${EY}"
psql -c "DROP DATABASE local_dev;" 
if (psql -lqt | cut -d \| -f 1 | grep -qw local_dev)
then
	echo "\n${SR}Error:${ER} ${SC} Unable to drop old local_dev database. Likeley being used by something right now.${EC}"
	echo "${SR}Aborting...\n${ER}"
 	exit 1
fi

# Create new database.

echo "${SY}\nCreating new local database...\n${EY}"
psql -c "CREATE DATABASE local_dev TEMPLATE template0;"
if (psql -lqt | cut -d \| -f 1 | grep -qw local_dev)
then
	echo "\n${SC}New database created successfully.${EC}"
else
	echo "\n${SR}Error:${ER} ${SC} Unable to create new local_dev database.${EC}"
	echo "${SR}Aborting...\n${ER}"
 	exit 1
fi

# Import new data. 

echo "${SY}\nImporting remove database data to local...\n${EY}"
psql local_dev < $sql_dump_file 

# Run local.

sh dev.sh
