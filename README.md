# kh-deepstackai
Use DeepStackAI to analyze IP Camera photos
Installation after docker is setup and runnning
```
docker pull deepquestai/deepstack
```

```

docker run -e VISION-DETECTION=True -v localstorage:/datastore -p 81:5000 deepquestai/deepstack
```

### Download from Git
```
git clone https://github.com/Palt0n/kh-deepstackai.git
```

### Setup python virtual environment with venv
Create python virtual enviroment with venv
```
python -m venv env
```
To activate venv
```
source env/Scripts/activate
python -m pip install --upgrade pip
pip install requests
pip install pillow
```

