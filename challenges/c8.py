from challenge import Challenge
import flask

class c8(Challenge):
    '''
    Challenge 8
    ASCII Binary Values
    '''

    def __init__(self):
        super()
        self._id = '7c100d2f1d51dbeee5edab2b9d7c9c65694941243554536ab40a8690ecfb56ba'
        self._hints = {1: 'ASCII'}

    def get_response(self, app):
        return app.send_static_file('c8/index.html')
