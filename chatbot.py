from openai import OpenAI  # type: ignore
from dotenv import load_dotenv # type: ignore
import json
import os
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# print(OPENROUTER_API_KEY)

def chatbot(message):
    try:
      client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key= OPENROUTER_API_KEY,

      )

      completion = client.chat.completions.create(
      extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
      },
      extra_body={},
      #model --> https://openrouter.ai/models?q=deepseek%3A%20r1
      model = "deepseek/deepseek-r1-distill-llama-70b:free",
      messages=[
        {
          "role": "user",
          "content": message
        }
      ]
      )
      json_recponce = completion.dict()
      # print(json_recponce)
      # print(type(json_recponce))
      # print("defination")
      # print(json_recponce['choices'][0]["message"]['content'])

      return json_recponce
      
    except Exception as e:
      raise Exception("Somee technical error Deep ko bulaooo " )
   



#https://openrouter.ai/activity