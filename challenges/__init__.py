from os.path import dirname, basename, isfile
import glob
import sys

modules = glob.glob(dirname(__file__)+"/c*[0-9].py")
sys.path.append(dirname(__file__))

# Load all of the modules containing the challenge classes
modules = [basename(path)[:-3] for path in modules]
modules = [__import__(mod) for mod in modules]

# Extract the challenge class from each module
challengeClasses = []
for module in modules:
    moduleName = module.__name__
    try:
        challengeClasses.append(getattr(module, moduleName))
    except:
        print('WARNING: Your class or module is named incorrectly in challenge: ' + moduleName)
