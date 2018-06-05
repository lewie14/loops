#---------------For Loops-------------------

dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)
   
#----------------------------------------
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
	print(game)
  
for sport in sport_games:
	print(sport)
	
#-----------------------------------------------

promise = "I will not chew gum in class"

for i in range(5):
  print(promise)
  
for i in range(3):
  print(i)
#-------------------------------------------

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)
  
  
#-----------------Break-------------------------------
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break
    
#-------------------Continue--------------------------------
#This only prints the values over 21

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)
  
#---------------------While Loops-------------------------------------
#This takes the first list and pops off the last element into a new list
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

index = 0
while index < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  index += 1
print(students_in_poetry)

#------------------------Nested loops-----------------------------
#Here we start with sales data for 3 shops.

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)#This prints data from each location
  for element in location:
    scoops_sold += element#This adds the data from each location to scoops_sold
    
print(scoops_sold)

#---------------List Comprehensions-------------------------

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
print(usernames)
   
#First, we created a new empty list, usernames, and as we looped through 
#the words list, we added every word that matched our criterion.
#Python has a convenient shorthand to create lists like this with one line:
usernames = [word for word in words if word[0] == '@']
print(usernames)
#This is called a list comprehension. It will produce the same output as the for loop did

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

messages = [user + " please follow me!" for user in usernames]
print(messages)

my_upvotes = [192, 34, 22, 175, 75, 101, 97]
updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]
print(updated_upvotes)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temp*(9/5)+32 for temp in celsius]
print(fahrenheit)

#--------------Exercises--------------------------

squares = []

single_digits = range(0,10)
for digit in single_digits:
  print(digit)
  squares.append(digit*digit)
#Squares each value
print(squares)
#Cubes each value using just one line
cubes = [digit**3 for digit in single_digits]
print(cubes)

