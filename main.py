# Thijs van Driel This sequence 

import time
print("Welcome to the Fraser High School canteen") 
time.sleep(1.5) 
print("What is your name") 
n = input ( )
print("Kia Ora " + n)
time.sleep(1.5) 
print("We sell pies and burgers at the Fraser High canteen!") 
buy = input ("Would you like a pie, or a burger, " + n + "?"'\n')
time.sleep(1.5) 

if buy.lower() == 'burger': 
  print("Thats great") 
  time.sleep(1.5) 
  print("The burger will be he ready in 5 seconds") 
  time.sleep(5)  
  print("🍔") 

if buy.lower() == 'pie':
  print("Pie are my favourite") 
  time.sleep(1.5) 
  print("The pie will be he ready in 5 seconds") 
  time.sleep(5) 
  print("Here is a fresh hot mince pie") 
  print("🥧")
 

