python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt  --break-system-packages

echo "venv/
.env" > .gitignore

pip freeze


echo "DB_HOST="127.0.0.1"
DB_USER="root"
DB_PASSWORD=""
DB_NAME="data3g"
DB_PORT=3306 # Para MySQL o 5432 para PostgreSQL

TOKEN_API_PERU="ebbc6eec08842f507333ea397050e4760f3826e57d6ffb322a21d37269dab885" 
"> .env 