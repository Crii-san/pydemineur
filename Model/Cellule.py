# Model/Cellule.py
#
from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect(cont : int) -> bool:
    if type(cont) != int:
        a = False
    elif cont >= -1 and cont <= 8:
        a = True
    else:
        a = False
    return a

def construireCellule(cont : int = 0, visible : bool = False) -> dict:
    if isContenuCorrect(cont) == False:
        raise ValueError("construireCellule : le contenu", cont, "n’est pas correct")
    if not type(visible) == bool:
        raise TypeError("construireCellule : le second paramètre", type(visible), "n’est pas un booléen")
    lst = [(const.CONTENU, cont), (const.VISIBLE, visible), (const.ANNOTATION, None)]
    return dict(lst)

def getContenuCellule(cell : dict) -> int:
    if type_cellule(cell) == False:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cell[const.CONTENU]

def isVisibleCellule(cell : dict) -> bool:
    if type_cellule(cell) == False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cell[const.VISIBLE]

def setContenuCellule(cell : dict, cont : int) -> None:
    if isContenuCorrect(cont) == False and type(cont) == int:
        raise ValueError("setContenuCellule : la valeur du contenu", cont, "n’est pas correcte.")
    elif isContenuCorrect(cont) == False and type(cont) != int:
        raise TypeError("setContenuCellule : la valeur du contenu", cont, "n’est pas correcte.")
    if type_cellule(cell) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if not type(cont) == int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    else:
        cell[const.CONTENU] = cont
    return None

def setVisibleCellule(cell : dict, visible : bool) -> None:
    if not type_cellule(cell) == True:
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if not type(visible) == bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen.")
    cell[const.VISIBLE] = visible
    return None

def contientMineCellule(cell : dict) -> bool:
    if not type_cellule(cell) == True:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    a = 0
    if getContenuCellule(cell) == -1:
        a = True
    else:
        a = False
    return a

def isAnnotationCorrecte(annot : str) -> bool:
    return bool(annot == None or annot == const.DOUTE or annot ==  const.FLAG)

def getAnnotationCellule(cell : dict) -> str:
    if not type_cellule(cell) == True:
        raise TypeError("getAnnotationCellule : le paramètre", cell[const.ANNOTATION], "n’est pas une cellule ")
    if const.ANNOTATION not in cell:
        cell[const.ANNOTATION] = None
    return cell[const.ANNOTATION]

