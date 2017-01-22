from challenge import Challenge
import flask

class c11(Challenge):
    '''
    Challenge 11
    Win screen
    '''

    def __init__(self):
        super()
        self._id = '0aaeb7a4cf49f562b6c806f70f3aff98ecf6353c'
        self._hints = {}

    def get_response(self, app):
       return app.send_static_file('c11/index.html')
