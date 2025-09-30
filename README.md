# Search Sense 🤖

An AI-powered research assistant that combines web search with document analysis to provide comprehensive answers to your questions. Built with multiple interfaces and advanced RAG capabilities.

## ✨ Features

### 🔍 **AI-Powered Research**
- **Intelligent Search**: Ask any question and get comprehensive, well-structured answers
- **Web Search Integration**: Real-time web search using Tavily API with DuckDuckGo fallback
- **AI Synthesis**: DeepSeek V3 analyzes and synthesizes information from multiple sources
- **Proper Citations**: All answers include traceable source citations

### 📄 **Document Analysis (RAG)**
- **Document Upload**: Support for PDF, DOCX, TXT, HTML, and Markdown files
- **Vector Search**: Semantic similarity search using Sentence Transformers
- **Chunking**: Intelligent text segmentation for optimal retrieval
- **Persistent Storage**: ChromaDB vector database with local persistence

### 🎨 **Multiple Interfaces**
- **Next.js Frontend**: Modern React interface with TypeScript
- **Gradio Interface**: Python-based web UI with custom styling
- **Streamlit App**: Deployable dashboard interface
- **RAG Interface**: Advanced document analysis with hybrid search

## 🚀 Quick Start

### Option 1: Next.js Frontend (Recommended)
```bash
npm install
npm run dev
```
Navigate to http://localhost:3000

### Option 2: Gradio Interface
```bash
pip install -r requirements_gradio.txt
python gradio_app.py
```
Navigate to http://localhost:7860

### Option 3: Streamlit Interface
```bash
pip install -r requirements_streamlit.txt
streamlit run streamlit_app.py
```
Navigate to http://localhost:8501

### Option 4: RAG Interface (Advanced)
```bash
pip install -r requirements_rag.txt
python rag_gradio_app.py
```
Navigate to http://localhost:7862

## 🔧 Configuration

### Environment Variables
Create a `.env.local` file with your API keys:

```env
# Required
OPENROUTER_API_KEY=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

# Optional (improves search quality)
TAVILY_API_KEY=your_tavily_api_key_here
BRAVE_SEARCH_API_KEY=your_brave_search_api_key_here
```

### API Keys Setup
- **OpenRouter API**: Already configured with free tier access to DeepSeek V3
- **Tavily API**: Free tier available at [tavily.com](https://tavily.com)
- **Brave Search API**: Free tier at [api.search.brave.com](https://api.search.brave.com/)

## 🏗️ Architecture

### **Technology Stack**
- **Frontend**: Next.js 15, React 19, TypeScript, Tailwind CSS
- **Backend**: Python (FastAPI, Gradio, Streamlit)
- **AI Model**: DeepSeek V3 via OpenRouter API
- **Vector Store**: ChromaDB with Sentence Transformers
- **Search APIs**: Tavily, DuckDuckGo, Brave Search
- **Document Processing**: PyPDF2, docx2txt, BeautifulSoup

### **Project Structure**
```
├── src/                          # Next.js frontend
│   ├── app/
│   │   ├── api/synthesize/       # AI synthesis endpoint
│   │   └── page.tsx             # Main interface
│   ├── components/              # React components
│   └── lib/                     # Utilities and API clients
├── gradio_app.py                # Gradio interface
├── streamlit_app.py             # Streamlit interface
├── rag_gradio_app.py            # RAG interface
├── vector_store.py              # Vector database management
├── document_processor.py        # Document processing
├── real_web_search.py           # Web search integration
├── python_openrouter.py         # AI API client
└── requirements_*.txt           # Python dependencies
```

## 📖 How It Works

### **Basic Search Flow**
1. **Query Input**: User enters a question
2. **Web Search**: System searches the web using Tavily API
3. **AI Analysis**: DeepSeek V3 synthesizes information from search results
4. **Response**: Formatted answer with source citations

### **RAG Search Flow**
1. **Document Upload**: User uploads documents to knowledge base
2. **Query Processing**: Question is embedded and searched against document vectors
3. **Hybrid Search**: Combines document search with web search
4. **AI Synthesis**: Generates comprehensive answers from multiple sources

## 🎯 Use Cases

- **Research Assistant**: Get comprehensive answers to complex questions
- **Document Analysis**: Search through your personal document collection
- **Academic Research**: Combine web sources with your research papers
- **Business Intelligence**: Analyze documents and web sources together
- **Learning Tool**: Understand complex topics with AI-powered explanations

## 🔄 Interface Comparison

| Feature | Next.js | Gradio | Streamlit | RAG |
|---------|---------|--------|-----------|-----|
| **Setup** | npm install | pip install | pip install | pip install |
| **UI Style** | Modern React | Web Interface | Dashboard | Advanced |
| **Document Upload** | ❌ | ❌ | ❌ | ✅ |
| **Vector Search** | ❌ | ❌ | ❌ | ✅ |
| **Deployment** | Vercel/Netlify | Hugging Face | Streamlit Cloud | Railway |
| **Customization** | High | Medium | Medium | High |

## 🚀 Deployment Options

### **Next.js Frontend**
```bash
# Deploy to Vercel
npm run build
# Connect to Vercel via GitHub integration
```

### **Gradio Interface**
```bash
# Deploy to Hugging Face Spaces
# Upload files to HF Spaces
```

### **Streamlit Interface**
```bash
# Deploy to Streamlit Cloud
# Connect GitHub repo to Streamlit Cloud
```

### **RAG Interface**
```bash
# Deploy to Railway or VPS
# Use Docker for containerization
```

## 📊 Performance

- **Search Latency**: ~3-8 seconds per query
- **AI Response**: ~2-5 seconds for synthesis
- **Document Processing**: ~1-3 seconds per document
- **Vector Search**: ~100-500ms per query

## 🔧 Customization

### **Change AI Model**
Edit `python_openrouter.py`:
```python
self.model = 'anthropic/claude-3-sonnet'  # Use Claude
self.model = 'openai/gpt-4'              # Use GPT-4
```

### **Add Search Providers**
Modify `real_web_search.py` to integrate additional APIs:
- SerpAPI (Google Search)
- Bing Search API
- Custom search providers

### **Extend Document Support**
Update `document_processor.py` to support additional formats:
```python
def _process_custom_format(self, file_path: str) -> str:
    # Add your custom processing logic
    pass
```

## 🛠️ Troubleshooting

### **Common Issues**

**API Key Errors**
```bash
# Check your .env.local file
# Ensure API keys are properly formatted
```

**Import Errors**
```bash
pip install --upgrade sentence-transformers chromadb
```

**Memory Issues**
- Reduce chunk size in `document_processor.py`
- Process documents individually in RAG mode

## 📈 Future Enhancements

- [ ] Multi-language support
- [ ] Audio/video content processing
- [ ] Advanced filtering and faceted search
- [ ] User authentication and multiple collections
- [ ] API endpoints for integration
- [ ] Real-time document monitoring

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

## 🎉 Getting Started

Choose your preferred interface and start exploring the power of AI-assisted research!

**Repository**: https://github.com/NIKHIL0653/Search-Sense.git