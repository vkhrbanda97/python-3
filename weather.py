from pyowm import OWM

API_key = '8c13c0726439fa72767f1ab13ce4fed2'
owm = OWM(API_key)


obs = owm.weather_at_coords(28.6139391, 77.2090212)

w = obs.get_weather()
x=w.get_status()
y=w.get_temperature('celsius')
z=w.get_reference_time(timeformat='iso') 
a=w.get_humidity()

if(a>50):
  print("The humidity is",a)
  print("The weather is",x,"in the location")
  print("The temperature is",y)
else:
  print(" The humidity is",a,"and the weather is",x)  
  print("The temperature is",y)