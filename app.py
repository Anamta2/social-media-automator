import streamlit as st
from agents import ContentAgents

# Page config
st.set_page_config(
    page_title="Social Media Automator",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Social Media Automator")
st.markdown("Transform video content or text into ready-to-publish social media posts")

# Initialize agents
if 'agents' not in st.session_state:
    st.session_state.agents = ContentAgents()

# Input section
st.markdown("### 📥 Input")
input_type = st.radio("Choose input type:", ["Text/Transcript", "YouTube URL"], horizontal=True)

if input_type == "YouTube URL":
    user_input = st.text_input("Enter YouTube URL:", placeholder="https://www.youtube.com/watch?v=...")
else:
    user_input = st.text_area("Paste your content:", height=200, 
                               placeholder="Paste video transcript, article, or any content...")

# Output options
st.markdown("### ⚙️ Output Options")
include_twitter = st.checkbox("🐦 Also generate Twitter/X thread", value=True)

# Generate button
if st.button("🚀 Generate Content", type="primary", use_container_width=True):
    if user_input.strip():
        with st.spinner("🤖 AI Agents are working..."):
            results = st.session_state.agents.run_full_pipeline(user_input, include_twitter=include_twitter)
        
        if results["success"]:
            st.success("✅ Content generated successfully!")
            
            # Display results in tabs
            if include_twitter:
                tab1, tab2, tab3, tab4 = st.tabs(["📝 Key Points", "✍️ LinkedIn Post", "🐦 Twitter Thread", "🎨 Image Concept"])
            else:
                tab1, tab2, tab3 = st.tabs(["📝 Key Points", "✍️ LinkedIn Post", "🎨 Image Concept"])
            
            with tab1:
                st.info(results["key_points"])
            
            with tab2:
                st.success(results["linkedin_post"])
                st.markdown("**Copy this post:**")
                st.code(results["linkedin_post"], language=None)
            
            if include_twitter:
                with tab3:
                    st.success(results["twitter_thread"])
                    st.markdown("**Copy this thread:**")
                    st.code(results["twitter_thread"], language=None)
                    with tab4:
                        st.info(results["image_description"])
            else:
                with tab3:
                    st.info(results["image_description"])
                    
        else:
            st.error(f"❌ Error: {results['error']}")
    else:
        st.warning("Please enter some content first!")

# Footer
st.markdown("---")
st.markdown("**💡 Tip:** For best results, use detailed content (200+ words)")
