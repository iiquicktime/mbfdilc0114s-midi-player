
import pygame
import pygame.midi
import time

class MidiPlayer:
    def __init__(self):
        pygame.init()
        pygame.midi.init()
        self.player = pygame.midi.Output(0)

    def play_note(self, note, velocity=127, duration=0.5):
        self.player.note_on(note, velocity)
        time.sleep(duration)
        self.player.note_off(note, velocity)

    def play_chord(self, notes, velocity=127, duration=0.5):
        for note in notes:
            self.player.note_on(note, velocity)
        time.sleep(duration)
        for note in notes:
            self.player.note_off(note, velocity)

    def play_sequence(self, sequence):
        for event in sequence:
            if isinstance(event, int):
                self.play_note(event)
            elif isinstance(event, list):
                self.play_chord(event)
            elif isinstance(event, tuple):
                self.play_note(event[0], duration=event[1])

    def close(self):
        del self.player
        pygame.midi.quit()

if __name__ == "__main__":
    player = MidiPlayer()
    
    # Example usage
    player.play_note(60)  # Play middle C
    player.play_chord([60, 64, 67])  # Play C major chord
    player.play_sequence([60, 62, 64, (65, 1), [60, 64, 67]])
    
    player.close()
