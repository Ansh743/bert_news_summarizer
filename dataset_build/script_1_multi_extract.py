import numpy as np
import multiprocessing as multi
from multiprocessing import Queue
import sys
import pandas as pd
from scrapper import Scrapper
from preprocess import removeUnicodeChar




def chunks(n, page_list):
    """Splits the list into n chunks"""
    return np.array_split(page_list,n)
 

def trgt_fun(df, queue):
    sc = Scrapper()
    x = []
    for index, row in df.iterrows():
        sc.setUrl(row['link'])
        temp = {
            'id': row['id'],
            'text': removeUnicodeChar(sc.getArticle())
        }
        x.append(temp)
    res = queue.get()
    res.extend(x)
    queue.put(res)

if __name__ == '__main__':
    df = pd.read_csv('selected_links.csv')
    res = []

    name = 'anshul'
    mem_dict = {
        'anshul':{
            'l': 0,
            'r': 15340
        },
        'timi':{
            'l': 15340,
            'r': 30680
        },
        'piyush':{
            'l': 30680,
            'r': 46020
        },
        'anish':{
            'l': 46020,
            'r': 61361
        },
    }

    df = df.iloc[mem_dict[name]['l']:mem_dict[name]['r']]

    '''
    anshul - 0:15340
    timi - 15340:30680
    piyush - 30680:46020
    anish - 46020:61361
    '''
    cpus = multi.cpu_count()

    workers = []
    page_list = df
    page_bins = chunks(cpus, page_list)
    queue = Queue()
    queue.put(res)
    print('Using {}/{} CPU(s)'.format(cpus,cpus))
    for cpu in range(cpus):
        sys.stdout.write("CPU " + str(cpu) + "\n")
        worker = multi.Process(name=str(cpu), 
                            target=trgt_fun, 
                            args=(page_bins[cpu],queue))
        worker.start()
        workers.append(worker)

    for worker in workers:
        worker.join()

    df1 = pd.DataFrame().from_records(queue.get())
    df1.to_csv('texts_{}.csv'.format(name))
