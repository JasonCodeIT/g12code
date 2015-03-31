__author__ = 'Jason Poh'
import abc


class BaseObject(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def to_dict(self):
        '''
            Abstract method to support easy printing to JSON format
        '''
        return
