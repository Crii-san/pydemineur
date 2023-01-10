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

def construireCellule(cont = 0, visible = False) -> dict:
    lst = [(const.CONTENU, cont), (const.VISIBLE, visible)]
    return dict(lst)

def getContenuCellule(cell : dict) -> int:
    return cell[const.CONTENU]

def isVisibleCellule(cell : dict) -> bool:
    return cell[const.VISIBLE]

def setContenuCellule(cell : dict, cont : int) -> None:
    if isContenuCorrect(cont) != True:
        raise ValueError("setContenuCellule : la valeur du contenu", cont, "n’est pas correcte")
    else:
        cell[const.CONTENU] = cont
    return None

def setVisibleCellule(cell : dict, visible : bool) -> None:
    cell[const.VISIBLE] = visible
    return None

def contientMineCellule(cell : dict) -> bool:
    a = 0
    if getContenuCellule(cell) == -1:
        a = True
    else:
        a = False
    return a

