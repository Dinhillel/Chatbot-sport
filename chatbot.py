import openai
import os
from dotenv import load_dotenv
import sys

sys.path.append('C:/Users/97250/OneDrive/Desktop/python/src')


load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(question, context):
    """
    Uses the OpenAI API (chat model) to generate a response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": "You are an expert on NBA games."},
                {"role": "user", "content": f"Question: {question}\nContext: {context}"}
            ],
            max_tokens=150,
            temperature=0.7,
              timeout=10,  # Set a timeout for the API call
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"


# 🔽 chack
if __name__ == "__main__":
    question = "What was the result of the game between Lakers and Bulls?"
    context = "The Lakers scored 102 and the Bulls scored 97."

    response = generate_response(question, context)
    print("AI Response:", response)
