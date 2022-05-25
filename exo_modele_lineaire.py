# 1. Librairies 

from matplotlib import pyplot 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 2. Donnnées

## a) Création des données (vous pouvez les charger avec read_csv comme vu en cours)
X = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [96, 100, 104, 110, 120, 130, 145, 160, 170, 175]
print(X)
print(y)

## b) Division des données en apprentissage et test

# On répartit les données aléatoirement : 80% en données d'apprentissage, et 20% pour tester (le 0.2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# c) On les affiche
print(X_train)
print(y_train)
print(X_test)
print(y_test)

# d) Transformation

# On transforme en vecteur colonne pour le modèle (ne change pas les données, seulement leur forme)
X_train = np.reshape(X_train, (-1, 1)) # Si on met (1, -1), il s'agira d'un vecteur colonne
print(X_train) 

X_test = np.reshape(X_test, (-1, 1))
print(X_test) 

# 3. Modèle

## a) Création du modèle

# On crée le modèle
model = LinearRegression()

# On remplit le modèle
model.fit(X_train, y_train)

# On évalue ses performances
print(model.score(X_train, y_train))

# On regarde les informations du modèle
print(model.coef_)
print(model.intercept_)

## b) Prédiction

# On teste la capacité du modèle à prédire (les fameux 20% de données qu'on a mises de côté pour tester notre modèle
print(model.predict(X_test))
