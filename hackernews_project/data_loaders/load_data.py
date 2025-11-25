import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load top 100 stories from HackerNews API
    """
    # 1. Get the list of Top Story IDs
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    response = requests.get(url)
    story_ids = response.json()[:100]  # Limit to top 100 for speed
    
    # 2. Fetch details for each story
    stories = []
    base_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"
    
    print(f"Fetching {len(story_ids)} stories...")
    
    for _id in story_ids:
        r = requests.get(base_url.format(_id))
        if r.status_code == 200:
            stories.append(r.json())
            
    # 3. Convert to DataFrame
    df = pd.DataFrame(stories)
    
    # Select only relevant columns
    cols = ['id', 'title', 'url', 'score', 'time', 'by']
    # Filter to ensure columns exist (some stories might be missing fields)
    existing_cols = [c for c in cols if c in df.columns]
    
    return df[existing_cols]

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert len(output.index) >= 10, 'Should have at least 10 stories'