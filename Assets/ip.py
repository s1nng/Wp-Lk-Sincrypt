import datetime
import os, sys
import random
from time import sleep
#colours ------------code's--- 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
#------------------------------



#script banner--------------------------


#ALL comment are under tested so ignore him when i update it then its help me out to think better so thanks for using tool
#we will update soon
#we will add spoofing x bombing 
#soon
#by vaimpier ritik
#-------------------------------------------




#script banner fuction---




def backie():
	ritik_welcome = [

	'Thanks for using our tool', 
	'Keep using this tool Thanks Brother !!!', 
	'Bye dear :)', 
	'Hope you enjoy with this tool',
	'We are Sincryption :) Bye',
	'Thankyou so much dear :)',
	'Keep learning keep hacking :)',
	'Bye :) Next Update soon',
	'We have many tools like this subscribe our channel to get more',
	'Have a Good day dear :) ',
	'Sincryption says :) Thanks dear Bye :_)'


	]

	print(r+"└─"+w+"[!] "+y+random.choice(ritik_welcome))
	back=input(r+"..└─"+w+"\033[1;37mExit [ y / n ]: "+r)
	if back=='y' or back=='Y':
		
		sys.exit()
	if back=='n' or back=='N':
		backie()
	else:
		sys.exit()

def bye():
    backie()
    

def ip():
	
	
	print(r+"└─"+w+"\033[1;37m[ 1 ] IP Track: ")
	print(r+"└─"+w+"\033[1;37m[ 2 ] Own IP Track: ")
	print(r+"└─"+w+"\033[1;37m[ 3 ] Exit : ")

	opp=int(input(r+"└─"+w+"\033[1;37mEnter Desire Option: "+r))	
	if opp==1:
		os.system("clear")
		
		os.system("php Vaimip.php")
	elif opp==2:
		os.system("php Vaimip2.php")


	elif opp==3:
		bye()
    
            

	


	backie()

if __name__ == '__main__':
	ip()