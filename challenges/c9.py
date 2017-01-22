from challenge import Challenge
import flask

class c9(Challenge):
    '''
    Challenge 9
    PNG Metadata
    '''

    def __init__(self):
        super()
        self._id = '9'
        self._hints = {}

    def get_response(self, app):
        return app.send_static_file('c9/img.png')
