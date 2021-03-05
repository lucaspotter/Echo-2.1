from termcolor import colored 
import sys, random, time


# ----- [ Variables ] ---- #
femnames = ["Rachel","Mia","Emily","Tiffany"]
malenames = ["Michael","Brian","John","Peter"]
tastes = ["potato chips","toothpaste","vomit","lipstick","kale","steak","cotton candy"]
deathage = random.randint(0,100)
deathcause = random.randint(1,4)
puberty = False
pubertyage = random.randint(12,15)
pubertyeage = random.randint(17,20)
looks = random.randint(1,5)
smarts = random.randint(1,5)
alcoholtry = random.randint(1,5)
fkiss = random.randint(13,18)
fkissname = random.randint(0,3)
fkissage = random.randint(13,18)
fmarriage = random.randint(18,30)

# ----- [ Config First Kiss ] ----- #
firstkissname = femnames[fkissname]
kissreact = random.randint(1,5)
tonguereact = random.randint(1,5)
ttaste = random.randint(0,6)
tonguetaste = colored(tastes[ttaste],"yellow")
htongue = random.randint(1,3)
love = 5

if htongue == 1:
	htongue = True
else:
	htongue = False

if kissreact == 1:
	kissreact = colored("amazing","green")
elif kissreact == 2:
	kissreact = colored("good","green")
elif kissreact == 3:
	kissreact = colored("ok","yellow")
elif kissreact == 4:
	kissreact = colored("bad","red")
elif kissreact == 5:
	kissreact = colored("terrible","red")

if tonguereact == 1:
	if kissreact == colored("amazing","green"):
		love += 5;
	elif kissreact == colored("good","green"):
		love += 4;
	elif kissreact == colored("ok","yellow"):
		love += 3;
	elif kissreact == colored("bad","red"):
		love += 2;
	elif kissreact == colored("terrible","red"):
		love += 1;
	tonguereact = colored("amazing","green")
elif tonguereact == 2:
	if kissreact == colored("amazing","green"):
		love += 4;
	elif kissreact == colored("good","green"):
		love += 3;
	elif kissreact == colored("ok","yellow"):
		love += 2;
	elif kissreact == colored("bad","red"):
		love += 1;
	elif kissreact == colored("terrible","red"):
		love += 0;
	tonguereact = colored("good","green")
elif tonguereact == 3:
	if kissreact == colored("amazing","green"):
		love += 3;
	elif kissreact == colored("good","green"):
		love += 2;
	elif kissreact == colored("ok","yellow"):
		love += 0;
	elif kissreact == colored("bad","red"):
		love -= 1;
	elif kissreact == colored("terrible","red"):
		love += 2;
	tonguereact = colored("ok","yellow")
elif tonguereact == 4:
	if kissreact == colored("amazing","green"):
		love += 1;
	elif kissreact == colored("good","green"):
		love += 0;
	elif kissreact == colored("ok","yellow"):
		love -= 1;
	elif kissreact == colored("bad","red"):
		love -= 2;
	elif kissreact == colored("terrible","red"):
		love -= 3;
	tonguereact = colored("bad","red")
elif tonguereact == 5:
	if kissreact == colored("amazing","green"):
		love += 0;
	elif kissreact == colored("good","green"):
		love -= 1;
	elif kissreact == colored("ok","yellow"):
		love -= 2;
	elif kissreact == colored("bad","red"):
		love -= 3;
	elif kissreact == colored("terrible","red"):
		love -= 4;
	tonguereact = colored("terrible","red")

def firstkiss():
	print("Echo has a chance to kiss",firstkissname)
	time.sleep(1)
	kiss = input("Should he? [y/n]\n")
	if kiss == "y":
		withtongue = input("Should he kiss her with his tongue? [y/n]\n")
		if withtongue == "y":
			print("Echo kissed",firstkissname,"with his tongue")
			time.sleep(1)
			print("She tasted like",tonguetaste)
			time.sleep(1)
			print("Echo thought it went",kissreact)
			print(firstkissname,"thought it went",tonguereact)
		elif withtongue == "n":
			print("Echo kissed",firstkissname,"without his tongue")
			time.sleep(1)
			if htongue == True:
				print(firstkissname,"suprised Echo by kissing him with her tongue")
				time.sleep(1)
				print("Echo thought the kiss went",tonguereact)
				print(firstkissname,"thought it went",kissreact)
			else:
				print("Echo thought it went",kissreact)
				print(firstkissname,"thought it went",tonguereact)
		else:
			sys.exit(colored("Man you had a chance, but you gotta start over","white"))
	elif kiss == "kissthedev":
		print("Aww, thanks, since you wanted to kiss me, here:")
		deathage = 999999999
		sys.exit(colored("Echo will now live forever","white"))
	elif kiss == "n":
		print("Echo didn't kiss",firstkissname)
	else:
		sys.exit(colored("Man you had a chance, but you gotta start over","white"))


# ----- [ Config for Marriage ] ----- #


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
for i in range(1000000001):
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
	elif age == fkissage:
		firstkiss()
	elif age == 16:
		print("Echo can now",colored("drive","blue"))
	elif age == 21:
		print("Echo tried alcohol for the first time, it went",alcoholtry)
	time.sleep(1)
