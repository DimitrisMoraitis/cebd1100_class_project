# convert a value into Celsius and Farenheit

temp = input("Enter temperature to convert > ")
temp = int(temp)

farenheit = round((9/5) * temp + 32, 1)
celsius = round((temp - 32) / (9/5), 1)

print("The temperature in Fareneheit is " + str(farenheit) + " degrees F")
print("The temperature in Celsius is " + str(celsius) + " degrees C")
