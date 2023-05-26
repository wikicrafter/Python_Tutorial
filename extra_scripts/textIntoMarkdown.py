import tkinter as tk
import markdown
import re

def convert_to_markdown():
    input_text = text_entry.get("1.0", "end-1c").strip()
    
    if input_text:
        try:
            markdown_text = markdown.markdown(input_text)
            markdown_text = highlight_headings(markdown_text)
            markdown_text = highlight_code_blocks(markdown_text)
            markdown_text = highlight_hyperlinks(markdown_text)
            
            output_text.delete("1.0", "end")
            output_text.insert("1.0", markdown_text)
        except Exception as e:
            output_text.delete("1.0", "end")
            output_text.insert("1.0", "Error occurred during conversion:\n{}".format(str(e)))
    else:
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Please enter some text.")

def highlight_headings(text):
    headings = re.findall(r'<h(\d)>(.*?)<\/h\1>', text)
    for heading in headings:
        heading_level = int(heading[0])
        heading_text = heading[1]
        replacement = '#' * heading_level + ' ' + heading_text + '\n'
        text = text.replace('<h{}>{}</h{}>'.format(heading_level, heading_text, heading_level), replacement)
    return text

def highlight_code_blocks(text):
    code_blocks = re.findall(r'<pre><code>(.*?)<\/code><\/pre>', text, re.DOTALL)
    for code_block in code_blocks:
        replacement = '```' + '\n' + code_block + '\n' + '```' + '\n'
        text = text.replace('<pre><code>{}</code></pre>'.format(code_block), replacement)
    return text

def highlight_hyperlinks(text):
    hyperlinks = re.findall(r'<a href="(.*?)">(.*?)<\/a>', text)
    for hyperlink in hyperlinks:
        link_url = hyperlink[0]
        link_text = hyperlink[1]
        replacement = '[{}]({})'.format(link_text, link_url)
        text = text.replace('<a href="{}">{}</a>'.format(link_url, link_text), replacement)
    return text

# Create the main window
window = tk.Tk()
window.title("Text to Markdown Converter")

# Create the text entry field
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Create the "Convert" button
convert_button = tk.Button(window, text="Convert", command=convert_to_markdown)
convert_button.pack()

# Create the output text field
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Start the main event loop
window.mainloop()
