from challenge import Challenge
import flask

class c4(Challenge):
    '''
    Challenge 4
    Cookies
    '''

    def __init__(self):
        super()
        self._id = '983d09117bf1d67d10356cea9e361bf3fc216d92'
        self._hints = {}

    def get_response(self, app):
        resp = app.send_static_file('c4/cookie.png')
        resp.set_cookie('next_clue', '6360f685c52760b5c680948c604263cd6c68719c')
        return resp
