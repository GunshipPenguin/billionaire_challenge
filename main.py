from flask import Flask
from challengeswrapper import ChallengesWrapper

challengesWrapper = ChallengesWrapper()
app = Flask(__name__)

@app.route('/<challenge_id>')
def challenge(challenge_id):
    '''
    Controller that gives responses for a specific challenge. challenge_id is
    the unique id of the challenge. If challend_id does not represent a valid
    challenge, return 404.
    '''
    challenge = challengesWrapper.get_challenge(challenge_id)

    if (not challenge):
        return 'Not found', 404

    return challenge.get_response(app)


@app.route('/<challenge_id>/hint/<hint>')
def hint(challenge_id, hint):
    '''
    Controller that gives responses for challenge hints. hint is the hint
    number for the challenge with id challenge_id. If hint is not a valid
    hint number for the challenge with id challenge_id, return 404.
    '''
    challenge = challengesWrapper.get_challenge(challenge_id)

    # Ensure that challenge_id is valid
    if (not challenge):
        return 'Not found', 404

    # Ensure that the hint number provided is a valid integer
    hintNum = 0
    try:
        hintNum = int(hint)
    except:
        print ('asdf')
        return 'Invalid hint number', 404

    # Ensure that the hint number is a valid hint number
    if (not challenge.get_hint(hintNum)):
        return 'Invalid Hint Number', 404

    return challenge.get_hint(hintNum)

if __name__ == '__main__':
    app.run()
