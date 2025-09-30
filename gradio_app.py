#!/usr/bin/env python3
"""
Simple AI Research Assistant
Users input questions, app searches web and gives concise answers
"""

import gradio as gr
import asyncio
from dotenv import load_dotenv

load_dotenv()

from real_web_search import search_web
from python_openrouter import get_openrouter_client

# Centered, larger UI
custom_css = """
.gradio-container {
    max-width: 900px !important;
    margin: 0 auto !important;
    padding: 40px !important;
    font-family: system-ui, -apple-system, sans-serif !important;
    text-align: center !important;
}

.search-container {
    display: flex !important;
    gap: 12px !important;
    margin-bottom: 32px !important;
    justify-content: center !important;
    align-items: center !important;
}

.input-container input {
    flex: 1 !important;
    padding: 12px 16px !important;
    border: 2px solid #d1d5db !important;
    border-radius: 8px !important;
    font-size: 16px !important;
    background: white !important;
    min-width: 300px !important;
}

.input-container input:focus {
    outline: none !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
}

.btn-send {
    padding: 12px 24px !important;
    background: #3b82f6 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    cursor: pointer !important;
    min-width: 100px !important;
}

.btn-send:hover {
    background: #2563eb !important;
}

.output-container {
    border: 2px solid #e5e7eb !important;
    border-radius: 12px !important;
    padding: 24px !important;
    background: white !important;
    margin: 0 auto !important;
    max-width: 700px !important;
}

.output-container h1,
.output-container h2,
.output-container h3 {
    font-weight: 600 !important;
    margin: 20px 0 12px 0 !important;
    color: #111827 !important;
    font-size: 18px !important;
}

.output-container p {
    margin: 12px 0 !important;
    color: #374151 !important;
    line-height: 1.7 !important;
    font-size: 16px !important;
}

.output-container ul,
.output-container ol {
    margin: 12px 0 !important;
    padding-left: 24px !important;
}

.output-container li {
    margin: 6px 0 !important;
    color: #374151 !important;
    font-size: 16px !important;
}

.output-container strong {
    font-weight: 600 !important;
    color: #111827 !important;
}

.output-container code {
    background: #f3f4f6 !important;
    padding: 3px 6px !important;
    border-radius: 4px !important;
    font-family: monospace !important;
    font-size: 14px !important;
}
"""

async def search_and_answer(query):
    """Simple function to search web and get AI answer"""
    if not query.strip():
        return "Please enter a question."

    try:
        # Search the web
        search_response = await search_web(query, max_results=3)

        if not search_response.results:
            return "No search results found. Try a different question."

        # Get AI synthesis
        client = get_openrouter_client()
        answer = client.synthesize_search_results(query, search_response.results)

        return answer

    except Exception as e:
        return f"Error: {str(e)}"

def create_interface():
    """Create centered, larger interface"""

    def search_handler(query):
        """Handle search requests"""
        if not query.strip():
            return "Please enter a question."

        try:
            # Create event loop for async
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            # Run async search
            result = loop.run_until_complete(search_and_answer(query))
            return result

        except Exception as e:
            return f"Error: {str(e)}"

    with gr.Blocks(css=custom_css) as demo:
        gr.Markdown("# 🤖 AI Research Assistant")
        gr.Markdown("*Get concise answers to your questions powered by web search and AI*")

        with gr.Row(elem_classes=["search-container"]):
            query_input = gr.Textbox(
                placeholder="What would you like to know?",
                label="",
                elem_classes=["input-container"]
            )
            search_btn = gr.Button("🔍Search", elem_classes=["btn-send"])

        output = gr.Markdown(
            value="## Welcome!\n\nEnter your question above and click Search to get started.",
            elem_classes=["output-container"]
        )

        search_btn.click(search_handler, inputs=[query_input], outputs=[output])
        query_input.submit(search_handler, inputs=[query_input], outputs=[output])

    return demo

if __name__ == "__main__":
    import os

    if not os.getenv('OPENROUTER_API_KEY'):
        print("Warning: OPENROUTER_API_KEY not found")
        print("Please set it in your .env file")

    demo = create_interface()
    demo.launch(server_port=7864)
