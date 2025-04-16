import streamlit as st
import base64

st.title("Upload Photo → View in New Tab")

uploaded_file = st.file_uploader("Choose a photo...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Convert image to base64
    encoded = base64.b64encode(uploaded_file.getvalue()).decode()
    mime_type = uploaded_file.type
    data_url = f"data:{mime_type};base64,{encoded}"

    # HTML content for new tab (directly embeds image)
    viewer_html = f"""
    <html>
      <head><title>Your Photo</title></head>
      <body style="text-align:center; padding:2em;">
        <h2>Your Uploaded Photo</h2>
        <img src="{data_url}" style="max-width:90%; border:1px solid #ccc;" />
        <p><i>This image is embedded directly — no localStorage needed.</i></p>
      </body>
    </html>
    """

    # Encode entire HTML as base64 so we can open it via data URL
    html_data_url = "data:text/html;base64," + base64.b64encode(viewer_html.encode()).decode()

    # Display the "Open in New Tab" button
    st.markdown(f"""
    <a href="{html_data_url}" target="_blank">
        <button style="padding:10px 20px; font-size:16px;">Open Photo in New Tab</button>
    </a>
    """, unsafe_allow_html=True)
