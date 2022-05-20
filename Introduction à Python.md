# Introduction à Python.

# **Légende du cours**

# Ceci est un titre majeur

## Ceci est un sous-titre

**Ceci est un point important**

📝 Ceci est un exemple single line

⚠️ Ceci est une mise en garde

💡 Ceci est un conseil

[Ceci est un texte avec un lien vers un site ressource](https://www.w3schools.com/python/default.asp)

**Exemple**

```python
# Ceci est un exemple de code
```

# Introduction

## Qu’est-ce que le python ?

Le python est un langage de programmation très populaire créé au début des années 90.

**Il est utilisé majoritairement pour :**

- Le développement web (backend / côté serveur).
- La création d’applications.
- Les mathématiques (modélisation, statistiques, machine learning, etc.).

**Qu’est-ce que le python peut faire ?**

- Le python peut être utilisé sur un serveur pour créer des applications web.
- Il peut être utilisé pour connecter des bases de données, et peut être utilisé pour lire et modifier des fichiers.
- Le python est souvent utilisé pour traiter des grands jeux de données et appliquer des fonctions mathématiques complexes.
- Et enfin, il peut être utilisé pour faire du prototypage, et de la création d’application prêtes pour le déploiement.

**Ce qu’il faut savoir :**

- La version majeure la plus récente de python est `Python 3` (py3) , celui qu’on va utiliser pendant ce cours d’introduction. Même si `Python 3` (py2) est très populaire mais plus maintenu.

**La syntaxe du python par rapport à d’autres langages de prorammation**

- Le python a été designé pour la lisibilité et partage de nombreuses similarités avec l’anglais, tout en étant influencé par les mathématiques.
- Le python utilise de **nouvelles lignes** pour compléter une commande, comparé à d’autres langages qui utilisent des point-virgule `;` ou des parenthèses `(` `)`.
- Le python utilise l’**indentation** et les espaces vides pour définir la portée, le cadre d’une **fonction**, d’une **boucle** ou d’une **classe**. La majorité des langages utilisent les accolades `{`  `}` pour cela. Ainsi, au sein des boucles, on utilise l’indentation au lieu de *begin* et de *end*.

## Pour bien commencer

La majorité des PC et des Mac auront Python de préinstallé.

- La dernière version est la `3.10` (`3.11` en version bêta) mais généralement, on en est à `3.9.12` (surtout sur Mac).
- Pour vérifier si vous avez python d’installé sur votre PC ou Mac, lancez un terminal de commandes et tapez la commande suivante :

```bash
python --version
py --version
python3 -- version
```

Si la commande n’est pas trouvée, vous pouvez installer python sur leur [site](https://www.python.org/).

**Logiciels & plateformes**

Il existe un large éventail de logiciels permettant de coder en Python :

- [Atom](https://atom.io).
- [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/download/#section=windows).
- [Spyder](https://www.spyder-ide.org).
- [Visual Studio Code](https://code.visualstudio.com/#alt-downloads).

Il existe aussi des plateformes permettant de travailler à plusieurs comme [Colab](https://colab.research.google.com). 

On est aussi souvent amené à travailler sur des fichiers en `.ipynb`. Ceux-ci offre la possibilité de mêler du `Python` à du `Markdown` (langage qui permet de mettre en forme : titres, sous-titres, liens, etc.). On peut les manipuler facilement avec Jupyter ou Google Colab. Nous verrons tout au long de ce cours que beaucoup de ressources et projets se trouvent sur des [Notebooks](https://jupyter.org) Jupyter.

## Vos premières lignes de code

### Explications

Le python est un langage de programmation interprété, ce qui veut dire que en tant que développeur, vous écrivez des fichiers en python (`.py`) dans un éditeur de fichiers, puis vous utilisez l’interpréteur pour les exécuter.

Voici la démarche :

```bash
python miashsvie.py
```

Où `miashsvie.py` est le nom de votre fichier.

### Exemple

Créons notre premier fichier, que nous allons appeler `miashsvie.py`. Cela peut être fait dans n’importe quel éditeur de texte (Ou des applications comme [Atom](https://atom.io), [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/download/#section=windows), [Spyder](https://www.spyder-ide.org) ou [Visual Studio Code](https://code.visualstudio.com/#alt-downloads) par exemple).

Dedans, écrivez :

```python
print("Go les MIASHS")
```

Sauvegardez votre fichier, ouvrez votre terminal de commandes dans le dossier ou vous avez enregistré le fichier et exécutez :

```python
python miashsvie.py
```

La sortie de cette commande devrait être :

```python
Go les MIASHS
```

Félicitations ! Vous avez écrit et exécuté votre premier programme en `Python` !

## Le terminal de commandes en Python

Pour tester une *petite quantité* de code en python, il est parfois préférable et plus rapide de l’exécuter dans le terminal en python.

Pour cela écrivez la commande suivante dans votre terminal de commandes :

```bash
python
```

*(Oui oui, aussi simple que ça)*

Depuis ici, vous pourrez écrire n’importe quoi en python, même l’exemple que nous avions fait plus tôt.

```python
# C:\Users\Your Name>python
# Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.

>>> print("Go les MIASHS")
Go les MIASHS
```

Dès que vous avez terminé avec le console Python, vous pouvez écrire la commande suivante pour la quitter :

```python
exit() # Il s'agit d'une fonction, ne pas oublier les parenthèses
```

# Fonctionnalités

## Librairies

### **Objectif**

Elles fournissent des outils et fonctions avancées pour ce qu'on souhaite faire : ouvrir des fichiers avec des extensions particulières, visualiser des données, effectuer des tests statistiques et de performances, modéliser des données cérébrales, réaliser des cartes, etc.

### **Installation**

Il suffit d’ouvrir le terminal (comme vu précédemment) et d’utiliser `pip install` (possible pour des versions `Python` ultérieures à 3.4) suivi du nom de la librairie.

```bash
pip install NomLibrairie
```
Si la commande pip n’est pas reconnue, vous pouvez faire :
```bash
py -m ensurepip—upgrade 
```

Si on souhaite une version particulière, on peut la stipuler avec `pip`.

```bash
pip install NomLibrairie==1.4 
```

Si on souhaite une version ultérieure à une version spécifique, on peut aussi le préciser.

```bash
pip install NomLibrairie>=1.4 
```

Pour mettre à jour une librairie (qui sont souvent mises à jour car Python est en pleine expansion).

```bash
pip install --upgrade NomLibrairie
```

### **Méthode**

On utilise `import` avant de préciser le **nom** de la librairie (comme les packages sur `R`) qu’on souhaite utiliser, et `as` suivi de comment on veut les **appeler** dans le reste du programme (pour éviter d’avoir à réecrire un nom très long).

```python
import NomLibrairie as NomRaccourci
```

**Exemple**

```python
import numpy as np
```

On peut aussi importer une fonction spécifique d’une librairie en utilisant `from`.

**Exemple**

```python
from numpy import asarray
```

On peut choisir de tout importer en utilisant `*`.

```python
from nilearn import *
```

### **Les indispensables**

Manipuler et traiter des [grands tableaux](https://courspython.com/apprendre-numpy.html) de données.

```python
import numpy as np
```

Manipuler et traiter des [petits et moyens tableaux](https://datascientest.com/pandas-python-data-science) (vecteurs, matrices) de données.

```python
import pandas as pd
```

Visualiser [graphiquement](https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/4740942-maitrisez-les-possibilites-offertes-par-matplotlib) des données. 

```python
import matplotlib.pyplot as plt
```

Visualiser [graphiquement](https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/5559011-realisez-de-beaux-graphiques-avec-seaborn) (complète `matplotlib`).

```python
import seaborn as sns
```

Évaluer les [performances](https://scikit-learn.org/stable/modules/model_evaluation.html) de classification : si l'IA fait bien son travail, et comment.

```python
from sklearn import metrics
```

## Variables

Comme pour la plupart des langages, le `Python` permet de manipuler différents types de variables : 

- Booléen (`bool`) : Vrai / Faux.
- Entier (`int`).
- Texte (`str`).
- Liste (`list`).
- Réel (`float`).

Contrairement à certains langages (#Pascal), le type de variable est précisé lorsqu’on attribue une valeur à la variable.

Ainsi, si on stocke le nombre 8 dans la variable `dinosaure`, elle sera du type `**int**`.

```bash
dinosaure = 8
print(type(dinosaure))
# Ce qui affiche
>> int
```

Mais si on stocke “vive la MIASHS” dans la variable `dinosaure`, elle sera du type `**str**`.

```bash
dinosaure = "vive la MIASHS"
print(type(dinosaure))
# Ce qui affiche
>> str
```

## Opérateurs

Les opérateurs sont utilisés pour réaliser des opérations sur des variables et des valeurs.

En `Python`, les opérateurs sont séparés dans différents groupes :

- Opérateurs arithmétiques.
- Opérateurs d’assignement.
- Opérateurs de comparaison.
- Opérateurs logiques.
- Opérateurs d’identité.
- Opérateurs d’appartenance.
- Opérateurs de comparaison (Bitwise).

### Opérateurs arithmétiques

Les opérateurs arithmétiques sont utilisés avec des valeurs numériques pour réaliser des opérations mathématiques courantes :

| Opérateur | Nom | Exemple |
| --- | --- | --- |
| + | Addition | x + y |
| - | Soustraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulo | x % y |
| ** | Exponentielle | x ** y |
| // | Division Euclidienne | x // y |

### Opérateurs d’assignement

Les opérateurs d’assignement sont utilisés pour assigner des valeurs à des variables.

| Opérateur | Exemple | Équivalence |
| --- | --- | --- |
| = | x = 5 | x = 5 |
| += | x += 5 | x = x + 5 |
| -= | x -= 5 | x = x - 5 |
| *= | x *= 5 | x = x * 5 |
| /= | x /= 5 | x = x / 5 |
| %= | x %= 5 | x = x % 5 |
| //= | x //= 5 | x = x // 5 |
| **= | x **= 5 | x = x ** 5 |

### Opérateurs de comparaison

Les opérateurs de comparaison sont utilisés pour comparer deux valeurs.

| Opérateur | Nom | Exemple |
| --- | --- | --- |
| == | Egal | x == y |
| |= | Non égal | x |= y |
| > | Plus grand que | x > y |
| < | Plus petit que | x < y |
| >= | Plus grand ou égal | x >= y |
| <= | Plus petit ou égal | x <= y |

### Opérateurs logiques

Les opérateurs logiques sont utilisés pour combiner des instructions conditionnelles.

| Opérateur | Description | Exemple |
| --- | --- | --- |
| and | Retourne true si les deux instructions sont vraies | x < 5 and x < 10 |
| or | Retourne true si l’une des deux instructions sont vraies | x < 5 or x < 4 |
| not | Inverse le résultat, retourne false si le résultat est true | not(x < 5 and x < 10) |

### Opérateurs d’identité

Les opérateurs d’identité sont utilisés pour comparer des objets, non pas s’ils sont égaux, mais si ils sont actuellement le même objet avec le même emplacement mémoire.

| Opérateur | Description | Exemple |
| --- | --- | --- |
| is | Retourne true si les deux variables sont le même objet | x is y |
| is not | Retourne true si les deux objets ne sont pas le même objet |  x is not y |

### Opérateurs d’appartenance

Les opérateurs d’appartenance sont utilisés pour tester si une séquence est présente dans un objet.

| Opérateur | Description | Exemple |
| --- | --- | --- |
| in | Retourne true si une séquence avec la valeur spécifiée est présente dans l’objet | x in y |
| not in | Retourne true si une séquence avec la valeur spécifiée n’est pas présente dans l’objet | x not in y |

### Opérateurs de comparaison (Bitwise)

Les opérateurs bitwise sont utilisés pour comparer des nombres binaires.

| Opérateur | Nom | Description |
| --- | --- | --- |
| & (et commercial) | AND | Définit chaque bit à 1 si les deux bits sont 1 |
| | (pipe) | OR | Définit chaque bit à 1 si l’un des deux bits est 1 |
| ^  | XOR | Définit chaque bit à 1 si uniquement l’un des deux bits est 1 |
| ~ (tilde) | NOT | Inverse tout les bits |

## Structures

### Listes

**Créer une liste vide.**

```python
NomListe = list()
```

**Compléter la liste.**

```python
NomListe.append(Item1) # Les items peuvent être des nombres, du texte, etc.
# Par exemple
NomListe.append ("dinosaure")
NomListe.append (34.6)
```

**Créer et remplir une liste.**

```python
NomListe = ["dinosaure", "pancakes"] # Liste de mots
NomListe = [1, 2, 3] # Liste de chiffres
NomListe = [17, "pirouette", 3, "cacahouète"] # Liste mixte
NomListe = list(range(20))
NomListe = list(range(0, 10)) # Liste de chiffres de 0 à 9
NomListe = list(range(1, 10, 2)) # Liste de chiffres de 1 à 10 en allant de 2 en 2
```

**Mesurer sa longueur.** 

```python
LongueurListe = len(NomListe)
```

**Accéder à un élément.**

```python
Element = NomListe[3] #4ème élément (l'index commence à 0)
```

**Liste de listes.**

```python
MegaListe = [Liste1, Liste2, Liste3]
```

**Accéder à un élément d’une liste de listes.**

```python
Element = MegaListe[2][0] #3ème liste, 1er élément (l'index commence à 0)

```

**Ordonner les données.**

```python
NomListe.sort() # Ordonner les données d'une liste
```

### Tableaux

Ils permettent de stocker, visualiser et manipuler les jeux de données facilement grâce à des [DataFrame](http://www.python-simple.com/python-pandas/creation-dataframes.php).

**Import.**

```python
from pandas import DataFrame as df
import pandas as pd
```

**Sélectionner des colonnes / lignes particulières.**

Par indices (lignes, colonnes).

```python
df.iloc[0,5] # 1ère ligne, 5ème colonne
df.iloc [0:5, 0:3] # 1ère à 5ème lignes et 1ère à 3ème colonnes
df.iloc[:, 0:3] # toutes les lignes et 1ère à 3ème colonnes
df.loc[:, 'NomColonne'] # toutes les lignes et colonne "NomColonne"
```

Par position.

```python
df.head(5) # Afficher les 5 premières lignes
df.head(10) # Afficher les 10 premières lignes
```

**Comprendre le contenu.**

```python
df.index # Noms des lignes
df.columns # Noms des colonnes
df.dtypes # Types de données du tableau
df.columns.__str__().lower() # Passer le contenu en minuscules
df.columns.__str__().upper() # Passer le contenu en majuscules
df.size # Quantité d'informations contenues dans le tableau
df.shape # Dimensions (Nombre de lignes et colonnes)
```

**Modifier.**

```python
pd.factorize() # Obtenir une liste des modalités de la variable (similaire SELECT DISTINCT en SQL)
pd.to_numeric() # Convertir en nombre (similaire à inttostr() en Pascal)
df.astype(NomType) # Convertir en type de variable à préciser
df.copy() # Permet de dupliquer un tableau
```

## Fonctions

---

### Fonctions utiles

**Importer un fichier .csv (comptatible avec `Excel`).**

```python
from pandas import read_csv
import pandas as pd
```

On précise :

- Le *fichier* souhaité (ou son *[chemin](https://www.pcastuces.com/pratique/astuces/5995.htm)* s’il se situe dans un répertoire différent).
- S'il possède des *entêtes* (ici, aucune).
- La colonne qui sert d'*index*, c'est-à-dire de référence, du style un numéro unique, comme les clés en BDD (ici, la première colonne, donc 0, sert d'index).
- Le type de *séparateur* *de* *données* (par défaut : `,`).
- Le type de *séparateur* *décimal* (par défaut : `.`, souvent `,` pour des jeux de données européens).

```python
data = pd.read_csv('NomFichier.csv', header = 0, index_col = 0, sep= ';', decimal = ',')
```

Il est donc important d’ouvrir le fichier avant pour vérifier ces informations

À noter qu’on peut aussi importer un jeu de données directement depuis le web. 

```python
data = pd.read_csv('https://UrlDuFichierFinissantPar.csv', header = 0, index_col = 0, sep = ';', decimal = ',')
```

**Afficher du texte et des variables.**

```python
print (”Go les MIASHS”)
```

Ce qui nous donne :

```bash
Go les MIASHS
```

On peut aussi mélanger du texte brut avec des variables.

```python
prenom = "Stéphane"
nom = "Chrétien"
print ("Directeur de l'UFR :", prenom, nom)
```

Ce qui nous donne :

```bash
>> Directeur de l'UFR : Stéphane Chrétien
```

**Visualiser les données.**

Cela permet de voir rapidement le type de données et leur répartition. Cela permet d’orienter les décisions concernant les traitements et tests à effectuer.

```python
df.sort_values() # Ordonner les données d'un dataframe
describe() # Equivalent à summary() en R : résume les données
```

### Créer une fonction

Il existe un large éventail de **fonctions prédéfinies**, mais il arrive qu’on ait besoin de réaliser régulièrement le même **ensemble de traitements**. Pour éviter d’abuser du copier-coller, on peut alors définir ses propres fonctions.

Pour ce faire, on utilise `def`, on **nomme** la fonction (utiliser un nom assez explicite, tout en évitant qu’il soit trop long si on y fait souvent appel). 

Puis, on précise s’il y a des variables en **entrée** (par exemple pour afficher des données, les tranformer, etc.). Il est possible qu’il n’y ait aucun paramètre en entrée (comme pour un compteur par exemple). 

On utilise les `:` pour préciser que le **bloc d’instructions** va suivre. On décrit ensuite les instructions après **indentation** (précise le début du bloc et la fin du bloc).

Enfin, on peut préciser des variables de **sortie** (si on effectue des calculs par exemple). De même, il se peut qu’il n’y ait pas de paramètres de sortie.

```python
def NomFonction (paramètre_1, paramètre_2, paramètre_3):
 
	# Instruction 1
	# Instruction 2
	# Instruction 3

	return sortie_1, sortie_2
```

On peut ensuite appeler cette fonction autant de fois qu’on le souhaite en spécifiant les paramètres soit directement en suivant l’ordre dans lequel ils ont été déclarés, soit dans un ordre différent en précisant les paramètres.

**Exemple**

```python
def CarteEtu (nom, prenom, numetu)

	print ("--- Carte étudiante ---")
	print ("Nom :", nom)
	print ("Prénom :", prenom)
	print ("Numéro étudiant :", numetu)
```

On peut alors soit appeler la fonction en précisant les variables en entrée en suivant le même ordre.

```python
CarteEtu (”Chrétien”, “Stéphane”, 219574)
```

Ce qui nous affiche  :

```bash
>> --- Carte étudiante ---
	 Nom : Chrétien
	 Prénom : Stéphane
	 Numéro étudiant : 219574
```

Mais si on ne se souvient plus de l’ordre, ou qu’on aime se rebeller, on peut préciser à quoi correspondent nos variables en entrée.

```python
CarteEtu (numetu = 219574, prenom = “Stéphane”, nom =”Chrétien”)
```

Ce qui nous affiche  :

```bash
>> --- Carte étudiante ---
	 Nom : Chrétien
	 Prénom : Stéphane
	 Numéro étudiant : 219574
```

## Boucles & Conditions

### **Conditions et instructions `If`**

Le python supporte les conditions logiques classiques provenant des mathématiques :

- Egal : `a == b`
- Non égal : `a != b`
- Inférieur à : `a < b`
- Inférieur ou égal à : `a <= b`
- Supérieur à : `a > b`
- Supérieur ou égal à : `a >= b`

Ces conditions peuvent être utilisés dans plusieurs méthodes, la plus commune des utilisations reste les conditions `if` et les boucles.

Une condition `if` est écrite en utilisant le mot clé `if`.

**Exemple**

```python
a = 33
b = 200

if b > a:
	print("b est plus grand que a")
```

Dans cet exemple, nous utilisons deux variables : `a` et `b` qui sont utilisées par l’instruction if pour tester si `b` est plus grand que `a` , sachant que `a` est égal à `33` et que `b` est égal à `200`, nous savons que `200` est plus grand que `33`, nous écrivons donc que “b est plus grand que a”.

### Indentation

Le python se base sur l’indentation (une tabulation au début de la ligne), pour définir la portée du code. Les autres langages utilisent principalement les “curly-brackets” : `{ }` pour cette utilisation.

**Exemple (qui génèrera une erreur)**

```python
a = 33
b = 200

if b > a:
print("b est plus grand que a") # Pas d'indentation, la portée n'est pas définie
```

### Elif

Le mot-clé `elif` est plus communément utilisé comme `else if` dans les autres langages. C’est la façon de dire “Si la condition précédente n’était pas vraie, alors essayer cette condition”.

**Exemple**

```jsx
a = 33
b = 33

if b > a:
	print("b est plus grand que a")
elif a == b:
	print("a et b sont égaux")
```

### Else

`Else` est utilisé dans le cas ou la ou les conditions précédentes ne sont pas remplies

**Exemple**

```jsx
a = 200
b = 33

if b > a:
	print("b est plus grand que a")
elif a == b:
	print("a et b sont égaux")
else:
	print("a est plus grand que b")
```

### And

Le terme `and` est un opérateur logique, et utilisé pour combiner des instructions conditionnelles.

**Exemple**

```jsx
a = 200
b = 33
c = 500

if a > b and c > a:
	print("Les deux conditions sont vraies")
```

### Or

`or` est un opérateur logique utilisé comme `and` pour combiner des instructions conditionnelles.

**Exemple**

```jsx
a = 200
b = 33
c = 500

if a > b or a > c:
	print("Au moins une des conditions est vraie")
```

### Pass

Les instructions `if` ne peuvent pas être vides, mais si pour une raison vous avez un `if` sans contenu, utilisez l’instruction `pass` pour empêcher la génération d’erreurs.

**Exemple**

```jsx
a = 33
b = 200

if b > a:
	pass
```

### Boucles `While`

Avec les boucles `while`, nous pouvons éxecuter une suite d’instructions tant qu’une condition est vraie.

**Exemple**

```jsx
i = 1
while i < 6:
	print(i)
	i += 1
```

<aside>
⚠️ Pensez à incrémenter (+1) i, sinon la boucle sera infinie.

</aside>

Les boucles `while` requièrent des variables déjà déclarées, c’est pour cela que dans cet exemple nous déclarons `i` et définissons sa valeur à `1`.

### Break

L’instruction `break` est utilisée pour stopper les boucles, même si la condition active est vraie.

**Exemple**

```jsx
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1
```

### Continue

Avec l’instruction `continue` nous pouvons stopper l’itération actuelle, puis continuer avec la suivante

**Exemple**

```python
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)
```

### Else

Comme pour les `if`,  nous pouvons exécuter un bloc de code quand la condition n’est plus vraie.

**Exemple**

```python
i = 1
while i < 6:
	print(i)
	i += 1
else:
	print("i n'est plus plus petit que 6")
```

### Les Boucles `For`

Une boucle `for` est utilisée pour itérer sur une séquence, qui peut être une liste, un dictionnaire, une chaîne de carctère etc.

Ce type de boucle ressemble moins aux boucles `for` d’autres langages. Elle fonctionne plus comme une méthode d’itération trouvée dans les langages de programmation orienté objet.

Avec la boucle `for` nous pouvons éxecuter une suite d’instructions, pour chaque item dans une liste, une suite ou autre...

**Exemple**

```python
fruits = ["pomme", "banane", "cerises"]
for x in fruits:
	print(x)
```

La boucle `for` ne nécessite pas d’indexer une variable déclarée au préalable.

### Boucler dans une chaîne de caractères (String)

Même les chaîne de caractères (String) sont des objets itérables, ils contiennent une séquence de caractères :

**Exemple**

```python
for x in "banane":
	print(x)
```

### Break

Avec l’instruction `break` nous pouvons stopper une boucle avant qu’elle ne soit passée par tout les items :

**Exemples**

```python
fruits = ["pomme", "banane", "cerise"]
for x in fruits:
	print(x)
	if x == "banane":
		break
```

```python
fruits = ["pomme", "banane", "cerise"]
for x in fruits:
	if x == "banane":
		break
	print(x)
```

### Continue

L’instruction `continue`est utilisée pour stopper l’itération actuelle et continuer à la prochaine : 

**Exemple**

```python
fruits = ["pomme", "banane", "cerise"]
for x in fruits:
	if x == "banane":
		continue
	print(x)
```

### La fonction `range()`

Pour boucler dans un suite de code un certain nombre de fois, nous pouvons utiliser la fonction `range()`.

La fonction `range()` retourne une séquence de nombres, démarrant de 0 par défaut, et s’incrémentant par 1 (par défaut), et se termine par le nombre spécifié.

**Exemple**

```python
for x in range(6):
	print(x)
```

<aside>
⚠️ Notez que `range(6)` comprend les valeurs de 0 à 5 et non de 0 à 6, c’est le nombre d’itérations.

</aside>

La fonction `range()` commence par défaut à 0 comme valeur de départ. Cependant il est possible de spécifier une valeur de départ en ajoutant un paramètre : `range(2, 6)`, ce qui veut dire les valeurs de 2 à 6 (N’incluant pas 6)

**Exemple**

```python
for x in range(2, 6):
	print(x)
```

Il est aussi possible de spécifier une valeur d’incrément (qui est par défaut 1) en ajoutant un troisième paramètre : `range(2, 30, 3)` : 

**Exemple**

```python
for x in range(2, 30 ,3):
	print(x)
```

### Else

L’instruction `else` dans une boucle `for` permet de spécifier un bloc de code qui sera exécuté quand la boucle se termine :

**Exemple**

```python
for x in range(6):
	print(x)
else:
	print("Boucle terminée")
```

<aside>
⚠️ Notez que le bloc `else` ne sera pas exécuté si la boucle est stoppée par un `break`

</aside>

**Exemple**

```python
for x in range(6):
	if x == 3: break
	print(x)
else:
	print("Boucle terminée")
```

### Pass

Les boucles `for` ne peuvent pas être vides, mais si pour une raison vous avez une boucle `for` avec aucun contenu, insérez l’instruction `pass` pour éviter les erreurs.

**Exemple**

```python
for x in [0, 1, 2]:
	pass
```

## Graphiques

---

Cela permet de voir rapidement le type de données et leur répartition. Cela permet d’orienter les décisions concernant les traitements et [tests](https://www.notion.so/Cours-Python-Stagiaires-b6077b03b28e462997b3cab2aa3d0c85) à effectuer.

**Courbe**

```python
from matplotlib import pyplot # Librairie

pyplot.plot(data) # Créer une courbe
pyplot.show() #Afficher la courbe
```

**Histogramme**

```python
import matplotlib.pyplot as plt # Librairie

plt.hist(data) # Afficher un histogramme
```

**Nuage de points**

```python
import matplotlib.pyplot as plt # Librairie

plt.scatter(data1, data2) # Créer le nuage
plt.show() #Afficher le nuage
```

## Statistiques

<aside>
💡 Si vous ne disposez pas des librairies et/ou modules utilisés, il suffit de les installer en se référant au chapitre à ce propos.

</aside>

### Statistiques descriptives

```python
import pandas as pd # Librairie
df = pd.dataframe(data)
df.describe() # Equivalent à summary() en R : résume les données

import numpy # Librairie
numpy.sum(data) # Somme
numpy.mean(data) # Moyenne
numpy.median(data) # Médiane
numpy.var(data) # Variance
numpy.std(data) # Ecart-Type
numpy.percentile(data, 25) # Percentile (ici on a précisé 25, soit Q1, on peut aussi mettre 75 pour Q3 ou tout autre percentile entre 1 et 100))

from scipy import stats # Librairie
stats.mode(data) # Mode (variable avec le plus gros effectif)
```

### Calculs

```python
round() # Arrondir
r2 = metrics.r2_score(donnees_reelles, donnees_predites) # Coefficient de détermination (à quel point le modèle explique les données)
```

### Statistiques inférentielles (tests)

[Récapitulatif Tests Statistiques](https://drive.google.com/file/d/1HCrS5oVhnTjMpFRnBLYlykfv_ZYR7a0n/view?usp=sharing)

<aside>
💡 Si vous ne disposez pas des librairies et/ou modules utilisés, il suffit de les installer en se référant au chapitre à ce propos.

</aside>


### Tests de normalité

**Test de Shapiro-Wilk**

Test de Normalité (suit une Loi Normale).

```python
from scipy.stats import shapiro # Librairie
shapiro(data) # Fonction (où data représente le tableau de données, qu'on peut nommer dinosare ou pancakes si on veut
```

### Tests de corrélation

**Test de Pearson**

Test de corrélation (lien d’évolution entre des variables).

```python
from scipy. stats import pearsonr # Librairie
pearsonr(data) # Fonction
```

**Test de Spearman**

Test de corrélation (lien d’évolution entre des variables) basé sur les rangs (leur classement, leur position par rapport aux autres) et non les valeurs.

```python
from scipy. stats import spearmanr # Librairie
spearmanr(data) # Fonction
```

**Test du Chi-Deux**

Tester si des variables qualitatives sont dépendantes.

```python
from scipy.stats import chi2_contingency # Librairie
chi2_contingency(data) # Fonction
```

### Tests paramétriques 

**Test de Student**

Tester si les moyennes de deux grands échantillons indépendants sont significativement différentes.

```python
from scipy.stats import ttest_ind # Librairie
ttest_ind(data1, data2) # Fonction où data1 et data2 représentent les jeux de données à comparer, là encore, on les nommes comme on le souhaite)
```

**Test d’Analyse de la Variance (ANOVA)**

Tester si les moyennes de plusieurs grands échantillons sont significativement différentes.

```python
from scipy.stats import f_oneway # Librairie
stat, p = f_oneway(data1, data2, data3) # Fonction où data1, data2 et data3 représentent les jeux de données à comparer
```

### Tests non-paramétriques

**Test Mann-Whitney**

Comparer la distribution de deux petits échantillons indépendants.

```python
from scipy.stats import mannwhitneyu # Librairie
stat, p = mannwhitneyu(data1, data2) # Fonction où data1 et data2 représentent les jeux de données à comparer
```

**Test de Wilcoxon**

Comparer la distribution de deux petits échantillons indépendants en se basant sur leurs rangs.

```python
from scipy.stats import wilcoxon # Librairie
wilcoxon(data1, data2) # Fonction où data1 et data2 représentent les jeux de données à comparer
```

## Machine Learning

💡 Pour un tutoriel pas à pas, se référer à ce [Notebook](https://colab.research.google.com/drive/1il2ATJY_97tQaJGQPs4MnAdTnL3tb5Gk?usp=sharing#scrollTo=nqdXdZa8RI5J).

### Deep Learning

#### PyTorch

**Objectifs**

`PyTorch` est une librairie `Python` très pratique pour le Machine Learning. Il s’avère très pratique quand on fait appel à des réseaux neuronaux profonds (*Deep Learning*).

**Librairie**

On doit d’abord installer la librairie sur le terminal de commande.

```powershell
pip install torch
```

On l’appelle ensuite comme on le fait pour les autres.

```python
import torch
```

**Utilisation**

💡 [Tutoriel](https://ledatascientist.com/debuter-avec-pytorch/) en français.

### Gradient Boosting

On utilise un [module](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html) de la bibliothèque SciKit-Learn.

```python
from sklearn.ensemble import GradientBoostingRegressor
```

💡 Pour un tutoriel pas à pas, se référer à ce [Notebook](https://colab.research.google.com/drive/1il2ATJY_97tQaJGQPs4MnAdTnL3tb5Gk?usp=sharing#scrollTo=nqdXdZa8RI5J).

On va ensuite séparer les données en 2 parties : 

- Un jeu de données assez grand (au moins la moitié) pour que le modèle puisse apprendre à prédire.
- Un plus petit jeu de données pour qu’il puisse s’entraîner.

S’il ne s’entraîne pas, il sera bon sur les données sur lesquelles il a appris, mais très mauvais en généralisation, c’est ce qu’on appelle de l’**overfitting**.

### Random Forest

On utilise un autre [module](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) de la bibliothèque SciKit-Learn.

```python
from sklearn.ensemble import RandomForestRegressor
```

On va ensuite séparer les données en 2 parties : 

- Un jeu de données assez grand (au moins la moitié) pour que le modèle puisse apprendre à prédire.
- Un plus petit jeu de données pour qu’il puisse s’entraîner.

💡 Pour un tutoriel pas à pas, se référer à ce [Notebook](https://colab.research.google.com/drive/1il2ATJY_97tQaJGQPs4MnAdTnL3tb5Gk?usp=sharing#scrollTo=nqdXdZa8RI5J).

## Modèles Linéaires

### Régressions simple et multiple

On utilise encore un [module](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso) de la bibliothèque Scikit-Learn.

```python
from sklearn.linear_model import LinearRegression # Librairie

model = LinearRegression().fit(X, y) # Créer la régression à partir de X (variable indépendante) et y (variable dépendante)
model.score(X, y) # Score de régression (coefficient de détermination R2)
model.coef_ # Coefficient(s) de régression (β1, β2, etc.) NB : il s'agit d'un modèle simple lorsqu'on a uniquement β1Rég
model.intercept # Coefficient β0 (ordonnée à l'origine)
predict(X) # Prédire grâce au modèle
model.summary() # On affiche les statistiques importantes (AIC, BIC, R2, R2, ajusté, résidus, etc.)
```

### Régression logistique

On utilise un autre [module](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) de la même bibliothèque.

```python
from sklearn.linear_model import LogisticRegression # Librairie

model = LogisticRegression().fit(X, y) # Créer la régression à partir de X (variable indépendante) et y (variable dépendante)
model.score(X, y) # Score de régression (coefficient de détermination R2)
model.coef_ # Coefficient(s) de régression (β1, β2, etc.) NB : il s'agit d'un modèle simple lorsqu'on a uniquement β1Rég
model.intercept # Coefficient β0 (ordonnée à l'origine)
predict(X) # Prédire grâce au modèle
model.summary() # On affiche les statistiques importantes (AIC, BIC, R2, R2, ajusté, résidus, etc.)
```

# Ressources

[Exercices](https://github.com/mpalenciaolivar/Intro-au-Python) (énoncés et corrigés) par [Miguel Palencia-Olivar](https://github.com/mpalenciaolivar).

[Ressource](https://www.w3schools.com/python/) très complète d’aide et tutos.

[Tutoriel](https://ledatascientist.com/debuter-avec-pytorch/) sur `PyTorch` en français.

[Notebooks](https://www.numerical-tours.com/python/) explicatifs (Machine Learning, optimisation, ondelettes, etc.).

[Notebook](https://colab.research.google.com/drive/1il2ATJY_97tQaJGQPs4MnAdTnL3tb5Gk?usp=sharing) sur le Quantile Boosting & Random Forest sur des données temporelles.


---
&copy; [As'](https://github.com/astridgcn) & [Ben'](https://github.com/SayneGit)
