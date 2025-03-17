import pandas as pd
import flask

app = flask.Flask(__name__)

numberOfTiles = (0,0)
@app.route("/")
def showRules():
    return flask.jsonify({"numberOfTiles: ": numberOfTiles, "numberOfParts: ": numberOfParts, "entropyTolerance: ": entropyTolerance})
    
@app.route("/numberOfTiles")
def getNumberOfTiles():
    return flask.jsonify(numberOfTiles)
    
@app.route("/numberOfParts")
def getNumberOfParts():
    return flask.jsonify(numberOfParts)

@app.route("/entropyTolerance")
def getEntropyTolerance():
    return flask.jsonify(entropyTolerance)



# MANAGER



# READ RULES
data = pd.read_excel("rules.xlsx", usecols="B")

numberOfTiles = (int(data.values[0][0]),int(data.values[1][0]))
numberOfParts = int(data.values[2][0])
entropyTolerance = int(data.values[3][0])



# WAVE FUNCTION TILE LOOKUP TABLE
data = pd.read_excel("restrictions.xlsx", usecols="AI")

tileCompatibilityList = []
tileCompatibilityLookUpTable = {}

ind = 0

for tile in data.values:
    tileCompatibilityList.append(int(tile[0],2))
    tileCompatibilityLookUpTable[2**ind] = int(tile[0],2)
    ind += 1


                                
binaryLookUpTable = {"grass":0b000000001,
                     "wald":0b000000010,
                     "kuh":0b000000100,
                     "strand":0b000001000,
                     "wasser":0b000010000,
                     "fisch":0b000100000,
                     "berg":0b001000000,
                     "bergschnee":0b010000000,
                     "schneemann":0b100000000}
                     
                     
                     
