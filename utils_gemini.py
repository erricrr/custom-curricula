import os
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import Markdown

# Get the gemini key from the .env file
load_dotenv('.env', override=True)
google_api_key = os.getenv('GOOGLE_API_KEY')
client = genai.configure(api_key=google_api_key)

def get_llm_response(prompt, temperature=0.7, top_p=1.0, top_k=1):
    you_are = [{"parts":
      [{"text": "You are an AI assistant."}],
         "role": "user"}]
    
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=you_are)

    try:
        generation_config = genai.GenerationConfig(temperature=temperature, top_p=top_p, top_k=top_k)

        # model_response = chat.send_message(prompt)
        # model_response = model.generate_content(prompt, generation_config=generation_config)
        
        model_response = chat.send_message(prompt,generation_config=generation_config)

        response = model_response.text.replace("*", "")
        return response
    except genai.types.generation_types.BlockedPromptException:
        return "That's not nice! Be kind."
    except Exception as e:
        return "Error! Try again."


# # Initialize different models
# text_model = genai.GenerativeModel('gemini-pro')
# code_model = genai.GenerativeModel('code-davinci-002')
# translation_model = genai.GenerativeModel('translation-en-es')
# summarization_model = genai.GenerativeModel('summarization-model-v1')
# qa_model = genai.GenerativeModel('qa-model-v1')
# sentiment_model = genai.GenerativeModel('sentiment-analysis-model-v1')

# model_type = [text_model, code_model, translation_model, summarization_model, qa_model, sentiment_model]

# # Function to get a response from a model
# def get_model_response(model, prompt, temperature=0.0):
#     chat = model.start_chat(history=[])

#     try:
#         response = chat.send_message(prompt, temperature=temperature)
#         respuesta = response.text.replace("*", "")
#         return respuesta
#     except genai.types.generation_types.BlockedPromptException:
#         return "That's not nice! Be kind."
#     except Exception as e:
#         return "Error! Try again."

