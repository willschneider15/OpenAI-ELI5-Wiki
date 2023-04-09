import os
import json
import re
from pathlib import Path

# Set up paths
repo_root = Path(__file__).parent.parent
data_dir = repo_root / 'data'
scripts_dir = repo_root / 'scripts'
hallucinations_path = data_dir / 'hallucinations.json'

# Extract the PR message content
pr_message = os.environ['PR_MESSAGE']

# Split the PR message into lines
pr_lines = pr_message.splitlines()

# Extract the title from the first line
title_match = pr_lines[0].strip()

# Combine the remaining lines to form the explanation body
body_match = '\n'.join(pr_lines[1:]).strip()

if title_match and body_match:
    title = title_match.group(1)
    updated_body = body_match.group(1)

    # Load the existing hallucinations data
    with open(hallucinations_path, 'r') as f:
        hallucinations = json.load(f)

    # Add or update the hallucination entry
    if title in hallucinations:
        hallucinations[title]['ELI5-Explanation-Body-Updated'] = updated_body
    else:
        hallucinations[title] = {
            'ELI5-Explanation-Body-Updated': updated_body,
            'ELI5-Explanation-Body-Original': updated_body
        }

    # Save the updated hallucinations data
    with open(hallucinations_path, 'w') as f:
        json.dump(hallucinations, f, indent=2)
else:
    print("No title or explanation body found in the PR message.")