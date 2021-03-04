from termcolor import colored 
import sys, random, time


# ----- [ Variables ] ---- #
'''
femnames = ["Rachel","Mia","Emily","Tiffany",""]
malenames = ["Michael","Brian","John","Peter"]
'''
deathage = random.randint(0,100)
deathcause = random.randint(1,4)
puberty = False
pubertyage = random.randint(12,15)
pubertyeage = random.randint(17,20)
looks = random.randint(1,5)
smarts = random.randint(1,5)
alcoholtry = random.randint(1,5)
'''
fkiss = random.randint(13,18)
fkissname = random.randint(1,10)

# ----- [ Config First Kiss ] ----- #
def firstkiss():

'''


# ----- [ Config of Alcohol Try ] ----- #
if alcoholtry == 1:
	alcoholtry = colored("amazing","green")
elif alcoholtry == 2:
	alcoholtry = colored("good","green")
elif alcoholtry == 3:
	alcoholtry = colored("ok","yellow")
elif alcoholtry == 4:
	alcoholtry = colored("bad","red")
elif alcoholtry == 5:
	alcoholtry = colored("terrible","red")

# ----- [ Config of Smarts ] ----- #
if smarts == 1:
	smarts = colored("a genius","green")
elif smarts == 2:
	smarts = colored("smart","green")
elif smarts == 3:
	smarts = colored("average","yellow")
elif smarts == 4:
	smarts = colored("dumb","red")
elif smarts == 5:
	smarts = colored("cognitively impaired","red")

# ----- [ Config of Looks ] ----- #
if looks == 1:
	looks = colored("beautiful","green")
elif looks == 2:
	looks = colored("good","green")
elif looks == 3:
	looks = colored("ok","yellow")
elif looks == 4:
	looks = colored("ugly","red")
elif looks == 5:
	looks = colored("revolting","red")

# ----- [ Config of deathage & deathcause ] ----- #
if deathage == 0:
	deathcause = colored("was a miscarrige","red")
else:
	if deathcause == 1:
		deathcause = colored("died of natural causes","red")
	elif deathcause == 2:
		deathcause = colored("died of a birth defect","red")
	elif deathcause == 3:
		deathcause = colored("died of alcohol poisoning","red")
	elif deathcause == 4:
		deathcause = colored("drank motor oil","red")


# ----- [ Echo's Life 'For Loop' ] ----- #
for i in range(101):
	age = i;
	print("Echo is",str(age),"years old");
	if age == deathage:
		print("Echo",deathcause)
		sys.exit()
	elif age == pubertyage:
		puberty = True
		print("Echo is going through",colored("puberty","blue"))
	elif age == pubertyeage and puberty == True:
		puberty = False
		print("Echo is finished with",colored("puberty","blue"))
		time.sleep(1)
		print("Echo looks",looks)
		time.sleep(1)
		print("Echo is",smarts)
	elif age == 16:
		print("Echo can now",colored("drive","blue"))
	elif age == 21:
		print("Echo tried alcohol for the first time, it went",alcoholtry)
	time.sleep(1)
