import streamlit as st
import requests
import os
import urllib.request

# Set the URL of the YouTube video
video_url = st.text_input("Enter the YouTube video URL")

# Set the download directory
download_dir = st.text_input("Enter the download directory")

# Set the file name
file_name = st.text_input("Enter the file name")

# Download the video
def download_video(video_url, download_dir, file_name):
    # Send a GET request to the YouTube video URL
    response = requests.get(video_url, stream=True)

    # Check if the response was successful
    if response.status_code == 200:
        # Open the file in binary write mode
        with open(os.path.join(download_dir, file_name), 'wb') as f:
            # Write the video data to the file
            for chunk in response.iter_content(1024):
                f.write(chunk)
        st.success("Video downloaded successfully!")
    else:
        st.error("Failed to download video")

# Create a button to trigger the download
if st.button("Download Video"):
    download_video(video_url, download_dir, file_name)
