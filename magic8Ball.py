#IMPORT RANDOM MODULE
import random

#VARIABLES DECLARED 
name = "John"
question = "Will I have a bountiful and fulfilling life?"
answer = ""
random_number = random.randint(1, 10)

#CONDITIONAL
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidely so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Looking good!"
else:
  answer = "Error"

#OUTPUT 
print(name + " asks: " + question)
print("Magic 8-Ball's answer:", answer)
