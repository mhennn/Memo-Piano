# MEMO-PIANO 🎹🎶

Do you love music? Want to turn your message into a simple piano notes? This program lets you create and harmonize songs using your own words

### Features
- 🎶 Turn your message into a music notes
- 🎶 Generate music within a seconds
- 🎶 Customized at your own pace

### Streamlit Preview
![Memo-Piano-Interface](/interface/ui_interface.png)
![Demo-Preview](/demo/demo.gif)

### Usage instructions
1. Requirements installation
```bash
pip install -r requirements.txt
```
2. Run the application
```bash
streamlit run app.py
```

### Notes behind every message
```bash
self.NOTE_MAP = {'A': 60, 'B': 61, 'C': 62, 'D': 63, 'E': 64, 'F': 65, 'G': 66, 'H': 67, 'I': 68, 'J': 69, 'K': 70, 'L': 71, 'M': 72, 'N': 73, 'O': 74, 'P': 75, 'Q': 76, 'R': 77, 'S': 78, 'T': 79, 'U': 80, 'V': 81, 'W': 82, 'X': 83, 'Y': 84, 'Z': 85}
```

### Notes description
```bash
# Default to instrument Piano
self.track = 0
# How long the silence of song  
self.time = 0
# How long the notes will be played
self.duration = 30
# How loud the notes 0-127
self.volume = 100
```
---
##### Build your message with your own notes 🎶