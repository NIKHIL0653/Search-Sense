import streamlit as st
import asyncio
from dotenv import load_dotenv

load_dotenv()

from real_web_search import search_web
from python_openrouter import get_openrouter_client

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f2937;
        margin-bottom: 2rem;
    }
    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .search-container {
        background: #f8fafc;
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid #e5e7eb;
        margin-bottom: 2rem;
    }
    .answer-container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid #e5e7eb;
        margin-top: 2rem;
    }
    .stButton>button {
        background: #3b82f6 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background: #2563eb !important;
    }
    .stTextArea>div>textarea {
        border: 2px solid #d1d5db !important;
        border-radius: 8px !important;
        font-size: 16px !important;
    }
    .stTextArea>div>textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

async def search_and_answer(query):
    if not query.strip():
        return "", "Please enter a question."

    try:
        progress_bar = st.progress(0)
        status_text = st.empty()

        status_text.text("🔍 Searching the web...")
        progress_bar.progress(25)

        search_response = await search_web(query, max_results=3)
        progress_bar.progress(50)

        if not search_response.results:
            progress_bar.empty()
            status_text.empty()
            return "", "No search results found. Try a different question."

        status_text.text(" Analyzing and synthesizing answer...")
        progress_bar.progress(75)

        client = get_openrouter_client()
        answer = client.synthesize_search_results(query, search_response.results)

        sources_text = "## Sources\n\n"
        for i, result in enumerate(search_response.results, 1):
            sources_text += f"**{i}.** [{result.title}]({result.url})\n"
            sources_text += f"*{result.domain}*\n\n"

        progress_bar.progress(100)
        progress_bar.empty()
        status_text.empty()

        return sources_text, answer

    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "", f"Error: {str(e)}"

def main():
    st.markdown('<h1 class="main-header">Search Sense</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Get concise answers to your questions powered by web search and AI</p>', unsafe_allow_html=True)

    st.markdown('<div class="search-container">', unsafe_allow_html=True)

    query = st.text_area(
        "Enter your question:",
        placeholder="What would you like to know?",
        height=100,
        key="query_input"
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        search_button = st.button("🔍Search", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if search_button and query.strip():
        with st.spinner("Processing your question..."):
            try:
                try:
                    loop = asyncio.get_event_loop()
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)

                sources, answer = loop.run_until_complete(search_and_answer(query))

                st.markdown('<div class="answer-container">', unsafe_allow_html=True)
                st.markdown(sources)
                st.markdown("---")
                st.markdown("## Answer")
                st.markdown(answer)
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    elif search_button and not query.strip():
        st.warning("Please enter a question first.")

    st.markdown("---")
    st.markdown("*Powered by Grok AI and web search*")

if __name__ == "__main__":
    import os

    if not os.getenv('OPENROUTER_API_KEY'):
        st.error("⚠️ OpenRouter API key not found. Please set OPENROUTER_API_KEY in your .env file")
        st.stop()

    main()