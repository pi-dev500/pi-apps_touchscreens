import tkinter as tk

root = tk.Tk()



# Create a frame with a width of 40 pixels
frame = tk.Frame(root, width=40, borderwidth=2, relief="groove")
frame.pack_propagate(False)


# Add some widgets to the frame
label = tk.Label(frame, text="This is a label")
label.pack()
label1= tk.Label(root, text="This is header")
label1.pack(side='top')
label1= tk.Label(root, text="This is header")

button = tk.Button(frame, text="This is a button")
button.pack()
frame.pack(side="right", fill="y")
label1.pack(side='top')
root.mainloop()
