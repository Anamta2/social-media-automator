# 🤖 Social Media Automator

> Transform YouTube videos and text content into ready-to-publish social media posts using AI agents

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 What It Does

This AI-powered tool uses **multi-agent orchestration** to automatically generate social media content from YouTube videos or any text input. It coordinates three specialized AI agents:

1. **🔍 Researcher Agent** - Extracts key points and insights
2. **✍️ Writer Agent** - Creates engaging LinkedIn posts and Twitter threads
3. **🎨 Artist Agent** - Generates image descriptions for visual content

## 💡 Why This Tool Is Useful

### **For Content Creators & Influencers**
- Convert 1 hour of video research → 2 minutes of ready content
- Maintain consistent posting schedule without burnout
- Generate multiple content formats from single source

### **For Educators & Course Creators**
- Quickly share insights from educational videos
- Create promotional content for courses
- Engage students on social media efficiently

### **For Marketing Teams**
- Transform webinars/talks into thought leadership posts
- Reduce content creation time from 30+ minutes to seconds
- Maintain brand presence across platforms

### **For Job Seekers & Professionals**
- Build personal brand by sharing learnings
- Create professional content without writing expertise
- Stand out with consistent, high-quality posts

### **Real Business Value**
Similar SaaS tools charge $20-50/month. This is **100% free** and runs locally!

## ✨ Features

- ✅ **YouTube Video Processing** - Extract content from any public YouTube video
- ✅ **Text Input Support** - Works with articles, transcripts, blog posts
- ✅ **LinkedIn Post Generation** - Professional, engaging posts with emojis
- ✅ **Twitter/X Thread Creation** - Viral-ready threads under 280 characters
- ✅ **Image Concept Design** - AI-generated image descriptions
- ✅ **Clean Web Interface** - Built with Streamlit
- ✅ **Free & Fast** - Uses Groq's free API (Llama 3.3 70B)

## 🚀 Quick Start

### Prerequisites
- Python 3.10-3.13
- macOS, Linux, or Windows

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/social-media-automator.git
cd social-media-automator
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up API key**
- Get your free API key from [Groq Console](https://console.groq.com)
- Create a `.env` file:
```bash
echo "GROQ_API_KEY=your_key_here" > .env
```

5. **Run the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage

### Option 1: Text Input (Recommended)
1. Select "Text/Transcript" mode
2. Paste any content (article, transcript, blog post)
3. Check "Also generate Twitter/X thread" if needed
4. Click "Generate Content"
5. Copy your ready-to-publish posts!

### Option 2: YouTube URL
1. Select "YouTube URL" mode
2. Paste a YouTube video link
3. The tool extracts video description/metadata
4. Generate content as above

**Note:** YouTube transcript extraction can be unreliable. Text mode is more stable.

## 🏗️ Technical Architecture

### Multi-Agent System
```
Input (Video/Text)
    ↓
Researcher Agent (Extract key points)
    ↓
Writer Agents (LinkedIn + Twitter)
    ↓
Artist Agent (Image concepts)
    ↓
Output (Ready content)
```

### Tech Stack
- **LLM**: Llama 3.3 70B via Groq API
- **Frontend**: Streamlit
- **YouTube Extraction**: yt-dlp
- **Language**: Python 3.12

### Project Structure
```
social-media-automator/
├── agents.py          # AI agent logic
├── app.py             # Streamlit web interface
├── requirements.txt   # Python dependencies
├── .env              # API keys (not in repo)
└── README.md         # This file
```

## 🎓 Learning Outcomes

Building this project teaches:
- **AI Agent Orchestration** - Coordinating multiple AI workers
- **API Integration** - Working with LLM APIs (Groq)
- **Prompt Engineering** - Crafting effective AI prompts
- **Web Development** - Building UIs with Streamlit
- **Real-World Problem Solving** - Addressing content creation pain points

## 🔮 Future Enhancements

- [ ] Instagram caption generator
- [ ] Blog post outline creator
- [ ] Email newsletter generator
- [ ] Actual image generation (Stable Diffusion)
- [ ] Multi-language support
- [ ] Content scheduling integration
- [ ] Analytics and A/B testing

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

MIT License - feel free to use this project for learning or commercial purposes.

## 👤 Author

**Anamta **
- GitHub: [@Anamta2](https://github.com/Anamta2)


## 🙏 Acknowledgments

- Built with [Groq](https://groq.com) for fast LLM inference
- Powered by Meta's Llama 3.3 70B model
- UI created with [Streamlit](https://streamlit.io)

---

⭐ **Star this repo if you found it useful!**
