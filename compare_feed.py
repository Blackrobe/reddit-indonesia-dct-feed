#!/usr/bin/python3

import json
from pprint import pprint

with open('feed.json', 'r') as f:
  parse = json.loads(f.read())
  
comments = parse[1]

with open('feed_old.json', 'r') as f:
  parse_old = json.loads(f.read())
  
comments_old = parse_old[1]

extract = []
for item in comments['data']['children']:
  data = item['data']
  if 'author' in data:
    extract.append({ 'author': data['author'], 'comment': data['body'] })

extract_old = []
for item in comments_old['data']['children']:
  data = item['data']
  if 'author' in data:
    extract_old.append({ 'author': data['author'], 'comment': data['body'] })

for item in extract:
  if item not in extract_old:
    print(item['author'])
    print(item['comment'])
