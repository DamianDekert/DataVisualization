from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

submissions_ids = r.json()
submissions_dicts = []
for submission_id in submissions_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'hn_link':
            f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submissions_dicts.append(submission_dict)

    submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'),
            reverse=True)
    
    for submission_dict in submissions_dicts:
        print(f"\nTytuł artykułu: {submission_dict['title']}")
        print(f"Łącze do dyskusji: {submission_dict['hn_link']}")
        print(f"Liczba komentarzy: {submission_dict['comments']}")

