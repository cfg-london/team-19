import json, flask, _mysql
app = flask.Flask(__name__)

db = _mysql.connect(db="datarep", user="root")

POSSIBLE_RESTRAINTS = {
	"country": "Country",
	"years": "Survey"
}

@app.route("/<path:path>")
def index(path):
	return flask.send_from_directory("site", path)

@app.route("/data")
def api():
	query = "SELECT * FROM `table 2`"
	wheres = []

	print(POSSIBLE_RESTRAINTS.keys(), flask.request.args)

	for restraint in POSSIBLE_RESTRAINTS.keys():
		if restraint in flask.request.args.keys():
			where = "WHERE " + POSSIBLE_RESTRAINTS[restraint] + " "
			if restraint == "years":
				where += "BETWEEN " + " AND ".join(flask.request.args[restraint].split("..")[:2])
			else:
				where += "= \"" + flask.request.args[restraint] + "\""

			wheres.append(where)

	if 

	query += " " + " ".join(wheres)
	print(query)
	db.query(query)

	rows = db.store_result()
	rows = rows.fetch_row(0)

	rows = tuple(tuple(rows[i][j].decode("utf-8") for j in range(len(rows[i]))) for i in range(len(rows)))

	return json.dumps(rows)
