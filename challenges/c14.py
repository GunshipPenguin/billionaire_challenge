from challenge import Challenge
import flask

class c14(Challenge):
    '''
    Challenge 14
    HTTP 418 I'm a Teapot
    '''

    def __init__(self):
        super()
        self._id = '14'
        self._hints = {1: 'RFC 2324'}

    def get_response(self, app):
        resp = app.send_static_file('c14/index.html')
        return resp, 418
