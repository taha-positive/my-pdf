import tkinter as tk
from tkinter import filedialog
from txt_tools import TxtTools
import customtkinter


def add_pdf_file():
    root = tk.Tk()
    root.withdraw()

    pdf_files = filedialog.askopenfilenames(
        title="Choose PDF Files",
        filetypes=[("PDF files", "*.pdf")],
    )

    if pdf_files:
        txt = TxtTools("./data.txt")
        txt.add_pdf_file_to_txt(pdf_files)
        txt.delete_duplicate_lines_from_txt()
    else:
        ...




class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
