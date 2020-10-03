# MIT License

# Copyright (c) 2020 Jdeep

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
import passmanager as pm
import subprocess
import Database as db
import analyse as an
import tkinter.messagebox
from importlib import reload

class Openpalm(tk.Tk):

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
            parent=container, controller=self)  # Calls the Teacher_Page_Login Class

        self.frames["Master_Page"] = Master_Page( #Calls the Master_Page 
            parent = container,controller=self)

        self.frames["Editor"].grid(row=0, column=0, sticky="nsew")
        self.frames["Login_Page"].grid(row=0, column=0, sticky="nsew")
        self.frames["Teacher_Page_Login"].grid(row=0, column=0, sticky="nsew")
        self.frames["Master_Page"].grid(row=0,column=0,sticky="nsew")

        self.show_frame("Editor")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Editor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.mainframe = tk.Frame(self , width=1600)

        # The Design Aspect of the frame
        self.Text_box = tk.Text(self.mainframe, bg='#333333', fg='#f2f2f2')
        self.Text_box.configure(font=("Courier", 16, ''),
                                insertbackground='white')
        # The Frame that contains all the buttons
        self.frm_btns = tk.Frame(self.mainframe)

        # The instatiation of buttons
        self.btn_submit = ttk.Button(self.frm_btns, text='SUBMIT')
        self.btn_clear = ttk.Button(self.frm_btns, text='CLEAR')
        self.btn_open = ttk.Button(
            self.frm_btns, text='OPEN', command=self.open_file)
        self.btn_save = ttk.Button(
            self.frm_btns, text='SAVE', command=self.save_file)
        self.btn_test = ttk.Button(
            self.frm_btns, text='Test', command = self.test_it)

        self.option = tk.StringVar()
        self.option.set("Select Code")
        self.dropdown = ttk.Combobox(self.frm_btns ,state = "readonly", textvariable = self.option , width= 15)
        self.dropdown['values'] = ["#1" , "#2" , "#3" , "#4"]

        # The gridding of buttons
        self.btn_submit.grid(row=4, column=0, sticky='ew')
        self.btn_clear.grid(row=1, column=0, sticky='ew')
        self.btn_open.grid(row=2, column=0, sticky='ew')
        self.btn_save.grid(row=3, column=0, sticky='ew')
        self.btn_test.grid(row=0, column=0, sticky='ew')
        self.dropdown.grid(row = 6 , column=0 , sticky = 'es')

        # The gridding of the frame that contains all the buttons
        self.frm_btns.grid(row=0, column=2, sticky='ns')

        # The gridding of the Text Box
        self.Text_box.grid(row=0, column=0, sticky='nsew')
        # THe Design aspect of the frame

        move_to_page_1 = ttk.Button(self.frm_btns, text="Go to Login Page",
                                   command=lambda: controller.show_frame("Login_Page"))

        move_to_page_1.grid(row=5, column=0, sticky='ew')

        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.mainframe.rowconfigure(0, minsize=800, weight=1)
        self.mainframe.columnconfigure(0, weight=1)

    def open_file(self):  # Opens a saved file
        self.path = askopenfilename(filetypes=(
            ("python files", ".py"), ("All Files", "*.py")))
        if not self.path:
            return
        self.Text_box.delete(1.0, tk.END)
        with open(self.path, 'r') as file:
            self.text = file.read()
            self.Text_box.insert(tk.END, self.text)

    def save_file(self):
        self.filepath = asksaveasfilename(
        defaultextension="py",
        filetypes=[("python files", "*.py"), ("All Files", "*.*")],
        )
        if not self.filepath:
            return

        with open(self.filepath, "w") as output_file:
            text = self.Text_box.get("1.0", tk.END)
            output_file.write(text)

    def save_for_test(self):
        with open("test_it.py","w+") as file:
            text = self.Text_box.get("1.0", tk.END)
            file.write(text)

    def test_it(self):
        self.save_for_test()

        import test_it
        test_it = reload(test_it)
        self.questions = an.questions
        self.testcases = an.testcases
        tmp_qns = ["check_even", "bubble_sort", "fibonacci", "check_palin"]

        self.code = self.option.get()[1]

        if self.code.isalpha() :
            tk.messagebox.showerror("Select Question Code" , "Please Select a question Code")

        else:
            ver_soln = an.chk(int(self.code) , self.testcases[int(self.code)] )
            user_soln = []

            #---------user soln----------------

            testdata = self.testcases[int(self.code)]

            for k in testdata:
                try:
                    ans = getattr(test_it,tmp_qns[int(self.code)-1])(k)
                    user_soln.append(ans)

                except Exception as exception:
                    print(exception)
                    print(exception.__class__.__name__)
                    break
            if user_soln == ver_soln :
                tk.messagebox.showinfo("Congatulations" , "Your code has passed all the test cases. You may now submit the solution.")
                print(user_soln)
            else:
                tk.messagebox.showinfo("Try Again" , "Your code has failed in one or multiple test cases.")
                print(user_soln)

class Login_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainframe = tk.Frame(self)
        # The Design Aspect of the frame

        img = ImageTk.PhotoImage(Image.open("../favicon/logo.png"))
        imglbl = tk.Label(self.mainframe , image = img)
        imglbl.image = img
        #imglbl.place(x=0, y=0, relwidth=1, relheight=1)
        imglbl.grid(row = 3 , column = 0)

        login_label = tk.Label(self.mainframe, text="This is Login Page")
        login_label.grid(row=0, column=0)

        # The Design Aspect of the frame
        teacher_btn = ttk.Button(self.mainframe, text='TEACHER', width=15,
                                command=lambda: self.controller.show_frame("Teacher_Page_Login"))
        teacher_btn.grid(row=1, column=0 )

        button = ttk.Button(self.mainframe, text="Go to the Editor",
                           command=lambda: controller.show_frame("Editor"), width=15)
        button.grid(row=2, column=0)
        self.mainframe.pack()

class Teacher_Page_Login(tk.Frame):
    '''
    The theory is simple.
    All the Entry Boxes , 'Username' labels are servants of the frame : 'semi_frm'
    The 'semi_frm' and 'TEACHER PAGE' label are servants of mainframe
    The mainframe is a servant if self.
    '''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # The Frame that contains all the objects of the Teacher Page. It is the servant of self(Window)

        self.mainframe = tk.Frame(self)

        # The Design Aspect of the frame

        img = ImageTk.PhotoImage(Image.open("../favicon/logo.png"))
        imglbl = tk.Label(self.mainframe , image = img)
        imglbl.image = img
        #imglbl.place(x=0, y=0, relwidth=1, relheight=1)
        imglbl.grid(row = 4 , column = 0)

        lbl = tk.Label(self.mainframe, text="TEACHER'S PAGE",font=("Ubuntu", 14, ''))
        lbl.grid(row=0, column=0, sticky='nsew')

        semi_frm = tk.Frame(self.mainframe)

        usr_lbl = tk.Label(semi_frm, text='User Name',font=("Courier", 12, ''))
        usr_lbl.grid(row=1, column=0)

        self.user_box = tk.Entry(semi_frm)
        self.user_box.grid(row=1, column=1)

        passwd_lbl = tk.Label(semi_frm, text='Password',font=("courier", 12, ''))
        passwd_lbl.grid(row=2, column=0)

        self.passwd_box = tk.Entry(semi_frm, show ="*")
        self.passwd_box.grid(row=2, column=1)

        # The Design Aspect of the frame
        self.sign_in = ttk.Button(semi_frm, text="Sign In",command=self.get_user_info)
        self.sign_in.grid(row=4, column=1, sticky='nsew')

        goto_login = ttk.Button(semi_frm, text='Login Page',
                               command=lambda: self.controller.show_frame("Login_Page"))
        goto_login.grid(row=4, column=0, sticky='nsew')

        semi_frm.grid(row=1, column=0)

        self.mainframe.pack()  # Packing of the mainframe

    def get_user_info(self,event=None):
        self.prompt = tk.Label(self.mainframe , text = "" , fg = 'red')
        self.prompt.grid(row=3 , column = 0 , sticky = 'nsew')

        if subprocess.check_output('xset q | grep LED', shell=True)[65] == 51 :
            capslock = True
            self.prompt = tk.Label(self.mainframe , text = "*Caps Lock is ON" , fg = 'black')
            self.prompt.grid(row=3 , column = 0 , sticky = 'nsew')

        master_creds = ["nova_tech" , "nova_tech_jaydeep"]

        usrid = self.user_box.get()
        usrpass = self.passwd_box.get()

        userid = pm.cipherpass(usrid)
        userpass = pm.cipherpass(usrpass)

        self.controller.show_frame("Master_Page") #Waring : Immediately delete this line after the project is over.

        dic = pm.get_pass()

        if [usrid,usrpass] == master_creds:
            print("passed")
            self.passwd_box.delete(0,"end")
            self.user_box.delete(0,'end')
            self.controller.show_frame("Master_Page")


        elif userid in dic:
            if userpass == dic[userid]:
                print("passed")
                self.passwd_box.delete(0,"end"), self.user_box.delete(0,'end')
                self.controller.show_frame("Master_Page")

            else:
                print("failed due to incorrect password")
                self.prompt = tk.Label(self.mainframe , text = "The Username or the password is incorrect" , fg = 'red')
                self.prompt.grid(row=2 , column = 0 , sticky = 'nsew')
        else:
            print("failed")
            self.prompt = tk.Label(self.mainframe , text =  "The Username or the password is incorrect" , fg = 'red')
            self.prompt.grid(row=2 , column = 0 , sticky = 'nsew')

class Master_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainframe = tk.Frame(self)

        lbl_frm_table = ttk.LabelFrame(self.mainframe, text = "Student Data")
        lbl_frm_data = ttk.LabelFrame(self.mainframe , text = "Information")
        lbl_frm_info = ttk.LabelFrame(self.mainframe , text = "Data Entry")

#       ----------------------------------------------------/\/\ micellaneous/\/\-----------------------------------------------
        self.v1 = tk.StringVar()            #textvar of src_ent 
        self.v2 = tk.StringVar()            #self.name_ent            
        self.v3 = tk.StringVar()            #self.class_ent
        self.v4 = tk.StringVar()            #self.sec_ent
        self.v5 = tk.StringVar()            #self.roll_ent
        self.v6 = tk.StringVar()            #
#       ----------------------------------------------------/\/\ micellaneous/\/\-----------------------------------------------

#       ----------------------------------------------------/\/\ Frame table (lbl_frm_table) (s)/\/\-----------------------------------------------
        self.trview = ttk.Treeview(lbl_frm_table , columns = (1,2,3,4),show = "headings" , height = 6)
        self.trview.pack(fill = "both" ,expand=True , ipady = 5)
        self.trview.heading(1,text="Name")
        self.trview.heading(2,text="Class")
        self.trview.heading(3,text="Section")
        self.trview.heading(4,text="Roll no")
        self.trview.bind("<Double-Button-1>" , self.idrow)
#       ----------------------------------------------------/\/\ Frame table (lbl_frm_table)(e) /\/\-----------------------------------------------

#       ----------------------------------------------------/\/\ Frame data (lbl_frm_data)(s) /\/\-----------------------------------------------
        src_lbl = ttk.Label(lbl_frm_data, text="Search by name : ")
        self.src_ent = ttk.Entry(lbl_frm_data , textvariable = self.v1 )
        src_btn = ttk.Button(lbl_frm_data, text="Search", command= self.search_data)
        src_lbl.pack(side = "left" , padx = 20)
        self.src_ent.pack(side="left" )
        src_btn.pack(side="left", padx = 10)
        rfs_btn = ttk.Button(lbl_frm_data , text = "Refresh" , command=self.refresh)
        rfs_btn.pack(side="left", padx=10)
#       ----------------------------------------------------/\/\ Frame data (lbl_frm_data)(e) /\/\-----------------------------------------------

#       ----------------------------------------------------/\/\ Frame info (lbl_frm_info)(s) /\/\-----------------------------------------------
        name_lbl = ttk.Label(lbl_frm_info , text = "Name ")
        class_lbl = ttk.Label(lbl_frm_info , text = "Class ")
        sec_lbl = ttk.Label(lbl_frm_info , text = "Section ")
        roll_lbl = ttk.Label(lbl_frm_info , text = "Roll no ")

        name_lbl.grid(row = 0 , column = 0 , pady = 10)
        class_lbl.grid(row = 1 , column = 0, pady = 10)
        sec_lbl.grid(row = 2 , column = 0, pady = 10)
        roll_lbl.grid(row = 3 , column = 0, pady = 10)

        self.name_ent = ttk.Entry(lbl_frm_info , width = 35 , textvariable = self.v2)
        self.class_ent = ttk.Entry(lbl_frm_info, width = 35, textvariable = self.v3)
        self.sec_ent = ttk.Entry(lbl_frm_info, width = 35, textvariable = self.v4)
        self.roll_ent = ttk.Entry(lbl_frm_info, width = 35, textvariable = self.v5)

        self.name_ent.grid(row = 0 , column = 1 , pady = 10)
        self.class_ent.grid(row = 1 , column = 1, pady = 10)
        self.sec_ent.grid(row = 2 , column = 1, pady = 10)
        self.roll_ent.grid(row = 3 , column = 1, pady = 10)

        frm_btn = tk.Frame(lbl_frm_info)
        frm_btn.grid(row = 4,column = 1)

        add_btn = ttk.Button(frm_btn , text = "Add " , command = self.add_user_info)
        update_btn = ttk.Button(frm_btn, text = "Update ",command = self.update_data)
        del_btn = ttk.Button(frm_btn, text = "Delete ",command = self.delete_user_info)

        add_btn.grid(row = 0 , column = 0 ,padx =10)
        update_btn.grid(row = 0 , column = 1,padx =10)
        del_btn.grid(row = 0 , column = 2,padx =10)

        std_data = db.get_response("StudentInfo")
        self.data =std_data.get_all_data()
        self.update_user_info(self.data)

        # ----------------------------------------------------/\/\ Frame info (lbl_frm_info)(e) /\/\-----------------------------------------------

        lbl_frm_table.pack(fill = "both" , expand = True , padx=20 , pady = 10)
        lbl_frm_data.pack(fill = "both" , expand = True , padx=20 , pady = 10)
        lbl_frm_info.pack(fill = "both" , expand = True , padx=20 , pady = 10)

        self.mainframe.pack(fill = "both" , expand = True)  # Packing of the mainframe

    def add_user_info(self):
        datab = db.make_db('StudentInfo')
        x = datab.check_dup(self.v2.get(),self.v3.get(),self.v4.get(),self.v5.get())
        print(x)

        datab.store_values(self.v2.get(),self.v3.get(),self.v4.get(),self.v5.get())
        self.refresh()

    def update_user_info(self , data):
        self.trview.delete(*self.trview.get_children())
        for i in data:
            self.trview.insert('','end',values=i)

    def delete_user_info(self):
        if tk.messagebox.askyesno("Confirm Delete" , "Do you really want to delete this Student ?"):
            obj = db.get_response("StudentInfo")
            obj.delete_data( self.v2.get(), self.v3.get(), self.v4.get() , self.v5.get() )
            self.refresh()
        else:
            pass

    def update_data(self):
        pass

    def idrow(self,event):
        rownum = self.trview.identify('item',event.x,event.y)
        item = self.trview.item(self.trview.focus())
        try:
            self.v2.set(item['values'][0])
            self.v3.set(item['values'][1])
            self.v4.set(item['values'][2])
            self.v5.set(item['values'][3])
        except:
            pass

    def search_data(self):
        std_name = self.src_ent.get()
        obj = db.get_response('StudentInfo')
        req_data = obj.get_data_by_query(std_name)
        self.update_user_info(req_data)

    def refresh(self):
        self.data =db.get_response('StudentInfo').get_all_data()
        self.update_user_info(self.data)

if __name__ == "__main__":
    window = Openpalm()
    window.iconphoto(True, tk.PhotoImage(       #Comment this if you using Windows
        r'..\favicon\favicon.png'))
    #window.iconbitmap(tk.PhotoImage(           #Uncomment this if you are using Windows
    #    r'..\favicon\favicon.png'))

    window.title('OpenPalm')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(0, minsize=800, weight=1)
    window.mainloop()
