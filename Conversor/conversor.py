#first version
#temperature conversor

#variables
number=int(input("Select the conversion: (1: temperature) "))

if (number != 1):
   print ("Invalid conversion type")
   exit()

categories = {
    'temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
}

value = float(input("Enter the value to convert: "))
origin = input("Enter the origin: ")
destiny = input("Enter the destiny: ")

def temperature(value, origin, destiny):
    if origin == "Celsius" and destiny == "Fahrenheit":
        result = (value*9/5)+32
        print (result, destiny)
    elif origin == "Celsius" and destiny == "Kelvin":
        result = (value+273.15)
        print (result, destiny)
    elif origin == "Fahrenheit" and destiny == "Celsius":
        result = (value-32)*5/9
        print (result, destiny)
    elif origin == "Fahrenheit" and destiny == "Kelvin":
        result = (value-32)*5/9+273.15
        print (result, destiny)
    elif origin == "Kelvin" and destiny == "Celsius":
        result = (value-273.15)
        print (result, destiny)
    elif origin == "Kelvin" and destiny == "Fahrenheit":
        result = (value-273.15)*9/5+32
        print (result, destiny)
    else:
       return "no valid"

match number:
  case 1:
    print("Temperature conversion selected.")
    temperature(value, origin, destiny)
  case _:
    print("Invalid conversion selected.")


