#-------------------------------------------------------------------------------
# You need all of the database credentials to run for production.
#
# export DB_HOST=<HOST>
# export DB_NAME=<NAME>
# export DB_USER=<USER>
# export DB_PORT=<PORT>
# export DB_PASS=<PASS>
#
# Production also requires the SECRET_KEY.
#
# export SECRET_KEY=<SECRET_KEY>
#-------------------------------------------------------------------------------

# Colorize for clarity.

SY='\033[0;33m' # Start yellow.
EY='\033[0m' # End yellow. 
SR='\033[0;31m' # Start red.
ER='\033[0m' # End red. 
SG='\033[0;32m' # Start green.
EG='\033[0m' # End green. 
SC='\033[0;36m' # Start cyan.
EC='\033[0m' # End cyan. 

#-------------------------------------------------------------------------------
# Export Heroku Production DB config and Django app SECRET_KEY.
#-------------------------------------------------------------------------------

# Source the production credentials file.

source ./creds/heroku_prod.sh

# Make sure all necessary variables are set.

if [ -z "$PROD_DB_HOST" ] || [ -z "$PROD_DB_NAME" ] || [ -z "$PROD_DB_USER" ] || [ -z "$PROD_DB_PORT" ] || [ -z "$PROD_DB_PASS" ] || [ -z "$PROD_DATABASE_URL" ]; then
	echo "\n${SR}Error:${ER} ${SC}Production DB credentials are required to deploy to production.\n${EC}"
	echo "${SR}Aborting...\n${ER}"
 	exit 1
fi

# Make sure SECRET_KEY variabble set.

if [ -z "$PROD_SECRET_KEY" ]; then
	echo "\n${SR}Error:${ER} ${SC}Production SECRET_KEY is required to deploy to production.\n${EC}"
	echo "${SR}Aborting...\n${ER}"
 	exit 1
fi

# Export development environment database configs.

echo "${SY}\nSetting production DATABASE_URL environment variable.\n${EY}"
heroku config:set DATABASE_URL=$PROD_DATABASE_URL

# Export SECRET_KEY environment variable for production.

echo "${SY}\nSetting production SECRET_KEY deployment environment variable.\n${EY}"
heroku config:set SECRET_KEY=$PROD_SECRET_KEY

#-------------------------------------------------------------------------------
# Export Production Google Cloud credentials for GCS bucket storage.
#-------------------------------------------------------------------------------

# Source the Google Cloud Storage credentials file.

source ./creds/gcloud.sh

# Make sure Google Cloud variabble set.

if [ -z "$GCLOUD_BUCKET" ] || [ -z "$GCLOUD_PROJECT" ] || [ -z "$GCLOUD_CLIENT_ID" ] || [ -z "$GCLOUD_CLIENT_EMAIL" ] || [ -z "$GCLOUD_PK_ID" ] || [ -z "$GCLOUD_PK" ]; then
	echo "\n${SR}Error:${ER} ${SC}Google Cloud credentials are required to deploy to production.\n${EC}"
	echo "${SR}Aborting...\n${ER}"
 	exit 1
fi

# Export Google Cloud Storage environment variable for Heroku production.

echo "${SY}\nSetting production Google Cloud Storage deployment environment variable.\n${EY}"
heroku config:set GCLOUD_BUCKET=$GCLOUD_BUCKET
heroku config:set GCLOUD_PROJECT=$GCLOUD_PROJECT
heroku config:set GCLOUD_CLIENT_ID=$GCLOUD_CLIENT_ID
heroku config:set GCLOUD_CLIENT_EMAIL=$GCLOUD_CLIENT_EMAIL
heroku config:set GCLOUD_PK_ID=$GCLOUD_PK_ID
heroku config:set GCLOUD_PK_B64=$GCLOUD_PK_B64

#-------------------------------------------------------------------------------
# Export ENV variable for Heroku as "production".
#-------------------------------------------------------------------------------

# Export development environment general config.

echo "${SY}\nSetting production ENV deployment environment variable.\n${EY}"
heroku config:set ENV=production

#-------------------------------------------------------------------------------
# Run production.
#-------------------------------------------------------------------------------


echo "${SC}\nNotice: This does not make any migrations or push changes you may have.\n${EC}"
heroku open
