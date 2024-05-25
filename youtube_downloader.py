import streamlit as st
from pytube import YouTube
import os

st.title('YouTube Video Downloader')

url = st.text_input('Enter the URL of the YouTube video you wish to download:')
download_path = st.text_input('Enter the path where you want to save the video:', '/path/to/download')

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

        # Check if the specified download path is writable
        if os.access(download_path, os.W_OK):
            try:
                # Download the video directly to the specified path
                final_path = os.path.join(download_path, safe_filename + '.mp4')
                selected_stream.download(output_path=download_path, filename=safe_filename)
                st.success(f"Downloaded successfully to {final_path}")
                st.write("You can now go to the specified path to access your video.")
            except Exception as e:
                st.error(f"Failed to download the video: {e}")
        else:
            st.error("The specified path is not writable. Please check your path and permissions.")
