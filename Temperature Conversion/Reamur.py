print ( " \n☁️  Temperature Conversion Program ☁️\n " )

# celcius
province = str ( input ( "Enter the Province : " ) )
print ( "The Province is", province, "Province \n" ) 

city = str ( input ( "Enter the City : " ) )
print ( "The City is", city, "City \n" )

reamur = float ( input ( "Enter the temperature on Reamur : " ) )
print ( "The temperature is", reamur, "degree Reamur \n" )

result = str ( input ( "Do you want to find out the result ? " )  )
print ( "\nHere the final result : 🌡️ \n")

# Reamur -> Celcius
celcius = (5/4) * reamur
print ( "The temperature on Celcius is ", celcius, "degree Celcius \n" )

# Reamur -> Fahrenheit 
fahrenheit = ( (9/4) * reamur ) + 32
print ( "The temperature on Fahrenheit is ", fahrenheit, "degree Fahrenheit \n")

#Reamur -> Kelvin
kelvin = ( (5/4) * reamur ) + 273.15
print ( "The temperature on Kelvin is ", kelvin, "Kelvin \n")