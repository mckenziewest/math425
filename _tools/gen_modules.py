# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:18:29 2022

@author: WESTMR
"""
from course_info import course
#import markdown2canvas as mc

for w in range(1,16):
    course.create_module({'name':f'Week {w}'})
import datetime
first = datetime.date(2022,9,5)
two_days = datetime.timedelta(days=2)
seven_days = datetime.timedelta(days=7)
first + two_days

modules_to_edit = [m for m in course.get_modules() if any([f'Week {i}' in m.name for i in range(1,16)])]

for m in modules_to_edit:
    the_week = int(m.name[5:])-1
    mon = first + (the_week)*seven_days
    wed = mon + two_days
    fri = wed + two_days
    m.create_module_item({'title':f"Monday {mon.month}/{mon.day}", 'type':'SubHeader'})
    m.create_module_item({'title':f"Wednesday {wed.month}/{wed.day}", 'type':'SubHeader'})
    m.create_module_item({'title':f"Friday {fri.month}/{fri.day}", 'type':'SubHeader'})