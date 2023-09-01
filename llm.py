import os
from langchain import PromptTemplate, OpenAI, LLMChain
from dotenv import load_dotenv


load_dotenv('.env')

api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key


prompt_template = """
You are a director for a small show involving 2 characters, Blue and Pink.
You must write script for an episode made up of multiple scenes.
Each scene has the following variables:
- text: the text to be displayed on screen
- blue: boolean value to represent whether or not Blue is in the scene
- pink: boolean value to represent whether or not Pink is in the scene
- length: length of the scene in seconds
Scene format: string in the following order:
{{characters in the scene(last one is the one who speaks)(only write first letter in name)}} {{length in seconds}} {{text}}

Given the following user request, return a series of formatted scenes seperated by according to user request.
User request: {user_request}
Formatted scenes:
"""

llm = OpenAI(temperature=0)
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)


def create_episode(user_request):
    response = llm_chain(user_request)['text']
    with open("script.txt", "w") as file:
        file.write(response)


create_episode(
    "blue and pink talk about their favorite anime, at least 5 scenes long")


__all__ = ['create_episode']
