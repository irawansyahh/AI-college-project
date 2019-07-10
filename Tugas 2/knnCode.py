# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:20:38 2019

@author: Reza Siahaan
"""
#2019 Tugas AI
#This code is Created by mrezaprwr on Github https://github.com/mrezaprwr/AI-college-project repository
#Ask for permission to download this file by email rsiahaan4@gmail.com

import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from statistics import mean 

data_Train = np.genfromtxt('dataTrainAI.csv', delimiter=',', skip_header=1)
trains = data_Train[0:, 0:]
X_train = trains[:,0:4]
Y_train = trains[:,4]

X= np.array(X_train)
y= np.array(Y_train)

data_Test = np.genfromtxt ('dataTestAI.csv', delimiter=',', skip_header=1, usecols=(0,1,2,3))
Test = data_Test[0:, 0:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.27, train_size=None, random_state=49)

def predictKelas(X_train, y_train, x_test, k):
	# Buat list dan target label
	distances = []
	targets = []

	for i in range(len(X_train)):
		# Hitung jarak euclideannya
		distance = np.sqrt(np.sum(np.square(x_test - X_train[i, :])))
		# Masukkan ke list distances
		distances.append([distance, i])

	# Urutkan listnya agar terurut ascending (kecil ke besar)
	distances = sorted(distances)

	# Buat list untuk target label sebanyak k
	for i in range(k):
		index = distances[i][1]
		targets.append(y_train[index])

	# return target label dengan jumlah terbanyak
	return Counter(targets).most_common(1)[0][0]

def kNearestNeighbor(X_train, y_train, X_test, k):
	predictions = []
	# Lakukan prediksi kelas untuk tiap data Test
	for i in range(len(X_test)):
		predictions.append(predictKelas(X_train, y_train, X_test[i, :], k))
	return predictions

#Hitung akurasi 
def akurasi(y_test, prediksi):
	correct = 0
	for x in range(len(prediksi)):
	    if y_test[x] == prediksi[x]:
	        correct += 1
	return (correct/float(len(prediksi))) * 100.0

k=57
prediksi = kNearestNeighbor(X_train, y_train, X_test, k)
print(akurasi(y_test,prediksi), '%')
result = kNearestNeighbor(X_train, y_train, Test, k)

resultTable=pd.DataFrame(result)
resultTable.to_csv("Prediksi_Tugas2AI_[1301161771].csv", index=False, header=False)
