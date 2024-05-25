import streamlit as st
import pytube

# Create a Streamlit app
st.title("YouTube Video Downloader")
st.header("Enter a YouTube video URL:")
video_url_input = st.text_input("")

if st.button("Download Video"):
    # Get the video URL from the input field
    video_url = video_url_input

    # Create a PyTube object
    yt = pytube.YouTube(video_url)

    # Download the video
    stream = yt.streams.filter(only_audio=False).first()
    stream.download()

    # Display a success message
    st.success(f"Video downloaded successfully")
