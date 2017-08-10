import urllib.request
import json
import turtle
import time

url = 'http://api.open-notify.org/astros.json'
url2 = 'http://api.open-notify.org/iss-now.json'
url3 = 'http://api.open-notify.org/iss-pass.json'
response1 = urllib.request.urlopen(url2)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
result2 = json.loads(response1.read())
print("To know the overhead time of the ISS Enter your Location Below")

print('Number of people in  space: ',result["number"])
for i in  result["people"]:
	per = 'Name: '+i['name'] + ' Craft: '+ i["craft"]
	print(per)

print('Know your Location: '+'www.latlong.net')
latUser = float(input("Enter Your Latitude: "))
longUser = float(input("Enter Your Longitude: "))

urlPass = url3 + '?lat=' + str(latUser) + '&lon=' +str(longUser)

location =result2["iss_position"]
lat =location["latitude"]
long =location["longitude"]
print(type(long))

print("The current latitude of (International Space Station)ISS:" ,lat)
print("The current longitude of (International Sapce Station)ISS:" ,long)


screen = turtle.Screen()
screen.setup(800,400)
screen.setworldcoordinates(-180,-90,90,180)
screen.bgpic('map.gif')
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

#To move the ISS to the current Location
iss.penup()
#Converting Str to float
iss.goto(float(long),float(lat))


location=turtle.Turtle()
location.penup()
location.color('red')
location.goto(longUser,latUser)
location.dot(5)
location.hideturtle()


#getting Passing Overhead data
responsePass = urllib.request.urlopen(urlPass)
resultPass = json.loads(responsePass.read())
over = resultPass['response'][1]['risetime']
style = ('Arial',10,'bold')
location.write(time.ctime(over),font=style)
turtle.done()
