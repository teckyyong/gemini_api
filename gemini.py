# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
# from google import genai
# from google.genai import types
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Create the model
generation_config = {
"temperature": 1,
"top_p": 0.95,
"top_k": 40,
"max_output_tokens": 8192,
# "response_mime_type": "text/plain",
}

model = genai.GenerativeModel( model_name =  "gemini-2.0-flash",
                             generation_config= generation_config,
)

chat_session = model.start_chat(
    history  = [],
)

response = chat_session.send_message("Write me a paragraph of essay about badminton")

print(response.text)


