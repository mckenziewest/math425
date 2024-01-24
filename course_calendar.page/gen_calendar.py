# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:18:29 2022

@author: WESTMR

There should be a text file with the daily schedule for the course in a
file named "basic_schedule.txt". The content from this schedule will be placed
sequentially in a grid with 3 columns.

TODO Make this a csv with columns: short description, long description, reading, notes
"""
from bs4 import BeautifulSoup

with open('source.md','r') as current_calendar:
    html_source = current_calendar.read()
    
soup = BeautifulSoup(html_source,'html.parser')
table_body = soup.table.tbody
table_body.clear()

with open('basic_schedule.txt','r') as list_form:
    calendar_details = list_form.read().split('\n')

import datetime
first = datetime.date(2024,1,29)
last = datetime.date(2024,5,10)
spring_term = first.month in [1,2]
break_days = [datetime.date(2024,3,ii) for ii in range(18,23)]
one_day = datetime.timedelta(days=1)
two_days = datetime.timedelta(days=2)
seven_days = datetime.timedelta(days=7)

mon = first
week_number = 1
ii = 0


while mon <= last:
    wed = mon + two_days
    thu = wed + one_day
    fri = thu + one_day
    
    
    new_tr = soup.new_tag("tr")
    new_th = soup.new_tag('th')
     
    if spring_term and mon in break_days:
        new_th.string = "Break"
    else:
        new_th.string = f"Week {week_number}"
        week_number += 1

    new_tr.append(new_th)
    
    for day in [mon,wed,fri]:
        new_td = soup.new_tag('td')
        if day in break_days:
            content = "No Class"
        elif ii < len(calendar_details):
            splitted = calendar_details[ii].split(",")
            if len(splitted) == 1:
                content = splitted[0]
            elif len(splitted) == 2:
                send_to = "page:" + splitted[1]
                content = soup.new_tag('a',"html.parser",attrs={"href":send_to})
                content.string = splitted[0]
            else:
                content == ""
            ii += 1
        else:
            content = ''
        new_td.string = f"{day.month}/{day.day} - "
        new_td.append(content)
        new_tr.append(new_td)
    table_body.append(new_tr)
    
    
    mon = mon+seven_days

with open('source.md','w') as current_calendar:
    current_calendar.write(soup.prettify())