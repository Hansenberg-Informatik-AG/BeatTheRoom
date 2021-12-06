import subprocess

process = None

def start_radio(filename):
	global process
	process = subprocess.Popen(["./fm/fm_transmitter", "-f", "100", "-r", filename])

def terminate():
	process.terminate()
	process.kill()
