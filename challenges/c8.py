from challenge import Challenge
import flask

class c8(Challenge):
    '''
    Challenge 8
    ASCII Binary Values
    '''

    def __init__(self):
        super()
        self._id = '148f2c3d5f873e59ea58d618702f761f4bc8442c'
        self._hints = {1: 'ASCII'}

    def get_response(self, app):
        return app.send_static_file('c8/index.html')
