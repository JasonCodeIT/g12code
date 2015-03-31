__author__ = 'Jason Poh'
from classes import baseobject

def list_to_json(objlist):
    '''
    :param objlist: a list of BaseObject as defined in 'classes/baseobject.py'
    :return: a list of dictionaries
    '''
    list_of_dict = []
    for item in objlist:
        list_of_dict.append(item.to_dict())
    return list_of_dict