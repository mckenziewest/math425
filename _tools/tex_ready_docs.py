# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:30:05 2023

@author: WESTMR
"""
import os 
import subprocess


def tex_if_needed(filenames='_tools/publish_this_time.txt',verbose=True):
    with open(filenames) as file:
        ready_files = file.read().split('\n')
        
    for directory in [rf for rf in ready_files if rf != '' and not (rf.startswith("#") or rf.startswith("%"))]:
        items = os.listdir(directory)
        for filename in items:
            if filename.endswith(".tex") and filename != "questions.tex":
                full_path_tex = os.path.join(directory,filename)
                associated_pdf = filename[:-4]+".pdf"
                full_path_pdf = os.path.join(directory,associated_pdf)
                if associated_pdf not in items:
                    print(f"Currently texing {directory}\\{filename}")
                    x = subprocess.call(f'pdflatex -output-directory "{directory}" "{filename}"')
                else: 
                    tex_time = os.path.getmtime(full_path_tex)
                    pdf_time = os.path.getmtime(full_path_pdf) 
                    if pdf_time<tex_time:
                        print(f"Currently texing {full_path_tex}")
                        x = subprocess.call(f'pdflatex -output-directory "{directory}" {filename}')
                    else: 
                        x=0
                        if verbose:
                            print(f"Not re-texing {full_path_tex}")
                if x != 0:
                    print(f"error compiling {full_path_tex}")
                    
if __name__ == "__main__":
    tex_if_needed()