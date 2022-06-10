
def get_weather_desc_and_temp():
    import requests
    api_key = '468de70ed6f17c023ae55a130b264827'
    city = 'Orlando'
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    requests = requests.get(url)
    json = requests.json()

    description = json.get('weather')[0].get('description')
    temp_min = json.get('main').get('temp_min')
    temp_max = json.get('main').get('temp_min')
    
    return {'description':description,
            'temp_min':temp_min,
            'temp_max':temp_max}

def main():
    #print requests
    weather_dict = get_weather_desc_and_temp()
    print('today forecast is', weather_dict.get('description'))
    print('the minimum temperature is', weather_dict.get('temp_min'))
    print('the maximum temperature is', weather_dict.get('temp_max'))

main()