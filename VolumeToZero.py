
import soco
import time
speakers = soco.discover()


for speaker in speakers:
        CurrentVolume = speaker.volume
        print "%s (%s)" % (speaker.player_name, speaker.ip_address)
        print CurrentVolume
        speaker.play_mode='NORMAL'
        while CurrentVolume > 0:
                speaker.volume = speaker.volume-1
                CurrentVolume = speaker.volume
                print speaker.volume
                time.sleep(1)
speaker.partymode()



