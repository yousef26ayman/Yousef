# first off welcome to the tutorial on how to make your very own fortune cookie message generator

# let's start by adding the random import

import random as rd

print(r"""
Welcome to Fortune Cookie 1.0
Please enter the following: "o" for open cookie or "q" for quit

       _.--.._
     ' \     / '
    /   \___/   \
   | _/      \_ |
   | _       _   |
    |_\     /_  |
    \  /---\   /
    ' /     \ '
      -..--..-
""")

# so we have this nice ui here. this makes it more appealing to the user.

# next let's add the list of values.

cookie_msg = [
    "| Take care of your health. |",
    "| Be patient and persistent. |",
    "| Change is coming. |",
    "| Listen to your intuition. |",
    "| A new friendship will blossom. |",
    "| You have a kind heart and a generous soul. |",
    "| Appearances can be deceiving. |",
    "| Believe in yourself. |",
    "| The future is full of possibilities. |",
    "| Good news will come to you by mail. |",
    "| Appearances can be deceiving. |",
    "| Let go of your fears. |",
    "| What you seek is already within you. |",
    "| Be patient and persistent. |",
    "| Good news will come to you by mail. |",
    "| Trust your gut feeling. |",
    "| Don't give up on your goals. |",
    "| A loved one will think of you today. |",
    "| Appearances can be deceiving. |",
    "| Don't give up on your goals. |",
    "| What you seek is already within you. |",
    "| You have a kind heart and a generous soul. |",
    "| Be kind to yourself and others. |",
    "| Listen to your intuition. |",
    "| Be open to change. |",
    "| Your dreams will come true. |",
    "| A loved one will think of you today. |",
    "| Trust your gut feeling. |",
    "| The future is full of possibilities. |",
    "| Listen to your intuition. |",
    "| Believe in yourself. |",
    "| A new friendship will blossom. |",
    "| You will travel to a faraway place. |",
    "| The path to success is not always straight. |",
    "| What you seek is already within you. |",
    "| Good news will come to you by mail. |",
    "| Listen to your intuition. |",
    "| Change is coming. |",
    "| The path to success is not always straight. |",
    "| Take care of your health. |",
    "| Don't give up on your goals. |",
    "| Appearances can be deceiving. |",
    "| Appearances can be deceiving. |",
    "| Trust your gut feeling. |",
    "| Appearances can be deceiving. |",
    "| You have a kind heart and a generous soul. |",
    "| Be kind to yourself and others. |",
    "| Enjoy the journey. |",
    "| Good news will come to you by mail. |",
    "| Learn from your mistakes. |",
    "| Listen to your intuition. |",
    "| Believe in yourself. |",
    "| Let go of your fears. |",
    "| You will have a stroke of good luck. |",
    "| Appearances can be deceiving. |",
    "| A loved one will think of you today. |",
    "| A new friendship will blossom. |",
    "| Be patient and persistent. |",
    "| Follow your dreams. |",
    "| You have a kind heart and a generous soul. |",
    "| Follow your dreams. |",
    "| You will have a stroke of good luck. |",
    "| Don't give up on your goals. |",
    "| Listen to your intuition. |",
    "| Don't give up on your goals. |",
    "| Trust your gut feeling. |",
    "| Sometimes, the best things in life are unexpected. |",
    "| Be open to change. |",
    "| You will have a stroke of good luck. |",
    "| Sometimes, the best things in life are unexpected. |",
    "| Be grateful for what you have. |",
    "| Change is coming. |",
    "| The future is full of possibilities. |",
    "| Be open to change. |",
    "| Believe in yourself. |",
    "| Don't give up on your goals. |",
    "| Change is coming. |",
    "| Learn from your mistakes. |",
    "| Be kind to yourself and others. |",
    "| You have a kind heart and a generous soul. |",
    "| A pleasant surprise awaits you. |",
    "| A new friendship will blossom. |",
    "| You will have a stroke of good luck. |",
    "| You have a kind heart and a generous soul. |",
    "| Change is coming. |",
    "| You will have a stroke of good luck. |",
    "| A pleasant surprise awaits you. |",
    "| A loved one will think of you today. |",
    "| The answer is hidden in plain sight. |",
    "| A new friendship will blossom. |",
    "| Appearances can be deceiving. |",
    "| Let go of your fears. |",
    "| Listen to your intuition. |",
    "| Change is coming. |",
    "| The answer is hidden in plain sight. |",
    "| Trust your gut feeling. |",
    "| A loved one will think of you today. |",
    "| The answer is hidden in plain sight. |",
    "| The path to success is not always straight. |",
    "| Follow your dreams. |"
]

# now we can start to code our logic for this.

# first let's request user input

option = input("> ")  # always remember to close your opening brackets!

while option != "q" and option != "Q": 

# while the option is not equal to q and option is not equal to Q if option is equal to o or option is equal to O then print a random message from the list cookie_msg. 

    if option == "o" or option == "O":
        print(rd.choice(cookie_msg))

        # add a second input command so that if the user wants to generate more fortune cookies they can

        option = input("> ")
    else:

    # if option is not equal to q, Q, o or O then the else statement ensures that a error message is printed to the console saying invalid option, the user is then given an option to input a character that does match the valid list of options.
        print("Invalid option. Try again.")
        option = input("> ")
else:
# if the user enters q or Q as input a goodbye message is printed to the console and the program exits.

    print("Goodbye!")
    quit()

# let's test this code

# let's first input an o, good, it works!

# now let's try a capital O, also works!

# now let's try a different letter that isn't coded. also works!

# finally let's try the quit option. and from that we can see it works perfectly!

# if you enjoyed my tutorial be sure to subscribe for more!
# also leave a like!



