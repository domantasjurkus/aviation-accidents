import os, sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
	databaseGenerated = 1 if os.path.isfile('data/data.db') else 0
	print databaseGenerated
	return render_template('index.html', databaseGenerated=databaseGenerated)

# Needed to allow accessing French data via columns
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/france")
def france():
	conn = sqlite3.connect('data/data.db')
	conn.row_factory = dict_factory
	c = conn.cursor()
	data = c.execute("SELECT * FROM ntsb WHERE country LIKE '%France%' AND latitude NOT NULL AND longitude NOT NULL").fetchall()
	conn.close()
	return jsonify(data)

if __name__ == "__main__":
	app.run()