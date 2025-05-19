import requests
import google.generativeai as genai
from django.conf import settings

class TextSummarizerService:
    def __init__(self):
        print("Initializing TextSummarizerService")
        print(settings.GEMINI_API_KEY)
        genai.configure(api_key=settings.GEMINI_API_KEY)

        # Or initialize the client directly with the API key
        self.client = genai.GenerativeModel('gemini-2.0-flash')

    def summarize_text(self, text: str) -> str:
        """
        Sends a request to the API to summarize the given text.

        :param text: The text to be summarized.
        :return: The summarized text.
        """
        
        response = self.client.generate_content(
            contents=f"summarize the following text {text}",
        )
        return response.text
        



