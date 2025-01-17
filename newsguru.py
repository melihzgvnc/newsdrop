import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai = OpenAI()

class NewsGuru:

    prompt_lists = [
    """Read and comprehend the news, paying attention to key points.
    Give your insights in a clear and concise way from what you understood, under a title 'Insights'. """,

    """Format the text so that it is in a respresentable markdown format.
    Example format:
    # Title
    ## Subtitle
    Text
    """,

    """Translate the text into Turkish. Keep the formatting as it is.
    """,

    """Summarize the text so that it is no more than 250 characters. Make sure you never go over this limit."""
    ]

    
    def __init__(self):

        self.model = "gpt-4o-mini"

    
    def llm_run(self, user_prompt):
        
        response = openai.chat.completions.create(
            model=self.model,
            messages = [
                {"role":"user", "content":user_prompt}
            ]
        )
        response = response.choices[0].message.content
        return response

    
    def chain(self, llm_input):
        
        result = llm_input
        for i, prompt in enumerate(self.prompt_lists, 1):
            result = self.llm_run(f"{prompt} \n Input:\n{result}")
        return result