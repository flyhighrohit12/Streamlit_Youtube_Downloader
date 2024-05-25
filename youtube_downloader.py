import streamlit as st
from pytube import YouTube
import tempfile
import os
import webbrowser

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
                download_dir = os.path.join(os.path.dirname(result), os.path.basename(result))
                st.success(download_dir)
                os.rename(result, download_dir)
                webbrowser.open(download_dir)  # This will open the downloaded file
            else:
                st.error(f"Error downloading video: {result}")
    else:
        st.error("Please enter a valid URL")
