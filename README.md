1. Test Foods
2. Code for detecting volt drop and test
3. Find Sounds
4. Code for playing sounds
pydub??
pip install pygobject


from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("note.wav")
print('playing sound using pydub')
play(song)

sudo apt-get install ffmpeg libavcodec-extra
pip install pydub