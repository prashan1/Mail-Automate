import requests, json, os
from django.conf import settings
from django.core.mail import send_mail


class SendingClass:
    # Creating instance variable for every receiver ends.
    def __init__(self,recipient_name,recipient_email, recipient_city ):
        self.recipient_name = recipient_name
        self.recipient_email = recipient_email
        self.recipient_city = recipient_city

    # It is used for fetching information about weather using openweathermap api
    def get_weather_api(self):
        api_key = os.environ.get('WEATHER_API_KEY')
        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name
        city_name = self.recipient_city

        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # "404", means city is found otherwise,
        # city is not found

        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            return [ y['temp'] , str(weather_description) ]

        else:
            return [None,None]



    # Logic for building relevant emoji w.r.t weather of a city
    def relevant_emoji(self,weather_description):

        # Dictionary of possible weather as keys and their emojis as value
        weather_emoji ={"fog":'\U0001F32B', "mist":'\U0001F32B' , "haze":'\U0001F32B','wind':'\U0001F32A','rain':'\U0001F328','clouds':'\U0001F327'}

        for emoji in weather_emoji:

            # if relevant weather is found in our dictionary, return corresponding emoji
            if len(weather_description) <= len(emoji) and weather_description in emoji or len(weather_description) > len(emoji) and emoji in weather_description : 
                return weather_emoji[emoji]
        return weather_emoji["mist"]
        

    # Using django's inbuilt module for sending email
    def sendEmail(self):

        # fetching temperate and weather info using get_weather_api method
        city_temperature , weather_description = self.get_weather_api()

        # fetching relevant emoji w.r.t a weather
        emoji = self.relevant_emoji(weather_description)

        # Building our email 
        subject = f'Hi {self.recipient_name}, interested in our services' 
        body = f'Temperature in {self.recipient_city} is { int(city_temperature-273.15) }*C [{weather_description}], {emoji} {emoji} {emoji}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.recipient_email, ]
        
        # Finally sending the email.
        send_mail( subject, body, email_from, recipient_list )
        