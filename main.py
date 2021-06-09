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
  time.sleep(1.5)
  print("Thats great") 
  time.sleep(1.5)

