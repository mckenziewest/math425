# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 09:58:54 2022

@author: WESTMR
"""

from bs4 import BeautifulSoup

with open('../../course_objectives.page/source.md',encoding='utf-8') as src:
    info = src.read()
    
soup = BeautifulSoup(info, 'html.parser')

names = [d for d in soup.find_all('h2') if d.get_attribute_list('class') == ['section']]
contents = [d for d in soup.find_all('div') if d.get_attribute_list('class') == ['content']]


mini_names = [n.text.split(':')[0] for n in names] + ['','','']
names_with_descriptions = {n.text.split(':')[0]:n.text.split(':',1)[1].strip() for n in names}
first_due = [d.text.strip().split('\n')[0].split()[-1] for d in contents] + ['','','']

offset = len(mini_names)//3
for i in range(offset):
    mn = mini_names[i]
    mn2 = mini_names[i+offset]
    due = first_due[i]
    due2 = first_due[i+offset]
    mn3 = mini_names[i+2*offset]
    due3 = first_due[i+2*offset]
    print(f"&&{mn}&&&&{mn2}&&&&{mn3}&\\\\\\hline")
    #print(f"&&&{mn}&{due}&&&&{mn2}&{due2}&&&&{mn3}&{due3}\\\\\\hline")

num_supps=36
offset = num_supps//3
for i in range(offset):
    
    #print(f"\\item Supp-{i+1}\\tab First due: ")
    print(f"&&Supp-{i+1}&&&&Supp-{i+1+offset}&&&&Supp-{i+1+2*offset}&\\\\\\hline")