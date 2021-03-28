# Un fichier permettant de lancer le programme et de modifier ses paramètres prédéfinis tel que la taille de la
# fenêtre

# Point important: le code representé ici est modulaire, c'est-à-dire que l'interface graphique et le
# labyrinthe lui-même ne se dépendent pas ainsi on peut en faire ce qu'on veut, on pourrait par exemple au lieu d'une
# interface graphique, le représenter sur le terminal

# Autre point important, après discussion avec M.Barbosa, il se trouve que nous ayons mal compris la notion de graphe
# et que nous pensions qu'un tableau en deux dimensions représentait la matrice d'un graphe, mais dans notre cas,
# ca n'est pas un graphe, simplement un tableau de points

from interface import Interface

interface = Interface("Maze [A.PERROT - E.COLLIN]", 1000, 700)
interface.start()
