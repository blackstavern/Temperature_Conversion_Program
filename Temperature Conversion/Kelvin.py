print ( " \n☁️  Temperature Conversion Program ☁️\n " )

# celcius
province = str ( input ( "Enter the Province : " ) )
print ( "The Province is", province, "Province \n" ) 

city = str ( input ( "Enter the City : " ) )
print ( "The City is", city, "City \n" )

kelvin = float ( input ( "Enter the temperature on Kelvin : " ) )
print ( "The temperature is", kelvin, "Kelvin \n" )

result = str ( input ( "Do you want to find out the result ? " )  )
print ( "\nHere the final result : 🌡️ \n")

#Kelvin -> Celcius
celcius = kelvin - 273.15
print ( "The temperature on Celcius is", celcius, "degree Celcius \n" )

#Kelvin -> Reamur
reamur = ( 4/5 * (kelvin-273.15) )
print ( "The temperature on Reamur is", reamur, "degree Reamur \n" )

#Kelvin -> Fahrenheit
fahrenheit = ( ( 9/5 * (kelvin-273.15) ) + 32 )
print ( "The temperature on Fahrenheit is", fahrenheit, "degree Fahrenheit \n" )
