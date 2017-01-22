from challenge import Challenge
import flask

class c9(Challenge):
    '''
    Challenge 9
    418 I'm a Teapot
    '''

    def __init__(self):
        super()
        self._id = '46d0ffbfddf889fcc4646dd8d60b381cefe18543'
        self._hints = {}

    def get_response(self, app):
        return app.send_static_file('c9/index.html'), 418
