from challenge import Challenge
import flask

class c2(Challenge):
    '''
    Challenge 2
    '''

    def __init__(self):
        super()
        self._id = '7dd683c43334e4777b46d87dd98e678cb9805c2b'
        self._hints = {}

    def get_response(self, app):
        return app.send_static_file('c2/index.html')
