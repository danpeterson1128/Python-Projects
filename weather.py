import pip._vendor.requests


def get_weather_desc_and_temp():
    api_key = "67da29cb91129f1a68c1c06c1be92daa"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    request = pip._vendor.requests.get(url)
    json = request.json()
    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description':description,
             'temp_min':temp_min,
             'temp_max':temp_max}

def main():
    weather_dict = get_weather_desc_and_temp()
    #print the results
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum tempterature is", weather_dict.get('temp_max'))

main()
