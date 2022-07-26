to get up and running you need to do the following commands.

Running without docker:
    sudo apt install -y python3 pip
    pip install -r requirements.txt
    python3 -m uvicorn main:app
    application is run on localhost port 8000
    example get requires 127.0.0.0:8000/healthz

Running in docker
    sudo apt install -y docker
    docker build -t sam:latest .
    docker run -d -p 8000:8000 sam:latest
    example get requires 127.0.0.0:8000/healthz

Get testing metrics (run commands from project root):
    pip install -r requirements.txt
    coverage run --source ./ -m pytest
    coverage report