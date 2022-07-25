to get up and running you need to do the following commands.

sudo apt install -y python3 pip

pip install -r requirements.txt

python3 -m uvicorn main:app

application is run on localhost port 8000

example get requires 127.0.0.0:8000/healthz
