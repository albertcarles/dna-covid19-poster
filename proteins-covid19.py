#######################
# 
# Proteins COVID-19 poster
# for Nodebox 1.9.7rc1 (Mac OS X)
# https://www.nodebox.net/code/index.php/Home
#
# by Albert Carles
# v1.0 2020/04/12
# https://github.com/albertcarles/dna-covid19-poster
# licensed under the GNU General Public License v3.0
#
#######################

import csv
import math
import os
import os.path
import inspect

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

file = path+'/codons-aminoacids.csv'
global codAmin
codAmin = []
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=';')
    for row in rd:
        codAmin.append(row)
        
    
def searchCodon(codon):
    resp = None
    for i in codAmin:
        if i["codon"] == codon:
            resp = i
    return resp
        

red = color(1,0,0)
green = color(0,1,0)
blue = color(0,0,1)
yellow = color(1,1,0)
black = color(0,0,0)

unit = 1

class Aminoacid:
	def __init__(self,x,y,letter):
		self.x = x
		self.y = y
		self.letter = letter
		self.radius = self.getData()["radius"]
	def getData(self):
		info = {"complete":"","abbr":"","letter":self.letter,"color":color(0,0,0),"radius":0,"codons":[]}
		for a in codAmin:
			if a["letter"] == self.letter:
				info["complete"] = a["complete"]
				info["abbr"] = a["abbr"]
				info["color"] = color(int(a["color-red"])/255.0, int(a["color-green"])/255.0, int(a["color-blue"])/255.0)
				info["radius"] = int(a["radius"])
				info["codons"].append(a["codon"])
		return info
	def show(self):
		data = self.getData()
		r = data["radius"]/(unit*10)
		fill(data["color"])
		oval(self.x,self.y,r,r)
		cx = self.x+r/2-unit/2.0
		cy = self.y+r/2-unit/2.0
		if self.letter == "R":
			fill(blue)
			oval(cx,cy,unit,unit)
			oval(cx-r/4,cy-r/4,unit,unit)
			oval(cx+r/4,cy-r/4,unit,unit)
		elif self.letter == "N" or self.letter == "Q":
			fill(blue)
			oval(cx,cy-r/3.5,unit,unit)
			fill(red)
			oval(cx-r/3.5,cy,unit,unit)
		elif self.letter == "D" or self.letter == "E":
			fill(red)
			oval(cx-r/5,cy-r/5,unit,unit)
			oval(cx+r/5,cy-r/5,unit,unit)
		elif self.letter == "C" or self.letter == "M":
			fill(yellow)
			oval(cx,cy,unit,unit)
		elif self.letter == "H":
			fill(1)
			oval(cx,cy,unit,unit)
			fill(blue)
			oval(cx-r/3.5,cy,unit,unit)
			oval(cx+r/4.5,cy-r/4.5,unit,unit)
		elif self.letter == "K":
			fill(blue)
			oval(cx,cy-r/3,unit,unit)
		elif self.letter == "F":
			fill(1)
			oval(cx,cy,unit,unit)
		elif self.letter == "S" or self.letter == "T":
			fill(red)
			oval(cx,cy,unit,unit)
		elif self.letter == "W":
			fill(1)
			oval(cx,cy,unit,unit)
			fill(blue)
			oval(cx+r/4.5,cy+r/4.5,unit,unit)
		elif self.letter == "Y":
			fill(1)
			oval(cx,cy,unit,unit)
			fill(red)
			oval(cx,cy-r/3,unit,unit)


dir =  path+'/covid-proteins/'

proteines = []
for i in os.listdir(dir):
	f = open(dir+i)
	protein = f.read()
	f.close()
	proteines.append(protein)

max = 0
for i in proteines:
	if len(i) > max:
		max = len(i)

size(1000,1191)

x = 0
y = 0


for prot in proteines:
	for a in prot:
		amino = Aminoacid(x,y,a)
		r = amino.radius/(unit*10.0)
		amino.show()
		if x < 864:
			x += r
		else:
			x = 0
			y += unit*5
	x = 0
	y += unit*10


