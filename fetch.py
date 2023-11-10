import requests

url = "https://e-amrit.niti.gov.in//getChargingStation"

response = requests.get(url, verify=False)

if response.status_code == 200:
    print(response.content)
    with open("data.json", "wb") as f:
        f.write(response.content)
else:
    print("Error fetching data")
    print(response.status_code)
    print(response.content)
    exit(1)
