# Math 425 for Canvas
 Content for Math 425, Abstract Algebra
 
 This is full Canvas content for Math 425, abstract algebra.
 I taught this course with specifications grading, for more on that, see the syllabus.

 Included here are:
   * [Course Calendar](https://github.com/mckenziewest/math425/blob/main/course_calendar.page/source.md), a day-to-Day summary of content covered from Nicholson's 4th edition book.
   * [Syllabus](https://github.com/mckenziewest/math425/blob/main/syllabus.page/source.md), which includes a full description of the specifications grading scheme.
   * [List of Objectives](https://github.com/mckenziewest/math425/blob/main/course_objectives.page/objectives.md), statements of the explicit course objectives.
   * [Standard Homework Assignments](https://github.com/mckenziewest/math425/tree/main/assignments_with_submissions)
       * `Homework n.assignment` includes a tex document for the assignment, a meta file with points possible, due date, etc, and a simple source file that is the content of the Canvas page.
       * `Rewrites n.assignment` includes only the meta and source files, as these are the locations on Canvas to submit any rewrites.
   * Links to WeBWorK assignments, which can be shared upon request, and with time.
   * [Completion assignments for each objective with rewrites](https://github.com/mckenziewest/math425/tree/main/objective_assignments). 
     Within this directory, there are two types of assignments: proof-based and computation-based. Each folder, `Type-n.assignment`, contains
       * `Type-n.tex`, a tex document describing the objective and WebWork instructions, if it is a computation-based assignment, or if it a proof-based assignment, including 3-5 possible exercises that a student could complete to satisfy that objective.
       * `meta.json`, includes the WeBWorK link and information, if needed.
       * `source.md`, basic information about scoring and links to appropriate tex and pdf files.
   * [Supplemental problem assignments](https://github.com/mckenziewest/math425/tree/main/supplemental_assignments), which are described below in the description of the structure of the specifications grading.
   * [Project Descripton, Assignmens, and Rubrics](https://github.com/mckenziewest/math425/tree/main/project). 
       * Please see the [project instructions](https://github.com/mckenziewest/math425/blob/main/project/instructions.file/algebra_project_instructions.tex) file.
       * The rubrics are available in the directories that start with `artifact`.
   * Daily course notes and summaries organized by Chapter. 
       * Each of the sections covered has a `Section N.M.slides` directory containing a tex file for beamer slides with content for the day. 
       * Every day of class has a `Section----.slides` directory containing a `source.md` file describing the main learning objectives for the day, some related reading and/or video, and a suggested practice problem. In theory, students view these before class.
   * [Various Handouts](https://github.com/mckenziewest/math425/tree/main/handouts) 
   * [tools](https://github.com/mckenziewest/math425/tree/main/_tools) includes a variety of files to help construct the course and track complete content. Noteable are
       * [setup.tex](https://github.com/mckenziewest/math425/blob/main/_tools/setup.tex) is the header file for the slides
       * [upload_ready.py](https://github.com/mckenziewest/math425/blob/main/_tools/upload_ready.py) is the python file to run and automatically upload the files listed in an untracked file, `publish_this_time.txt`, to the course described in `course_info.py` using the credentials in the untracked file `maccess.py`.


 ## Specifications Grading Structure
 
 There are three components to the overall grade in the course:
   * 60% - completion of specifications
   * 15% - completion of supplemental exercises
   * 25% - course project
 You should read the syllabus for more information about what all of this means.
 
 ## Changes to be Made
 
 1. Objectives should earning a "sufficient" should not earn full credit toward completion of the objective. Maybe half credit to match with the supplemental exercises.
 2. Supplemental exercises should not be allowed rewrites. There are more than enough of them, and they should distinguish A vs B students. 
 
 ## Markdown2Canvas
 To upload content automatically to Canvas, the [markdown2Canvas](https://github.com/ofloveandhate/markdown2canvas) library is required.
 
 Notes:
 1. All file paths are written using Windows syntax (aka they use `\` instead of `/`.)
 2. The file `_tools/upload_ready.py` is run using Spyder and it upload all of the files nicely.
 3. Since I am using Spyder and do not have a global variable `CANVAS_CREDENTIAL_FILE` as listed in the instructions for [markdown2Canvas](https://github.com/ofloveandhate/markdown2canvas), I have my Canvas credentials in the untracked file, `_tools/maccess.py`. These are read in and the course is generated within `_tools/course_info.py`.
