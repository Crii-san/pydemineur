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

def construireCellule(cont = 0, b = False) -> dict:
    lst = [(const.CONTENU, cont), (const.VISIBLE, b)]
    return dict(lst)
'''

'''
