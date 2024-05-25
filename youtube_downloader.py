import streamlit as st
import urllib.request
import os

# Set the URL of the YouTube video
video_url = st.text_input("Enter the YouTube video URL")

# Set the download directory
download_dir = st.text_input("Enter the download directory")

# Set the file name
file_name = st.text_input("Enter the file name")

# Download the video
def download_video(video_url, download_dir, file_name):
    # Construct the file path
    file_path = os.path.join(download_dir, file_name)

    # Open the file in binary write mode
    with open(file_path, 'wb') as f:
        # Send a GET request to the YouTube video URL
        response = urllib.request.urlopen(video_url)

        # Write the response to the file
        while True:
            chunk = response.read(1024)
            if not chunk:
                break
            f.write(chunk)

    st.success("Video downloaded successfully!")

# Create a button to trigger the download
if st.button("Download Video"):
    download_video(video_url, download_dir, file_name)
