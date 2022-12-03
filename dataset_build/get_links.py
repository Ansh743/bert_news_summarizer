import json
import csv


links = []
with open(r'C:\Users\Anshul\Downloads\newsroom-thin.tar\newsroom-thin\train.jsonl\train-shell.jsonl', 'r') as f:
    for jline, i in zip(f.readlines(), range(50_000)):
        obj = json.loads(jline)
        d = {
            'index': i,
            'link': obj['archive']
        }
        links.append(d)

with open(r'dataset_build\links.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['index', 'link'])
    writer.writeheader()
    writer.writerows(links)