import json
import random
import streamlit as st

# Determines input types
st.title('The Tag Suggester!')
st.write('This script extracts the tags from my blogs and generates randomised Google search URLs for content ideation.')

keyword = st.text_input('Enter additional keyword for search')

num_of_tags = st.number_input('Enter number of tags to load', 1, 2)

load_tag_ideas = st.button('Load tag ideas')

def randomise_tags(file_path, num_combinations=5):

    with open(file_path, 'r') as f:
        tag_data = json.load(f)

    # Create a weighted distribution of tags
    tag_weights = [1/n for n in tag_data["Count"]]

    # Generate random combinations
    combinations = []
    for _ in range(num_combinations):
        combination = random.choices(tag_data["Tag"], weights=tag_weights, k=num_of_tags)
        combinations.append(combination)

    return combinations

file_paths = [
    "sampleface.co.uk.json",
    "cultrface.co.uk.json",
    "logicface.co.uk.json",
    "playrface.co.uk.json",
    "distantarcade.co.uk.json"
]

if load_tag_ideas:
    for file_path in file_paths:
        st.header(f"Ideas for {file_path.replace('.json', '')}")
        combinations = randomise_tags(file_path)
        for combination in combinations:
            if keyword:
                st.write(f"https://google.com/search?q={keyword}+{'+'.join(combination).lower().replace(' ', '+')}")
            else:
                st.write(f"https://google.com/search?q={'+'.join(combination).lower().replace(' ', '+')}")