import streamlit as st
from core.note_process import NoteProcess
import time

class UiApp:
    def __init__(self):
        st.markdown(
            "<h1><span style='color:#78BF7D'>Memo-Piano 🎹</span></h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<h6><span style='color:#A66953'>Turn your message into a piano music 🎶</span></h6>",
            unsafe_allow_html=True
        )

        self.container = st.container(border=True)
        self.studio()
        self.chosen_time = 0
        self.chosen_duration = 0
        self.chosen_volume = 0
        self.chosen_message = ""
        
    def studio(self):
        with self.container:
            note_field = st.columns(3)
            with note_field[0]:
                self.chosen_time = st.number_input("Time", key="time_key", min_value=0.0, max_value=100.0, step=0.1)
            with note_field[1]:
                self.chosen_duration = st.number_input("Duration", key="duration_key", min_value=1.0, max_value=100.0, step=0.1)
            with note_field[2]:
                self.chosen_volume = st.number_input("Volume", key="volume_key", min_value=1, max_value=127, value=100, help="default: 100")

            self.chosen_message = st.text_area("Write your message", key="message_key")
            if self.generate_music():
                note_process = self.translate_message()
                midi_data = note_process.create_music(self.chosen_message)
                st.download_button("Download Music", data=midi_data, mime="audio/midi", file_name=f"{self.chosen_message}.midi")

    def translate_message(self):
        self.noteProcess = NoteProcess(self.chosen_time, self.chosen_duration, self.chosen_volume)
        return self.noteProcess

    def generate_music(self):
        if st.button("Create Music"):
            progress_text = f"Creating Music for {self.chosen_message}"
            music_bar = st.progress(0, text=progress_text)

            for music in range(100):
                time.sleep(0.2)
                music_bar.progress(music + 1, text=progress_text)
            time.sleep(1)
            st.success("Successfully generated music 🎶")
            return True