import os
import sys
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(WORK_DIR + "/../../app/")
import functions 

def main():
	return functions.load_file(WORK_DIR + '/main.html')

