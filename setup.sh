# Requirements Install File
# chmod 775 the setup.sh file 
# run   sudo ./setup.sh

python3 -m venv capstone_venv       #sets up virtual enviornment
source capstone_venv/bin/active
pip install -r requirements.txt
python main.py
