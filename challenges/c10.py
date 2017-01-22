from challenge import Challenge
import flask

class c10(Challenge):
    '''
    Challenge 10
    Response Esoteric Languages
    '''

    def __init__(self):
        super()
        self._id = '3167edc3d1bcf789d56e2455d78d848aa29bbe8e'
        self._hints = {}

    def get_response(self, app):
       return app.send_static_file('c10/index.html')
