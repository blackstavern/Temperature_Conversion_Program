print ( " \n☁️  Temperature Conversion Program ☁️\n " )

# celcius
province = str ( input ( "Enter the Province : " ) )
print ( "The Province is", province, "Province \n" ) 

city = str ( input ( "Enter the City : " ) )
print ( "The City is", city, "City \n" )

fahrenheit = float ( input ( "Enter the temperature on Fahrenheit : " ) )
print ( "The temperature is", fahrenheit, "degree Fahrenheit \n" )

result = str ( input ( "Do you want to find out the result ? " )  )
print ( "\nHere the final result : 🌡️ \n")

# Fahrenheit -> Celcius
celcius = ( 5/9 * (fahrenheit-32) )
print ( "The temperature on Celcius is ", celcius, "degree Celcius \n " )

# Fahrenheit -> Reamur
reamur = ( 4/9 * (fahrenheit-32) )
print ( "The temperature on Reamur is ", reamur, "degree Reamur \n" )

kelvin = ( ( 5/9 * (fahrenheit-32) ) + 273.15)
print ( "The temperature on Kelvin is ", kelvin, "Kelvin \n" )