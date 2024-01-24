import sys
import json

if len(sys.argv) == 1:
    assert False, "No objective specified"

def assignment_in_name(objective):
    if not objective.endswith(".assignment"):
        return objective + ".assignment"
    else:
        return objective

with open("proof_objective_template.tex") as the_file:
    proof_template = the_file.read()

with open("computation_objective_template.tex") as the_file:
    computation_template = the_file.read()

question_header = "\n\n%%%%\n\n\\newpage\nName: \\underline{\\hspace*{3in}}\n\t\\vskip .25in\n\n"

for objective in sys.argv[1:]:
    objective = assignment_in_name(objective)
    obname = objective.rstrip(".assignment")
    with open(objective+"/meta.json") as the_file:
        meta = json.load(the_file)

    if meta["name"] != obname:
        meta["name"] = obname
        with open(objective+"/meta.json","w") as the_file:
            json.dump(meta, the_file, indent = 4)

    ob_desc = meta["objective_description"] 
    
    if meta["objective_type"] == "proof":
        with open(objective+"/questions.tex") as the_file:
            question_tex = the_file.read()
        split_contents = question_tex.split(r"%%")
        this_tex = proof_template.replace(r"%%CUSTOM COMMANDS",split_contents[1]).replace("OBJECTIVE",obname).replace("DESCRIPTION",ob_desc)
        question_replacer = ""
        question_counter = 2
        for question in split_contents[2:]:
            question_replacer += question_header
            question_replacer += f"\\textbf{{{obname}.{question_counter}}}\n "
            question_replacer += question.lstrip("\n") 
            question_counter += 1

        this_tex = this_tex.replace(r"	%%QUESTIONS",question_replacer)

    elif meta["objective_type"] == "computation":
        this_tex = computation_template.replace("OBJECTIVE",obname).replace("DESCRIPTION",ob_desc)

    with open(objective+f"/{obname}.tex","w") as the_file:
        the_file.write(this_tex)