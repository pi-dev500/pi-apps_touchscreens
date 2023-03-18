import tkinter as tk
import subprocess
class Terminal(tk.Frame):
    def __init__(self, master=None, font='Monospace 12'):
        super().__init__(master)
        self.master = master
        self.create_widgets(font)

    def create_widgets(self,font):
        # Create a frame to hold the xterm window
        self.xterm_frame = tk.Frame(self.master,bg="white")
        self.xterm_frame.pack(fill="both", expand=True)
        # Wait for the xterm_frame to be created
        self.xterm_frame.update_idletasks()

        # Get the xterm_frame window ID
        xterm_window_id = self.xterm_frame.winfo_id()

        if xterm_window_id:
            # Calculate the width and height of the xterm window based on the size of the frame
            width = self.xterm_frame.winfo_width()
            height = self.xterm_frame.winfo_height()
            #print(width,'x',height)
            # Launch the xterm window with the appropriate dimensions and font
            command = f"xterm -into {xterm_window_id} -geometry {width}x{height} -fn '{font} -rightbar' 2>/dev/null"
            subprocess.Popen([command], shell=True)
        else:
            print("Unable to get window ID for xterm")
    def display_true(self):
        self.xterm_frame.pack(fill="both", expand=True)
        self.xterm_frame.update_idletasks()
    def display_false(self):
        self.xterm_frame.pack_forget()
        
if __name__=="__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.geometry("700x600")
    app = Terminal(root)

    button=tk.Button(root,text="switch",bg="white")
    def switch(switchy):
        if switchy==1:
            #root.configure(bg="black")
            app.display_true()
        else:
            root.configure(bg="white")
            app.display_false()
        switchy=switchy*-1
        button.configure(command=lambda: switch(switchy))
        #root.after(50, lambda: switch(switchy)) # big joke
    switch(-1)
    button.pack(fill="x")
    switch(1)
    root.mainloop()