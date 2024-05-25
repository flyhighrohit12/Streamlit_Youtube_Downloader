import streamlit as st
from pytube import YouTube
import tempfile
import os

st.title('YouTube Video Downloader')

url = st.text_input('Enter the URL of the YouTube video you wish to download:')

if url:
    yt = YouTube(url)
    st.write(f"**Video Title:** {yt.title}")
    st.image(yt.thumbnail_url)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    options = [(i.itag, i.resolution) for i in stream]
    selected_option = st.selectbox('Choose the quality/resolution of the video to download:', options, format_func=lambda x: x[1])

    if st.button('Prepare Download'):
        selected_stream = stream.get_by_itag(selected_option[0])
        safe_filename = yt.title.replace('/', '-').replace('\\', '-').replace(':', '-').replace('|', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-')

        # Create a temporary file and download the video
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            try:
                selected_stream.download(output_path=os.path.dirname(tmpfile.name), filename=safe_filename)
                tmpfile.close()
                final_path = os.path.join(os.path.dirname(tmpfile.name), safe_filename + '.mp4')
                st.success("Video downloaded successfully. Ready to be saved to your device.")

                # Check if the file exists before attempting to offer it for download
                if os.path.exists(final_path):
                    with open(final_path, 'rb') as f:
                        st.download_button(label="Download Video",
                                           data=f,
                                           file_name=safe_filename + ".mp4",
                                           mime="video/mp4")
                else:
                    st.error("Failed to locate the downloaded file. Please try again.")

            except Exception as e:
                st.error(f"An error occurred while downloading the video: {e}")
            finally:
                # Attempt to clean up if there's an error or not
                if tmpfile.name:
                    os.remove(tmpfile.name)
