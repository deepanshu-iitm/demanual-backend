An AI-powered FastAPI service that uses Google Gemini API and LangChain to fetch recent news on a given topic and generate professional LinkedIn-style posts.

## 🚀 Features

- **AI-Powered Content Generation**: Uses Google Gemini 2.0 Flash for intelligent LinkedIn post creation
- **Real-time News Search**: Integrates Tavily search API via LangChain for current news retrieval
- **Professional LinkedIn Format**: Generates engaging, concise posts suitable for professional networks

## 🛠 Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: Framework for developing applications with language models
- **Google Gemini**: Advanced AI model for text generation
- **Tavily Search**: Real-time search API optimized for AI applications
- **Python 3.10+**: Core programming language

## 📋 Prerequisites

- Python 3.10 or higher
- API Keys:
  - **Gemini API Key**: Get from [Google AI Studio](https://aistudio.google.com/)
  - **Tavily API Key**: Get from [Tavily](https://tavily.com/)

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <https://github.com/deepanshu-iitm/demanual-backend.git>
cd demanual-backend
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5. Run the Application
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

## 📖 API Documentation

### Swagger UI
Access interactive API documentation at: `http://localhost:8000/docs`

### Endpoints

#### Health Check
```http
GET /health
```
**Response:**
```json
{
  "status": "ok"
}
```

#### Generate LinkedIn Post
```http
POST /generate-post
```

**Request Body:**
```json
{
  "topic": "Artificial Intelligence"
}
```

**Response:**
```json
{
  "topic": "Artificial Intelligence",
  "news_sources": [
    "https://example.com/ai-news-1",
    "https://example.com/ai-news-2",
    "https://example.com/ai-news-3"
  ],
  "linkedin_post": "🚀 AI is transforming industries at an unprecedented pace! Recent developments show how machine learning is revolutionizing everything from healthcare diagnostics to autonomous vehicles. As we witness this technological evolution, it's crucial for professionals to stay informed and adapt to these changes. The future belongs to those who embrace AI as a collaborative tool rather than a replacement. What are your thoughts on AI's impact in your industry? #ArtificialIntelligence #Innovation #TechTrends",
  "image_suggestion": null
}
```

