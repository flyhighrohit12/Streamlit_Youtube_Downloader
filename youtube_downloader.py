import streamlit as st
from pytube import YouTube
import tempfile
import os

st.title('YouTube Video Downloader')

url = st.text_input('Enter the URL of the YouTube video you wish to download:')

if url:
    yt = YouTube(url)
    st.write(f"**Video Title:** {yt.title}")
    st.image(yt.thumbnail_url)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    options = [(i.itag, i.resolution) for i in stream]
    selected_option = st.selectbox('Choose the quality/resolution of the video to download:', options, format_func=lambda x: x[1])

    if st.button('Download Video'):
        selected_stream = stream.get_by_itag(selected_option[0])
        safe_filename = yt.title.replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-')

        with tempfile.TemporaryDirectory() as tmpdirname:
            file_path = os.path.join(tmpdirname, safe_filename + '.mp4')
            # Attempt to download the video
            try:
                selected_stream.download(output_path=tmpdirname, filename=safe_filename)
                st.success("Downloaded successfully!")
            except Exception as e:
                st.error(f"Failed to download the video: {e}")

            # Attempt to open the file and create a download button
            try:
                with open(file_path, 'rb') as f:
                    st.download_button(label="Download Video",
                                       data=f,
                                       file_name=safe_filename + ".mp4",
                                       mime="video/mp4")
            except FileNotFoundError:
                st.error("Failed to find the downloaded file. Please try again.")
