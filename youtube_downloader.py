import streamlit as st
from pytube import YouTube
import tempfile

st.title('YouTube Video Downloader')

# Text input for the YouTube video URL
url = st.text_input('Enter the URL of the YouTube video you wish to download:')

if url:
    # Initialize YouTube object with the URL
    yt = YouTube(url)
    st.write(f"**Video Title:** {yt.title}")
    st.image(yt.thumbnail_url)

    # Filtering available video streams
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    options = [(i.itag, i.resolution) for i in stream]
    selected_option = st.selectbox('Choose the quality/resolution of the video to download:', options, format_func=lambda x: x[1])

    if st.button('Download Video'):
        selected_stream = stream.get_by_itag(selected_option[0])
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            # Download the video to a temporary file
            selected_stream.download(output_path=tmpfile.name, filename=yt.title)
            tmpfile.flush()
            
            # Reopen the temporary file and create a download button
            with open(tmpfile.name + '.mp4', 'rb') as f:
                st.download_button(label="Download Video",
                                   data=f,
                                   file_name=yt.title + ".mp4",
                                   mime="video/mp4")
