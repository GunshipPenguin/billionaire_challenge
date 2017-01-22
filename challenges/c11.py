from challenge import Challenge
import flask

class c11(Challenge):
    '''
    Challenge 11
    ASCII Binary Values
    '''

    def __init__(self):
        super()
        self._id = '11'
        self._hints = {}

    def get_response(self, app):
        return app.send_static_file('c11/index.html')
