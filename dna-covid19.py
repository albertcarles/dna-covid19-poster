#######################
# 
# DNA COVID-19 poster
# for Nodebox 1.9.7rc1 (Mac OS X)
# https://www.nodebox.net/code/index.php/Home
#
# by Albert Carles
# v1.0 2020/12/04
# https://github.com/albertcarles/dna-covid19-poster
# licensed under the GNU General Public License v3.0
#
#######################

import math
import string
import os
import os.path
import inspect

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

basesDNA = 'ATGC'
equivDNADNA = {'A':'T','T':'A','G':'C','C':'G'}
equivColors = {'A':color(1,0,0),'T':color(1,1,0),'G':color(0,1,0),'C':color(0,0,1),'U':color(0,1,1)}
        
DNA = {"53":"","35":""}
f = open(path+"/covid19.dna","r")
l = f.readline()
while l:
	DNA["53"] += string.strip(l.upper())
	l = f.readline()
f.close()

for b in DNA["53"]:
    DNA["35"] += equivDNADNA[b]

size(1191,1684)

mW = 3
mH = 6

global x
global y

x = 172
y = 169
w = 847

def nucl(dir,num):
	global x, y
	if dir == "LR" or dir == "TB":
		sign = 1
	elif dir == "RL" or dir == "BT":
		sign = -1
	if dir == "LR" or dir == "RL":
		stroke(equivColors[DNA["53"][num]])
		line(x+sign*mW/2.0,y,x+sign*mW/2.0,y+mH/2.0)
		stroke(equivColors[DNA["35"][num]])
		line(x+sign*mW/2.0,y+mH/2.0,x+sign*mW/2.0,y+mH)
		stroke(0)
		line(x,y,x+sign*mW,y)
		line(x,y+mH,x+sign*mW,y+mH)
		x += sign*mW
		
	if dir == "TB":
		stroke(equivColors[DNA["53"][num]])
		line(x+mH,y+mW/2.0,x+mH/2.0,y+mW/2.0)
		stroke(equivColors[DNA["35"][num]])
		line(x+mH/2.0,y+mW/2.0,x,y+mW/2.0)
		stroke(0)
		line(x,y,x,y+mW)
		line(x+mH,y,x+mH,y+mW)
		y += mW
		
	if dir == "LBr":
		stroke(equivColors[DNA["53"][num]])
		line(x+mH/2.0, y+mH/2, x+mH/4.0, y+3*mH/4.0)
		stroke(equivColors[DNA["35"][num]])
		line(x+mH/4.0, y+3*mH/4.0, x, y+mH)
		stroke(0)
		line(x,y,x+mH,y+mH)
		y += mH
		
	if dir == "LBl":
		stroke(equivColors[DNA["53"][num]])
		line(x+mH/2.0, y+mH/2, x+3*mH/4.0, y+mH/4.0)
		stroke(equivColors[DNA["35"][num]])
		line(x+3*mH/4.0, y+mH/4.0, x+mH, y)
		stroke(0)
		line(x,y,x+mH,y+mH)
		x += mH
		
	if dir == "TLr":
		stroke(equivColors[DNA["53"][num]])
		line(x+mH/2.0,y+mH/2.0,x+mH/4.0,y+mH/4.0)
		stroke(equivColors[DNA["35"][num]])
		line(x+mH/4.0,y+mH/4.0,x,y)
		stroke(0)
		line(x+mH,y,x,y+mH)

	if dir == "TLl":
		stroke(equivColors[DNA["53"][num]])
		line(x-mH/2.0,y+mH/2.0,x-mH/4.0,y+3*mH/4.0)
		stroke(equivColors[DNA["35"][num]])
		line(x-mH/4.0,y+3*mH/4.0,x,y+mH)
		stroke(0)
		line(x,y,x-mH,y+mH)
		y +=  mH
		x -= mH


stroke(0)
nofill()

max = len(DNA["53"])-1

dir = "LR"
gir = {"L":["LBr","TB","TLr","RL"], "R":["TLl","TB","LBl","LR"]}
girant = False 
punt = 0
for i in range(0,max,1):
	if girant:
		dir = gir[girant][punt]
		punt += 1
	else:
		if (x >= w+172 and dir == "LR") or (x < 172 and dir == "RL"):
			girant = dir[0]

	nucl(dir,i)
	
	if punt > 3:
		girant = False 
		punt = 0


		




    
    
    
    