# Colorize for clarity.

SY='\033[0;33m' # Start yellow.
EY='\033[0m' # End yellow. 
SR='\033[0;31m' # Start red.
ER='\033[0m' # End red. 
SG='\033[0;32m' # Start green.
EG='\033[0m' # End green. 
SC='\033[0;36m' # Start cyan.
EC='\033[0m' # End cyan. 
# Export development environment database configs.

source ./creds/local_dev.sh
source ./creds/gcloud.sh

python3 manage.py runserver
