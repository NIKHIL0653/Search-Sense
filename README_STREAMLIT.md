# 🤖 AI Research Assistant - Streamlit Version

A deployable AI-powered research assistant that searches the web and provides concise answers using Grok AI.

## ✨ Features

- **Web Search Integration**: Searches the web using Tavily API
- **AI Synthesis**: Uses Grok AI to provide concise, well-structured answers
- **Clean UI**: Modern Streamlit interface perfect for portfolios
- **Progress Feedback**: Real-time progress indicators during search
- **Deployable**: Can be deployed to Streamlit Cloud, Heroku, or other platforms

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements_streamlit.txt
```

### 2. Set up Environment Variables
Create a `.env` file with your API keys:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 3. Run Locally
```bash
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

## 🌐 Deployment Options

### Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set environment variables in the Streamlit Cloud dashboard
5. Deploy!

### Heroku
1. Create a `Procfile`:
   ```
   web: streamlit run streamlit_app.py --server.port $PORT --server.headless true
   ```

2. Deploy using Heroku CLI or GitHub integration

### Other Platforms
- **Railway**: Connect GitHub repo and set environment variables
- **Render**: Use their Streamlit template
- **Vercel**: Use their Python runtime

## 🎯 How It Works

1. **User Input**: Enter any question in the text area
2. **Web Search**: App searches the web using Tavily API
3. **AI Analysis**: Grok AI analyzes search results and synthesizes a concise answer
4. **Display**: Clean, formatted response with progress indicators

## 📋 Example Questions

- "What are the latest developments in AI?"
- "How does quantum computing work?"
- "What are the benefits of renewable energy?"
- "Explain machine learning algorithms"

## 🔧 Configuration

### API Keys Required
- **OpenRouter API Key**: For Grok AI access (free tier available)
- **Tavily API Key**: For web search (free tier available)

### Optional Configuration
- Adjust `max_results` in `search_and_answer()` for more/less sources
- Modify the system prompt in `python_openrouter.py` for different AI behavior

## 🛠️ Project Structure

```
mini perplexity/
├── streamlit_app.py          # Main Streamlit application
├── python_openrouter.py      # OpenRouter/Grok AI integration
├── real_web_search.py        # Web search functionality
├── requirements_streamlit.txt # Python dependencies
├── .env                      # Environment variables
└── README_STREAMLIT.md       # This file
```

## 🎨 UI Features

- **Centered Layout**: Clean, professional appearance
- **Progress Indicators**: Visual feedback during search
- **Responsive Design**: Works on desktop and mobile
- **Modern Styling**: Custom CSS for enhanced appearance

## 🔒 Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- The app includes input validation and error handling

## 📈 Performance

- **Search Time**: ~5-10 seconds per query
- **AI Response**: ~2-5 seconds for synthesis
- **Total Response Time**: ~7-15 seconds

## 🚀 Ready for Recruiters!

This Streamlit app is perfect for:
- **Portfolio Projects**: Showcase AI/ML skills
- **Live Demos**: Deploy and share with recruiters
- **Technical Interviews**: Demonstrate full-stack AI applications

---

**Deploy your AI research assistant today and impress recruiters with your AI skills!**