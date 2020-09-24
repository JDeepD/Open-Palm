import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
import passmanager as pm

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
        self.mainframe = tk.Frame(self, width=1600)

        # The Design Aspect of the frame
        self.Text_box = tk.Text(self.mainframe, bg='#333333', fg='#f2f2f2')
        self.Text_box.configure(font=("Courier", 16, ''),
                                insertbackground='white')
        # The Frame that contains all the buttons
        self.frm_btns = tk.Frame(self.mainframe)

        # The instatiation of buttons
        self.btn_submit = tk.Button(self.frm_btns, text='SUBMIT')
        self.btn_clear = tk.Button(self.frm_btns, text='CLEAR)
        self.btn_open = tk.Button(
            self.frm_btns, text='OPEN', command=self.open_file)

        # The gridding of buttons
        self.btn_submit.grid(row=0, column=0, sticky='ew')
        self.btn_clear.grid(row=1, column=0, sticky='ew')
        self.btn_open.grid(row=2, column=0, sticky='ew')

        # The gridding of the frame that contains all the buttons
        self.frm_btns.grid(row=0, column=2, sticky='ns')

        # The gridding of the Text Box
        self.Text_box.grid(row=0, column=0, sticky='nsew')
        # THe Design aspect of the frame

        move_to_page_1 = tk.Button(self.frm_btns, text="Go to Login Page",
                                   command=lambda: controller.show_frame("Login_Page"))

        move_to_page_1.grid(row=3, column=0, sticky='ew')

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


class Login_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainframe = tk.Frame(self)
        # The Design Aspect of the frame


        img = ImageTk.PhotoImage(Image.open("./favicon/logo.png"))
        imglbl = tk.Label(self.mainframe , image = img)
        imglbl.image = img
        #imglbl.place(x=0, y=0, relwidth=1, relheight=1)
        imglbl.grid(row = 3 , column = 0)


        login_label = tk.Label(self.mainframe, text="This is Login Page")
        login_label.grid(row=0, column=0)

        # The Design Aspect of the frame
        teacher_btn = tk.Button(self.mainframe, text='TEACHER', height=1, width=15,
                                command=lambda: self.controller.show_frame("Teacher_Page_Login"))
        teacher_btn.grid(row=1, column=0 )

        button = tk.Button(self.mainframe, text="Go to the Editor",
                           command=lambda: controller.show_frame("Editor"), height=1, width=15)
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

        img = ImageTk.PhotoImage(Image.open("./favicon/logo.png"))
        imglbl = tk.Label(self.mainframe , image = img)
        imglbl.image = img
        #imglbl.place(x=0, y=0, relwidth=1, relheight=1)
        imglbl.grid(row = 3 , column = 0)

        lbl = tk.Label(self.mainframe, text="TEACHER'S PAGE",font=("Ubuntu", 14, ''))
        lbl.grid(row=0, column=0, sticky='nsew')

        semi_frm = tk.Frame(self.mainframe)

        usr_lbl = tk.Label(semi_frm, text='User Name',font=("Courier", 12, ''))
        usr_lbl.grid(row=1, column=0)

        self.user_box = tk.Entry(semi_frm)
        self.user_box.grid(row=1, column=1)

        passwd_lbl = tk.Label(semi_frm, text='Password',font=("courier", 12, ''))
        passwd_lbl.grid(row=2, column=0)

        self.passwd_box = tk.Entry(semi_frm , show ="*")
        self.passwd_box.grid(row=2, column=1)

        # The Design Aspect of the frame
        self.sign_in = tk.Button(semi_frm, text="Sign In",command=self.get_user_info)
        self.sign_in.grid(row=4, column=1, sticky='nsew')

        goto_login = tk.Button(semi_frm, text='Login Page',
                               command=lambda: self.controller.show_frame("Login_Page"))
        goto_login.grid(row=4, column=0, sticky='nsew')

        semi_frm.grid(row=1, column=0)

        self.mainframe.pack()  # Packing of the mainframe

    def store_user_info(self):
        pass
    def get_user_info(self):
        userid = pm.cipherpass(self.user_box.get())
        userpass = pm.cipherpass(self.passwd_box.get())

        dic = pm.get_pass()

        if userid in dic:
            if userpass == dic[userid]:
                print("passed")
                self.passwd_box.delete(0,"end")
                self.user_box.delete(0,'end')
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

        toolfrm = tk.Frame(self.mainframe)
        toolfrm.grid(row = 0 , column = 0)

        infofrm = tk.Frame(self.mainframe)
        infofrm.grid(row = 0 , column = 1)

        datafrm = tk.Frame(self.mainframe)
        datafrm.grid(row = 1)

        #--------------------------------------------------/\/\ Toolfrm start/\/\-------------------------------------------------------------
        semi_frm_tool = tk.Frame(toolfrm)

        send_data_btn = tk.Button(semi_frm_tool , text = "Send Data",height = 1 , width = 15)
        send_data_btn.grid(row = 0 , column=0)

        set_question_btn = tk.Button(semi_frm_tool, text="Questions",height = 1 , width = 15)
        set_question_btn.grid(row =1 , column = 0)

        back_btn = tk.Button(semi_frm_tool , text = "Back" , command = lambda: self.controller.show_frame("Login_Page"),height = 1 , width = 15)
        back_btn.grid(row = 2 , column = 0 )

        semi_frm_tool.grid(row = 0 , column=0)
        #--------------------------------------------------/\/\ Toolfrm end  /\/\-------------------------------------------------------------

        #--------------------------------------------------/\/\ Info start   /\/\-------------------------------------------------------------
        semi_frm_info = tk.Frame(infofrm)

        std_name = tk.Label(semi_frm_info , text="NAME")
        std_name.grid(row = 0 ,column = 0)

        semi_frm_info.grid(row=0,column=0)
        #--------------------------------------------------/\/\ Info end     /\/\-------------------------------------------------------------
        self.mainframe.pack()  # Packing of the mainframe


if __name__ == "__main__":
    window = Openpalm()
    window.iconphoto(True, tk.PhotoImage(
        r'.\favicon\favicon.png'))
    window.title('OpenPalm')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(0, minsize=800, weight=1)
    window.mainloop()
