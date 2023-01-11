# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nbL : int, nbC : int) -> list:
    if nbL <= 0 or nbC <= 0:
        raise ValueError("construireGrilleDemineur : Le nombre de lignes", nbL, "ou de colonnes" , nbC, "est négatif ou nul.")
    a = []
    for i in range(nbL):
        b = []
        for j in range(nbC):
            b.append(construireCellule())
        a.append(b)
    return a

def getNbLignesGrilleDemineur(grille : list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille)

def getNbColonnesGrilleDemineur(grille : list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    a = 0
    for i in grille:
        a = len(i)
    return a

def isCoordonneeCorrecte(grille : list, coord : tuple) -> bool:
    if not (type(grille) == list or type(coord) == tuple or type_grille_demineur(grille) == True or type_coordonnee(coord) == True):
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    if getLigneCoordonnee(coord) >= getNbLignesGrilleDemineur(grille):
        a = False
    elif getLigneCoordonnee(coord) < getNbLignesGrilleDemineur(grille):
        if getLigneCoordonnee(coord) >= 0:
            a = True
        else:
            a = False
    if getColonneCoordonnee(coord) >= getNbColonnesGrilleDemineur(grille):
        b = False
    elif getColonneCoordonnee(coord) < getNbColonnesGrilleDemineur(grille):
        if getColonneCoordonnee(coord) >= 0:
            b = True
        else:
            b = False
    return bool(a and b)

def getCelluleGrilleDemineur(grille : list, coord : tuple) -> dict:
    if not (type(grille) == list or type(coord) == tuple or type_grille_demineur(grille) == True or type_coordonnee(coord) == True):
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    ligne = getLigneCoordonnee(coord)
    colonne = getColonneCoordonnee(coord)
    cellule = ""
    ligne2 = grille[ligne]
    cellule = ligne2[colonne]
    return cellule

def getContenuGrilleDemineur(grille : list, coord : tuple) -> int:
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))

def setContenuGrilleDemineur(grille : list, coord : tuple, cont : int):
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), cont)

def isVisibleGrilleDemineur(grille : list, coord : tuple) -> bool:
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))

def setVisibleGrilleDemineur(grille : list, coord : tuple, visibilite : bool):
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visibilite)

def contientMineGrilleDemineur(grille : list, coord : tuple) -> bool:
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))



