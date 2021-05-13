import random
import colorama
import time
from colorama import Fore
from colorama import Style
colorama.init(autoreset=True)

print(f"{Style.BRIGHT}Welcome to Stone, Paper, Seasor game 🥳 \n")
print(f"{Fore.RED}Note: You only have 10 chance!")
raw = ["stone", "paper", "seasor"]
# storing possible answers as list
usr_nm = input(f"\nEnter your name : {Fore.RED}")
# User will give his/her name here

gus_lmt = 0
# gus_lmt is the guess limit
user_point = 0

while gus_lmt<=9:# if guess limit will go more than 10 this loop will stop
	r8_ans = random.choice(raw)
	#module creats an choice by itself
	
	
	print(Style.RESET_ALL)
	choice = input("\nEnter your choice : ")
	#choice is the answer taken from the user
	ch = choice.lower() 
	# Making the user input lower case so that it can match with the list 'raw' even if user gave upper case letters 
	gus_lmt = gus_lmt + 1
	#Guess time will increase +1 after every attempt
	if ch==r8_ans :
		#
		print("Match draw!!")
		#  draw
		#
		time.sleep(0.2)
		
		continue
	elif ch=="stone" and r8_ans=="seasor" or ch=="seasor" and r8_ans=="paper" or ch=="paper" and r8_ans=="stone" :
		# win
		print(f"{Fore.GREEN}You won this round 🥳🎉  \n"+'\033[39m'+f"You used {gus_lmt} guss limit. \nYou entered {ch} \nComputer answered {r8_ans} . \n Your score is {user_point} . \n ")
		user_point = user_point + 1
		
	elif ch=="stone" and r8_ans=="paper" or ch=="seasor" and r8_ans=="stone" or ch=="paper" and r8_ans=="seasor":
		
		# lose
		print(f"{Fore.RED}You lost this round 😔😓. Hope you will win next round 🙏\n"+'\033[39m'+f"You used {gus_lmt} guss limit. \nYou entered {ch} \nComputer answered {r8_ans} . \n Your score is {user_point} . \n  ")
	else:
		# invalid input
		print("Check your input!!")
		time.sleep(1)
		#
		
		continue
	continue
	

# Telling user his/her score
print(f" ⚠️ Game Over!!\nYour score is {user_point} . ")
if user_point>5:
	print(f"{Fore.GREEN}Well played {usr_nm.capitalize()}!! 🎊🎁🎉 \n") # congratulating the user
elif user_point==5:
	print("Match draw! 😑 \n")
elif user_point<5:
	print("Better luck next time. 🙂 \n ")
else:
	print("Error!! \n")


print(f"Thanks for playing {usr_nm.capitalize()}!")
#thanking the player
player = open("player.txt", "a")
#storing the player name and score after opening this file
player.write(f"Player name : {usr_nm.capitalize()}. Score : {user_point}. \n")
player.close()
time.sleep(1.1)
exit()
