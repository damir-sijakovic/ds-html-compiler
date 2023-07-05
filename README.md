**

## DS HTML Compiler

**WHAT DOES IT DO?**

Compiles components into single page html.

Your components are in "components" directory. You already have example "head" and "tail" components that contain html head and footer data. You can add more components and import them in "app/view.py" file. You can also use template {{example}} tokens to pass data into your components. When all components are collected with view.py, string is passed to pythons developer web server. All of this is done with "serve.py" script. "public" dir is used to store assets. To build use "build.py" script. This will crate new "build" directory, new "index.html" is created where all components are merged and assets from public directory are copied into new directory.

**STRUCTURE**

/public - this is what python dev server uses as web root
/app/view.py - this file collects all components
/app/functions.py - various functions
/components - html components

**COMPONENT**

To create new components, simply copy existing ones.

**VIEW FILE**

view.py is file where you should collect all components and return html string.

**USAGE**

python3 ./serve.py
python3 ./build.py


**REQUIRES MODULES**

csscompressor
jsmin
BeautifulSoup

**Have fun!**
