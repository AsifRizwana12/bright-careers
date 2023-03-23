from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru ,India',
    'salary': '10LPA',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi ,India',
    'salary': '15LPA',
  },
  {
    'id': 3,
    'title': 'Front-End Engineer',
    'location': 'Remote',
    'salary': '12LPA',
  },
  {
    'id': 4,
    'title': 'Backend-Engineer',
    'location': 'San Francisco , USA',
    'salary': '$150,000',
  },
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='Bright')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":

  app.run(host='0.0.0.0', debug=True)
