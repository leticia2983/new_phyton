# Linux
sudo apt-get install python3-venv  # If needed
python3 -m venv .env
source .env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r ./requirements.txt
export set FLASK_APP=hello_app.webapp
python3 -m flask run
first=input("First: ")
second=input("second: ")
sum=float(first)+float(second)
print("sum: " int(sum))
