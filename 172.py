# еще крутая функция вместо print - красиво печатает словари/списки/тд
from pprint import pprint

cities = {}
with open('week_temperature.txt') as f_week_temperature:
	for city in f_week_temperature:
		#print('city:',city)
		temperatures = f_week_temperature.readline() #- делает итерацию.
		#print('temp:', temperatures)	
		cities[city.strip()] = temperatures.split()

for city, temperatures in cities.items():
	avg = 0
	for t in temperatures:
		avg += int(t)
	avg = avg / len(temperatures)	
	print(city, "%.2f" % avg)

pprint(cities)