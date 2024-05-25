import streamlit as st
from pytube import YouTube
import tempfile
import os

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        temp_dir = tempfile.mkdtemp()
        download_path = os.path.join(temp_dir, stream.default_filename)
        stream.download(temp_dir)
        return download_path
    except Exception as e:
        return str(e)

st.title("YouTube Video Downloader")

url = st.text_input("Enter the YouTube video URL")

if st.button("Download"):
    if url:
        with st.spinner("Downloading..."):
            result = download_video(url)
            if os.path.isfile(result):
                st.success("Video downloaded successfully!")
                st.download_button(
                    label="Download the video",
                    data=open(result, 'rb'),
                    file_name=os.path.basename(result),
                    mime='video/mp4'
                )
            else:
                st.error(f"Error downloading video: {result}")
    else:
        st.error("Please enter a valid URL")
