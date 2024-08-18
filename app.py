import requests

# API key from wheaterapi.com
api_key = '6e29be1d755049f2b5e103506241808'

# City name input for making request to the API
user_input = input('Enter city: ')

# Requesting .json format data
weather_data = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}&aqi=no")

# Implementing some variables
location = ''
weather = ''

# Error handling: Is it a valid location ?

# Boolean variable to keep eye on location status
is_valid = False

# If the request status code is 404 print error message
if weather_data.status_code == '404':
    print('No city found.')

# if location is valid we collect the data from .json
elif weather_data.status_code == '200':
    # Changing boolean value to true
    is_valid = True

    # Collecting country name, region and city name of searched location
    # Then store them into single variable
    country = weather_data.json()['location']['country']
    region = weather_data.json()['location']['region']
    city = weather_data.json()['location']['name']

    location = f"Location: {city}, {region}, {country}"

    # Collecting weather data for the location
    last_updated = weather_data.json()['current']['last_updated']
    temp = round(weather_data.json()['current']['temp_c'])
    feels_like = round(weather_data.json()['current']['feelslike_c'])
    wind_speed = round(weather_data.json()['current']['wind_kph'])
    gusts_speed = round(weather_data.json()['current']['gust_kph'])
    wind_degree = weather_data.json()['current']['wind_degree']
    wind_direction = weather_data.json()['current']['wind_dir']
    pressure = round(weather_data.json()['current']['pressure_mb'])
    humidity = weather_data.json()['current']['humidity']
    cloud = weather_data.json()['current']['cloud']
    dew_point = round(weather_data.json()['current']['dewpoint_c'])
    visibility = round(weather_data.json()['current']['vis_km'])
    uv_index = round(weather_data.json()['current']['uv'])

    # Converting collected variables into single variable
    weather = f"Last updated: {last_updated}\n" \
                           f"Temperature: {temp} °C\n" \
                           f"Feels like: {feels_like} °C\n" \
                           f"Wind speed: {wind_speed} km/h\n" \
                           f"Gusts speed: {gusts_speed} km/h\n" \
                           f"Wind direction: {wind_direction}\n" \
                           f"Wind degree: {wind_degree}\n" \
                           f"Pressure: {pressure} hPa\n" \
                           f"Humidity {humidity} %\n" \
                           f"Cloud: {cloud} %\n" \
                           f"Dew point: {dew_point} °C\n" \
                           f"Visibility: {visibility} km\n" \
                           f"UV Index: {uv_index}"

# If location is valid
# The software prints out Location and Weather information
if is_valid:
    print(location)
    print()
    print(weather)

print(weather_data.json())