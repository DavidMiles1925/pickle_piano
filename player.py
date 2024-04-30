from os import chdir
from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
from threading import Thread
from time import sleep

pickle_pin = 26


notes = {
    26: 'C.wav',
    13: 'D.wav',
    6: 'E.wav',
    5: 'G.wav'
}

def setup_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in notes.keys():
        GPIO.setup(pin, GPIO.IN)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=touch_callback, bouncetime=200)


def play_sound(file_path):
    note_to_play = AudioSegment.from_wav(file_path)
    play(note_to_play)


def touch_callback(channel=None):
    print(f"called {channel}")
    file_path = notes[channel]
    new_thread = Thread(target=play_sound, args=(file_path,))
    new_thread.start()


if __name__ == "__main__":
    setup_pins()
    try:
        while True:
            pass

    except KeyboardInterrupt:
        print("Program closed using Ctrl+C")
        GPIO.cleanup()
