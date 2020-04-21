# -*- coding: utf-8 -*-
"""final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XsbU3XNuKrnMDi21xj8V_5axdg4mb-9m
"""

import urllib.request
import bs4
import re
url = "https://www.phonecurry.com/benchmarks?fbclid=IwAR3GV0ujDslsugeVuX17dE-okfEOHXUNEXUi37eF-vo2lFNiMuBSKGxcAiw"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url= url, headers=headers)
data = urllib.request.urlopen(req).read()
root = bs4.BeautifulSoup(data, "html.parser")

rank_table = root.find(class_="table table-condensed benchmarks-table")
rank_detail = []
processor_rank = {}
for r in rank_table.findAll(class_="rank-column"):
  i = int(r.text)
  if not (i in processor_rank):
    processor_rank[i] = ""
  r = r.find_next('td')
  processor_rank[i] = (r.text).lower()

def processor2ranking(processor):
  for rank in range(1, len(processor_rank)+1):
    pro = processor_rank[rank]
    if(pro in processor) or (processor in pro):
      return rank

train_df = open('data(used to process CPU).csv', encoding='utf-8').read()
output = open('data(after processing CPU).csv', 'w')
train_df = train_df.split('\n')
t = train_df[0].split(',')
for i in t:
  output.write(i + '\t')
output.write('\n')
del train_df[-1]
count = 0
processor_in_rank = []
for i, t in enumerate(train_df[1:]):
  t = t.split(',')
  tmp = processor2ranking(t[5].lower())
  if("exynos 9820" in t[5].lower()):
    tmp = 7
  if(tmp == None):
    count = count + 1
    print(t[5], tmp)
  else:
    t[5] = str(tmp)
    for i in t:
      output.write(i + '\t')
    output.write('\n')
  processor_in_rank.append(tmp)
print(count)

