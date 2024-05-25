import streamlit as st
from pytube import YouTube
import os
from tempfile import NamedTemporaryFile

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # Create a temporary file to store download
    temp_file = NamedTemporaryFile(delete=False)
    stream.download(output_path=temp_file.name[:-len(temp_file.name.split('/')[-1])], filename=temp_file.name.split('/')[-1])
    return temp_file.name

def main():
    st.title("YouTube Video Downloader")
    url = st.text_input("Enter the URL of the YouTube video:")
    if st.button("Download Video"):
        # Show a message while downloading
        with st.spinner('Downloading... Please wait'):
            file_path = download_video(url)
        
        # Provide the link to download the file
        if file_path:
            file_name = os.path.basename(file_path)
            with open(file_path, "rb") as file:
                btn = st.download_button(
                    label="Download Video",
                    data=file,
                    file_name=file_name,
                    mime="video/mp4"
                )
            os.unlink(file_path)  # Optionally delete the temp file after serving it
        else:
            st.error("Failed to download video")

if __name__ == "__main__":
    main()
