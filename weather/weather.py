import requests

API_KEY = "d633fd7283df78d430f2cde1c71b2b7c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}

city = input("enter a city name: ")
# country_code = input("enter a country code")

# request_url = f"https://jsonplaceholder.typicode.com/posts"
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"



response = requests.get(request_url)

# print(response.status_code)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data['weather'][0]["description"]
    print(f"weather : {weather}")
    temperature = data["main"]["temp"] -273.15
    print(f" Temperature { round(temperature)} C ")
else:
    print("an errror occurred")
