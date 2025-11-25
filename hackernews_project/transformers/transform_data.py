import pandas as pd
import re
from datetime import date

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.
    """
    # 1. Clean Text: Lowercase and remove punctuation
    clean_titles = df['title'].astype(str).str.lower().apply(lambda x: re.sub(r'[^\w\s]', '', x))
    
    # 2. Tokenize: Split titles into individual words and "explode" rows
    # (One row per story -> One row per word)
    words = clean_titles.str.split().explode()
    
    # 3. Remove Stop Words (Common words that add no value)
    stop_words = set([
        'the', 'a', 'an', 'to', 'for', 'in', 'on', 'of', 'and', 'is', 'with', 'by', 'at', 
        'from', 'be', 'it', 'that', 'this', 'are', 'hn:', 'show', 'ask', 'why', 'how', 
        'what', 'new', 'launch', 'out'
    ])
    
    # Filter out stop words and empty strings
    filtered_words = words[~words.isin(stop_words) & (words != '')]
    
    # 4. Aggregate: Count frequency of each keyword
    trends = filtered_words.value_counts().reset_index()
    trends.columns = ['keyword', 'count']
    
    # 5. Add Timestamp (Crucial for a daily batch pipeline)
    trends['date'] = date.today()
    
    print(f"Top Trend: {trends.iloc[0]['keyword']} with count {trends.iloc[0]['count']}")
    
    return trends

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'keyword' in output.columns, 'Missing keyword column'
    assert 'count' in output.columns, 'Missing count column'