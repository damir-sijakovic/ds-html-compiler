from app import functions
import http.server
import os
import shutil

work_dir = os.path.dirname(os.path.abspath(__file__))
public_dir = work_dir + "/public" 
build_dir = work_dir + "/build"

if os.path.exists(build_dir):
    shutil.rmtree(build_dir)

shutil.copytree(public_dir, build_dir)

output = functions.load_view() 
with open(build_dir + '/index.html', 'w') as file:
	file.write(output)






