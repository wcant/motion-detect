import sqlite3
from bottle import Bottle, route, run, debug
from bottle import redirect, request, template

app = Bottle()

@route('/')
def home():
		return 'Hello'

@route('/list')
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

run(app, host='10.1.10.91', port=8080, debug=True)
