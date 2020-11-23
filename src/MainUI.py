"""This will be used for creating the UI elements and apis for OpenPalm"""

from os import (path, mkdir)
from functools import wraps
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox  # pylint: disable=unused-import
from importlib import reload
import passmanager as pm
import Database as db
import analyse as an
import Mail as mail


def validate(func):
    """
    This is the `validate` function
    params: args: In case, if this function is called
    from a method , then args=self
    It checks whether the `creds` directory exists or not.
    If it does not exist, it first creates it and then
    execute the function.
    It will be wrapper function for some methods.
    The `wraps(func)` decorator of functools library
    will allow to retain the docstring of the method to
    which it wraps.
    For example:

    def decorated(func):
        def wrapper():
            print("Decorated")
            func()
        return wrapper

    @decorated
    def main():
    '''This is the function docstring'''
        print("This is the original func")

    main()
    >> Decorated
       This is the original func

    main.__docs__
    >> None

    Here, the docstring of `main` is lost because of
    the wrapper function.
    To prevent this, we decorate our decorator with
    functools.wrap(func) decorator which retains the
    metadata and docstrings from the original function.
    """

    @logs
    @wraps(func)
    def inner(*args):
        if not path.isdir("creds"):
            mkdir("creds")
            func(*args)
        else:
            func(*args)  # if directory exists, do the function

    return inner


def logs(func):
    """
    In case, called from a class , then *args=self.
    This function will work as a decorator that will
    call the wrapped function in a `try` - `except` block
    and in case of any exception, it will create/append a
    `logs.txt` file that will contain the exception information.
    """
    def inner(*args):
        try:
            func(*args)     # if called from class: Translates to : func(self)
        except Exception as e:
            with open('log.txt', 'a+') as logs:
                logs.write(repr(e)+'\n')

    return inner


class Openpalm(tk.Tk):
    """
    This class will inherit the methods of tk.Tk class
    This class has the following methods:
        1. constructor(__init__)
            This constructor initialises:
                (i) container (tk.Frame object)
                (ii) frames (dictionary object)

            (a) `container` is tkinter Frame object and a
                child of the tkinter window. Note that in
                Open Palm, we have only tkinter Window instance
                open. All the other UI frame child of
                the `container`

            (b) `frames` (or self.frames after binding it to the object)
                is a dictionary that contains the
                 ->(i) `name of the page` as key
                 ->(ii) `the instance of the child `frames` of
                        `container` as value.
                        This means if you call any item of the
                        dictionary `frames` , then it will return a
                        `tk.Frame` object which will be used to show that
                        frame.

        2. show_frame takes name of the frame as argument and shows that frame
           whenever this function is called.

    """

    def __init__(self):
        # Initialises all the variables or tk.Tk
        tk.Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # self.frames is a dictionary that stores function calls
        self.frames = {}

        self.frames["Editor"] = Editor(
            parent=container, controller=self)  # Calls the Editor Class

        self.frames["Login_Page"] = Login_Page(
            parent=container, controller=self)  # Calls the Login_Page Class

        self.frames["Teacher_Page_Login"] = Teacher_Page_Login(
            parent=container, controller=self)  # Calls Teacher_Page_Login

        self.frames["Master_Page"] = Master_Page(  # Calls Master_Page
            parent=container, controller=self)

        self.frames["Editor"].grid(row=0, column=0, sticky="nsew")
        self.frames["Login_Page"].grid(row=0, column=0, sticky="nsew")
        self.frames["Teacher_Page_Login"].grid(row=0, column=0, sticky="nsew")
        self.frames["Master_Page"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("Editor")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Editor(tk.Frame):
    """
    This is the Editor class.
    It inherits tkinter Frame class and returns a
    tkinter Frame object. Its methods & attributes are:
        1. constructor(__init__)
           takes in args : parent & controller.

               *parent* is the argument which will tell
               this Frame whose child it is.
               For example: parent=container is same as
               creating a tkinter Frame:
               child = tk.Frame(container)

               *controller* is a argument which
               allows out tkinter Frame(Editor)
               to access selective attributes of its parent
               without explicitly calling all the methods
               using `super().__init__(self)`

               Exmple:
               In our Openpalm class(above) , we had given
               `controller=self` meaning that our controller
               variable(or argument) now contains the instance
               of Openpalm class.

               Therefore using: `controller.show_frame()`
               is same as saying `Openpalm.show_frame()`
               that is accessing only the `show_frame` method
               of Openpalm class.


    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.mainframe = tk.Frame(self, width=1600)

        # The Design Aspect of the frame
        self.Text_box = tk.Text(self.mainframe, bg='#333333', fg='#f2f2f2')  # noqa:E501 pylint:disable=invalid-name

        self.Text_box.configure(font=("Courier", 16, ''),
                                insertbackground='white')
        # The Frame that contains all the buttons
        self.frm_btns = tk.Frame(self.mainframe)

        # The instatiation of buttons
        self.btn_submit = ttk.Button(self.frm_btns, text='SUBMIT', command=self.submit)  # noqa E501
        self.btn_clear = ttk.Button(self.frm_btns, text='CLEAR')
        self.btn_docs = ttk.Button(self.frm_btns, text='Docs')
        self.btn_open = ttk.Button(
            self.frm_btns, text='OPEN', command=self.open_file)
        self.btn_save = ttk.Button(
            self.frm_btns, text='SAVE', command=self.save_file)
        self.btn_test = ttk.Button(
            self.frm_btns, text='Test', command=self.testit)

        self.option = tk.StringVar()

        self.option.set("Select Code")
        self.dropdown = ttk.Combobox(self.frm_btns, state="readonly", textvariable=self.option, width=15)  # noqa: E501 pylint: disable=line-too-long
        self.dropdown['values'] = ["#1", "#2", "#3", "#4"]
        self.dropdown.bind("<<ComboboxSelected>>", self.write_func)

        # The gridding of buttons
        self.btn_submit.grid(row=4, column=0, sticky='ew')
        self.btn_clear.grid(row=1, column=0, sticky='ew')
        self.btn_docs.grid(row=6, column=0, sticky='ew')
        self.btn_open.grid(row=2, column=0, sticky='ew')
        self.btn_save.grid(row=3, column=0, sticky='ew')
        self.btn_test.grid(row=0, column=0, sticky='ew')
        self.dropdown.grid(row=7, column=0, sticky='es')

        # The gridding of the frame that contains all the buttons
        self.frm_btns.grid(row=0, column=2, sticky='ns')

        # The gridding of the Text Box
        self.Text_box.grid(row=0, column=0, sticky='nsew')
        # THe Design aspect of the frame

        move_to_page_1 = ttk.Button(self.frm_btns, text="Go to Login Page",  # noqa E501
                                   command=lambda: controller.show_frame("Login_Page"))  # noqa E501

        move_to_page_1.grid(row=5, column=0, sticky='ew')

        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.mainframe.rowconfigure(0, minsize=800, weight=1)
        self.mainframe.columnconfigure(0, weight=1)

        self.Text_box.insert('1.0', "#It is highly recommended that you check your code first in IDLE first for syntax errors and then Test it here.\n\n")  # noqa E501 pylint: disable-all
        self.Text_box.insert('3.0', "#If your code has syntax errors ,Open-Palm will freeze. You have to restart it in that case \n\n")  # noqa E501

    def open_file(self):  # Opens a saved file
        """This method is bound to the
           `OPEN` button of Editor frame.
           This method opens any `.py` file
           in the Editor buffer
        """
        self.path = askopenfilename(filetypes=(
            ("python files", ".py"), ("All Files", "*.py")))
        if not self.path:
            return
        self.Text_box.delete(1.0, tk.END)
        with open(self.path, 'r') as file:
            self.text = file.read()
            self.Text_box.insert(tk.END, self.text)

    def save_file(self):
        """
        This method is used to save the current file
        in the buffer to the system
        """
        self.filepath = asksaveasfilename(defaultextension="py", filetypes=[("python files", "*.py"), ("All Files", "*.*")],)  # noqa E501 pylint: disable=all
        if not self.filepath:
            return

        with open(self.filepath, "w") as output_file:
            text = self.Text_box.get("1.0", tk.END)
            output_file.write(text)

    def save_for_test(self):
        """
        This function is a special method that
        saves the current buffer in the Editor
        frame in the `test_it.py` file.
        """
        with open("test_it.py", "w+") as file:
            text = self.Text_box.get("1.0", tk.END)
            file.write(text)

    @logs
    def testit(self, *args):  # pylint: disable=unused-argument
        """
        This method has the following tasks:
            1. Save the current file in the Editor buffer in `test_it.py`
            2. import test_it.py and run test cases on it
        This method is wrapped around the `logs` function to capture
        any errors that happen during the evaluation process.
        """
        self.questions = an.questions  # noqa:E501 pylint: disable=attribute-defined-outside-init
        self.testcases = an.testcases  # noqa:E501 pylint: disable=attribute-defined-outside-init
        tmp_qns = ["check_even", "bubble_sort", "fibonacci", "check_palin"]

        # It selects only the code number and not the '#'
        self.code = self.option.get()[1]  # noqa: E501 pylint: disable=attribute-defined-outside-init

        if self.code.isalpha():
            tk.messagebox.showerror("Select Question Code", "Please Select a question Code")  # noqa: E501  pylint: disable=line-too-long

        else:
            import test_it  # noqa: E501  # pylint: disable=import-outside-toplevel,syntax-error
            self.save_for_test()
            test_it = reload(test_it)

            ver_soln = an.chk(int(self.code), self.testcases[int(self.code)])
            user_soln = []

            # ---------user soln----------------

            testdata = self.testcases[int(self.code)]

            for k in testdata:
                try:
                    ans = getattr(test_it, tmp_qns[int(self.code)-1])(k)
                    user_soln.append(ans)

                except Exception as exception:
                    print(exception)
                    print(exception.__class__.__name__)

                    break
            if user_soln == ver_soln:
                tk.messagebox.showinfo("Congratulations", "Your code has passed all the test cases. You may now submit the solution.")  # noqa E501
                print(user_soln)
            else:
                tk.messagebox.showinfo("Try Again" , "Your code has failed in one or multiple test cases.")  # noqa E501
                print(user_soln)

    def write_func(self, event):  # pylint: disable=all
        """
        This method writes the boiler plates for each question whenever
        a selection is made by the user.
        """
        if self.dropdown.get() == "#1":
            self.Text_box.delete('1.0', tk.END)

            self.Text_box.insert('1.0', "#It is highly recommended that you check your code first in IDLE first for syntax errors and then Test it here.\n\n")  # noqa E501
            self.Text_box.insert('3.0', "#If your code has syntax errors ,Open-Palm will freeze. You have to restart it in that case \n\n")  # noqa E501

            self.Text_box.insert('5.0', "def check_even(n):\n")
            self.Text_box.insert('6.0', "\t#Enter Code here\n")
            self.Text_box.insert('7.0', "\tpass")

        if self.dropdown.get() == "#2":
            self.Text_box.delete('1.0', tk.END)
            self.Text_box.insert('1.0', "#It is highly recommended that you check your code first in IDLE first for syntax errors and then Test it here.\n\n")  # noqa E501
            self.Text_box.insert('3.0', "#If your code has syntax errors ,Open-Palm will freeze. You have to restart it in that case \n\n")  # noqa E501

            self.Text_box.insert('5.0', "def bubble_sort(arr):\n")
            self.Text_box.insert('6.0', "\t#Enter Code here\n")
            self.Text_box.insert('7.0', "\tpass")

        if self.dropdown.get() == "#3":

            self.Text_box.delete('1.0', tk.END)

            self.Text_box.insert('1.0', "#It is highly recommended that you check your code first in IDLE first for syntax errors and then Test it here.\n\n")  # noqa E501
            self.Text_box.insert('3.0', "#If your code has syntax errors ,Open-Palm will freeze. You have to restart it in that case \n\n")  # noqa E501

            self.Text_box.insert('5.0', "def fibonacci(n):\n")
            self.Text_box.insert('6.0', "\t#Enter Code here\n")
            self.Text_box.insert('7.0', "\tpass")

        if self.dropdown.get() == "#4":

            self.Text_box.delete('1.0', tk.END)
            self.Text_box.insert('1.0', "#It is highly recommended that you check your code first in IDLE first for syntax errors and then Test it here.\n\n")  # noqa E501
            self.Text_box.insert('3.0', "#If your code has syntax errors ,Open-Palm will freeze. You have to restart it in that case \n\n")  # noqa E501

            self.Text_box.insert('5.0', "def check_palin(s):\n")
            self.Text_box.insert('6.0', "\t#Enter Code here\n")
            self.Text_box.insert('7.0', "\tpass")

    def submit(self):
        """This method generates a prompt whenever the user
        clicks the submit button"""
        if tk.messagebox.askyesno("Confirm Submit", "Are you sure you want to submit? Once submitted , it cannot be undone."):  # noqa E501
            body = "Open Palm Service Mail"
            # Enter the password of the email address
            ml = mail.Mail("", body, "", "")
            if ml.send_mail():
                tk.messagebox.showinfo("Done", "Mail Send")
            else:
                tk.messagebox.showinfo("Failed", "Failed to send the mail. Check your internet connection or call your admin")  # noqa E501


class Login_Page(tk.Frame):
    """
    This page creates a basic login page
    which asks the user to go the the
    Teacher page login or the Editor
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainframe = tk.Frame(self)
        # The Design Aspect of the frame

        login_label = tk.Label(self.mainframe, text="This is Login Page")
        login_label.grid(row=0, column=0)

        # The Design Aspect of the frame
        teacher_btn = ttk.Button(self.mainframe, text='TEACHER', width=15,
                                command=lambda: self.controller.show_frame("Teacher_Page_Login"))  # noqa E501
        teacher_btn.grid(row=1, column=0)

        button = ttk.Button(self.mainframe, text="Go to the Editor",
                           command=lambda: controller.show_frame("Editor"), width=15)  # noqa E501
        button.grid(row=2, column=0)
        self.mainframe.pack()


class Teacher_Page_Login(tk.Frame):
    """
    This page creates a basic login interface
    that asks the user for a password to access
    the Master page.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # The Frame that contains all the objects of the Teacher Page. It is the servant of self(Window)  # noqa E501

        self.mainframe = tk.Frame(self)

        # The Design Aspect of the frame
        lbl = tk.Label(self.mainframe, text="TEACHER'S PAGE", font=("Ubuntu", 14, ''))  # noqa E501
        lbl.grid(row=0, column=0, sticky='nsew')

        semi_frm = tk.Frame(self.mainframe)

        usr_lbl = tk.Label(semi_frm, text='User Name', font=("Courier", 12, ''))  # noqa E501J
        usr_lbl.grid(row=1, column=0)

        self.user_box = tk.Entry(semi_frm)
        self.user_box.grid(row=1, column=1)

        passwd_lbl = tk.Label(semi_frm, text='Password', font=("courier", 12, ''))  # noqa E501
        passwd_lbl.grid(row=2, column=0)

        self.passwd_box = tk.Entry(semi_frm, show="*")
        self.passwd_box.grid(row=2, column=1)

        # The Design Aspect of the frame
        self.sign_in = ttk.Button(semi_frm, text="Sign In", command=self.get_user_info)  # noqa E501
        self.sign_in.grid(row=4, column=1, sticky='nsew')

        goto_login = ttk.Button(semi_frm, text='Login Page',
                               command=lambda: self.controller.show_frame("Login_Page"))  # noqa E501
        goto_login.grid(row=4, column=0, sticky='nsew')

        semi_frm.grid(row=1, column=0)

        self.mainframe.pack()  # Packing of the mainframe

    def get_user_info(self, event=None):
        """This method is bound to `sign_in` button.
           It fetches whatever is written in the
           `username` and `password` entry boxes
           and checcks if those credentials exists in `admins.csv`
           file.
        """
        self.prompt = tk.Label(self.mainframe, text="", fg='red')
        self.prompt.grid(row=3, column=0, sticky='nsew')

        master_creds = ["jaydeep", "12345"]

        usrid = self.user_box.get()
        usrpass = self.passwd_box.get()

        userid = pm.cipherpass(usrid)
        userpass = pm.cipherpass(usrpass)

        dic = pm.get_pass()

        if [usrid, usrpass] == master_creds:
            print("passed")
            self.passwd_box.delete(0, "end")
            self.user_box.delete(0, 'end')
            self.controller.show_frame("Master_Page")

        elif userid in dic:
            if userpass == dic[userid]:
                print("passed")
                self.passwd_box.delete(0,"end"), self.user_box.delete(0, 'end')  # noqa E501
                self.controller.show_frame("Master_Page")

            else:
                print("failed due to incorrect password")
                self.prompt = tk.Label(self.mainframe , text = "The Username or the password is incorrect", fg='red')  # noqa E501
                self.prompt.grid(row=2, column=0, sticky='nsew')
        else:
            print("failed")
            self.prompt = tk.Label(self.mainframe, text="The Username or the password is incorrect", fg='red')  # noqa E501
            self.prompt.grid(row=2, column=0, sticky='nsew')


class Master_Page(tk.Frame):

    """
    This is the master page. It handles all the database
    connectivity and UI of the Students Table.
    Its methods are:
        1. class constructor (__init__)
                It creates the UI for this Frame
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainframe = tk.Frame(self)

        lbl_frm_table = ttk.LabelFrame(self.mainframe, text="Student Data")
        lbl_frm_data = ttk.LabelFrame(self.mainframe, text="Information")
        lbl_frm_info = ttk.LabelFrame(self.mainframe, text="Data Entry")
        lbl_frm_admin = ttk.LabelFrame(self.mainframe, text="Admin")

        # --------------/\/\ micellaneous/\/\---------------------
        self.v1 = tk.StringVar()            # textvar of src_ent
        self.v2 = tk.StringVar()            # self.name_ent
        self.v3 = tk.StringVar()            # self.class_ent
        self.v4 = tk.StringVar()            # self.sec_ent
        self.v5 = tk.StringVar()            # self.roll_ent
        self.v6 = tk.StringVar()            # Admin-User
        self.v7 = tk.StringVar()            # Admin-Pass
        # -------------/\/\ micellaneous/\/\----------------------

        # ------------/\/\ Frame table (lbl_frm_table) (s)/\/\----
        self.trview = ttk.Treeview(lbl_frm_table, columns=(1, 2, 3, 4), show="headings", height=6)  # noqa E501
        self.trview.pack(fill="both", expand=True, ipady=5)
        self.trview.heading(1, text="Name")
        self.trview.heading(2, text="Class")
        self.trview.heading(3, text="Section")
        self.trview.heading(4, text="Roll no")
        self.trview.bind("<Double-Button-1>", self.idrow)
        # -----------/\/\ Frame table (lbl_frm_table)(e) /\/\-----

        # -----------/\/\ Frame data (lbl_frm_data)(s) /\/\-------
        src_lbl = ttk.Label(lbl_frm_data, text="Search by name : ")
        self.src_ent = ttk.Entry(lbl_frm_data, textvariable=self.v1)
        src_btn = ttk.Button(lbl_frm_data, text="Search", command=self.search_data)  # noqa E501
        src_lbl.pack(side="left", padx=20)
        self.src_ent.pack(side="left")
        src_btn.pack(side="left", padx=10)
        rfs_btn = ttk.Button(lbl_frm_data, text="Refresh", command=self.refresh)  # noqa E501J
        rfs_btn.pack(side="left", padx=10)
        # ----------/\/\ Frame data (lbl_frm_data)(e) /\/\---------

        # ---------/\/\ Frame info (lbl_frm_info)(s) /\/\----------
        name_lbl = ttk.Label(lbl_frm_info, text="Name ")
        class_lbl = ttk.Label(lbl_frm_info, text="Class ")
        sec_lbl = ttk.Label(lbl_frm_info, text="Section ")
        roll_lbl = ttk.Label(lbl_frm_info, text="Roll no ")

        name_lbl.grid(row=0, column=0, pady=10)
        class_lbl.grid(row=1, column=0, pady=10)
        sec_lbl.grid(row=2, column=0, pady=10)
        roll_lbl.grid(row=3, column=0, pady=10)

        self.name_ent = ttk.Entry(lbl_frm_info, width=35, textvariable=self.v2)
        self.class_ent = ttk.Entry(lbl_frm_info, width=35, textvariable=self.v3)  # noqa E501
        self.sec_ent = ttk.Entry(lbl_frm_info, width=35, textvariable=self.v4)
        self.roll_ent = ttk.Entry(lbl_frm_info, width=35, textvariable=self.v5)

        self.name_ent.grid(row=0, column=1, pady=10)
        self.class_ent.grid(row=1, column=1, pady=10)
        self.sec_ent.grid(row=2, column=1, pady=10)
        self.roll_ent.grid(row=3, column=1, pady=10)

        frm_btn = tk.Frame(lbl_frm_info)
        frm_btn.grid(row=4, column=1)

        add_btn = ttk.Button(frm_btn, text="Add ", command=self.add_user_info)
        update_btn = ttk.Button(frm_btn, text="Update ", command=self.update_data)  # noqa E501
        del_btn = ttk.Button(frm_btn, text="Delete ", command=self.delete_user_info)  # noqa E501

        add_btn.grid(row=0, column=0, padx=10)
        update_btn.grid(row=0, column=1, padx=10)
        del_btn.grid(row=0, column=2, padx=10)

        std_data = db.get_response("StudentInfo")
        self.data = std_data.get_all_data()
        self.update_user_info(self.data)

        # ----------/\/\ Frame info (lbl_frm_info)(e) /\/\---------

        # ----------/\/\ Frame info (lbl_frm_admin)(s) /\/\------
        btn_frm = ttk.Frame(lbl_frm_admin)
        ent_frm = ttk.Frame(lbl_frm_admin)
        add_admin = ttk.Button(btn_frm, text="Add User", command=self.add_admin)  # noqa E501
        back_btn = ttk.Button(btn_frm, text="Back", command=lambda: controller.show_frame("Editor"))  # noqa E501
        set_mail = ttk.Button(btn_frm, text="Add Email Address")

        self.usr_ent = ttk.Entry(ent_frm, width=20, textvariable=self.v6)
        self.pass_ent = ttk.Entry(ent_frm, width=20, textvariable=self.v7)

        add_admin.grid(row=0, column=0, padx=10)
        back_btn.grid(row=0, column=1, padx=10)
        set_mail.grid(row=0, column=2, padx=10)

        self.usr_ent.grid(row=1, column=0, pady=5, padx=5)
        self.pass_ent.grid(row=1, column=1, pady=5, padx=5)
        btn_frm.grid(row=0, column=0)
        ent_frm.grid(row=1, column=0)
        # ----------/\/\ Frame info (lbl_frm_admin)(e) /\/\-------

        lbl_frm_table.pack(fill="both", expand=True, padx=20, pady=10)
        lbl_frm_data.pack(fill="both", expand=True, padx=20, pady=10)
        lbl_frm_info.pack(fill="both", expand=True, padx=20, pady=10)
        lbl_frm_admin.pack(fill="both", expand=True, padx=20, pady=10)

        self.mainframe.pack(fill="both", expand=True)  # Packing of mainframe

    @validate
    def add_admin(self, *args):
        """This method will be used to add new master users to Open Palm"""

        user_id = pm.cipherpass(self.usr_ent.get())
        user_pass = pm.cipherpass(self.pass_ent.get())

        pm.storepass(user_id, user_pass)

    @validate
    def set_mail(self):
        """This method will be used to set new email ids."""
        pass

    def add_user_info(self):
        datab = db.make_db('StudentInfo')
        x = datab.check_dup(self.v2.get(), self.v3.get(), self.v4.get(), self.v5.get())  # noqa E501
        print(x)

        datab.store_values(self.v2.get(), self.v3.get(), self.v4.get(), self.v5.get())  # noqa E501
        self.refresh()

    def update_user_info(self, data):
        """
        Every time a new entry has been made,
        the `refresh` method will call this method
        to display update the table to show the newly
        inserted data
        *self.trview is an unpacked tuple
        """
        self.trview.delete(*self.trview.get_children())
        for i in data:
            self.trview.insert('', 'end', values=i)

    def delete_user_info(self):
        if tk.messagebox.askyesno("Confirm Delete", "Do you really want to delete this Student ?"):  # noqa E501
            obj = db.get_response("StudentInfo")
            obj.delete_data(self.v2.get(), self.v3.get(), self.v4.get(), self.v5.get())  # noqa E501
            self.refresh()
        else:
            pass

    def update_data(self):
        pass

    @logs
    def idrow(self, _):
        """
        Whenever a user double clicks on any entry,
        it is shown in the editable boxes
        """
        item = self.trview.item(self.trview.focus())
        try:
            self.v2.set(item['values'][0])
            self.v3.set(item['values'][1])
            self.v4.set(item['values'][2])
            self.v5.set(item['values'][3])
        except:  # noqa E501
            pass

    def search_data(self):
        """
        This method is bound to the `search` button.
        Its task is to get the value given in tkinter entry box and
        search for that entry containing that value in the database.
        """
        std_name = self.src_ent.get()
        obj = db.get_response('StudentInfo')
        req_data = obj.get_data_by_query(std_name)
        self.update_user_info(req_data)

    def refresh(self):
        """
        This method is bound to the `refresh` button.
        Its task is to show all the values in the treeview
        after a search has been made.
        """
        self.data = db.get_response('StudentInfo').get_all_data()
        self.update_user_info(self.data)


if __name__ == "__main__":
    window = Openpalm()
    window.title('OpenPalm')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(0, minsize=800, weight=1)
    window.mainloop()
