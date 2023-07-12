import requests

base_url = "https://backpack.tf/api/classifieds/listings/snapshot"

api = "6484bdc2d83b49227d01d093"
token = "9sUT4ydeVfMUKCj7C0Q/TgYIJLN6xgFh/nyJym4GxNE="
appid = "440"
sku = "Strange Exorcizor"

urlF = base_url + "?token=" + token + "&api" + api + "&appid=440&sku=" + sku

response = requests.get(urlF)

if response.status_code == 200:
    for i in response.json()["listings"]:
        if i["intent"] == "sell":
            continue
        print(i["details"])
        #print(i["intent"], " ", i["currencies"])
else:
    print("Error:", response.status_code)
