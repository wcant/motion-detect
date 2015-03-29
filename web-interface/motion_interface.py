import sqlite3
from bottle import route, run, debug
from bottle import redirect, request, template

@route("/")
@route("/motion-detect-interface")
def log_list():
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

if __name__ == "__main__":
		debug(True)
		run()