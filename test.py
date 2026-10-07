import os
from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["AZURE_API_KEY"],
    base_url=os.environ["AZURE_API_BASE"],
)

print("Azure OpenAI client initialized successfully.")      
print("Using model:", os.environ["AZURE_DEPLOYMENT"])
print("Using API version:", os.environ["AZURE_API_VERSION"])
print("Using endpoint:", os.environ["AZURE_API_BASE"])


# r = client.chat.completions.create(
#     model=os.environ["AZURE_DEPLOYMENT"],
#     messages=[{"role": "user", "content": "say hi"}],
# )
# print(r.choices[0].message.content)

r = client.responses.create(
    model= os.environ["AZURE_DEPLOYMENT"],          # deployment name
    input="say hi",
)
print(r.output_text)