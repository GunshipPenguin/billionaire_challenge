from challenge import Challenge
import flask

class c12(Challenge):
    '''
    Challenge 12
    Response Esoteric Languages
    '''

    def __init__(self):
        super()
        self._id = '12'
        self._hints = {}

    def get_response(self, app):
       return app.send_static_file('c12/index.html')
