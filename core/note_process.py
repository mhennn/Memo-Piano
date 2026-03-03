import numpy as np
from scipy.io import wavfile
import io

class NoteProcess:
    def __init__(self, time_delay, duration, volume):
        self.NOTE_MAP = {
            'A': 60, 'B': 61, 'C': 62, 'D': 63, 'E': 64, 'F': 65, 'G': 66,
            'H': 67, 'I': 68, 'J': 69, 'K': 70, 'L': 71, 'M': 72, 'N': 73,
            'O': 74, 'P': 75, 'Q': 76, 'R': 77, 'S': 78, 'T': 79, 'U': 80,
            'V': 81, 'W': 82, 'X': 83, 'Y': 84, 'Z': 85
        }
        self.sample_rate = 44100
        self.time_delay = time_delay
        self.duration = duration
        self.volume = volume / 127.0
        self.PCM_MAX = 32767

    def midi_to_freq(self, midi_note):
        return 440.0 * (2.0 ** ((midi_note - 69) / 12.0))

    def create_music_wav(self, text):
        audio_buffer = []
        
        if self.time_delay > 0:
            silence = np.zeros(int(self.sample_rate * self.time_delay))
            audio_buffer.extend(silence)

        # 2. Convert Text to Sine Waves
        for char in text.upper():
            if char in self.NOTE_MAP:
                freq = self.midi_to_freq(self.NOTE_MAP[char])
                t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), False)
                fade = np.linspace(1.0, 0.0, len(t)) 
                note_wave = self.volume * np.sin(2 * np.pi * freq * t) * fade
                audio_buffer.extend(note_wave)
            else:
                pause = np.zeros(int(self.sample_rate * self.duration))
                audio_buffer.extend(pause)

        audio_array = np.array(audio_buffer)
        audio_int16 = (audio_array * self.PCM_MAX).astype(np.int16)
        
        byte_io = io.BytesIO()
        wavfile.write(byte_io, self.sample_rate, audio_int16)
        byte_io.seek(0)
        return byte_io