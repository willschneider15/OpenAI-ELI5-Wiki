import wikipediaapi
from pathlib import Path
from collections import deque
# pip3 install wikipedia-api

# Set up paths
repo_root = Path(__file__).parent.parent
data_dir = repo_root / 'data'
scripts_dir = repo_root / 'scripts'

# Set up Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')

# Define categories to fetch concepts from
categories = [
    # 'Category:Elementary_mathematics',
    'Category:Algebra',
    'Category:Calculus',
    'Category:Geometry',
    'Category:Statistics',
    'Category:Physics',
    'Category:Chemistry',
    'Category:Biology',
    # 'Category:Earth_sciences',
    'Category:Computer_science',
    # 'Category:Engineering',
    'Category:Psychology',
    # 'Category:Sociology',
    # 'Category:Political_science',
    'Category:Economics',
    # 'Category:Literary',
    # 'Category:History',
    # 'Category:Geography',
    # 'Category:Language',
    # 'Category:Music_theory',
    # 'Category:Art_history',
]

def fetch_titles_from_category(category, limit=1000):
    titles = set()
    queue = deque([category])

    while queue and len(titles) < limit:
        current_category = queue.popleft()
        cat = wiki_wiki.page(current_category)
        
        for page in cat.categorymembers.values():
            if len(titles) >= limit:
                break
            if page.ns == 0:
                titles.add(page.title)
            elif page.ns == 14:
                queue.append(page.title)

    return list(titles)[:limit]

for category in categories:
    titles = fetch_titles_from_category(category)
    category_file_name = category.replace(':', '_') + '.txt'
    category_file_path = data_dir / category_file_name

    # Save the titles to the category-specific text file
    with open(category_file_path, 'w') as f:
        for title in titles:
            f.write(f"{title}\n")