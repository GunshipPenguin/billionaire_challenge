import challenges

class ChallengesWrapper(object):
    '''
    Wrapper around all the challenges module, which contains all the individual
    challenge classes.
    '''

    def __init__(self):
        '''
        Instanstiate all challenges and set up and return the challenges wrapper.
        '''
        # Instantiate an instance of every class in challenges.challengeClasses
        self._challenges = {}
        for challenge in challenges.challengeClasses:
            newChallenge = challenge()
            self._challenges[newChallenge.get_id()] = newChallenge

    def get_challenge(self, id):
        '''
        Given a challenge id, return the challenge object with that id. Returns
        false if id is not a valid id.
        '''
        if id in self._challenges:
            return self._challenges[id]
        else:
            return False
