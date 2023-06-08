import pygame

class Audio:
    # Constructor
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sound.mp3")

    # Play sound
    def play_sound(self):
        """
        :return: void
        """
        pygame.mixer.music.play()
    
    def play_sound(self, sound):
        """
        :param sound: sound to play
        :return: void
        """
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()

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