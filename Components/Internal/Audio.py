import pygame

class Audio:
    # Constructor
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("beep.wav")

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