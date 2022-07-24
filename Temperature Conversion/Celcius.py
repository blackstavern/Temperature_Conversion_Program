print ( " \n☁️  Temperature Conversion Program ☁️\n " )

# celcius
province = str ( input ( "Enter the Province : " ) )
print ( "The Province is", province, "Province \n" ) 

city = str ( input ( "Enter the City : " ) )
print ( "The City is", city, "City \n" )

celcius = float ( input ( "Enter the temperature on Celcius : " ) )
print ( "The temperature is", celcius, "degree Celcius \n" )

result = str ( input ( "Do you want to find out the result ? " )  )
print ( "\nHere the final result : 🌡️ \n")

# Celcius -> Reamur 
reamur = (4/5) * celcius 
print ( "The temperature on Reamur is", reamur, "degree Reamur \n" )

# Celcius -> Fahrenheit 
fahrenheit = ( (9/5) * celcius ) + 32
print ( "The temperature on Fahrenheit is", fahrenheit, "degree Fahrenheit \n" )

# Celcius to Kelvin
kelvin = celcius + 273.15
print ( "The temperature on Kelvin is", kelvin, "Kelvin \n" )
