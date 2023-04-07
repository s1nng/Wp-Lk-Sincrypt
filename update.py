# colors 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r

#----------------modules
import os 
from os import system,name
from time import sleep


# -----clear 
system('cls' if name=='nt' else 'clear')

#-------update
system('rm -rf Wp-Lk-Sincrypt')

sleep(0.1)
system('git clone https://github.com/samay825/Wp-Lk-Sincrypt')
print(r+"└─ "+w+"\033[1;37m>> Script Updated <<")
sleep(0.9)
os.chdir(os.getcwd() + '/Wp-Lk-Sincrypt/')
system('python main.py' if name=='nt' else 'python3 main.py')
