from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# Test 1: YouTube (trying different video)
print("Testing YouTube API...")
try:
    # Using a popular tech video
    transcript = YouTubeTranscriptApi.get_transcript("9bZkp7q19f0")
    print(f"✅ YouTube works! Got {len(transcript)} lines")
except Exception as e:
    print(f"❌ YouTube error: {e}")

# Test 2: Groq
print("\nTesting Groq API...")
try:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ No API key found in .env file")
    else:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=10
        )
        print(f"✅ Groq works! Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ Groq error: {e}")
