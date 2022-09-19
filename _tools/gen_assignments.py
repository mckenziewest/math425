# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:03:12 2022

@author: WESTMR
"""
import os
objectives = [f"Supp-{a+1}" for a in range(20,30)]

for o in objectives:
    if not os.path.exists(f'..\supplemental_assignments\{o}.assignment'):
        os.mkdir(f'..\supplemental_assignments\{o}.assignment')
    with open(f'..\supplemental_assignments\{o}.assignment\meta.json','w') as file:
        file.write(f'{{\n\t"name":"{o}",\n\t"type":"assignment",')
        file.write('\n\t"assignment_group_name":"Completion of Supplemental Exercises",\n\t"omit_from_final_grade":"True"\n}')
    
    with open(f'..\supplemental_assignments\{o}.assignment\source.md','w') as file:
        file.write('This exercise first appeared in Homework N.\n\n')
        file.write(f'Standalone version of the exercise: [pdf]({o}.pdf) [tex]({o}.tex).\n\n')
        file.write('You may improve your mark on this assignment by submitted rewrites of it on future assignments.\n\n')
        file.write('Recall that an objective is considered complete when you earn a Satisfactory or Exceptional grade on it.')
        file.write(f'\n\n* A score of 2 on this assignment corresponds to you having earned an Exceptional mark on {o}.')
        file.write(f'\n\n* A score of 1 on this assignment corresponds to you having earned a Satisfactory mark on {o}.')
        file.write(f'\n\n* A score of 0 on this assignment corresponds to you having earned an unsatisfactory mark on {o}.')
    
    tex_string = '\\documentclass[12pt]{article}\n'
    tex_string += '\\usepackage{amsmath,amsthm,amssymb}\n'
    tex_string += '\\usepackage[margin=.75in]{geometry}\n'
    tex_string += '\\pagestyle{empty}\n'
    tex_string += '\\setlength{\\parindent}{0pt}\n'
    tex_string += '\n\n\n'
    tex_string += '\\begin{document}\n'
    tex_string += 'Name: \\underline{\\hspace*{3in}}\n\\vskip .25in\n'
    tex_string += '\n'
    tex_string += f'\\textbf{{({o})}} \n'
    tex_string += '\n\n\n'
    tex_string += '\\end{document}'
    with open(f'..\supplemental_assignments\{o}.assignment\{o}.tex','w') as file:
        file.write(tex_string)