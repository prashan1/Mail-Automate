# **Mail-Automate** 
(**LIVE** - https://mail-automate.herokuapp.com/ )
Login credential - prashantbisht / Internship200
## ``` Django server with integrated database for email automation. ```

## ``` Introduction  ```
* User can enter an name, email address of the receiver and his/her city.
* The email body contain the temperature of the city at the time of sending .
* https://openweathermap.org/api is used for fetching weather detail of a city.
* Django's inbuilt api is used for mailing service.
* Final backend project is hosted on free cloud platform heroku.

## ``` Workflow  ```
### * Using Signals to send an email whenever receiver's data is saved in database
### * SendingClass in weather_api module is use to build complete logic of sending email to receiver ends.
### * Weather_api module is responsible for fetching weather detail and it's relevant emoji.
### * Get_weather_api() method is used to make a api_request using openweathermap api inside Weather_api module.
### * SendEmail() method is used for finally sending email using django built in sennd_mail module.
