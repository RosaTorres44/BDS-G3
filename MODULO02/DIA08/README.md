python3 -m venv venv

source venv/bin/activate

echo ".gitignore" > .gitignore

pip3 install -r requirements.txt  --break-system-packages

pip3 freeze


