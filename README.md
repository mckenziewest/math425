# Math 425 for Canvas
 Content for Math 425, Abstract Algebra
 
 This is full Canvas content for Math 425, abstract algebra.
 To upload content automatically to Canvas, the [markdown2Canvas](https://github.com/ofloveandhate/markdown2canvas) library is required.
 
 Notes:
 1. All file paths are written using Windows syntax (aka they use `\` instead of `/`.)
 2. The file `_tools/upload_ready.py` is run using Spyder and it upload all of the files nicely.
 3. Since I am using Spyder and do not have a global variable `CANVAS_CREDENTIAL_FILE` as listed in the instructions for [markdown2Canvas](https://github.com/ofloveandhate/markdown2canvas), I have my Canvas credentials in the untracked file, `_tools/maccess.py`. These are read in and the course is generated within `_tools/course_info.py`.