# sudo /home/pi/FM/FM_Transmitter_RPi3/fm_transmitter -f 107.3 /home/pi/FM/FM_Transmitter_RPi3/Test_44_16.wav
import subprocess
from threading import Thread

process = None

def start_radio():
	def _start():
		global process
		process = subprocess.Popen(["/home/pi/FM/FM_Transmitter_RPi3/fm_transmitter", "-f", "107.3", "/home/pi/FM/FM_Transmitter_RPi3/Test_44_16.wav"])
	t = Thread(target=start)

def terminate():
	process.terminate()
	process.kill()

if __name__=="__main__":
	start_radio()