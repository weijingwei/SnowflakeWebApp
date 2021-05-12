import pandas as pd
from flask import Flask, render_template, request
from snowflake import connector

app = Flask("my website")


@app.route('/')
def homepage():
    return render_template('index.html', dfhtml=dfhtml)


@app.route('/submit')
def submitpage():
    return render_template('submit.html')


@app.route('/thanks4submit', methods=['POST'])
def thanks4submit():
    colorName = request.form.get("cname")
    username = request.form.get("uname")
    return render_template("thanks4submit.html", colorName=colorName, username=username)

cnx = connector.connect(
    account='xda06983',
    user='weijingwei',
    password='Biptwjw@205491',
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)

cur = cnx.cursor()
cur.execute("SELECT * FROM COLORS")
rows = pd.DataFrame(cur.fetchall(), columns=['Color UID', 'Color Name'])
dfhtml = rows.to_html()
print(dfhtml)

app.run()
