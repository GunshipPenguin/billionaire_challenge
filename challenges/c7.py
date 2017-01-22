from challenge import Challenge
import flask

class c7(Challenge):
    '''
    Challenge 7
    Satoshi Base58 Encoding
    '''

    def __init__(self):
        super()
        self._id = '3aed4348ed11e6adf1b54885b297078070ac4556'
        self._hints = {1: 'Base58 Encoding'}

    def get_response(self, app):
        return app.send_static_file('c7/index.html')
