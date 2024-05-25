import streamlit as st
from pytube import YouTube
import os

def download_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(output_path=path)

def main():
    st.title("YouTube Video Downloader")
    url = st.text_input("Enter the URL of the YouTube video:")
    path = st.text_input("Enter the download path:", value=os.path.join(os.getenv('USERPROFILE') or os.getenv('HOME'), 'Downloads'))

    if st.button("Download Video"):
        try:
            download_video(url, path)
            st.success("Downloaded Successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
