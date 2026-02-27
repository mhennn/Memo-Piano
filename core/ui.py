import streamlit as st

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

    def studio(self):
        with self.container:
            note_field = st.columns(3)
            with note_field[0]:
                chosen_time = st.number_input("Time", key="time_key", min_value=0.0, max_value=100.0, step=0.1)
            with note_field[1]:
                chosen_duration = st.number_input("Duration", key="duration_key", min_value=1.0, max_value=100.0, step=0.1)
            with note_field[2]:
                chosen_volume = st.number_input("Volume", key="volume_key", min_value=1, max_value=127)

            chosen_message = st.text_area("Write your message", key="message_key")