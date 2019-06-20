#Import CSV dan Panda
import csv
import pandas as pd

#Data Train
dataTrainKompetensi=[61,71,64,60,73.5,66.5,82.5,61,52.5,57.5,
72.5,73.5,50.5,62.5,62.5,68,38,52.5,81,72]

dataTrainKepribadian=[37.5,58.3,35.8,51.7,75,62.5,15,37.5,54.2,79.2,
56.7,75,70.8,58.3,60,20.8,82.5,70.8,61.7,67.5]

dataTrainHasil=["Tidak","Ya","Tidak","Tidak","Ya","Ya","Tidak","Tidak","Tidak","Ya",
"Ya","Ya","Ya","Tidak","Tidak","Tidak","Ya","Tidak","Ya","Ya"]

#Data Test
dataTestKompetensi = [61.5,66.5,71,64.5,57.5,80,81.5,61,46,78]
dataTestKepribadian = [52.5,58.5,45.8,55,79.2,45.8,53.3,64.2,65.8,49.2]
dataTestHasil =[]


#Fungsi Fuzzy
def programFuzzy(a, b):
	kompetensi = a
	kompRendah = 0
	kompSedang = 0
	kompTinggi = 0

	kepribadian = b
	kepriRendah = 0
	kepriSedang = 0
	kepriTinggi = 0

	#Fuzzification Input
	if (kompetensi <= 48.5):
		kompRendah = 1
		kompSedang = 0
		kompTinggi = 0
	elif (kompetensi >=72.5):
		kompRendah = 0
		kompSedang = 0
		kompTinggi = 1
	elif (kompetensi>=62.5 and kompetensi<=70):
		kompRendah = 0
		kompSedang = 1
		kompTinggi = 0
	else:	
		if (kompetensi > 48.5 and kompetensi < 62.5):
			kompRendah = (62.5-kompetensi)/(62.5-48.5)
			kompSedang = (kompetensi-48.5)/(62.5-48.5)
			kompTinggi = 0 
			
		elif (kompetensi > 70 and kompetensi < 72.5):
			kompRendah = 0
			kompSedang = (72.5-kompetensi)/(72.5-70)
			kompTinggi = (kompetensi-70)/(72.5-70)
			

	if (kepribadian <= 38.5):
		kepriRendah = 1
		kepriSedang = 0
		kepriTinggi = 0
	elif (kepribadian >= 72):
		kepriRendah = 0
		kepriSedang = 0
		kepriTinggi = 1
	elif (kepribadian >=55 and kepribadian <= 60):
		kepriRendah = 0
		kepriSedang = 1
		kepriTinggi = 0
	else:
		if(kepribadian > 38.5 and kepribadian < 55):
			kepriRendah = (55-kepribadian)/(55-38.5)
			kepriSedang = (kepribadian - 38.5)/(55-38.5)
			kepriTinggi = 0
			
		elif (kepribadian > 60 and kepribadian < 72):
			kepriRendah = 0
			kepriSedang = (72-kepribadian)/(72-60)
			kepriTinggi = (kepribadian - 60)/(72-60)
			
	ya=0
	mungkin=0
	tidak=0
	yaTemp=0
	mungkinTemp=0
	tidakTemp=0

	#Inference
	if(kompRendah!=0):
		if(kepriRendah!=0):
			tidakTemp=min(kompRendah,kepriRendah)
			if(tidakTemp>tidak):
				tidak=tidakTemp
		if(kepriSedang!=0):
			tidakTemp=min(kompRendah,kepriSedang)
			if(tidakTemp>tidak):
				tidak=tidakTemp
		if(kepriTinggi!=0):
			mungkinTemp=min(kompRendah,kepriTinggi)
			if(mungkinTemp>mungkin):
				mungkin=mungkinTemp

	if(kompSedang!=0):
		if(kepriRendah!=0):
			tidakTemp=min(kompSedang,kepriRendah)
			if(tidakTemp>tidak):
				tidak=tidakTemp
		if(kepriSedang!=0):
			mungkinTemp=min(kompSedang,kepriSedang)
			if(mungkinTemp>mungkin):
				mungkin=mungkinTemp
		if(kepriTinggi!=0):
			yaTemp=min(kompSedang,kepriTinggi)
			if(yaTemp>ya):
				ya=yaTemp
	
	if(kompTinggi!=0):
		if(kepriRendah!=0):
			mungkinTemp=min(kompTinggi,kepriRendah)
			if(mungkinTemp>mungkin):
				mungkin=mungkinTemp
		if(kepriSedang!=0):
			mungkinTemp=min(kompTinggi,kepriSedang)
			if(mungkinTemp>mungkin):
				mungkin=mungkinTemp
		if(kepriTinggi!=0):
			yaTemp=min(kompTinggi,kepriTinggi)
			if(yaTemp>ya):
				ya=yaTemp


	#Defuzzification

	nYa = (ya * 65)
	nMungkin = (mungkin * 50)
	nTidak = (tidak * 40)
	nilai = (nYa + nMungkin + nTidak)/(ya+mungkin+tidak)
	#return nilai
	if (nilai >= 49):
		hasil = 'Ya'
	else:
		hasil = 'Tidak'

	return hasil




#Main Program
if __name__ == '__main__':
	
	count=0
	correct = 0
	

	#Me
	while count < 20:
		train = dataTrainHasil[count]
		print(programFuzzy(dataTrainKompetensi[count], dataTrainKepribadian[count]))
		if (programFuzzy(dataTrainKompetensi[count],dataTrainKepribadian[count]) ==
	train):
			correct = correct + 1
		count = count + 1

	print("Akurasi: "+str((correct/20)*100) + "%")

	countTest = 0
	while countTest < 10:
		dataTestHasil.append(programFuzzy(dataTestKompetensi[countTest],dataTestKepribadian[countTest]))

		countTest = countTest + 1			

	df=pd.DataFrame(dataTestHasil)
	df.to_csv("TebakanTugas3.csv", index=False, header=False)