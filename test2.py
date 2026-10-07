
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["AZURE_API_KEY"],
    base_url=os.environ["AZURE_API_BASE"],
)
r = client.responses.create(
    model=os.environ["AZURE_DEPLOYMENT"],
    input="say hi in Amitabh Bachchan style",
)
print(r.output_text)