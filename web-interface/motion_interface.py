import sqlite3
from bottle import Bottle, route, run, debug
from bottle import redirect, request, template, static_file

app = Bottle()

@app.route('/')
def home():
		return '<a href="/list">Link to list</a>'

@app.route('/images/:filename')
def send_image(filename):
    return static_file(filename , root='/home/pi/motion-detect/images', mimetype='image/jpg')

@app.route('/list')
def list():
		"""
		Show motion detect records in a table
		"""
		conn = sqlite3.connect("/home/pi/motion-detect/motion.db")
		c = conn.cursor()
		c.execute("SELECT * FROM log")
		result = c.fetchall()
		c.close()

		output = template("motion_log", rows=result)
		return output

app.run(host='10.1.10.91', port=8080, debug=True)
