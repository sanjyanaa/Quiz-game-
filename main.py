print("Welcome to my quiz games!")
print("You will be tested on the capital city of countries")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Alright lets start playing!!")
score = 0

answer = input("What is the capital city of Australia? ")
if answer.lower() == "canberra":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of United States ")
if answer.lower() == "new york":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of Canada? ")
if answer.lower() == "ottawa":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Name one of the three capitals of South Africa? ")
if answer.lower() == "cape town":
    print("Correct")
elif answer.lower() == "bloemfontein":
    print("Correct")
elif answer.lower() == "pretoria":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of Russia? ")
if answer.lower() == "moscow":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of Inida? ")
if answer.lower() == "new delhi":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of switzerland? ")
if answer.lower() == "bern":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct out of 7!")
