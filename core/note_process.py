from midiutil import MIDIFile
import io

class NoteProcess:
    def __init__(self, time, duration, volume):
        self.NOTE_MAP = {
            'A': 60, 'B': 61, 'C': 62, 'D': 63, 'E': 64, 'F': 65, 'G': 66,
            'H': 67, 'I': 68, 'J': 69, 'K': 70, 'L': 71, 'M': 72, 'N': 73,
            'O': 74, 'P': 75, 'Q': 76, 'R': 77, 'S': 78, 'T': 79, 'U': 80,
            'V': 81, 'W': 82, 'X': 83, 'Y': 84, 'Z': 85
        }

        self.midi = MIDIFile(1)
        self.midi.addTempo(0, 0, 120)

        # Default to instrument Piano
        self.track = 0
        # How long the silence of song  
        self.time = time
        # How long the notes will be played
        self.duration = duration
        # How loud the notes 0-127
        self.volume = volume

    def create_music(self, text):
        for char in text.upper():
            if char in self.NOTE_MAP:
                # How high or low the notes
                pitch = self.NOTE_MAP[char]
                self.midi.addNote(self.track, 0, pitch, self.time, self.duration, self.volume)
                self.time += self.duration
            elif char == "":
                self.time += self.duration

        return self.saving_music()

    def saving_music(self):
        midi_stream = io.BytesIO()
        self.midi.writeFile(midi_stream)
        midi_stream.seek(0)
        return midi_stream