import os
import tkinter as tk
try:
    from tkhtmlview import HTMLLabel
except ImportError:
    os.system("pkexec pip3 install tkhtmlview")
root = tk.Tk()
#root.configure(bg="blue")
html_label = HTMLLabel(root, background="blue",  html="<h5> Hello World! </h5>")
html_label.config(highlightbackground="blue")
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()