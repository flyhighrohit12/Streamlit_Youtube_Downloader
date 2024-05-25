import streamlit as st
from pytube import YouTube
import os
import tempfile

st.title('YouTube Video Downloader')

url = st.text_input('Enter the URL of the YouTube video you wish to download:')

if url:
    yt = YouTube(url)
    st.write(f"Video Title: {yt.title}")
    st.image(yt.thumbnail_url)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    options = [(i.itag, i.resolution) for i in stream]
    selected_option = st.selectbox('Choose the quality/resolution of the video to download:', options, format_func=lambda x: x[1])

    if st.button('Download Video'):
        selected_stream = stream.get_by_itag(selected_option[0])
        safe_filename = yt.title.replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-')

        # Create a temporary directory to store the download
        with tempfile.TemporaryDirectory() as tmpdirname:
            video_path = os.path.join(tmpdirname, safe_filename + ".mp4")
            selected_stream.download(output_path=tmpdirname, filename=safe_filename)

            # Read the file for download
            with open(video_path, 'rb') as f:
                video_data = f.read()
            
            st.download_button(label='Download Video', data=video_data, file_name=safe_filename + ".mp4", mime="video/mp4")
