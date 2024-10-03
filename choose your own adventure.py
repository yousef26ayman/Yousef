name = input("Type Your Name: ")
print(f"Welcome {name} to this adventure game!")


answer = input(
    "You are on a road, it has come to end and you can go left or right. Which way you like to go? (left or right): ").lower()

if answer == "left":
    answer = input(
        "You come to a river, You can walk around it or swin accross. (walk or swim): ").lower()
    if answer == "walk":
        print("You walked for many miles. ran out of water and you lost the game.")
    elif answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or turn back? (cross or back): ").lower()
    if answer == "back":
        print("You go back and lose!")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to him? (yes or no): ").lower()
        if answer == "yes":
            print("You talk to the stranger. he give you gold. YOU WIN!")
        elif answer == "no":
            print("You ignore the starnger, and he is offended and you lose!")
        else:
            print("Not a valid option. You lose!")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")

print(f"Thank You For Trying {name}.")
