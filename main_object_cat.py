import requests
from PIL import Image
import os

ip_addr = os.environ.get("SERVER_IP", "localhost")

print("$SERVER_IP={}".format(ip_addr))
list_filepaths_cat = []
for file in os.listdir(r"photos\cat"):
    filepath = os.path.join(r"photos\cat", file)
    # print(filepath)
    list_filepaths_cat.append(filepath)

if not os.path.isdir("results"):
    os.mkdir("results")

i = 0
for filepath in list_filepaths_cat:
    image_data = open(filepath,"rb").read()
    response = requests.post(
        "http://{}:81/v1/vision/detection".format(ip_addr),
        files={"image":image_data},
        data={"min_confidence":0.50}
    )
    data_json = response.json()
    print(filepath)
    if len(data_json["predictions"]) > 0:
        print(data_json)
        for obj in data_json["predictions"]:
            label = obj["label"]
            y_max = int(obj["y_max"])
            y_min = int(obj["y_min"])
            x_max = int(obj["x_max"])
            x_min = int(obj["x_min"])
            image = Image.open(filepath).convert("RGB")
            cropped = image.crop((x_min,y_min,x_max,y_max))
            cropped.save(r"results\image{}_{}.jpg".format(i,label))
            i += 1