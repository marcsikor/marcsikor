def zad14():

	#####
	# Calculation of the area and circumference of a circle
	##

	# determine radius and PI
	radius = 5; pi = 3.14

	# calculate area 
	area = radius ** 2 * pi

	# calculate circumference 
	circumference = radius * 2 * pi

	# display results 
	print(f"area = {area}, circumference = {circumference}") 


def zad15():
	
	temp = float(input("temperature in degrees: " ))
	fahr = temp * 1.8 + 32
	kelvin = temp + 273.15
	
	print(f'the temperature is {fahr} in F and {kelvin} in K')
	

def zad19():
	
	from math import sqrt
	a = 3; b = 4; c = 5
	p = (a + b + c)/2
	area = sqrt(p*(p-a)*(p-b)*(p-c))
	print(f"area of the triangle is {area}")
	

def zad20():
	
	height = float(input('wzrost w cm: '))
	mass = float(input('masa: '))
	bmi = mass/(height/100) ** 2
	print(f'bmi index: {bmi}')	


def zad21():
	
	from random import randrange
	a = int(randrange(1,6)); b = int(randrange(1,6)); c = int(randrange(1,6))
	sum = a + b + c
	
	print(f'sum of dices is: {sum}')
	

def zad22():
    
    from random import randrange
    a = int(randrange(1,6))
    b = int(input('jaki numer został wylosowany?: '))
    
    print(f'{a==b}')


def zad23():

    value = 15.84
    vat = 0.23
    print(f'amount: {value} zł \nVAT {int(vat*100)}%: {value*vat:.2f} zł')


# uncomment to view

# zad15()	
# zad19()
# zad20()
# zad21()
# zad22()
zad23()
