from challenge import Challenge
import flask

class c4(Challenge):
    '''
    Challenge 4
    Cookies
    '''

    def __init__(self):
        super()
        self._id = '94fe6a3196c44b2cd7c2ea7776add10deb1fd968'
        self._hints = {1: 'Exactly what the picture is'}

    def get_response(self, app):
        resp = app.send_static_file('c4/cookie.png')
        resp.set_cookie('next_clue', '6360f685c52760b5c680948c604263cd6c68719c')
        return resp
