# converter/utils.py

from markdown import markdown

def text_to_html(text):
    return markdown(text)
