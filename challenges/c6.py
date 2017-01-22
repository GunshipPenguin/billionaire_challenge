from challenge import Challenge
import flask

class c6(Challenge):
    '''
    Challenge 6
    PNG Metadata
    '''

    def __init__(self):
        super()
        self._id = '9eaa24f4dd5f3b17291b36958f05e0a6895172f3'
        self._hints = {}

    def get_response(self, app):
        return app.send_static_file('c6/img.png')
