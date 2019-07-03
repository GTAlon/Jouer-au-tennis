# Quand jouer au tennis #

Le projet est composé de plusieurs étapes :
*	Analyser les données sous le format d'une table de décision
*	Construire la matrice de décision
*	Trouver l’arbre décisionnel le plus pertinent avec l’algorithme
*	Stocker le résultat dans un fichier
*	Mettre sous format HTML/JS/CSS/JSON le résultat obtenu
 	
 	## Les outils ##

*	Algorithme ID3 ( Iterative Dichtomiser 3 )
*	Fichier Excel ou texte contenant les données étudiées
*	IDLE Python
*	Notepad++
*	Uwamp (serveur web local)
*	API JQuery

J’ai utilisé une petite matrice, « jouer au tennis ». Pour ce faire, j’ai décomposé le processus en plusieurs étapes :

![](https://github.com/GTAlon/Jouer-au-tennis/blob/master/image018.png)

1.	J’ai ouvert le fichier en entrée. 
2.	J’ai traité la première ligne qui correspond aux noms des attributs que j’ai stocké dans une variable.
3.	J’ai initialisé une boucle « while » qui prend chaque ligne du document, les sépare et les place dans une liste ce sont les attributs non cibles.
4.	J’ai créé une autre variable liste qui prend uniquement les dernières valeurs de chaque ligne du document, ces valeurs représentent les attributs cibles.
5.	Puis j’initialise l’algorithme, j’affiche le résultat et j’ouvre un fichier pour écrire le résultat à l’intérieur.

Voici le programme : 

![](https://github.com/GTAlon/Jouer-au-tennis/blob/master/image021.png)

Voici le résultat en sortie :

![](https://github.com/GTAlon/Jouer-au-tennis/blob/master/image022.png)

La dernière consigne du stage est de mettre le résultat sous forme de page HTML.
On m’a fourni un plugin Jquery permettant de crée un arbre de décision dynamique via des boutons et des questions.
J’ai utilisé le résultat en sortie pour crée un processus de questionnement.
*	La variable « decisions » peut établir un ou plusieurs variable « answer » 
*	La variable « answer » crée un bouton
*	La variable « class » permet de choisir une couleur pour la variable « answer »
*	La variable « message » comme son nom l’indique, envoie un message.

Le code émet cette page.

![](https://github.com/GTAlon/Jouer-au-tennis/blob/master/image026.png)

J’ai cliqué sur Ensoleillé.

 ![](https://github.com/GTAlon/Jouer-au-tennis/blob/master/image028.png)

Ensuite sur Fort. 
 
Voici la réponse.

![](https://github.com/GTAlon/Jouer-au-tennis/blob/master/image030.png)
 
