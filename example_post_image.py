import requests

image_data = open("image.jpg","rb").read()

response = requests.post("http://localhost:81/v1/vision/scene",
files={"image":image_data}).json()
print(response)