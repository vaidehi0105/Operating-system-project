import subprocess
from flask import *
from flask_cors import *

app = Flask(__name__)
cors = CORS(app)

def runCmd(cmd):
	param=cmd.split()
	result = subprocess.run(param, stdout=subprocess.PIPE)
	s=result.stdout.decode()
	return s

@app.route('/checkconn',methods=["GET","POST"])
def conn():
	return 'Connected to lab'

@app.route('/runCommand', methods=["GET","POST"])
def command():
	cmd=request.args['cmd']
	x=runCmd(cmd)
	return x


app.run(host='0.0.0.0', port=8082)
