from midiutil import MIDIFile

class NoteProcess:
    def __init__(self):
        self.NOTE_MAP = {
            'A': 69,
            'B': 71,
            'C': 60,
            'D': 62,
            'E': 64,
            'F': 65,
            'G': 67
        }

        self.midi = MIDIFile(1)
        self.midi.addTempo(0, 0, 120)

        # Default to instrument Piano
        self.track = 0
        # How long the silence of song  
        self.time = 0
        # How long the notes will be played
        self.duration = 30
        # How loud the notes 0-127
        self.volume = 100

    def create_music(self, text):
        for char in text.upper():
            if char in self.NOTE_MAP:
                # How high or low the notes
                pitch = self.NOTE_MAP[char]
                self.midi.addNote(self.track, 0, 80, self.time, self.duration, self.volume)
                self.time += self.duration
            elif char == "":
                self.time += self.duration

        return self.saving_music()

    def saving_music(self):
        with open("message.mid", "wb") as output_notes:
            self.midi.writeFile(output_notes)