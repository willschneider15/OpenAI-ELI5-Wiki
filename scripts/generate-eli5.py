import os
import openai
from dotenv import load_dotenv
from pathlib import Path
import asyncio

# Load the API key from the .env file
load_dotenv()

# Add you key here
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Set up paths
repo_root = Path(__file__).parent.parent
data_dir = repo_root / 'data/GPT4_Concept_Lists'
output_dir = repo_root / 'content'
output_dir.mkdir(exist_ok=True)



# Generate ELI5 explanation
def generate_eli5(title):
    prompt = f"I am a Computer Science student. Explain the concept of {title} like I'm 5 in 150 words or less. Respond with a markdown file. Only include a well formatted explanation. Include bullet points when appropriate. Do not include titles."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are college Computer Science teacher."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message['content'].strip()

def process_category(category_file_name):
    category_file_path = data_dir / category_file_name
    category_output_dir = output_dir / category_file_name.replace(".txt", "")
    category_output_dir.mkdir(exist_ok=True)

    with open(category_file_path, "r") as f:
        titles = f.readlines()

    for title in titles:
        title = title.strip()
        eli5 = generate_eli5(title)
        markdown_file_name = f"{title}.md"
        markdown_file_path = category_output_dir / markdown_file_name

        with open(markdown_file_path, "w") as f:
            f.write(f"# {title}\n\n")
            f.write(f"{eli5}\n")

# Process just one category for testing
process_category("Computer_Science.txt")