import streamlit as st
from pytube import YouTube
import os
from tempfile import NamedTemporaryFile

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # Create a temporary file to store download
    temp_file = NamedTemporaryFile(delete=False, suffix=".mp4")
    stream.download(output_path=temp_file.name[:-len(temp_file.name.split('/')[-1])], filename=temp_file.name.split('/')[-1])
    return temp_file.name

def main():
    st.title("YouTube Video Downloader")
    url = st.text_input("Enter the URL of the YouTube video:")
    
    # We use a session state to control the download process and prevent re-triggering
    if 'download_path' not in st.session_state:
        st.session_state.download_path = None

    if st.button("Download Video"):
        if url:
            with st.spinner('Downloading... Please wait'):
                # Download the video and save the path in session state
                st.session_state.download_path = download_video(url)
                st.success("Download ready! Click the link below to save the video to your machine.")
        else:
            st.error("Please enter a valid YouTube URL")

    # Provide the link to download the file if available in the session state
    if st.session_state.download_path:
        with open(st.session_state.download_path, "rb") as file:
            st.download_button(
                label="Download Video",
                data=file,
                file_name="downloaded_video.mp4",
                mime="video/mp4"
            )
        os.unlink(st.session_state.download_path)  # Clean up the temporary file
        # Reset the path in session state to prevent re-download issues
        st.session_state.download_path = None

if __name__ == "__main__":
    main()
