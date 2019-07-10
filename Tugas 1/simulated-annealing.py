#2019 Tugas AI
#This code is Created by mrezaprwr on Github https://github.com/mrezaprwr/AI-college-project repository
#Ask for permission to download this file by email rsiahaan4@gmail.com

import random
from math import sin, cos, exp, sqrt

def fungsi(x1, x2):
	return (sin(x1)*cos(x2) + (4/5)*exp(1-sqrt(x1*x1+x2*x2)))*-1

if __name__ == '__main__':
		x1 = random.uniform(-10,10)
		x2 = random.uniform(-10,10)

		E0 = fungsi(x1,x2)
		x1best = x1
		x2best = x2
		Ebest = E0

		T=1000

		while True:
			if T==0:
				break
			x1b = x1 + random.uniform(-1,1) 
			x2b = x2 + random.uniform(-1,1)
			Eb = fungsi(x1b,x2b)
			dE = Eb-E0

			if dE<0:
				x1 = x1b
				x2 = x2b
				E0 = Eb

				if Eb<Ebest:
					x1best = x1
					x2best = x2
					Ebest = E0
			elif dE > 0:
				p = exp(-1*dE/T)
				r = random.uniform(0,1)
				if r<p:
					x1=x1b
					x2=x2b
					E0=Eb
			T = T*1/10000000000
		E = fungsi(x1best,x2best)
		print(x1best,x2best)
		print(E)
