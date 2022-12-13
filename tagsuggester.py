import streamlit as st
import json
import requests
import random

#Tags dictionary
tags = {
	'Tag': [],
	'ID': [],
	'Count': []
	}

# Determines input types
st.title('The Tag Suggester!')
st.write('This script extracts the tags from my blogs and generates randomised Google search URLs for content ideation.')

# Upper limits for tag page range
upper_limits = {
	'sampleface.co.uk': 4,
	'cultrface.co.uk': 4,
	'logicface.co.uk': 2,
	'playrface.co.uk': 2,
	'distantarcade.co.uk': 2,
	'ld89.org': 1
}

keyword = st.text_input('Enter additional keyword for search')

num_of_tags = st.number_input('Enter number of tags to load', 1, 2)

load_tag_ideas = st.button('Load tag ideas')

# Tag ideas functions

def blog_words(blog):

	with open(f"{blog}.json") as json_file:
		json_obj = json.load(json_file)
	blog_words_lists = json_obj['Tag']
	return blog_words_lists

def sampleface():

	st.header('Sampleface ideas')

	for sample in range(5):
		with open("sampleface.co.uk.json") as sf_json_file:
			sf = json.load(sf_json_file)
		sf_words_count_lists = sf['Count']
		try:
			x = [1/n for n in sf_words_count_lists]
		except ZeroDivisionError:
			continue
		sample = random.choices(blog_words('sampleface.co.uk'), x, k=num_of_tags)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))	
	
def cultrface():

	st.header('Cultrface ideas')

	for sample in range(5):
		with open("cultrface.co.uk.json") as cf_json_file:
			cf = json.load(cf_json_file)
		cf_words_count_lists = cf['Count']
		try:
			x = [1/n for n in cf_words_count_lists]
			st.write(x)
		except ZeroDivisionError:
			continue
		sample = random.choices(blog_words('cultrface.co.uk'), x, k=num_of_tags)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace('come in god','religion').replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))	

def logicface():

	st.header('LOGiCFACE ideas')

	for sample in range(5):

		lf_cats = ["blerds", "engineering", "mathematics", "mobile", "projects", "science", "biology", "chemistry", "earth sciences", "physics", "tech", "black tech", "computing", "internet", "web", "video games", "computer science", "ai"]

		lf_weights = [1, 1, 1.5, 1, 1, 1.5, 1, 1, 1, 1, 1.5, 1, 1, 1, 1, 1, 1, 1]

		lf_cats_sample = random.choices(lf_cats, lf_weights, k=1)

		with open("logicface.co.uk.json") as lf_json_file:
			lf = json.load(lf_json_file)
		lf_words_count_lists = lf['Count']

		try:
			x = [1/n for n in lf_words_count_lists]
		except ZeroDivisionError:
			continue
		sample = random.choices(blog_words('logicface.co.uk'), x, k=num_of_tags)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(lf_cats_sample).lower().replace(' ', '+') + '+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))

def playrface():

	st.header('Playrface ideas')

	for sample in range(5):

		pf_cats = ["american football", "athletics", "baseball", "basketball", "cycling", "golf", "motor sports", "olympics", "summer olympics", "snooker", "soccer", "sport", "tennis", "water sports", "winter sports", "ice hockey", "skiing", "wrestling", "winter olympics"]

		pf_weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5, 1, 1, 1, 1, 1, 1, 1]

		pf_cats_sample = random.choices(pf_cats, pf_weights, k=1)

		with open("playrface.co.uk.json") as pf_json_file:
			pf = json.load(pf_json_file)
		pf_words_count_lists = pf['Count']
		try:
			x = [1/n for n in pf_words_count_lists]
			st.write(x)
		except ZeroDivisionError:
			continue
		sample = random.choices(blog_words('playrface.co.uk'), x, k=num_of_tags)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(pf_cats_sample).lower().replace(' ', '+') + '+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))	

def distantarcade():

	st.header('Distant Arcade ideas')

	for sample in range(5):

		da_cats = ["gaming", "nintendo", "pc", "playstation", "pokemon", "sega", "xbox"]

		da_weights = [1.5, 1, 1, 1, 1, 1, 1]

		da_cats_sample = random.choices(da_cats, da_weights, k=1)

		with open("distantarcade.co.uk.json") as da_json_file:
			da = json.load(da_json_file)
		da_words_count_lists = da['Count']
		try:
			x = [1/n for n in da_words_count_lists]
		except ZeroDivisionError:
			continue
		sample = random.choices(blog_words('distantarcade.co.uk'), x, k=num_of_tags)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(da_cats_sample).lower().replace(' ', '+') + '+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))

def all_blogs():

	sampleface()
	cultrface()
	logicface()
	playrface()
	distantarcade()
		
# Execute functions
if load_tag_ideas:
	all_blogs()