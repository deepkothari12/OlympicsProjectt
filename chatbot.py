from openai import OpenAI  # type: ignore
from dotenv import load_dotenv # type: ignore
import json
import os
load_dotenv()


# print(OPENROUTER_API_KEY)

def chatbot(message):
            # print(OPENROUTER_API_KEY)
    try:
        OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
        OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
        #print(OPENROUTER_BASE_URL)
        client = OpenAI(
            
        base_url= OPENROUTER_BASE_URL,
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
        json_recponce = completion.model_dump()
        # print(json_recponce)
        # print(type(json_recponce))
        # print("defination")
        
        # print(json_recponce['choices'][0]["message"]['content'])

        return json_recponce
      
    except Exception as e:
       raise Exception("Somee technical error Deep ko bulaooo " )
   

# chatbot("Whi is narendra modi")

#https://openrouter.ai/activity