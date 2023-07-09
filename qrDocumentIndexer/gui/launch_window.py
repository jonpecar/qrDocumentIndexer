import customtkinter as ctk
from .file_select.file_select_window import FileSelectWindow
from .stamp_options_frame import StampOptionsFrame

ADD_PDF_TITLE = 'Add QR Codes to PDFs'


class LaunchWindow(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        ctk.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.generate_button = ctk.CTkButton(master=self, text=ADD_PDF_TITLE, command=self.click_stamp_docs)
        self.generate_button.pack(fill='both', side='top', expand=True)
        self.sort_button = ctk.CTkButton(master=self, text='Sort Images', command=self.click_sort_button)
        self.sort_button.pack(fill='both', side='bottom', expand=True)

        self.pack(side='top', fill='both', expand=True)

    def click_stamp_docs(self):
        FileSelectWindow(self, ADD_PDF_TITLE, ADD_PDF_TITLE, StampOptionsFrame)

    def click_sort_button(self):
        pass