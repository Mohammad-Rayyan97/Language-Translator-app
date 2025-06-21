from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os 

from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model = "gemma2-9b-it", groq_api_key=groq_api_key,temperature= 0.0)

# function to translate the language

def translate(input_language,output_language,input_text):
    prompt = ChatPromptTemplate.from_messages(
         [
            (
                'system',
                """You are a translation engine. Given a sentence, translate it from {input_language} to {output_language}. Your output should include:
1. The translation in the {output_language}'s native script.
2. The same translation written using the English (Latin) alphabet.

Do not explain anything. Just give the two lines of translated output as:
Tranlation : Native Script

Tranlation : English Transliteration"""
            ),
            ('human', '{input}')
        ]
    )

    chain = prompt | model

    response = chain.invoke(
        {
            "input_language":input_language,
            "output_language":output_language,
            "input" : input_text
        }
    )
    return response.content


