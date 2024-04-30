from os import chdir
from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
from time import sleep

pickle_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pickle_pin, GPIO.IN)


note = AudioSegment.from_wav("C.wav")


def touch_callback(channel=None):
    play(note)
    print("called")
    sleep(5)



if __name__ == "__main__":
    GPIO.add_event_detect(pickle_pin, GPIO.FALLING, callback=touch_callback, bouncetime=200)
    try:
        while True:
            pass

    except KeyboardInterrupt:
        print("Program closed using Ctrl+C")
        GPIO.cleanup()
