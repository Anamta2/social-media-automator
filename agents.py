"""
Social Media Automator - AI Agents
Three specialized AI workers that create content from YouTube videos
"""

from groq import Groq
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

class ContentAgents:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"
    
    def get_youtube_transcript(self, video_url):
        """Extract transcript from YouTube video using yt-dlp"""
        try:
            # Use yt-dlp to get subtitles
            result = subprocess.run(
                ['yt-dlp', '--skip-download', '--write-auto-sub', '--sub-lang', 'en', 
                 '--sub-format', 'json3', '--print', 'requested_subtitles', video_url],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                return None, "Could not fetch video data. Video may be private or restricted."
            
            # Try alternative: get description if subtitles fail
            result = subprocess.run(
                ['yt-dlp', '--skip-download', '--get-description', video_url],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            description = result.stdout.strip()
            
            if len(description) > 100:
                return description, None
            else:
                return None, "No transcript or description available for this video."
                
        except subprocess.TimeoutExpired:
            return None, "Request timed out. Try a different video."
        except FileNotFoundError:
            return None, "yt-dlp not installed properly. Using text mode is recommended."
        except Exception as e:
            return None, f"Error: {str(e)}"
    
    def agent_researcher(self, transcript):
        """Agent 1: Extract key points from transcript"""
        prompt = f"""You are a content researcher. Analyze this content and extract the 5 most important key points or tips.

Content:
{transcript[:4000]}  

Provide ONLY the 5 key points in a clear, numbered list. Be concise."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def agent_writer(self, key_points):
        """Agent 2: Create LinkedIn post from key points"""
        prompt = f"""You are a social media expert. Create an engaging LinkedIn post based on these key points:

{key_points}

Requirements:
- Start with a hook that grabs attention
- Use emojis strategically (2-3 max)
- Keep it under 200 words
- End with a call-to-action or question
- Professional but conversational tone

Write the LinkedIn post now:"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400,
                temperature=0.8
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def agent_twitter(self, key_points):
        """Agent 2B: Create Twitter/X thread from key points"""
        prompt = f"""You are a viral Twitter/X content creator. Create an engaging thread based on these key points:

{key_points}

Requirements:
- First tweet: Hook that stops the scroll (under 280 characters)
- Then 4-6 tweets, each under 280 characters
- Use emojis strategically
- Make it conversational and engaging
- End with a call-to-action
- Number each tweet (1/6, 2/6, etc.)

Format each tweet on a new line starting with the number.

Write the thread now:"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=600,
                temperature=0.8
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def agent_artist(self, linkedin_post):
        """Agent 3: Create image description for the post"""
        prompt = f"""You are a creative visual designer. Based on this LinkedIn post, describe an image that would perfectly complement it.

LinkedIn Post:
{linkedin_post}

Create a detailed image description (1-2 sentences) that:
- Captures the main theme
- Would work well on social media
- Is professional and eye-catching

Image description:"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def run_full_pipeline(self, video_url_or_text, include_twitter=False):
        """Run all agents in sequence"""
        results = {
            "success": False,
            "transcript": None,
            "key_points": None,
            "linkedin_post": None,
            "twitter_thread": None,
            "image_description": None,
            "error": None
        }
        
        # Check if input is a YouTube URL or text
        if video_url_or_text.startswith("http"):
            print("🎬 Fetching YouTube content...")
            transcript, error = self.get_youtube_transcript(video_url_or_text)
            if error:
                results["error"] = error
                return results
            results["transcript"] = transcript[:500] + "..."
        else:
            print("🎬 Using provided text...")
            transcript = video_url_or_text
            results["transcript"] = transcript[:500] + "..."
        
        # Step 2: Extract key points
        print("📝 Agent 1 (Researcher): Extracting key points...")
        key_points = self.agent_researcher(transcript)
        results["key_points"] = key_points
        
        # Step 3: Create LinkedIn post
        print("✍️  Agent 2 (Writer): Creating LinkedIn post...")
        linkedin_post = self.agent_writer(key_points)
        results["linkedin_post"] = linkedin_post
        
        # Step 3B: Create Twitter thread (if requested)
        if include_twitter:
            print("🐦 Agent 2B (Twitter Writer): Creating thread...")
            twitter_thread = self.agent_twitter(key_points)
            results["twitter_thread"] = twitter_thread
        
        # Step 4: Create image description
        print("🎨 Agent 3 (Artist): Designing image concept...")
        image_desc = self.agent_artist(linkedin_post)
        results["image_description"] = image_desc
        
        results["success"] = True
        print("✅ All agents completed successfully!")
        
        return results
