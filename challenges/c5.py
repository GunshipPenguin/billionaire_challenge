from challenge import Challenge
import flask

class c5(Challenge):
    '''
    Challenge 5
    Response Header
    '''

    def __init__(self):
        super()
        self._id = '6360f685c52760b5c680948c604263cd6c68719c'
        self._hints = {}

    def get_response(self, app):
        resp = app.send_static_file('c5/index.html')
        resp.headers['X-Next-Clue'] = '9eaa24f4dd5f3b17291b36958f05e0a6895172f3'
        return resp
