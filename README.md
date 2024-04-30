# Pickle Piano

## Project Description

This project was born out of curiosity. I saw an influencer playing pickles (I wish I could remember who it was!!) and it stuck with me. I wanted to understand how they may have built such a device, so I decided to build one for myself. The creator I'm thinking of did this in a much more sophistocated way, but with my limited knowledge of music, this is what I came up with. If you are the one who made a crazy cool pickle guitar, please let me know what you did!

## YouTube Video

Link Here
Photo Here

## Building the Device

### Parts List

| Component                         | Quantity | Link                |
| :-------------------------------- | :------: | :------------------ |
| Raspberry Pi (Recommend Zero 2 W) |    1     | link                |
| Jar of Pickles(Whole)             |    1     | Go out in the world |
| Dupont Wires (assorted)           |  1 pack  | link                |

### Diagram

Diagram when finished

### Set Up Raspberry Pi

Link to

### Procedure

1. Download Code
2. Install Dependencies

```bash
sudo apt-get install ffmpeg libavcodec-extra
```

AND

```bash
pip install pydub
```

3. Adjust Settings?
4. Hook Up Pickles

5. Run Code
6. Improve Code!

## My Process

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
