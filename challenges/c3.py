from challenge import Challenge
import flask

class c3(Challenge):
    '''
    Challenge 3
    JavaScript XOR
    '''

    def __init__(self):
        super()
        self._id = '0545b77581c302da4a59f52eeee4dc62904ad851'
        self._hints = {1: 'XOR'}

    def get_response(self, app):
        return app.send_static_file('c3/index.html')
