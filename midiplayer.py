
import pygame
import pygame.midi
import time
import os

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

    def play_midi_file(self, midi_file):
        pygame.mixer.music.load(midi_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def close(self):
        del self.player
        pygame.midi.quit()

if __name__ == "__main__":
    player = MidiPlayer()
    
    print("Available MIDI files:")
    midi_files = [f for f in os.listdir() if f.endswith('.mid')]
    for i, file in enumerate(midi_files):
        print(f"{i + 1}. {file}")
    
    choice = int(input("Enter the number of the MIDI file you want to play: ")) - 1
    
    if 0 <= choice < len(midi_files):
        print(f"Playing {midi_files[choice]}...")
        player.play_midi_file(midi_files[choice])
    else:
        print("Invalid choice. Playing default sequence.")
        player.play_sequence([60, 62, 64, (65, 1), [60, 64, 67]])
    
    player.close()

