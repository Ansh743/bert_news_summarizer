from scrapper import Scrapper
import csv

sc = Scrapper()
with open(r'dataset_build\links.csv', 'r') as f:
    reader = csv.DictReader(f,['index', 'link'], )
    for links in reader:
        print(links)
        break