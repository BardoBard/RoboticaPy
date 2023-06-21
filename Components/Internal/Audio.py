import pygame
import os

class Audio:

    BEEP =  "./Components/sounds/beep.wav"
    AHHOOH = "./Components/sounds/AhhOoh.mp3"
    BWUA = "./Components/sounds/bwua.mp3"
    FREEBIRD = "./Components/sounds/freebird.mp3"
    SCREAM = "./Components/Internal/Scream.mp3"
    STATICNOISES = "./Components/Internal/static_robot_noises.mp3"

    # Constructor
    def __init__(self):
        pygame.mixer.init()
        print(os.getcwd())
        print(__file__)

    # Play sound
    def play_sound(self):
        """
        :return: void
        """
        pygame.mixer.music.play()
    
    def play_sound(self, sound):
        """
        :string sound: location of sound file
        :return: void
        """
        sound_obj = pygame.mixer.Sound(sound)
        sound_obj.play()

    # Stop sound
    def stop_sound(self):
        """
        :return: void
        """
        pygame.mixer.music.stop()

    # Set volume
    def set_volume(self, volume):
        """
        :param volume: volume to set
        :return: void
        """
        pygame.mixer.music.set_volume(volume)

    # Get volume
    def get_volume(self):
        """
        :return: volume
        """
        pygame.mixer.music.get_volume()

    # Set sound
    def set_sound(self, sound):
        """
        :param sound: sound to set
        :return: void
        """
        pygame.mixer.music.load(sound)
        
    

if __name__ == '__main__':
    audio = Audio()
    audio.play_sound("freebird.mp3")
    # wait for the sound to finish(15 seconds)
    pygame.time.wait(15000)
