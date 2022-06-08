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

# Blog list
blogs = ['sampleface.co.uk', 'cultrface.co.uk', 'logicface.co.uk', 'playrface.co.uk', 'distantarcade.co.uk']

# Streamlit stuff

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

# Reload all tags function
def update_all_tags():

	with st.spinner('Reloading tags...'):

		for blog in blogs:
		
			# Get tag data
			for pg in range(1, upper_limits[blog]+1):

				tag_url = f'https://{blog}/wp-json/wp/v2/tags?per_page=100&page={pg}'
				r_tag = requests.get(tag_url)
				api_tags = r_tag.json()

				for n in range(0,len(api_tags)):
					tags['Tag'].append(api_tags[n]['name'])
					tags['ID'].append(api_tags[n]['id'])
					tags['Count'].append(api_tags[n]['count'])

				with open(f"{blog}.json", "w") as outfile:
					json.dump(tags, outfile)
			tags['Tag'] = []
			tags['ID'] = []
			tags['Count'] = []

list_of_blogs = st.radio("Select the corresponding blog", blogs)

keyword = st.text_input('Enter additional keyword for search')

update_tags = st.button('↻ Refresh tags')

load_tag_ideas = st.button('Load tag ideas')

if update_tags:
	update_all_tags()

# Tag ideas functions

def sf_words():

	with open("sampleface.co.uk.json") as sf_json_file:
		sf = json.load(sf_json_file)
	sf_words_lists = sf['Tag']
	return sf_words_lists

def cultr_words():

	with open("cultrface.co.uk.json") as cf_json_file:
		cf = json.load(cf_json_file)
	cf_words_lists = cf['Tag']
	return cf_words_lists

def logic_words():

	with open("logicface.co.uk.json") as lf_json_file:
		lf = json.load(lf_json_file)
	lf_words_lists = lf['Tag']
	return lf_words_lists

def playr_words():

	with open("playrface.co.uk.json") as pf_json_file:
		pf = json.load(pf_json_file)
	pf_words_lists = pf['Tag']
	return pf_words_lists

def da_words():

	with open("distantarcade.co.uk.json") as da_json_file:
		da = json.load(da_json_file)
	da_words_lists = da['Tag']
	return da_words_lists

all_words_list = [sf_words(), cultr_words(), logic_words(), playr_words(), da_words()]

def sampleface():

	st.header('Sampleface ideas')

	for sample in range(5):
		with open("sampleface.co.uk.json") as sf_json_file:
			sf = json.load(sf_json_file)
		sf_words_count_lists = sf['Count']
		try:
			x = [n/(n+1) for n in sf_words_count_lists]
		except ZeroDivisionError:
			continue
			# sf_choices = random.choices(sf_words_count_lists, weights=(1/n), k=2)
		sample = random.choices(sf_words(), x, k=2)
		
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
			x = [n/(n+1) for n in cf_words_count_lists]
		except ZeroDivisionError:
			continue
			# sf_choices = random.choices(sf_words_count_lists, weights=(1/n), k=2)
		sample = random.choices(cultr_words(), x, k=2)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))	

def logicface():

	st.header('LOGiCFACE ideas')

	for sample in range(5):
		with open("logicface.co.uk.json") as lf_json_file:
			lf = json.load(lf_json_file)
		lf_words_count_lists = lf['Count']
		try:
			x = [n/(n+1) for n in lf_words_count_lists]
		except ZeroDivisionError:
			continue
		sample = random.choices(logic_words(), x, k=2)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))

def playrface():

	st.header('Playrface ideas')

	for sample in range(5):
		with open("playrface.co.uk.json") as pf_json_file:
			pf = json.load(pf_json_file)
		pf_words_count_lists = pf['Count']
		try:
			x = [n/(n+1) for n in pf_words_count_lists]
		except ZeroDivisionError:
			continue
		sample = random.choices(playr_words(), x, k=2)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))	

def distantarcade():

	st.header('Distant Arcade ideas')

	for sample in range(5):
		with open("distantarcade.co.uk.json") as da_json_file:
			da = json.load(da_json_file)
		da_words_count_lists = da['Count']
		try:
			x = [n/(n+1) for n in da_words_count_lists]
		except ZeroDivisionError:
			continue
		sample = random.choices(da_words(), x, k=2)
		
		if keyword:
			st.write('https://google.com/search?q=' + f'{keyword}+' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))
		else:
			st.write('https://google.com/search?q=' + '+'.join(sample).lower().replace(' ', '+').replace('&', '').replace('\u00e9', 'e').replace('#039;', "'"))

def all_blogs():

	sampleface()
	cultrface()
	logicface()
	playrface()
	distantarcade()
		
# Execute functions
if load_tag_ideas:
	all_blogs()