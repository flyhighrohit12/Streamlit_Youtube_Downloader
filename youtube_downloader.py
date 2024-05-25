import streamlit as st
from pytube import YouTube
import os
from pathlib import Path

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_path = os.path.join(os.getcwd(), stream.default_filename)
        stream.download(os.getcwd())
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
                st.write(f"[Download the video]({result})")
            else:
                st.error(f"Error downloading video: {result}")
    else:
        st.error("Please enter a valid URL")
