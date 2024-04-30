from os import chdir
from pydub import AudioSegment
from pydub.playback import play



if __name__ == "__main__":
    chdir("Sounds")
    note = AudioSegment.from_wav("C.wav")
    play(note)

