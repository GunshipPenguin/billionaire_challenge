from challenge import Challenge
import flask

class c1(Challenge):
    '''
    Challenge 1
    Hidden element with CSS
    '''

    def __init__(self):
        super()
        self._id = 'f6fd1656d79b06918bb5cf85c8bae58c3884deaf'
        self._hints = {}

    def get_response(self, app):
        return app.send_static_file('c1/index.html')
