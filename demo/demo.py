# -*- coding: utf-8 -*-
"""demo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UQETwlYr4Lzd5MFSB9g-R0hEKn51wOsd
"""

import dill
import joblib
import pandas as pd
import numpy as np

classificador = joblib.load("classificador.pkl")
mitjana = joblib.load("mean.pkl")
desviacio_estandard = joblib.load("desviacio_estandard.pkl")

noves_dades = []

age = 49 #Introduir dada
noves_dades.append(age)

#1: Dona, 0:Home
sex = #Introduir dada
noves_dades.append(sex)

# 0:ASY, 1:ATA, 2:NAP, 3:TA

chest_pain_type =  #Introduir dada
noves_dades.append(chest_pain_type)

restingBP = #Introduir dada
noves_dades.append(restingBP)

cholesterol =  #Introduir dada
noves_dades.append(cholesterol)

#1: si FastingBS > 120 mg/dl, 0: en cas contrari

fastingBS = 0  #Introduir dada
noves_dades.append(fastingBS)

#0:LVH, 1:Normal, 2:ST

restingEGC =  #Introduir dada
noves_dades.append(restingEGC)

maxHR =  #Introduir dada
noves_dades.append(maxHR)

#0:N, 1:Y

exercise_angina =  #Introduir dada
noves_dades.append(exercise_angina)

oldpeak =  #Introduir dada
noves_dades.append(oldpeak)

#0:Down, 1:Flat, 2:Up

st_slope =  #Introduir dada
noves_dades.append(st_slope)

#1: malaltia cardíaca, 0: normal
heartdisease = 1 #Introduir dada
noves_dades.append(heartdisease)

dades = np.array(noves_dades)
x = dades[:-1]
y = dades[-1]

scaler_x = (x - mitjana)/desviacio_estandard

x2 = [scaler_x]
x3 = np.array(x2)

prediccio = classificador.predict(x3)
print(prediccio)

y2 = [y]
y3 = np.array(y2)

joblib.dump(prediccio,'prediccio.pkl')
joblib.dump(y3,'y_real.pkl')