summarization_percentage = [10,20,30,40,50,60,70,80,90] # List used for the dropdown menu 

# Function to delete and then write to textbox
def rewrite_textbox(textbox, text):
    textbox.delete('1.0','end')
    textbox.insert('1.0', text)

