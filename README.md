# MEMO-PIANO 🎹🎶

Do you love music? Want to turn your message into a simple piano notes? This program lets you create and harmonize songs using your own words

### Features
- 🎶 Turn your message into a music notes
- 🎶 Generate music within a seconds
- 🎶 Customized at your own pace

### Streamlit Preview
![Memo-Piano-Interface](/interface/ui_interface.png)

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
NOTE_MAP = {'A': 69, 'B': 71, 'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67}
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