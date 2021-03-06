# Cas-Kaggle APC

### Nom: Cristina Tost Abadias
### NIU: 1569280
### Dataset: Heart Failure Prediction Dataset
### URL: https://www.kaggle.com/fedesoriano/heart-failure-prediction


## Contexte
Les malalties cardiovasculars (MCV) són la primera causa de mort a nivell mundial, amb 17,9 milions de vides estimades cada any, la qual cosa representa el 31% de totes les morts a tot el món. Quatre de cada 5 morts per MCV es deuen a atacs cardíacs i accidents cerebrovasculars, i un terç d'aquestes morts es produeixen de manera prematura en persones menors de 70 anys. La insuficiència cardíaca és un esdeveniment comú causat per les MCV i aquest conjunt de dades conté 11 característiques que es poden utilitzar per predir una possible malaltia cardíaca.

Les persones amb malalties cardiovasculars o que tenen un risc cardiovascular elevat (per la presència d'un o més factors de risc com hipertensió, diabetis, hiperlipèmia o malaltia ja establerta) necessiten una detecció i una gestió precoç on un model d'aprenentatge automàtic pot ser de gran ajuda.

Aquest dataset es va crear combinant diferents conjunts de dades ja disponibles de manera independent però mai combinades abans. En aquest dataset, 5 conjunts de dades del cor es combinen amb 11 característiques comunes, cosa que el converteix en el conjunt de dades de malalties del cor més gran disponible fins ara amb finalitats d'investigació. 

## Atributs
Aquesta base de dades consta de 12 atributs:

  - *Age*: edat del pacient
  - *Sex*: sexe del pacient (M: masculi, F: femeni)
  - *Chest Pain Type*: tipus de dolor al pit (TA: angina típica, ATA: angina atípica, NAP: dolor no anginós, ASY: asimptomàtic)
  - *RestingBP*: pressió arterial en repòs
  - *Cholesterol*: colesterol sèric
  - *FastingBS*: sucre en sang en dejú (1: si FastingBS > 120 mg/dl, 0: en cas contrari)
  - *RestingECG*: resultats de l'electrocardiograma en repòs (Normal: normal, ST: amb anormalitat de l'ona, LVH: mostrant hipertròfia ventricular esquerre probable o definitiva segons els criteris d'Estes)
  - *MaxHR*: freqüència cardíaca màxima aconseguida
  - *ExerciseAngina*: angina induïda per l'exercici (Y: Sí, N: No)
  - *Oldpeak*: oldpeak = ST
  - *ST_Slope*: pendent de l'exercici màxim (Up, Flat, Down)
  - *HeartDisease*: Malaltia cardíaca (1: malaltia cardíaca, 0: normal)

### Objectiu

Aquesta base de dades té com a objectiu veure quins són els factors que fan que un pacient pateixi una malaltia cardíaca o no. Per tant, volem entrenar un model que ens pugui predir amb bons resultats si un pacient tindrà una malaltia cardíaca (1: malaltia cardíaca, 0: normal) i així poder estudiar quins atributs tenen més pes a l'hora de desenvolupar-ne una.

### Preprocessament

Abans de aplicar diferents models a la base de dades hem hagut de realitzar alguns canvis en ella.

Primerament, hem hagut de mirar els valors nulls del nostre dataset. Hem vist que no n'hi ha cap, aleshores no hem hagut de realitzar cap canvi. Seguidament hem mirat quants atributs tenim i de quin tipus són. Aquests són els resultats:

  - *Age*: int64
  - *Sex*: object
  - *Chest Pain Type*: object
  - *RestingBP*: int64
  - *Cholesterol*: int64
  - *FastingBS*: int64
  - *RestingECG*: object
  - *MaxHR*: int64
  - *ExerciseAngina*: object
  - *Oldpeak*: float64
  - *ST_Slope*: object
  - *HeartDisease*: int64

Observem que tenim varios atributs de tipus 'object', i com que no és el que volem, els passem a números. Per exemple, el sexe del pacient ara en comptes de ser M o F per al sexe masculí o femení, serà 1 ('M') i 0 ('F').

Un cop ja ens hem assegurat de que no hi han valors nulls i de que tots els atributs ara son numérics, ens fiquem a analitzar-los un per un amb l'atribut 'HeartDisease'. Aquest serà el nostre target, ja que volem predir si el pacient tindrà una malaltia cardíaca o no.
Primerament analitzem els atributs que anteriorment eran categòrics i, fent això observem:

  - Els homes pateixen de malalties cardíaques més sobint que les dones.
  - Els pacients asimptomàtics són els que majoritariament són diagnosticats amb malalties     cardíaques.
  - La malaltia cardíaca sovint es diagnostica quan hi ha angina de pit induïda per       l'exercici
  - Quan ST_Slope és Up, sovint es diagnostica com a normal. En canvi, si aquest és Flat o Down, solen ser diagnosticats amb una malaltia cardíaca.

Seguidament analitzem els atributs numèrics, i observem:

  - La mitjana d'edat de les persones diagnosticades amb malalties del cor és de 57 anys, que és més gran que el valor mitjà de les persones normals.
  -  A la figura de l'atribut 'RestingBP', hi ha un valor de 0. Si la pressió arterial és 0, en realitat no és possible, de manera que és probable que sigui un outlier.
  - A la figura de l'atribut 'cholesterol', hi ha valors que són 0. Si el colesterol sèric és 0, no és possible a la pràctica, de manera que és probable que sigui un outlier.

Per els casos dels atributs en els que hem trobat oitliers, hem canviat els outliers per el valor mitjà per tal d'eliminarlos.

Finalment mirem les correlacions dels atributs amb el nostre target i les plotejem. Els resultats han estat els següents:
  - ST_Slope         -0.558771
  - MaxHR            -0.400421
  - ChestPainType    -0.386828
  - Cholesterol       0.042988
  - RestingECG        0.057384
  - RestingBP         0.117798
  - FastingBS         0.267291
  - Age               0.282039
  - Sex               0.305445
  - *Oldpeak           0.403951*
  - *ExerciseAngina    0.494282*
  - HeartDisease      1.000000

Observem elsatribut amb major correlació amb l'atribut 'HeartDisease' són 'ExerciseAngina' i Oldpeak. Però com varios atributs tenen diferents tipus de resultats, creem nous atributs corresponents als posibles resultats dels atributs i mirem les noves correlacions. Els resultats han estat els següents:

  - ST_Slope_2         -0.622164
  - ExerciseAngina_0   -0.494282
  - ChestPainType_1    -0.401924
  - MaxHR              -0.400421
  - Sex_0              -0.305445
  - ChestPainType_2    -0.212964
  - RestingECG_1       -0.091580
  - ChestPainType_3    -0.054790
  - RestingECG_0        0.010670
  - Cholesterol         0.042988
  - RestingECG_2        0.102527
  - RestingBP           0.117798
  - ST_Slope_0          0.122527
  - FastingBS           0.267291
  - Age                 0.282039
  - Sex_1               0.305445
  - Oldpeak             0.403951
  - ExerciseAngina_1    0.494282
  - ChestPainType_0     0.516716
  - ST_Slope_1          0.554134

Podem concloure que definitivament els atributs que tenen més correlació amb 'HeartDisease' són 'ST_Slope_1' (Flat),'ChestPainType_0'(asimptomàtic), 'ExerciseAngina_1' (Si), 'Oldpeak' i 'Sex_1' (home). Amb 0.55,0.51,0.49,0.4,0.3 respectivament.

# Models

Abans de realitzar els diferents models, dividim les dades en train i test, i estandaritzem les dades.

Resultats al executar els models:

| Model | Accuracy | Temps |
| ------|----------|-------|
| Regressor Logístic | 0.8478 | 0.01766 |
| SVC | 0.8695 | 0.0312 |
| Random Forest | 0.8804 | 13.4230 |
| XGBOOST | 0.8804 | 0.1752 |
| Decission Tree | 0.8260 | 0.0092 |
| KNN | 0.8586 | 0.0013 |

Comparant el temps, els accuracy i la ROC Curve i la Precision-Recall Curve, veiem que el model que millor ens funciona amb la nostre base de dades és el XGBOOST.

# PCA

L'últim experiment que he fet és provar de fer un PCA amb el model XGBoost per veure fins quan podríem reduir les dimensions de l'espai. En el resultat podem veure que l'accuracy del model va decreixent a poc a poc a mida que reduïm la dimensió. Però podem observar un canvi bastant dràstic a partir de quan la dimensió és de 14 cap avall.


# Conclusions

Hem vist que el model que millor prediu el nostre atribut objectiu és el XgBoost. 
Observem que per intentar no patir una malaltía cardíaca s’hauria d’evitar tenir angina induïda per l'exercici on el dolor del pit fos asimptomàtic i que per tant el pendent de l’exercici màxim fos pla.






