import streamlit as st
from rembg import remove
from PIL import Image
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Background Remover",
    page_icon="🖼️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main {
        padding-top: 20px;
    }
    .stButton button {
        width: 100%;
        border-radius: 10px;
        font-size: 16px;
    }
    .footer {
    text-align: center;
    color: #6e7681;
    font-size: 12px;
    margin-top: 30px;
}   
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🖼️ AI Background Remover")
st.write("Upload an image and remove its background instantly using AI 🚀")

# ---------------- FILE UPLOADER ----------------
uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["png", "jpg", "jpeg", "webp"]
)
st.warning("⚠️ Large images may take longer to process. Please be patient ⏳")

if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("✨ Result")
        st.info("Click **Remove Background** to process")

    st.markdown("---")

    # ---------------- REMOVE BUTTON ----------------
    if st.button("🚀 Remove Background ", type="primary", use_container_width=True):
        with st.spinner("Processing image... please wait ⏳"):
            result = remove(image)

        # Convert result to bytes for download
        img_bytes = io.BytesIO()
        result.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📷 Original Image")
            st.image(image, use_container_width=True)

        with col2:
            st.subheader("✨ Background Removed")
            st.image(result, use_container_width=True)

        st.success("🎉 Background removed successfully!")

        # ---------------- DOWNLOAD BUTTON ----------------
        st.download_button(
            type="primary",
            use_container_width=True,
            label="⬇️ Download Image (PNG)",
            data=img_bytes,
            file_name="background_removed.png",
            mime="image/png"
        )

st.markdown(
    "<div class='footer'>@ 2026 Built with ❤️ Vinay Singh Tomar</div>",
    unsafe_allow_html=True
)

