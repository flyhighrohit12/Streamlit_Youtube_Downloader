import streamlit as st
from pytube import YouTube
import os
from tempfile import NamedTemporaryFile

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # Create a temporary file to store download
    temp_file = NamedTemporaryFile(delete=True, suffix=".mp4")
    stream.download(output_path=temp_file.name[:-len(temp_file.name.split('/')[-1])], filename=temp_file.name.split('/')[-1])
    # Return file handle to avoid deleting it before downloading
    return open(temp_file.name, 'rb')

def main():
    st.title("YouTube Video Downloader")
    url = st.text_input("Enter the URL of the YouTube video:")

    if st.button("Download Video"):
        if url:
            with st.spinner('Downloading... Please wait'):
                # File is downloaded and opened here
                file_handle = download_video(url)
                st.download_button(
                    label="Click here to download the video",
                    data=file_handle,
                    file_name="downloaded_video.mp4",
                    mime="video/mp4",
                    on_click=lambda: file_handle.close()  # Ensure file handle is closed after download
                )
        else:
            st.error("Please enter a valid YouTube URL")

if __name__ == "__main__":
    main()
