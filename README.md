# kh-deepstackai
Use DeepStackAI to analyze IP Camera photos
Installation after docker is setup and runnning
```
docker pull deepquestai/deepstack
```

```

docker run -e VISION-DETECTION=True -v localstorage:/datastore -p 81:5000 deepquestai/deepstack
```