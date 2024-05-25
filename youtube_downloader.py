import streamlit as st
from pytube import YouTube
import os

def save_video(stream, file_path):
    with open(file_path, 'wb') as file:
        stream.stream_to_buffer(file)

def download_video(url, path):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    file_path = os.path.join(path, yt.title + ".mp4")
    save_video(ys, file_path)
    return file_path

st.title('YouTube Video Downloader')

url = st.text_input('Enter the YouTube video URL')

path = st.text_input('Enter the path to save the video', value=os.getcwd())

if st.button('Download Video'):
    if url and path:
        try:
            file_path = download_video(url, path)
            st.success(f'Video downloaded successfully! Saved at {file_path}')
        except Exception as e:
            st.error(f'An error occurred: {str(e)}')
    else:
        st.error('Please enter a valid URL and path.')
