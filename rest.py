import json, flask
app = flask.Flask(__name__)

POSSIBLE_RESTRAINTS = {
	"country": "",
	"years": "",
}

@app.route("/")
def api():
	query = "SELECT * FROM EditedData"
	wheres = []

	for restraint in POSSIBLE_RESTRAINTS.keys():
		if restraint in request.args.keys():
			where = "WHERE " + POSSIBLE_RESTRAINTS[restraint] + " "
			if restraint == "years":
				where += "BETWEEN" + " AND ".join(request.args[restraint].split(".."))[:2]
			else:
				where += "= " + request.args[restraint]

	query += " " + " ".join(wheres)
