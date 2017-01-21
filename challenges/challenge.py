from flask import Flask

class Challenge(object):
    '''
    Base challenge class that all other challenges should inherit from.
    '''

    def __init__(self):
        '''
        Construct a new challenge with the specified hint number and
        '''
        self._hints = {}
        self._id = 'BASE'

    def get_response(self, app):
        '''
        Return the flask response that should be sent to the user upon
        requesting this challenge.
        '''
        return flask.response()

    def get_hint(self, hintNum, app):
        '''
        Return the hint with the given hint number.
        '''
        hint = ''
        try:
            hint = self._hints[hintNum]
            return hint
        except:
            return False

    def get_id(self):
        '''
        Return this challenge's id.
        '''
        return self._id
