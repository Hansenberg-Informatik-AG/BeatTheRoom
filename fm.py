# sudo /home/pi/FM/FM_Transmitter_RPi3/fm_transmitter -f 107.3 /home/pi/FM/FM_Transmitter_RPi3/Test_44_16.wav
import subprocess

process = None



def start_radio():
	global process
	process = subprocess.Popen(["/home/pi/FM/FM_Transmitter_RPi3/fm_transmitter", "-f", "107.3", "/home/pi/FM/FM_Transmitter_RPi3/Test_44_16.wav"])


def terminate():
	process.terminate()
	process.kill()

start_radio()