from app import functions

def view():		
	html =  functions.load_component('head') 
	body_string = functions.load_component('body') 
	html += functions.template_string(body_string, {
	  "title": "The title",
	  "paragraph": "The paragraph"
	})
	html += functions.load_component('tail') 
	return html
