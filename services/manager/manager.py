import pandas as pd
from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)


# MANAGER


# READ RULES
data = pd.read_excel("rules.xlsx", usecols="B")


app.config["numberOfTiles"] = int(data.values[0][0])
app.config["numberOfParts"] = int(data.values[2][0])
app.config["entropyTolerance"] = int(data.values[3][0])
app.config["numberOfWorkers"] = int(data.values[4][0])

print("numberOfTiles: ", app.config["numberOfTiles"])
print("numberOfParts: ", app.config["numberOfParts"])
print("entropyTolerance: ", app.config["entropyTolerance"])
print("numberOfWorkers: ", app.config["numberOfWorkers"])


# MANAGER SERVICE PATHS

@app.route("/")
def showRules():
    return Flask.jsonify({"numberOfTiles: ": (app.config["numberOfTiles"],app.config["numberOfTiles"]), "numberOfParts: ": app.config["numberOfParts"], "entropyTolerance: ": app.config["entropyTolerance"], "numberOfWorkers: ": app.config["numberOfWorkers"]})

@app.route('/setRules', methods=['GET', 'POST'])
def showHome():
    if request.method == 'POST':
        # processing current values
        app.config["numberOfTiles"] = int(request.form.get('var1'))
        app.config["numberOfParts"] = int(request.form.get('var2'))
        app.config["entropyTolerance"] = int(request.form.get('var3'))
        app.config["numberOfWorkers"] = int(request.form.get('var4'))
        # save or process values
        return render_template('manager.html', var1=app.config["numberOfTiles"], var2=app.config["numberOfParts"], var3=app.config["entropyTolerance"], var4=app.config["numberOfWorkers"])
    return render_template('manager.html', var1=app.config["numberOfTiles"], var2=app.config["numberOfParts"], var3=app.config["entropyTolerance"], var4=app.config["numberOfWorkers"])


@app.route("/numberOfTiles")
def getNumberOfTiles():
    return jsonify((app.config["numberOfTiles"],app.config["numberOfTiles"]))
    
@app.route("/numberOfParts")
def getNumberOfParts():
    return jsonify(app.config["numberOfParts"])

@app.route("/entropyTolerance")
def getEntropyTolerance():
    return jsonify(app.config["entropyTolerance"])
    
@app.route("/numberOfWorkers")
def getNumberOfWorkers():
    return jsonify(app.config["numberOfWorkers"])
    
@app.route("/restrictions")
def getRestrictions():
    return jsonify((tileCompatibilityList,tileCompatibilityLookUpTable,binaryLookUpTable))



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
                     
                     
                     
