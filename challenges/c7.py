from challenge import Challenge
import flask

class c7(Challenge):
    '''
    Challenge 7
    Satoshi Base58 Encoding
    '''

    def __init__(self):
        super()
        self._id = 'a1adda29d338287fe42d20c1a7d6e32481129a9b'
        self._hints = {1: 'Base58 Encoding'}

    def get_response(self, app):
        return app.send_static_file('c7/index.html')
