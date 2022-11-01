import requests # Import Requests module
from tkinter import * # Import tkinter components with the "tkinter."
import utils # Import items from utils.py
import tkinter.messagebox as box # Import messageboxes from tkinter as box
import os, sys # Import os and system

# Function to get path of resources when frozen
def resource_path(relative_path):
    absolute_path = os.path.abspath(__file__)
    root_path = os.path.dirname(absolute_path)
    base_path = getattr(sys, '_MEIPASS', root_path)
    return os.path.join(base_path, relative_path)

window = Tk() # Create window
window.title('PowerSummarize') # Set window title to PowerSummarize
window.wm_iconbitmap(resource_path('icon.ico'))

summary_menu = IntVar() # Create an intvar to interact with dropdown menu
summary_menu.set(10) # Set default value to 10 on the dropdown menu
summary_menu_dropdown = OptionMenu(window, summary_menu, *utils.summarization_percentage) # Create dropdown menu object

textbox = Text(window, height = 25, width = 100, yscrollcommand= True) # Create textbox object
textbox.insert('1.0','Put text to summarize here') # Write defualt text to the textbox

def summarize_ai(text_to_summarize, summary_percent):
	url = "https://text-analysis12.p.rapidapi.com/summarize-text/api/v1.1" # API url to POST to

	payload = { # json to send including text, language, and summary percentage
		"language": "english",
		"summary_percent": summary_percent,
		"text": text_to_summarize
	}
	headers = { # headers to send including content type, api key, and api host
		"content-type": "application/json",
		"X-RapidAPI-Key": "05ae7c4e3fmsh2263447a65c8077p14fbfcjsnf41466ee25c8",
		"X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
	}
	try:
		r = requests.request("POST", url, json=payload, headers=headers) # Try to POST to API and save response as r
	except Exception as e:
		box.showerror('PowerSummarize Error',str(e)) # Raise error if failed
	
	response = r.json() # Save dictionary of response

	summary = response.get('summary') # get summary out of json object and save as variable. 
	
	# Get other variables just in case of later use. 
	sentence_count = response.get('sentence_count')
	time_taken = response.get('time_taken')
	ai_version = response.get('app_version')

	try:
		utils.rewrite_textbox(textbox, summary) # Attempt to write summary to textbox
		
		if summary == ' ' or summary == '':
			box.showerror('PowerSummarize Error', "Text Can't be Summarized Further") # Show error if there is no summary

	except Exception:
		box.showerror('PowerSummarize Error', "Text Can't be Summarized Further") # Show error if there is one





button = Button(window, text = 'Summarize', command = lambda: summarize_ai(textbox.get('1.0','end'), summary_menu.get())) # Create button object


label = Label(window, text = 'Percentage of Summary Compared to Original Text:') # Create label object

# Pack Elements
label.pack()
summary_menu_dropdown.pack()
textbox.pack(padx=5)
button.pack(pady=5)

window.mainloop() # Window Mainloop