print ( " \n☁️  Temperature Conversion Program ☁️\n " )
print ( " Celcius \n" )

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

print ( " \n☁️  Temperature Conversion Program ☁️\n " )
print ( "Fahrenheit \n" )

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

print ( " \n☁️  Temperature Conversion Program ☁️\n " )
print ( "Reamur \n")

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

print ( " \n☁️  Temperature Conversion Program ☁️\n " )
print ( "Kelvin \n" )

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