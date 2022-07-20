#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Jul 20, 2022 12:59:47 AM +0700  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import form.gui_supportimport customtkinter


class Toplevel1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
        top is the toplevel containing window."""
        _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#d9d9d9"  # X11 color: 'gray85'
        _ana1color = "#d9d9d9"  # X11 color: 'gray85'
        _ana2color = "#ececec"  # Closest X11 color: 'gray92'
        
        
            
        
        
        
        

        top.geometry("824x504+267+122")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Toplevel 0")
        



        self.top = top
        self.combobox = tk.StringVar()
        self.checkCommentGhim = tk.IntVar()

        
        
        
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.011, rely=0.02, relheight=0.903, relwidth=0.976)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = customtkinter.CTkFrame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(
            0,
            text="""Trang chủ""",
            compound="left",
            underline="""-1""",
        )



        self.TNotebook1_t2 = customtkinter.CTkFrame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(
            1,
            text="""Cài đặt""",
            compound="left",
            underline="""-1""",
        )



        self.TNotebook1_t3 = customtkinter.CTkFrame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(
            2,
            text="""Log""",
            compound="left",
            underline="""-1""",
        )




        self.btnImport = customtkinter.CTkButton(self.TNotebook1_t1)
        self.btnImport.place(relx=0.018, rely=0.881, height=34, width=107)



        self.btnImport.configure(compound="left")




        self.btnImport.configure(pady="0")
        self.btnImport.configure(text="""Import""")

        
        self.Scrolledtreeview1 = ScrolledTreeView(self.TNotebook1_t1)
        self.Scrolledtreeview1.place(relx=0.0, rely=0.021, relheight=0.816, relwidth=0.998)
        self.Scrolledtreeview1.configure(columns="Col1")
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0", text="Tree")
        self.Scrolledtreeview1.heading("#0", anchor="center")
        self.Scrolledtreeview1.column("#0", width="389")
        self.Scrolledtreeview1.column("#0", minwidth="20")
        self.Scrolledtreeview1.column("#0", stretch="1")
        self.Scrolledtreeview1.column("#0", anchor="w")
        self.Scrolledtreeview1.heading("Col1", text="Col1")
        self.Scrolledtreeview1.heading("Col1", anchor="center")
        self.Scrolledtreeview1.column("Col1", width="390")
        self.Scrolledtreeview1.column("Col1", minwidth="20")
        self.Scrolledtreeview1.column("Col1", stretch="1")
        self.Scrolledtreeview1.column("Col1", anchor="w")

        self.btnUpload = customtkinter.CTkButton(self.TNotebook1_t1)
        self.btnUpload.place(relx=0.239, rely=0.881, height=34, width=107)



        self.btnUpload.configure(compound="left")




        self.btnUpload.configure(pady="0")
        self.btnUpload.configure(text="""Upload""")

        self.btnGetCookies2 = customtkinter.CTkButton(self.TNotebook1_t1)
        self.btnGetCookies2.place(relx=0.45, rely=0.881, height=34, width=107)



        self.btnGetCookies2.configure(compound="left")




        self.btnGetCookies2.configure(pady="0")
        self.btnGetCookies2.configure(text="""Get Cookies""")

        self.txtSoLuong = customtkinter.CTkEntry(self.TNotebook1_t2)
        self.txtSoLuong.place(relx=0.188, rely=0.023, height=21, relwidth=0.093)


        self.txtSoLuong.configure(font="TkFixedFont")







        self.txtSoVideoToiDa = customtkinter.CTkEntry(self.TNotebook1_t2)
        self.txtSoVideoToiDa.place(relx=0.188, rely=0.072, height=21, relwidth=0.093)


        self.txtSoVideoToiDa.configure(font="TkFixedFont")







        self.txtKeyactive = customtkinter.CTkEntry(self.TNotebook1_t2)
        self.txtKeyactive.place(relx=0.188, rely=0.126, height=21, relwidth=0.343)


        self.txtKeyactive.configure(font="TkFixedFont")







        self.check1 = tk.Checkbutton(self.TNotebook1_t2)
        self.check1.place(relx=0.013, rely=0.186, relheight=0.058, relwidth=0.165)


        self.check1.configure(anchor="w")

        self.check1.configure(compound="left")




        self.check1.configure(justify="left")
        self.check1.configure(text="""Bình luận và ghim""")
        self.check1.configure(variable=self.checkCommentGhim)

        self.Message1 = tk.Message(self.TNotebook1_t2)
        self.Message1.place(relx=0.0, rely=0.023, relheight=0.044, relwidth=0.088)




        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text="""Số luồng""")
        self.Message1.configure(width=70)

        self.Message2 = tk.Message(self.TNotebook1_t2)
        self.Message2.place(relx=0.0, rely=0.075, relheight=0.044, relwidth=0.12)





        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text="""Số video tối đa""")
        self.Message2.configure(width=100)

        self.Message3 = tk.Message(self.TNotebook1_t2)
        self.Message3.place(relx=0.0, rely=0.128, relheight=0.044, relwidth=0.113)




        self.Message3.configure(padx="1")
        self.Message3.configure(pady="1")
        self.Message3.configure(text="""Key kích hoạt""")
        self.Message3.configure(width=91)

        self.Message3_1 = tk.Message(self.TNotebook1_t2)
        self.Message3_1.place(relx=0.0, rely=0.256, relheight=0.044, relwidth=0.063)




        self.Message3_1.configure(padx="1")
        self.Message3_1.configure(pady="1")
        self.Message3_1.configure(text="""Proxy""")
        self.Message3_1.configure(width=50)

        self.comboProxy = ttk.Combobox(self.TNotebook1_t2)
        self.comboProxy.place(relx=0.188, rely=0.256, relheight=0.049, relwidth=0.18)
        self.comboProxy.configure(textvariable=self.combobox)
        self.comboProxy.configure(takefocus="")

        self.txtLog = tk.Text(self.TNotebook1_t3)
        self.txtLog.place(relx=0.0, rely=0.028, relheight=0.97, relwidth=0.995)

        self.txtLog.configure(font="TkTextFont")






        self.txtLog.configure(wrap="word")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.txtStatus = customtkinter.CTkEntry(self.top)
        self.txtStatus.place(relx=0.012, rely=0.933, height=20, relwidth=0.478)


        self.txtStatus.configure(font="TkFixedFont")







        self.txtHsd = customtkinter.CTkEntry(self.top)
        self.txtHsd.place(relx=0.498, rely=0.933, height=20, relwidth=0.49)


        self.txtHsd.configure(font="TkFixedFont")








# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient="vertical", command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient="horizontal", command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky="nsew")
        try:
            vsb.grid(column=1, row=0, sticky="ns")
        except:
            pass
        hsb.grid(column=0, row=1, sticky="ew")
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != "_" and meth not in ("config", "configure"):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""

    def wrapped(cls, master, **kw):
        container = customtkinter.CTkFrame(master)
        container.bind("<Enter>", lambda e: _bound_to_mousewheel(e, container))
        container.bind("<Leave>", lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    """A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == "Windows" or platform.system() == "Darwin":
        child.bind_all("<MouseWheel>", lambda e: _on_mousewheel(e, child))
        child.bind_all("<Shift-MouseWheel>", lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all("<Button-4>", lambda e: _on_mousewheel(e, child))
        child.bind_all("<Button-5>", lambda e: _on_mousewheel(e, child))
        child.bind_all("<Shift-Button-4>", lambda e: _on_shiftmouse(e, child))
        child.bind_all("<Shift-Button-5>", lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == "Windows" or platform.system() == "Darwin":
        widget.unbind_all("<MouseWheel>")
        widget.unbind_all("<Shift-MouseWheel>")
    else:
        widget.unbind_all("<Button-4>")
        widget.unbind_all("<Button-5>")
        widget.unbind_all("<Shift-Button-4>")
        widget.unbind_all("<Shift-Button-5>")


def _on_mousewheel(event, widget):
    if platform.system() == "Windows":
        widget.yview_scroll(-1 * int(event.delta / 120), "units")
    elif platform.system() == "Darwin":
        widget.yview_scroll(-1 * int(event.delta), "units")
    else:
        if event.num == 4:
            widget.yview_scroll(-1, "units")
        elif event.num == 5:
            widget.yview_scroll(1, "units")


def _on_shiftmouse(event, widget):
    if platform.system() == "Windows":
        widget.xview_scroll(-1 * int(event.delta / 120), "units")
    elif platform.system() == "Darwin":
        widget.xview_scroll(-1 * int(event.delta), "units")
    else:
        if event.num == 4:
            widget.xview_scroll(-1, "units")
        elif event.num == 5:
            widget.xview_scroll(1, "units")


def start_up():
    gui_support.main()


if __name__ == "__main__":
    gui_support.main()
