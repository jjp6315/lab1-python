temperature = float(input("Enter temperature: "))

unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  print("Converting Fahrenheit to Celsius.")
  
  c = (temperature - 32) * 5/9
 
  print(f"{temperature}\N{degree sign} in Fahrenheit is equivalent to {c}\N{degree sign} Celsius.")

elif unit == "C" or unit == "c":
  print("Converting Celsius to Fahrenheit.")
 
  f = temperature * 9/5 + 32
  
  print(f"{temperature}\N{degree sign} in Fahrenheit is equivalent to {f}\N{degree sign} Celsius.")



  
else: 
  print(f"Invalid unit({unit}).")






