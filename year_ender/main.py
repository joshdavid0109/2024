import streamlit as st
import os

# Set page configuration
st.set_page_config(
    page_title="Year-End Interactive Gallery",
    page_icon="🎉",
    layout="wide"
)

# Add a title and introduction
st.title("2024 Recap ♥️")

# Tab-based navigation
tabs = st.tabs(["💬 Message", "📸 Gallery"])

# Home Tab
with tabs[0]:
    st.subheader("Dear Hanna,")
    # Custom CSS for text alignment
    st.markdown(
        """
        <style>
        .justified-text {
            text-align: justify;
            margin: 0 auto;
            width: 80%; /* Adjust width for central alignment */
            font-size: 18px;
            line-height: 1.6;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Long message
    long_message = """
    Before this year ends, I find myself reflecting on all the moments we've shared, the laughter that echoed between us, and of course; the love that continues to grow stronger every day.
    I am so grateful that I started and ended 2024 with the person I love and care the most. Although I know, it is not as smooth as we expect it to be; but look at where we are now, we are close to ending this year together.
    Sa totoo lang, sobrang proud ako sa’yo. Sa lahat ng na-achieve mo, sa lahat ng effort mo, at sa pagiging ikaw lang. Hanna, you inspire me to be better, and you make everything feel worth it.
    As we end this year, gusto ko lang sabihin na I’m so excited for what’s ahead for us. Alam ko na basta magkasama tayo, kaya natin lahat. Lagi akong nandito para sa’yo—cheerleader mo, kakampi mo, at lagi mong taga-sunod.

    Thank you, my palagi, for everything. For being my safe space, my joy, and my love. Excited na ako for year 2025, but I know next year will be tough for us since ako g-graduate na, and ikaw malapit na rin mag-intern. Pero alam ko naman,
    kayang kaya natin 'to--- we have each other's hands e, 'diba?

    Happy new year, my love! 

    """

    # Display the long message with custom formatting
    st.markdown(f'<div class="justified-text">{long_message}', unsafe_allow_html=True)

# Gallery Tab
with tabs[1]:
    # Set the path to the directory containing the images
    image_directory = "images"

    # Get all image file paths from the directory, sorted by name
    image_files = sorted(
        [os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.endswith(('png', 'jpg', 'jpeg', 'JPG'))]
    )

    # Generate captions dynamically based on the filenames
    captions = [f"Photo {i+1}: {os.path.basename(img).split('.')[0]}" for i, img in enumerate(image_files)]

    st.subheader("📸 Photo Gallery")
    st.write("Isa isa natin balikan lahat ng moments natin together, I love you Hanna!")

    # Option 1: Interactive Expanders by Year or Group
    expander_groups = [
        ("📅 January - June", image_files[:len(image_files)//2]),
        ("📅 July - December", image_files[len(image_files)//2:]),
    ]

    for group_title, images in expander_groups:
        with st.expander(group_title):
            cols = st.columns(3)  # Display 3 images per row in the expander
            for i, img_path in enumerate(images):
                with cols[i % 3]:
                    st.image(img_path, caption=captions[image_files.index(img_path)], use_container_width=True)

    st.markdown("---")

    # Option 2: Fullscreen Carousel
    st.markdown("### 🎠 Image Carousel")
    st.write("Enjoy a slideshow of our best moments!")

    current_image_index = st.slider("Scroll through our gallery", 0, len(image_files) - 1, 0)
    st.image(image_files[current_image_index], caption=captions[current_image_index], use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>"
    "Pipiliin ka sa araw araw, Hanna!"
    "</div>",
    unsafe_allow_html=True,
)
