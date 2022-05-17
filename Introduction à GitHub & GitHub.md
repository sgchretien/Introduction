# Introduction à GitHub.
---

# **Légende du cours**

---

# Ceci est un titre majeur

## Ceci est un sous-titre

**Ceci est un point important**

📝 Ceci est un exemple single line

⚠️ Ceci est une mise en garde

💡 Ceci est un conseil

[Ceci est un texte avec un lien vers un site ressource](https://www.pierre-giraud.com/git-github-apprendre-cours/presentation-git-github/)

**Exemple**

```python
# Ceci est un exemple de code
# >> Ceci est une sortie de commande
```

# Introduction

## Git et GitHub

Avant toute chose, Git et GitHub sont deux services bien distincts.

Git est un système de contrôle de version très populaire chez les développeurs. Il a été créé par Linus Torvalds en 2005 et est aujourd’hui maintenu par Junion Hamano.

Git est utilisé pour :

- Tracker les changements de codes.
- Tracker qui a fait ces changements.
- Collaborer sur du code.

### Qu’est-ce que fait Git ?

- Il gère des projets avec des **Repositories (Repo)**.
- Il permet de **Cloner** des projets en faisant une copie locale.
- Contrôler et tracker les changements avec le **Staging** et le **Committing**.
- **Branch** et **Merge** pour permettre de travailler sur différentes parties d’un projets.
- **Pull** la dernières version d’un projet sur la copie locale.
- **Push** les mises à jour locales au projet principal.

### Travailler avec Git

- Initialiser Git dans un dossier, en faisant un, un **Repository**.
- Git créé un dossier caché pour garder la traces des changements dans ce dossier.
- Quand un fichier un modifié, ajouté, ou supprimé, il est considéré comme **modifié**.
- Vous sélectionnez les fichiers que vous voulez **Stage**.
- Les fichiers **Staged** sont **Commit,** ce qui demande à Git de stocker une version **Permanante** des fichiers.
- Git permet de voir l’historique de chaque commit.
- Vous pouvez revenir en arrière sur chaque commit.
- Git ne stocke pas de copie séparée de chaque fichier dans chaque commit, mais il garde la trace des changements fait dans tout les commits.

### Pourquoi Git ?

- Plus de 70% des développeurs utilisent Git.
- Les développeurs peuvent travailler ensemble de n’importe où.
- Cela permet de garder l’historique complet d’un projet.
- Et de revenir à des versions plus anciennes d’un projet.

### Qu’est-ce que GitHub ?

- Git n’est pas la même chose que GitHub.
- GitHub créé des outils qui utilisent Git.
- GitHub est le plus grand hébergeur de code source dans le monde.
- Nous allons voir comment utiliser Git avec GitHub.

# Installer et utiliser Git

---

Vous pouvez télécharger Git gratuitement depuis [ce site](https://www.git-scm.com/).

---

## Utiliser Git en terminal de commandes

Pour commencer à utiliser Git, nous allons d’abord ouvrir un terminal de commandes.

Pour Windows, vous pouvez utiliser Git Bash, qui est inclu dans Git pour Windows. Pour Mac et Linux, vous pouvez utiliser le terminal intégré.

La première chose que nous allons faire, c’est de vérifier que Git est correctement installé :

```bash
git --version
# >> git version 2.32.0.windows.1
```

Si Git est installé, la sortie de la commande devrait être `git versrion X.Y`.

### Configurer Git

---

Maintenant, apprenez à Git qui vous êtes. C’est important pour les systèmes de contrôle de versions, comme chaque commit utilise cette information.

```bash
git config --global user.name "Votre joli nom"
git config --global user.email "votre@joli.email"
```

Pensez à changer le nom et l’adresse mail en fonction de vous. Vous songerez sûrement à utiliser ces informations quand vous vous inscrirez sur github.

<aside>
⚠️ Utilisez le paramètre `global` ****pour mettre le nom et l’adresse email pour chaque repository sur votre ordinateur
Si vous souhaitez mettre un nom et un email juste pour le repo dans lequel vous êtes, vous pouvez supprimer le paramètre `global`

</aside>

### Créer un dossier Git

---

Maintenant, créons un nouveau dossier pour notre projet :

```bash
mkdir MonProjet
cd MonProjet
```

`mkdir` crée un nouveau dossier.

`cd` permet de se déplacer dans le dossier souhaité.

Maintenant que nous sommes dans le dossier voulu. Nous pouvons initialiser Git !

<aside>
💡 Si vous avez déjà un dossier que vous voulez utiliser pour Git :
Déplacez vous dans celui-ci avec l’explorateur de fichier, faites un clic-droit et sélectionnez “Git Bash here”

</aside>

### Initialiser Git

---

Une fois que vous êtes dans le bon dossier, vous pouvez initialiser Git dans celui-ci :

```bash
git init
# >> Initialized empty Git repository in /Votre/Dossier/.git/
```

Et voilà ! Vous avez créé votre premier repo Git !

---

# Créer de nouveaux fichiers

---

Vous venez de créer votre premier repo git, cependant il est vide.

Ajoutons donc quelques fichiers, ou créez en un avec votre éditeur de fichier préféré. Sauvegardez-le et déplacez-le dans le dossier que vous venez de créer.

Pour cet exemple je vais créer un fichier en Python très simple comme ceci :

**Exemple**

```python
def bonsoir(nom):
    print("Bonsoir ", nom)

bonsoir("Vous")
```

Sauvegardons le dans notre nouveau dossier en tant que `bonsoir.py`.
Retournons sur notre terminal et listons les fichiers qu’il y a dans notre dossier :

```bash
ls
# >> bonsoir.py
```

`ls` va lister les différents fichiers présents dans le dossier. Nous pouvons voir que ```bonsoir.py``` est présent.

Puis nous pouvons vérifier avec `git status` pour vérifier qu’il est présent dans notre repo :

**Exemple**

```bash
git status
# >> On branch master
# No commits yet
#
# Untracked files :
#     (use "git add ..." to include in what will be commited)
#       bonsoir.py
#
# nothing added to commit but untracked files present (use "git add" to track)
```

Maintenant, git connait notre fichier, mais ne l’a pas ajouté à notre repo.

Les fichiers présents dans votre repo peuvent avoir deux états :

- Tracked - les fichiers que Git connait et qui sont ajoutés dans votre repo.
- Untracked - fichiers qui sont dans votre dossier, mais qui ne sont pas ajoutés à votre repo.

Quand vous voulez ajouter des fichiers à un repo vide, ils sont tous **Untracked.** Pour que git puisse les track, vous aurez besoin de les **Stage**, ou les ajouter à l’environnement de **Staging**.

## Environnement de Staging

---

Une des fonctions principales de Git est l’environnement de **Staging** et les **Commits.**

Pendant votre travail, nous serez sûrement amenés à ajouter, modifier ou supprimer de s fichiers. Mais dès que vous atteindrez une étape de votre projet, vous aurez besoin d’ajouter vos fichiers à l’environnement de **Staging**.

Les fichiers **Staged** sont prêts à être **commit** dans le repo sur lequel vous êtes en train de travailler. Nous verrons les aspects du `commit` très bientôt.

Pour l’instant, maintenant que nous avons terminé de travailler avec notre fichier `bonsoir.py`, nous pouvons l’ajouter à notre environnement de **Staging**.

```bash
git add bonsoir.py
```

Notre fichier devrait être **Staged**, regardons maintenant le statut de notre git.

```bash
git status
# >> On branch master
#
# No commits yet
#
# Changes to be committed:
# (use "git rm --cached ..." to unstage)
#   new file: bonsoir.py
```

Le fichier a bien été ajouté à notre environnement de staging.

### Ajouter plus qu’un fichier à notre repo

---

Vous pouvez aussi ajouter plus qu’un seul fichier à la fois. Ajoutons donc deux fichiers dans notre dossier de travail.

Un fichier `README.md` qui décrit le repo.

**Exemple**

```markdown
# Bonsoir !

Ceci est un exemple de Readme qui décrit votre repo
```

Et un autre fichier.

**Exemple**

```python
def salut(nom):
	print("Salut ! ", nom)

salut("ben")
```

Maintenant que nous avons nos deux fichiers, ajoutons les dans notre environnement de staging :

```bash
git add --all
```

En utilisant le paramètre `--all` au lieu de chaque fichier, cela va `stage` tous les changements (nouveau, modifié, supprimé) de fichiers.

```bash
git status
# On branch master
#
# No commits yet
# 
# Changes to be committed:
#  (use "git rm --cached ..." to unstage)
#       new file:   README.md
#       new file:   bonsoir.py
#       new file:   salut.py
```

Maintenant que nos 3 fichiers sont ajouté à notre environnement de staging, nous somme prêts pour faire notre premier `commit` !

# Commits

---

Maintenant que nous avons terminé notre travail, nous sommes prêts à `commit` nos changements sur notre repo.

Ajouter des commits permet de garder la trace des changements dans notre travail. C’est le moment du projet où vous pouvez retourner en arrière si vous souhaitez trouver un bug, ou effectuer un changement.

Quand on `commit`, nous devons obligatoirement inclure un message.
*Si vous êtes seul·e sur un repo et que vous avez pas d’idée de message... Ce site peut vous aider : [http://whatthecommit.com/](http://whatthecommit.com/)*

**Exemple**

```bash
git commit -m "Premier Commit" !
# >> [master (root-commit) 22ec6e] Premier Commit !
#	3 files changed, 11 insertions(+)
# create mode 100644 README.md
# create mode 100644 bonsoir.py
#	create mode 100644 salut.py 
```

La commande `commit` effectue un commit, et le paramètre `-e "message"` ajoute un message.

L’environnement de staging a bien été commit dans notre repo.

## Commit Logs

---

Pour voir l’historique des commits pour un repo, vous pouvez utiliser la commande `log`.

**Exemple**

```bash
git log
# commit 9743198d9e734df337b6592568a036d39e4a0436 (HEAD -> master)
# Author: VotreJoliNom
# Date:   Mon May 9 01:03:06 2022 +0200

    Premier Commit !
```

# Les branches

---

Dans Git, les `branches` sont des versions séparées du repo principal.

Imaginons que vous avez un projet très large, et que vous avez besoin de mettre à jour le design de celui-ci.

Comment cela fonctionnerait avec et sans Git :

**Sans git :**

- Créer des copies de tout les fichiers nécessaires pour empêcher que cela impacte la version principale.
- Commencer à travailler sur le design et trouver le code qui dépend d’autre codes dans d’autres fichiers, qui ont aussi besoin d’être changés.
- Faire des copies des fichiers dépendants.
- Sauvegarder tout les fichiers, mettre une note sur les noms des copies sur lesquelles vous étiez en train de travailler.
- Etc.

**Avec git :**

- Créer une nouvelle branche appellée new-design, éditer le code directement sans impacter la branche principale.
- Terminer le travail sur la branche.
- Fusionner le branche new-design avec la branche principale.

Les branches permettent de travailler sur différentes parties d’un projet sans impacter la branche principale

Quand le travail est terminé, une branche peut être **merged** *(fusionnée)* sur la branche principale / le projet principal.

## Créer une nouvelle branche

Imaginons que nous voulons mettre à jour notre fichier `bonsoir.py`.

Nous sommes en train de travailler dans notre repo local, et nous ne voulons pas déranger ou possiblement casser le projet principal.

Nous allons donc créer une nouvelle `branche` :

```bash
git branch bonsoir-python-bonjour
```

Vérifions que cette `branche` a bien été créée :

```bash
git branch
	bonsoir-python-bonjour
* master
```

Nous pouvons voir que la nouvelle branche “bonsoir-python-bonjour” est bien présente, mais l’astérisque (`*`) derrière `master` montre que nous sommes actuellement sur cette `branche`.

`checkout` est une commande utilisée pour se déplacer de branches en branches *(comme tarzan).* Dans notre cas :

```bash
git checkout bonsoir-python-bonjour
# >> Switched to branch 'bonsoir-python-bonjour'
```

Maintenant que nous sommes dans notre nouvel environnement de travail, nous pouvons commencer à modifier nos fichiers.

Pour cet exemple, je vais créer une fonction `bonjour` dans le fichier `bonsoir.py`, en plus de cela je vais ajouter un fichier `merci.py`.

**Exemple**

```python
def bonsoir(nom):
    print("Bonsoir ", nom)

def bonjour(nom):
		print("Bonjour ", nom)

nom = "Ben"

bonjour(nom)
bonsoir(nom)
```

```python
def merci(nom):
	print("Merci ", nom)

nom = "Ben"

merci(nom)
```

Une fois que les changements ont été fait, nous pouvons vérifier le statut de notre `branche` actuelle :

```bash
git status
# >> On branch bonsoir-python-bonjour
# Changes not staged for commit:
#  (use "git add ..." to update what will be committed)
#  (use "git restore ..." to discard changes in working directory)
#        modified:   index.html
#        added: merci.py
#
# no changes added to commit (use "git add" and/or "git commit -a")
```

Vérifions ce qu’il se passe ici :

- Il y a des changements dans notre fichier bonsoir.py, mais le fichier n’est pas **staged** pour le `commit`.

Nous avons donc besoin d’ajouter notre fichier dans notre environnement de staging pour cette `branche`.

```bash
git add --all
```

Une fois que cela est fait nous pouvons vérifier le statut de la `branche`.

```bash
git status
# >> On branch bonsoir-python-bonjour
# Changes to be committed:
#  (use "git restore --staged ..." to unstage)
#   modified: bonsoir.py
#   new file: merci.py
```

Maintenant que nous sommes satisfaits de nos changements, nous pouvons commit dans la `branche`.

```bash
git commit -m "Fonction bonjour ajoutée"
# >> [bonsoir-python-bonjour 0312c55] Fonction bonjour ajoutée
# 2 files changed, 12 insertion(+)
# create mode 100644 merci.py
```

## Branche d’urgence

Imaginon que nous n’avons pas encore terminé avec la branche `bonsoir-python-bonjour` mais que nous avons besoin de régler une erreur dans la branche principale `master`.

On ne veut pas créer d’autres problèmes dans le master, ni dans notre branche d’ajout de fonctions tant qu’elle n’est pas terminée.

Nous allons donc créer une nouvelle branche pour gérer l’urgence :

```bash
git checkout -b fix-urgence
# >> Switched to a new branch 'fix-urgence'
```

Maintenant que nous avons créé notre nouvelle branche, nous pouvons régler le problème et les erreurs sans avoir à déranger les autres branches.

**Exemple**

```python
def bonsoir(nom):
    print("Bonsoir ", nom)

def bonjour(nom):
		print("Bonjour ", nom)

nom = "Ben"

bonjour(nom)
bonsoir(nom)
print("Erreur imaginaire gérée")
```

Une fois que les changements ont été fait, nous pouvons sauvegarder notre fichier pour envoyer notre édition dans la branche `master`

Vérifions le statut de la branche :

```bash
git status
# >> On branch fix-urgence
# Changes not staged for commit:
#  (use "git add ..." to update what will be committed)
#  (use "git restore ..." to discard changes in working directory)
#        modified:   bonsoir.py
#
# no changes added to commit (use "git add" and/or "git commit -a")
```

Ajoutons notre fichier a notre environnement de staging, et commit :

```bash
git add bonsoir.py
git commit -m "bonsoir.py, modifié pour fix d'erreur"
# >> [fix-urgence dfa79db] updated index.html with emergency fix
# 1 file changed, 1 insertion(+)
```

Maintenant que nous avons un fix prêt pour la branche `master`, nous avons besoin de fusionner nos deux branches.

## Se déplacer entre les branches *(comme Tarzan)*

Maintenant que nous avons travaillé sur notre branche secondaire, nous pouvons essayer de revenir sur la branche principale.

Actuellement, nous sommes dans la branche `bonsoir-python-bonjour`, vérifions les fichiers qui sont actuellement présents dans notre dossier :

```bash
ls
# >> README.md bonsoir.py salut.py merci.py
```

Nous pouvons voir que notre nouveau fichier `[merci.py](http://merci.py)` est bien présent.

Voyons ce qu’il se passe quand nous changeons de branche pour `master`.

```bash
git checkout master
# >> Switched to 'master'
```

Notre nouveau fichier ne fait pas partie de notre cette branche, vérifions les fichiers présents.

```bash
ls
# >> README.md bonsoir.py salut.py
```

`merci.py` n’est plus présent ! Et si nous ouvrons `bonsoir.py`nous pouvons voir que la fonction `bonjour.py` n’est pas non plus présente.

# Fusionner (merge) les branches

Notre fix imaginaire est prêt, fusionnons donc les branches `master` et `fix-urgence`.

D’abord, nous avons besoin de revenir sur notre branche principale :

```bash
git checkout master
# >> Switched to branch 'master'
```

Maintenant nous allons `merge` *(fusionner)* la branche actuelle `master` avec la branche `fix-urgence`.

```bash
git merge fix-urgence
# >> Updating 22ec6e..dfa79db
# Fast-forward
# bonsoir.py | 1 +-
# 1 file changed, 1 insertion(+)
```

Sachant que la branche `fix-urgence` provient directement de `master`, et qu’aucun autre changement n’a été fait sur master pendant que nous travaillions, Git voit cela comme la continuité de `master`. Donc cela permet de “fast-forward” (Accélérer le processus), et de juste pointer `master` et `fix-urgence` sur le même commit.

Maintenant que `master` et `fix-urgence` sont essentiellement les mêmes branches, nous pouvons supprimer la branche `fix-urgence`, sachant qu’elle n’est plus utile.

```bash
git branch -d fix-urgence
# >> Deleted branch fix-urgence (was dfa79db).
```

# GitHub

---

Nous allons maintenant s’attaquer a GitHub, qui est là pour nous faciliter la vie avec Git.

Allez sur [GitHub](https://github.com) et créez un compte.

<aside>
💡 Pensez à utiliser la même adresse mail que vous avec utilisée dans la configuration Git.

</aside>

Une fois que vous êtes sur votre page d’accueil GitHub, vous pouvez désormais commencer à travailler sur un projet commun à d’autres développeurs.

Pour faciliter la collaboration et empêcher que n’importe qui puisse contribuer à un projet, GitHub à mit en place un système de `fork` qui permet de créer une copie du repo sur votre compte GitHub.

## Fork un repo

---

`Fork` est une fonction utile de Github dans le cas où vous voulez travailler sur un projet sans partir de zéro.

Connectez vous à github et [allez sur la page du projet auquel vous êtes associé](https://github.com/StagiairesMIASHS) :

Une fois que vous êtes sur le repo qui vous intéresse, vous pouvez cliquer sur le bouton **Fork** en haut d’un repo :

![fork](https://github.com/StagiairesMIASHS/Introduction/blob/main/fork.png?raw=true)

Une fois que vous aurez cliqué sur le bouton, une nouvelle fenêtre s’affichera : 

![forking](https://github.com/StagiairesMIASHS/Introduction/blob/main/forking.png?raw=true)

Cette fenêtre vous propose de changer le nom et la description du repo que vous êtes en train de fork. Une fois que vous avez cliqué sur “Create Fork”, la page du repo sur votre compte s’affichera.

Une fois que vous êtes sur votre page de repo vous voudrez sûrement commencer à coder !

Cliquez sur le bouton vert `Code` et copiez le lien comme ci-dessous :

![url](https://github.com/StagiairesMIASHS/Introduction/blob/main/url.png?raw=true)

Rendez-vous sur votre terminal préféré et exécutez la commande suivante :

**Exemple**

```bash
git clone <URL>
```

Cela créera une copie locale du repo à l’endroit ou vous aurez ouvert votre terminal.

Voilà ! Vous pouvez commencer à coder !

---

La suite des choses se fera voir en cours, et celui-ci sera mis à jour au fûr et à mesure.

Référez-vous aux [ressources](https://www.notion.so/Intro-GitHub-Stagiaires-704303af3dc54f09b3f03ea4549b2fcf) pour en savoir plus !

---

# Ressources

---

[Tutoriel](https://git-scm.com/book/en/v2) Git (en anglais).

[(Alternative en anglais)](https://www.w3schools.com/git/default.asp?remote=github)

[Cours](https://openclassrooms.com/fr/courses/7162856-gerez-du-code-avec-git-et-github) Git et GitHub (en français).



---
&copy; As' & Ben'
