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
        try:
            # Download video and get the temporary file path
            file_path = download_video(url)
            # Provide the link to download the file
            with open(file_path, "rb") as file:
                btn = st.download_button(
                    label="Download Video",
                    data=file,
                    file_name="downloaded_video.mp4",
                    mime="video/mp4"
                )
            os.unlink(file_path)  # Optionally delete the temp file after serving it
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
