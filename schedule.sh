#!/usr/bin/bash

URL=https://www.reddit.com/r/indonesia/comments/jllvpr/01_november_2020_daily_chat_thread/.json
BASE=/opt/reddit-feed

mv $BASE/feed.json $BASE/feed_old.json

curl --doh-url https://cloudflare-dns.com/dns-query -H "User-agent:reddit-indonesia-user" $URL > $BASE/feed.json

python3 $BASE/compare_feed.py
