import streamlit as st
from pytube import YouTube
import os

def download_video(url, path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)
        return os.path.join(path, stream.default_filename)
    except Exception as e:
        return str(e)

st.title("YouTube Video Downloader")

url = st.text_input("Enter the YouTube video URL")

if st.button("Download"):
    if url:
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        with st.spinner("Downloading..."):
            result = download_video(url, download_path)
            if os.path.isfile(result):
                st.success("Video downloaded successfully!")
                st.write(f"Video saved to your Downloads folder: {result}")
            else:
                st.error(f"Error downloading video: {result}")
    else:
        st.error("Please enter a valid URL")
