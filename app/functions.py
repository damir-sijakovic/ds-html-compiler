import re
import os
import importlib.util
from csscompressor import compress
from jsmin import jsmin
from bs4 import BeautifulSoup

work_dir = os.path.dirname(os.path.abspath(__file__))

def load_view():
	main_py_path = work_dir + '/../app/view.py'

	if not os.path.isfile(main_py_path):
		print(f"view.py file not found in {main_py_path}")
		return None

	try:
		spec = importlib.util.spec_from_file_location('view', main_py_path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)

		result = module.view()

		return result
	except Exception as e:
		print(f"Error loading or executing view.py: {e}")
		return None


def load_component(name):
	main_py_path = work_dir + "/../components/" + name + "/main.py"

	if not os.path.isfile(main_py_path):
		print(f"main.py file not found for {name} component")
		return ""

	try:
		spec = importlib.util.spec_from_file_location('main', main_py_path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		result = module.main()

		return result
	except Exception as e:
		print(f"Error loading or executing component: {e}")
		return ""
	
def template_string(string, dictionary):
    for key, value in dictionary.items():
        token = "{{" + key + "}}"
        string = string.replace(token, value)
    
    string = re.sub(r"\{\{.*?\}\}", "", string)    
    return string

"""
def template_string(string, assoc):
	if not isinstance(assoc, dict):
		print('templateString(): assoc parameter must be a dictionary!')
		return

	template = string

	for key, value in assoc.items():
		if isinstance(value, str):
			template = template.replace('{{' + key + '}}', value)
			return template
"""

def minify_css(string):    
	return compress(string)


def uglify_js(string):    
	return minify(string)

def prettify_html(string):    
	soup = BeautifulSoup(string, 'html.parser')
	return soup.prettify()

def load_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

def test():    
	print("hello test")

