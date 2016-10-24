#-*- coding: utf-8 -*-
#-*- coding: cp950 -*-
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

# create format for health/patient
healthX1 = []
healthX2 = []
patientX1 = []
patientX2 = []

health = []
patient = []
allP = []
AnsCounter = []
Counter = 0

# create data for health/patient/all
healthX1 = numpy.random.normal(0, 10.0, 10000)
healthX2 = numpy.random.normal(0, 1.0, 10000)
patientX1 = numpy.random.normal(30.0, 10.0, 10000)
patientX2 = numpy.random.normal(4.0, 1.0, 10000)

for i in range(0,10000,1):
	health.append([healthX1[i],healthX2[i],0])
	patient.append([ppX1[i],ppX2[i],1])
for i in range(0,10000,1):
    allP.append(health[i])
    allP.append(patient[i])

# randomly create datas for "all"
# size = 20000
random.shuffle(all)

# split all people into test subject(20%) and train subject(80%)
for i in range(0,4000,1):
	test.append([people[i][0],people[i][1]])
	testResult.append(people[i][2])
for i in range(4000,20000,1):
	train.append([people[i][0],people[i][1]])
	trainResult.append(people[i][2])

# implement KNN clasification
KNN = KNeighborsClassifier(n_neighbors = 3)
KNN.fit(train, trainingResult)

# calculate the mistakes
for i in range(0,4000,1):
	AnsCounter.append(KNN.predict(test[i]))
	if AnsCounter[i] != testResult[i]:
		Counter += 1

# change mistakes into the percentage of mistakes
Counter = Counter / 4000.0
print (Counter)

# function that draws pictures
def plot():
    plt.figure(figsize=(10,10))

    plt.scatter(healthX1 ,healthX2 ,color = 'blue',label='input scale', alpha=1)
    plt.scatter(patientX1 ,patientX2 ,color = 'red',label='input scale', alpha=1)
    plt.title('KNN test result')
    plt.xlabel('featureX1')
    plt.ylabel('featureX2')
    plt.grid()

    plt.tight_layout()

plot()
plt.show()
