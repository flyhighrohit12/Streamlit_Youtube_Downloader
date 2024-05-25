import streamlit as st
from pytube import YouTube
import os

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        stream.download(download_path)
        return os.path.join(download_path, stream.default_filename)
    except Exception as e:
        return str(e)

st.title("YouTube Video Downloader")

url = st.text_input("Enter the YouTube video URL")

if st.button("Download"):
    if url:
        with st.spinner("Downloading..."):
            result = download_video(url)
            if os.path.isfile(result):
                st.success(f"Video downloaded successfully: {result}")
            else:
                st.error(f"Error downloading video: {result}")
    else:
        st.error("Please enter a valid URL")
