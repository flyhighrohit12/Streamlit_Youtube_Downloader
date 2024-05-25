import streamlit as st
from pytube import YouTube
import os
import re

def sanitize_filename(filename):
    """Remove or replace characters that are not allowed in file names."""
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def ensure_dir_exists(path):
    """Ensure the directory exists, and if not, create it."""
    os.makedirs(path, exist_ok=True)

def save_video(stream, file_path):
    """Save the video file to the path."""
    with open(file_path, 'wb') as file:
        stream.stream_to_buffer(file)

def download_video(url, path):
    """Download the highest resolution video from the provided YouTube URL."""
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    safe_title = sanitize_filename(yt.title)
    file_path = os.path.join(path, safe_title + ".mp4")
    save_video(ys, file_path)
    return file_path

st.title('YouTube Video Downloader')

url = st.text_input('Enter the YouTube video URL')

path = st.text_input('Enter the path to save the video', value=os.getcwd())

if st.button('Download Video'):
    if url and path:
        try:
            ensure_dir_exists(path)  # Ensure the directory exists
            file_path = download_video(url, path)
            st.success(f'Video downloaded successfully! Saved at {file_path}')
        except Exception as e:
            st.error(f'An error occurred: {str(e)}')
    else:
        st.error('Please enter a valid URL and path.')
