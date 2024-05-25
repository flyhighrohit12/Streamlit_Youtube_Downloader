import streamlit as st
from pytube import YouTube
import os

def download_youtube_video(url, resolution='720p'):
    yt = YouTube(url)
    stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
    if stream:
        # Set filename and download path
        filename = yt.title.replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-')
        download_path = os.path.join(os.getcwd(), filename + ".mp4")
        
        # Download the video
        stream.download(filename=filename)
        return download_path
    else:
        return None

st.title('YouTube Video Downloader')

url = st.text_input('Enter the URL of the YouTube video you wish to download:')
if url:
    try:
        yt = YouTube(url)
        st.write(f"Video Title: {yt.title}")
        st.image(yt.thumbnail_url)
        
        if st.button('Download Video'):
            download_path = download_youtube_video(url)
            if download_path:
                st.success(f"Video successfully downloaded to: {download_path}")
            else:
                st.error("Failed to download the video. Please check the URL or try a different resolution.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
