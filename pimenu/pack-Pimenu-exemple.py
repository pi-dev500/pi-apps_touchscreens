import tkinter as tk

root = tk.Tk()



# Create a frame with a width of 40 pixels
frame = tk.Frame(root, width=40, borderwidth=3, relief="raised", bg='blue')
frame.pack_propagate(False)


# Add some widgets to the frame
label = tk.Label(frame, text="This is a label",bg='blue')
label.pack()
Search_back = tk.Frame(root,bg='blue',relief='flat',height=30)
Search_back.pack(side='top',fill='both')
label1= tk.Label(root, text="This is header")
button = tk.Button(frame, text="This is a button")
button.pack()
frame.pack(side="right", fill="y")
label1.pack(side='top')
root.mainloop()
