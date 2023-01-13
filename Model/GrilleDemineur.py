# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste

from random import *

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

def getCoordonneeVoisinsGrilleDemineur(grille : list, coord : tuple) -> list:
    if not (type_grille_demineur(grille) == True and type_coordonnee(coord) == True):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord) == True:
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    liste = []
    u, v = coord
    hautG = u - 1, v - 1
    haut = u - 1, v
    hautD = u - 1, v + 1
    G = u, v - 1
    D = u, v + 1
    basG = u + 1, v - 1
    bas = u + 1, v
    basD = u + 1, v + 1
    if isCoordonneeCorrecte(grille, hautG) == True:
        liste.append(hautG)
    if isCoordonneeCorrecte(grille, haut) == True:
        liste.append(haut)
    if isCoordonneeCorrecte(grille, hautD) == True:
        liste.append(hautD)
    if isCoordonneeCorrecte(grille, G) == True:
        liste.append(G)
    if isCoordonneeCorrecte(grille, D) == True:
        liste.append(D)
    if isCoordonneeCorrecte(grille, basG) == True:
        liste.append(basG)
    if isCoordonneeCorrecte(grille, bas) == True:
        liste.append(bas)
    if isCoordonneeCorrecte(grille, basD) == True:
        liste.append(basD)
    return liste

def placerMinesGrilleDemineur(grille : list, nb : int, coord : tuple):
    liste = []
    nbCellules = getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille)
    if nb < 0 or nb >= nbCellules:
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect ")
    if not isCoordonneeCorrecte(grille, coord) == True:
        raise IndexError("« placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    while len(liste) != nb:
        a = construireCoordonnee(randint(0, getNbLignesGrilleDemineur(grille) -1), randint(0, getNbColonnesGrilleDemineur(grille) -1))
        if a == coord:
            a = construireCoordonnee(randint(0, getNbLignesGrilleDemineur(grille) -1), randint(0, getNbColonnesGrilleDemineur(grille) -1))
        if not a in liste:
            liste.append(a)
    for i in range(len(liste)):
        setContenuGrilleDemineur(grille, liste[i], -1)
    compterMinesVoisinesGrilleDemineur(grille)


def compterMinesVoisinesGrilleDemineur(grille : list) -> None:
    a = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = (i, j)
            if contientMineGrilleDemineur(grille, coord) == False:
                coordvoisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
                nb = len(coordvoisins)
                cont = 0
                for k in range(nb):
                    if getContenuGrilleDemineur(grille, coordvoisins[k]) == -1:
                        cont += 1
                    setContenuGrilleDemineur(grille, coord, cont)
    return None

def getNbMinesGrilleDemineur(grille : list) -> int:
    if not type_grille_demineur(grille) == True:
        raise ValueError(" getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    a = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = (i, j)
            if contientMineGrilleDemineur(grille, coord) == True:
                a += 1
    return a

def getAnnotationGrilleDemineur(grille : list, coord : tuple) -> str:
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))

def getMinesRestantesGrilleDemineur(grille : list) -> int:
    nb = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = (i, j)
            if getAnnotationGrilleDemineur(grille, coord) == const.FLAG:
                nb += 1
    return getNbMinesGrilleDemineur(grille) - nb

def gagneGrilleDemineur(grille : list) -> bool:
    a = True
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = (i, j)
            if (contientMineGrilleDemineur(grille, coord) == False) and (isVisibleGrilleDemineur(grille, coord) == False):
                a = False
            elif (contientMineGrilleDemineur(grille, coord)) and isVisibleGrilleDemineur(grille, coord):
                a = False
            elif contientMineGrilleDemineur(grille, coord) == True and getAnnotationGrilleDemineur(grille, coord) != 'Flag':
                a = False
    return a

def perduGrilleDemineur(grille : list) -> bool:
    a = False
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = (i, j)
            if (contientMineGrilleDemineur(grille, coord)) and (isVisibleGrilleDemineur(grille, coord)):
                a = True
                break
    return a

def reinitialiserGrilleDemineur(grille : list) -> None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            coord = (i, j)
            reinitialiserCellule(getCelluleGrilleDemineur(grille, coord))
    return None

#échec
#la fonction empêche de cliquer sur les cases ne contenant pas de mine
'''
def decouvrirGrilleDemineur(grille : list, coord : tuple) -> set:
    s = set()
    setVisibleGrilleDemineur(grille, coord, True)
    g = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    if getContenuGrilleDemineur(grille, coord) == 0:
        for i in range(len(g)):
            setVisibleGrilleDemineur(grille, g[i], True)
            s.add(g[i])
            if getContenuGrilleDemineur(grille, g[i]) == 0:
                for j in getCoordonneeVoisinsGrilleDemineur(grille, g[i]):
                    setVisibleGrilleDemineur(grille, g[j], True)
                    s.add(g[j])
    return s
'''

#échec
'''
def simplifierGrilleDemineur(grille : list, coord : tuple) -> set:
    res = ''
    nbDrapeaux = 0
    b = []
    if isVisibleGrilleDemineur(grille, coord) == False:
        res = set()
    else:
        a = getCoordonneeVoisinsGrilleDemineur(grille, coord)
        for i in a:
            if getAnnotationGrilleDemineur(grille, i) == 'Flag':
                nbDrapeaux += 1
            else :
                b.append(i)
                res.add(i)
        if nbDrapeaux == getContenuGrilleDemineur(grille, coord):
            for j in b:
                setVisibleGrilleDemineur(grille, j, True)
    return res
'''

#échec

'''
def simplifierGrilleDemineur(grille : list, coord : tuple) -> set:
    ensemble = set()
    nbrFlags = 0
    coordVoisin = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    if isVisibleGrilleDemineur(grille, coord) == False:
        return set()
    else:
        for i in range(len(coordVoisin)):
            if grille[getNbLignesGrilleDemineur(coordVoisin)].get(const.ANNOTATION) == const.FLAG \
                    or grille[getNbColonnesGrilleDemineur(coordVoisin)].get(const.ANNOTATION) == const.FLAG:
                nbrFlags += 1
        if getContenuGrilleDemineur(grille, coord) == nbrFlags:
            for j in range(len(coordVoisin)):
                if isVisibleGrilleDemineur(coordVoisin):
                    if getAnnotationGrilleDemineur(grille, coordVoisin) == None:
                        setVisibleGrilleDemineur(True)
                        ensemble.add(coordVoisin)
    return ensemble
'''

#échec
'''
def ajouterFlagsGrilleDemineur(grille : list, coord : tuple) -> list:
    a = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    b = 0
    c = set()
    for i in a:
        if isVisibleGrilleDemineur(grille, i) == False:
            b += 1
        else:
            c.add(i)
    if getContenuGrilleDemineur(grille, coord) == b:
        for j in c:
            cell = getCelluleGrilleDemineur(grille, j)
            cell[const.ANNOTATION] = const.FLAG
    return c   
    '''

