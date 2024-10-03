print("Welcome to my computer!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok, Let's play :)")
score = 0
questions = 0

questions += 1
answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("incorrect!")

questions += 1
answer = input("What is GPU stands for? ")
if answer.lower() == "graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("incorrect!")

questions += 1
answer = input("What is RAM stands for? ")
if answer.lower() == "random access memory":
    score += 1
    print("Correct!")
else:
    print("incorrect!")

questions += 1
answer = input("What is PSU stands for? ")
if answer.lower() == "power supply":
    score += 1
    print("Correct!")
else:
    print("incorrect!")


print(f"You got {score} answers correct!")
print(f"You got {(score/questions) * 100} %")
