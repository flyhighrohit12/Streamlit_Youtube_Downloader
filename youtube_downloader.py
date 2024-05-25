import streamlit as st
from pytube import YouTube
import tempfile
import os

st.title('YouTube Video Downloader')

url = st.text_input('Enter the URL of the YouTube video you wish to download:')

if url:
    yt = YouTube(url)
    st.write(f"*Video Title:* {yt.title}")
    st.image(yt.thumbnail_url)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    options = [(i.itag, i.resolution) for i in stream]
    selected_option = st.selectbox('Choose the quality/resolution of the video to download:', options, format_func=lambda x: x[1])

    if st.button('Download Video'):
        selected_stream = stream.get_by_itag(selected_option[0])
        safe_filename = yt.title.replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-')

        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            try:
                # Download the video directly to a temporary file
                selected_stream.download(output_path=os.path.dirname(tmpfile.name), filename=safe_filename)
                tmpfile.close()

                # Provide a download button
                with open(tmpfile.name, 'rb') as f:
                    st.download_button(label="Download Video",
                                       data=f,
                                       file_name=safe_filename + ".mp4",
                                       mime="video/mp4")
            except Exception as e:
                st.error(f"Failed to download the video: {e}")
            finally:
                # Ensure the temporary file is deleted after serving
                if os.path.exists(tmpfile.name):
                    os.remove(tmpfile.name)
