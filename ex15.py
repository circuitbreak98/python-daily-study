def get_rainfall1():
    d = {}
    while- True:
        city = input().strip()
        if not city:
            break
        rainfall = int(input())
        if city in d: 
            d[city] += rainfall
        else:
            d[city] = rainfall
    
    for k,v in d.items():
        print(f'{k:10}: {v:5}')

def get_rainfall():
    rainfall = {}
    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break
        
        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

        for city, rain in rainfall.items():
            print(f'{city}: {rain}')

get_rainfall()