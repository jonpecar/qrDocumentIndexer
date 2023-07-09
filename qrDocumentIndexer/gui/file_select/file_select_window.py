from typing import Type

import tkinter as tk
import customtkinter as ctk

class FileSelectWindow(ctk.CTkToplevel):
    def __init__(self, master, title: str, 
                    action_button_text: str, 
                    options_frame: Type[ctk.CTkFrame],
                    *args, **kwargs):
        ctk.CTkToplevel.__init__(self, master, *args, **kwargs)
        self.geometry("1200x800")
        self.title(title)
        self.button_frame = ctk.CTkFrame(self)
        self.select_files = ctk.CTkButton(self.button_frame, text='Select Files',
                                        command=self._select_files_clicked)
        self.action_button = ctk.CTkButton(self.button_frame, text=action_button_text,
                                                command=self._action_button_clicked)
        
        self.button_frame.pack(side=tk.TOP, fill=tk.X)
        self.select_files.pack(side=tk.LEFT, fill=tk.X)
        self.action_button.pack(side=tk.RIGHT, fill=tk.X)

        if options_frame:
            self.options_frame = options_frame(self)
            self.options_frame.pack(side=tk.TOP, fill=tk.X)
        

    def _select_files_clicked(self):
        print("Select files")
        pass

    def _action_button_clicked(self):
        try:
            options = self.options_frame.options
            print(options)
        except:
            print("No options")
        pass