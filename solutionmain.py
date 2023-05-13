from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Text
import tkinter as tk
import sqlite3
from datetime import datetime
import threading
import time
from time import strftime
import smtplib
from email.message import EmailMessage
from itertools import product

##################################### FOUNDATION / MAIN WINDOW #########################################

def MainProgramStart():
    global root
    root = Tk()
    root.title("Login Form")
    root.geometry("800x480")


def DestroyPage():
    currentframe.destroy()

def HomeButtonCondition():
    #documentation for state module
    teambutton.config(state = tk.NORMAL)
    eventsbutton.config(state = tk.NORMAL)
    noticebutton.config(state = tk.NORMAL)
    teambutton.config(bg = 'white')
    eventsbutton.config(bg = 'white')
    noticebutton.config(bg = 'white')

def TeamButtonCondition():
    homebutton.config(state = tk.NORMAL)
    eventsbutton.config(state = tk.NORMAL)
    noticebutton.config(state = tk.NORMAL)
    homebutton.config(bg = 'white')
    eventsbutton.config(bg = 'white')
    noticebutton.config(bg = 'white')

def EventsButtonCondition():
    homebutton.config(state = tk.NORMAL)
    teambutton.config(state = tk.NORMAL)
    noticebutton.config(state = tk.NORMAL)
    homebutton.config(bg = 'white')
    teambutton.config(bg = 'white')
    noticebutton.config(bg = 'white')

def NoticeButtonCondition():
    homebutton.config(state = tk.NORMAL)
    teambutton.config(state = tk.NORMAL)
    eventsbutton.config(state = tk.NORMAL)
    homebutton.config(bg = 'white')
    teambutton.config(bg = 'white')
    eventsbutton.config(bg = 'white')

def InformationAboutProgram():
    master = Tk()
    master.withdraw()
    messagebox.showinfo("Program Specific Information", "The program was designed for the CS SL course, the 'Solution' Internal Assessment.\nThis was created by a Haileybury Astana student and not subject to redistribution.")

def DummyHomePage(): 
    global homeframe, currentframe, homeheader4, homeheader5
    
    homebutton.config(bg = '#4e5a64')
    homeframe = Frame(root2)
    currentframe = homeframe
    homeframe.pack(side = TOP)
    
    homeheader1 = Label(homeframe, text = "Homepage", font = ('arial', 20), width = 53, bd = 4, relief = "ridge")
    homeheader1.pack(side = TOP, pady = (0,35))
    homeheader2 = Label(homeframe,text = "Welcome,", font = ('arial', 28))
    homeheader2.pack(side = TOP)
    homeheader3 = Label(homeframe, text = displayname, font = ('arial', 28))
    homeheader3.pack(side = TOP)
    homeheader4 = Label(homeframe, font = ('arial', 28))
    homeheader4.pack(side = TOP, pady = (40, 0))
    homeheader5 = Label(homeframe, font = ('arial', 28))
    homeheader5.pack(side = TOP, pady = (0, 65))
    testbutton = Button(homeframe, text = "Program Information", font = ('arial', 10), bd = 1, command = InformationAboutProgram)
    testbutton.pack(side = TOP)

    Clock()
    Date()
    
def HomePage(): 
    HomeButtonCondition()
    DestroyPage()
    homebutton.config(state = tk.DISABLED)
    homebutton.config(bg = '#4e5a64')
    
    global homeframe, currentframe, homeheader4, homeheader5
    
    homeframe = Frame(root2)
    currentframe = homeframe
    homeframe.pack(side = TOP)

    homeheader1 = Label(homeframe, text = "Homepage", font = ('arial', 20), width = 52, bd = 4, relief = "ridge")
    homeheader1.pack(side = TOP, pady = (0,35))
    homeheader2 = Label(homeframe,text = "Welcome,", font = ('arial', 28))
    homeheader2.pack(side = TOP)
    homeheader3 = Label(homeframe, text = displayname, font = ('arial', 28))
    homeheader3.pack(side = TOP)
    homeheader4 = Label(homeframe, font = ('arial', 28))
    homeheader4.pack(side = TOP, pady = (40, 0))
    homeheader5 = Label(homeframe, font = ('arial', 28))
    homeheader5.pack(side = TOP, pady = (0, 65))
    testbutton = Button(homeframe, text = "Program Information", font = ('arial', 10), bd = 1, command = InformationAboutProgram)
    testbutton.pack(side = TOP)
        
    Clock()
    Date()
    
def TeamFrame():
    TeamButtonCondition()
    DestroyPage()
    teambutton.config(state = tk.DISABLED)
    teambutton.config(bg = '#4e5a64')

    global currentframe

    TeamDatabase()
    root2.title("Team Management")
    TeamManagementFrame()
    
    teamheader = Label(teammanagementframe, text = "Team Management", font = ('arial', 20), width = 52, bd = 4, relief = "ridge")
    teamheader.pack(side = TOP)
    
    currentframe = teammanagementframe

    TeamEntryFrame()
    TeamButtonFrame()
    TeamTreeview()
    CheckDatabase()
    
def EventsFrame():
    EventsButtonCondition()
    DestroyPage()
    eventsbutton.config(state = tk.DISABLED)
    eventsbutton.config(bg = '#4e5a64')
    
    global eventsframe, currentframe
    
    eventsframe = Frame(root2)
    currentframe = eventsframe
    eventsframe.pack(side = TOP)
    
    eventsheader = Label(eventsframe, text = "Events Management", font = ('arial', 20), width = 52, bd = 4, relief = "ridge")
    eventsheader.pack(side = TOP)

def NoticeFrame(): 
    NoticeButtonCondition()
    DestroyPage()
    noticebutton.config(state = tk.DISABLED)
    noticebutton.config(bg = '#4e5a64')
    
    global noticeframe, currentframe, subjectentry, bodyentry, emailpasswordentry
    
    noticeframe = Frame(root2)
    currentframe = noticeframe
    noticeframe.pack(side = TOP)
    
    noticeheader = Label(noticeframe, text = "Notice Forwarding", font = ('arial', 20), width = 52, bd = 4, relief = "ridge")
    noticeheader.pack(side = TOP)
    subjectlabel = Label(noticeframe, text = "Subject of Notice:", font = ('arial', 18))
    subjectlabel.pack(side = TOP, pady = (25, 8))
    subjectentry = Entry(noticeframe, width = 20, font = ('arial', 16), bd = 3)
    subjectentry.pack(side = TOP, pady = (0,10))
    bodylabel = Label(noticeframe, text = "Main Text Body:", font = ('arial', 18))
    bodylabel.pack(side = TOP, pady = 10)
    bodyentry = Text(noticeframe, width = 30, height = 5, font = ('arial', 15), bd = 3)
    bodyentry.pack(side = TOP, pady = (0, 20))
    emailpasswordlabel = Label(noticeframe, text = "Email Password:", font = ('arial', 18))
    emailpasswordlabel.pack(side = TOP)
    emailpasswordentry = Entry(noticeframe, width = 20, font = ('arial', 15), show = "*", bd = 3)
    emailpasswordentry.pack(side = TOP, pady = (5,10))
    emailentryreset = Button(noticeframe, width = 10, font = ('arial', 13), text = "Reset Fields", bd = 3, command = ClearEmailEntry)
    emailentryreset.pack(side = TOP, pady = (15, 0))
    emailbutton = Button(noticeframe, width = 10, font = ('arial', 13), text = "Send Notice", bd = 3, command = SendMail)
    emailbutton.pack(side = TOP, pady = (5, 20))
    
    
    
    
def MenuButtons():
    global root2, homebutton, teambutton, eventsbutton, noticebutton, recipientsfull

    root2 = Tk()
    root2.title("Main Dashboard")
    
    menuframe = Frame(root2)
    menuframe.pack(side = TOP)
    
    programheader = Label(menuframe, text = "HBA COASH Management Tool (HCMT)", font = ('Helvetica', 24), width = 44, bd = 4, relief = "solid", bg = "#8b8faa")
    programheader.pack(side = TOP)
    
    homebutton = Button(menuframe, text = "Home", font = ('arial', 12), width = 22, command = HomePage)
    homebutton.pack(side = LEFT)
    teambutton = Button(menuframe, text = "Team", font = ('arial', 12), width = 23, command = TeamFrame)
    teambutton.pack(side = LEFT)
    eventsbutton = Button(menuframe, text = "Events", font = ('arial', 12), width = 23, command = EventsFrame)
    eventsbutton.pack(side = LEFT)
    noticebutton = Button(menuframe, text = "Notices", font = ('arial', 12), width = 22, command = NoticeFrame)
    noticebutton.pack(side = LEFT)
    
    DummyHomePage()

##################### REAL TIME CLOCK FOR HOMEFRAME ###########################
    
def Clock():
    global homeheader4
    time = strftime('%H:%M:%S %p')
    homeheader4.config(text = time)
    homeheader4.after(1000, Clock)
    
def Date():
    global homeheader5
    date = strftime('%d/%m/%Y %A')
    homeheader5.config(text = date)
    homeheader5.after(1000, Date)


######################## NOTICE FORWARDER ###########################################

def GetEmails():
    global emails
    conn = sqlite3.connect('clientsquad.db')
    cur = conn.cursor()

    cur.execute("select email from squad")
    emails = cur.fetchall()
	
    conn.commit()
    conn.close()

def SendMail():
    GetEmails()
    recipients = [i for sub in emails for i in sub]
    recipientsfull = ", ".join(recipients)
    
    sender = clientemail[0]
    password = emailpasswordentry.get()
    subject = subjectentry.get()
    message = bodyentry.get("1.0",END)
    print(recipientsfull)

    notice = EmailMessage()
    notice.set_content(message)
    notice['Subject'] = subject
    notice['From'] = sender
    notice['To'] = recipientsfull
    
    try:
        email = smtplib.SMTP('smtp.office365.com', 587)
        email.ehlo()
        email.starttls()
        email.ehlo()
    
        email.login(sender, password)
        email.send_message(notice)
        email.quit()
        print("Email sent.")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Incorrect email credentials.")

def ClearEmailEntry():
    subjectentry.delete(0, END)
    bodyentry.delete("1.0", END)
    emailpasswordentry.delete(0, END)

        
######################## LOGIN / REGISTER FORM ########################################
    
def ClientDatabase():
    #documentation
    conn = sqlite3.connect('client.db')
    cur = conn.cursor()

    cur.execute("""create table if not exists client(username text, password text, firstname text, email text);""")
	
    conn.commit()
    conn.close()
    
def RegisterClient():
    if usernameentry.get() == "" or passwordentry.get() == "" or firstnameentry.get() == "" or emailentry.get() == "":
        messagebox.showerror("Error", "Do not leave blank fields.")
    else:
        conn = sqlite3.connect('client.db')
        cur = conn.cursor()
        #tkinter documentation
        vusername = usernameentry.get()
        vpassword = passwordentry.get()
        vfirstname = firstnameentry.get()
        vemail = emailentry.get()
        #documentation sqlite
        enteredvalues = [[vusername, vpassword, vfirstname, vemail]]
        cur.executemany('insert into client values (?,?,?,?)', enteredvalues)
    
        conn.commit()
        conn.close()

        #documentation tkinter
        usernameentry.delete(0, END)
        passwordentry.delete(0, END)
        firstnameentry.delete(0, END)
        emailentry.delete(0, END)

        messagebox.showinfo("Success", "You have succesfully registered.")


def LoginClient():
    global homepagename, displayname, clientemail
    
    homepagename = ""
    
    if usernameentry.get() == "" or passwordentry.get() == "":
        messagebox.showerror("Error", "Do not leave fields blank.")
        
    else:
        conn = sqlite3.connect('client.db')
        vusername = usernameentry.get()
        vpassword = passwordentry.get()
        cur = conn.cursor()
        cur.execute('select * from client where username = ? AND password = ?', (vusername, vpassword))
        
        if cur.fetchone() is None: #sqlite documentation
            messagebox.showerror("Error", "Incorrect login credentials.")
            usernameentry.delete(0, END)
            passwordentry.delete(0, END)
            
        else:
            messagebox.showinfo("Success", "You have succesfully logged in.")
            cur.execute('select firstname from client where username = ? AND password = ?', (vusername, vpassword))
            displayname = cur.fetchone()
            cur.execute('select email from client where username = ? AND password = ?', (vusername, vpassword))
            clientemail = cur.fetchone()
            usernameentry.delete(0, END)
            passwordentry.delete(0, END)
            MenuButtons()
            root.destroy()
        conn.commit()
        conn.close()
    

    
def LoginFrame():
    global flogin, usernameentry, passwordentry, lusername, lpassword
    
    root.title("Login Form")
    root.geometry("800x460")
    flogin = Frame(root)
    flogin.pack(side = TOP)

    lheaderlogin1 = Label(flogin, text = "HBA COASH Management Tool", font = ('arial', 28), bd = 28)
    lheaderlogin1.pack(side = TOP, pady = (10,0))
    lusername1 = Label(flogin, text = "Username:", font = ('arial', 22), bd=8)
    lusername1.pack(side = TOP)
    usernameentry = Entry(flogin, font = ('arial', 20), width = 16, bd = 3)
    usernameentry.pack(side = TOP)

    lpassword1 = Label(flogin, text = "Password:", font = ('arial', 22), bd=8)
    lpassword1.pack(side = TOP)
    passwordentry = Entry(flogin, font = ('arial', 20), show = "*", width = 16, bd = 3)
    passwordentry.pack(side = TOP)
    
    blogin = Button(flogin, text = "Login", font = ('arial', 18), width = 20, command = LoginClient)
    blogin.pack(side = TOP, pady = 20)
    
    bgotoregister = Button(flogin, text = "Register here", fg = "blue", font = ('arial', 12), command = GoToRegister)
    bgotoregister.pack(side = TOP)


def RegisterFrame():
    global fregister, usernameentry, passwordentry, emailentry, firstnameentry
    
    root.title("Register Form")
    root.geometry("800x640")
    fregister = Frame(root)
    fregister.pack(side = TOP)
    
    lheaderregister2 = Label(fregister, text = "HBA COASH Management Tool", font = ('sans 16 bold', 28), bd = 28)
    lheaderregister2.pack(side = TOP, pady = (10,0))
    
    lusername2 = Label(fregister, text = "Username:", font = ('arial', 22), bd = 8)
    lusername2.pack(side = TOP)
    usernameentry = Entry(fregister, font = ('arial', 20), width = 16, bd = 3)
    usernameentry.pack(side = TOP)
    
    lpassword2 = Label(fregister, text = "Password:", font = ('arial', 22), bd = 8)
    lpassword2.pack(side = TOP)
    passwordentry = Entry(fregister, font = ('arial', 20), show = "*", width = 16, bd = 3)
    passwordentry.pack(side = TOP)
    
    lfirstname = Label(fregister, text = "First Name:", font = ('arial', 22), bd = 8)
    lfirstname.pack(side = TOP)
    firstnameentry = Entry(fregister, font = ('arial', 20), width = 16, bd = 3)
    firstnameentry.pack(side = TOP)
    
    lemail = Label(fregister, text = "School Email:", font = ('arial', 22), bd = 8)
    lemail.pack(side = TOP)
    emailentry = Entry(fregister, font = ('arial', 20), width = 16, bd = 3)
    emailentry.pack(side = TOP)
    
    bregister = Button(fregister, text = "Register", font = ('arial', 18), width = 20, command = RegisterClient)
    bregister.pack(side = TOP, pady = 20)
    
    bgotologin = Button(fregister, text = "Go back to login screen", fg = "blue", font = ('arial', 12), command = GoToLogin)
    bgotologin.pack(side = TOP)


def GoToLogin():
    fregister.destroy()
    LoginFrame()
    usernameentry.delete(0, END)
    passwordentry.delete(0, END)

def GoToRegister():#add the limit of users
    conn = sqlite3.connect('client.db')
    cur = conn.cursor()

    cur.execute("""create table if not exists client(username text, password text, firstname text, email text);""")
    cur.execute("select * from client")

    if cur.fetchone() is None:
        flogin.destroy()
        RegisterFrame()
        usernameentry.delete(0, END)
        passwordentry.delete(0, END)
        firstnameentry.delete(0, END)
        emailentry.delete(0, END)
    else:
        messagebox.showerror("Error", "User limit capacity reached.")

    conn.commit()
    conn.close()
    
################################# DATABASE MNGT PART ######################################################

def TeamDatabase():
        conn = sqlite3.connect('clientsquad.db')
        cur = conn.cursor()

        cur.execute("""create table if not exists squad(firstname text, lastname text, birthyear integer, gender text, email text)""")
	
        conn.commit()
        conn.close()

def teamclearentrydef():
        teamidentry.delete(0, END)
        teamfnentry.delete(0, END)
        teamlnentry.delete(0, END)
        teambirthyearentry.delete(0, END)
        teamgenderentry.delete(0, END)
        teamemailentry.delete(0, END)
        teamemailentry.insert(0, "@haileyburyastana.kz")

def CheckDatabase():
    teamclearentrydef()
    teamtree.delete(*teamtree.get_children())
    conn = sqlite3.connect('clientsquad.db')
    cur = conn.cursor()
    
    cur.execute("""create table if not exists squad(firstname text, lastname text, birthyear integer, gender text, email text)""")
    cur.execute("select rowid, * from squad")
    
    records = cur.fetchall()
    for record in records:
        
            #teamtree.insert('', 'end', values = (record[0], record[1], record[2], record[3], record[4], record[5]))
            teamtree.insert('', 'end', values = (record))
            
    conn.commit()
    conn.close()

def teamaddrecord():
    conn = sqlite3.connect('clientsquad.db')
    cur = conn.cursor()
    vteamfnentry = teamfnentry.get()
    vteamlnentry = teamlnentry.get()
    vteambirthyearentry = teambirthyearentry.get()
    vteamgenderentry = teamgenderentry.get()
    vteamemailentry = teamemailentry.get()

    enteredvalues = [[vteamfnentry, vteamlnentry, vteambirthyearentry, vteamgenderentry, vteamemailentry]]
    cur.executemany('insert into squad values (?,?,?,?,?)', enteredvalues)
                 
    conn.commit()
    conn.close()

    teamclearentrydef()

    CheckDatabase()

def checkforstudent():
    teamclearentrydef()
    teamtree.delete(*teamtree.get_children())
    
    conn = sqlite3.connect('clientsquad.db')
    cur = conn.cursor()

    vlastnameentry = lastnamequeryentry.get()
    
    cur.execute("select rowid, * from squad where lastname = ?", (vlastnameentry,))
    
    records = cur.fetchall()
    for record in records:
        
            #teamtree.insert('', 'end', values = (record[0], record[1], record[2], record[3], record[4], record[5]))
            teamtree.insert('', 'end', values = (record))
            
    conn.commit()
    conn.close()

def teamselectedrecord(e):
    teamclearentrydef()
    if teamtree.focus():
        
            selected = teamtree.focus()
            values = teamtree.item(selected, 'values')

            teamidentry.insert(0, values[0])
            teamfnentry.insert(0, values[1])
            teamlnentry.insert(0, values[2])
            teambirthyearentry.insert(0, values[3])
            teamgenderentry.insert(0, values[4])
            teamemailentry.delete(0, END)
            teamemailentry.insert(0, values[5])
    else:
            print('selection process')

def teamupdaterecord():
    conn = sqlite3.connect('clientsquad.db')
    cur = conn.cursor()
    
    vteamfnentry = teamfnentry.get()
    vteamlnentry = teamlnentry.get()
    vteambirthyearentry = teambirthyearentry.get()
    vteamgenderentry = teamgenderentry.get()
    vteamemailentry = teamemailentry.get()
    
    selected = teamtree.focus()
    contents = (teamtree.item(selected))
    selecteditem = contents['values']
    
    cur.execute('update squad set firstname = ?, lastname = ?,birthyear = ?,gender = ?,email = ? where rowid = ?',
                (vteamfnentry, vteamlnentry, vteambirthyearentry, vteamgenderentry, vteamemailentry, selecteditem[0]))
    
    conn.commit()
    conn.close()
    
    teamclearentrydef()
    CheckDatabase()

def teamdeleteallrecords():
    conn = sqlite3.connect('clientsquad.db')
    cur = conn.cursor()
    cur.execute('drop table squad')
    conn.commit()
    conn.close()

    CheckDatabase()
    
def teamdeleterecord():
    selectedid = teamidentry.get()
    
    conn = sqlite3.connect('clientsquad.db')
    cur = conn.cursor()
    
    cur.execute('delete from squad where rowid = ?', (selectedid,))

    conn.commit()
    conn.close()
    
    #recordtodelete = teamtree.selection()[0]
    #teamtree.delete(recordtodelete)
    teamclearentrydef()
    CheckDatabase()
    
def TeamEntryFrame():
        global teamidentry, teamfnentry, teamlnentry, teambirthyearentry, teamgenderentry, teamemailentry
        teamentryframe = LabelFrame(teammanagementframe)
        teamentryframe.pack(side = LEFT)

        teamidlabel = Label(teamentryframe, text = "Student ID")
        teamidlabel.grid(row = 0, column = 0, pady = 5, padx = 5)
        teamidentry = Entry(teamentryframe)
        teamidentry.grid(row = 1, column = 0, padx = 5)

        teamfnlabel = Label(teamentryframe, text = "First Name")
        teamfnlabel.grid(row = 2, column = 0, pady = 5, padx = 5)
        teamfnentry = Entry(teamentryframe)
        teamfnentry.grid(row = 3, column = 0, padx = 5)

        teamlnlabel = Label(teamentryframe, text = "Last Name")
        teamlnlabel.grid(row = 4, column = 0, pady = 5, padx = 5)
        teamlnentry = Entry(teamentryframe)
        teamlnentry.grid(row = 5, column = 0, padx = 5)

        teambirthyearlabel = Label(teamentryframe, text = "Year of Birth")
        teambirthyearlabel.grid(row = 6, column = 0, pady = 5, padx = 5)
        teambirthyearentry = Entry(teamentryframe)
        teambirthyearentry.grid(row = 7, column = 0, padx = 5)

        teamgenderlabel = Label(teamentryframe, text = "Gender")
        teamgenderlabel.grid(row = 8, column = 0, pady = 5, padx = 5)
        teamgenderentry = Entry(teamentryframe)
        teamgenderentry.grid(row = 9, column = 0, padx = 5)

        teamemaillabel = Label(teamentryframe, text = "E-mail")
        teamemaillabel.grid(row = 10, column = 0, pady = 5, padx = 5)
        teamemailentry = Entry(teamentryframe)
        teamemailentry.grid(row = 11, column = 0, pady = 5, padx = 5)
        
        teamadd = Button(teamentryframe, text = "Add record", command = teamaddrecord)
        teamadd.grid(row=12, column=0, pady=8, padx = 5)



def TeamButtonFrame():
        global lastnamequeryentry
        
        teambuttonframe = LabelFrame(teammanagementframe)
        teambuttonframe.pack(side = LEFT)

        lastnamequerylabel = Label(teambuttonframe, text="Enter lastname")
        lastnamequerylabel.grid(row = 0, column = 0, pady = 2, padx = 5)
        lastnamequeryentry = Entry(teambuttonframe)
        lastnamequeryentry.grid(row = 1, column = 0, pady = 2, padx = 5)

        teamsearch = Button(teambuttonframe, text = "Search for record", command = checkforstudent)
        teamsearch.grid(row = 2, column = 0, pady = 2, padx = 5)
        teamsearchreset = Button(teambuttonframe, text = "Reset search", command = CheckDatabase)
        teamsearchreset.grid(row = 3, column = 0, pady = (1, 14), padx = 5)
        teamupdate = Button(teambuttonframe, text = "Update Record", command = teamupdaterecord)
        teamupdate.grid(row = 4, column = 0, pady = 16, padx = 5)
        teamdelete = Button(teambuttonframe, text = "Delete Record", command = teamdeleterecord)
        teamdelete.grid(row = 5, column = 0, pady = 16, padx = 5)
        teamreset = Button(teambuttonframe, text = "Delete All Records", command = teamdeleteallrecords)
        teamreset.grid(row = 6, column = 0, pady = 16, padx = 5)
        teamclearentry = Button(teambuttonframe, text = "Clear Entry Data", command = teamclearentrydef)
        teamclearentry.grid(row = 7, column = 0, pady = 16, padx = 5)

def TeamManagementFrame():
        global teammanagementframe
        teammanagementframe = Frame(root2)
        teammanagementframe.pack()

def TeamTreeview():
        global teamtree

        teamtreeviewframe = Frame(teammanagementframe)
        teamtreeviewframe.pack(side = LEFT)
        teamstyle = ttk.Style(teamtreeviewframe)
        teamstyle.theme_use('default')
        teamstyle.configure("Treeview", rowheight = 33)

        teamscroll = Scrollbar(teamtreeviewframe)
        teamscroll.pack(side = RIGHT, fill = Y)
        teamtree = ttk.Treeview(teamtreeviewframe, style = "Treeview", yscrollcommand = teamscroll.set, selectmode = "extended")
        teamscroll.config(command = teamtree.yview)
        teamtree.pack(side = LEFT)

        teamtree['columns'] = ("studentID", "firstname", "lastname", "birthyear", "gender", "email")
        teamtree.column("#0", width = 0, stretch = NO)
        teamtree.column("studentID", width = 60, anchor = CENTER) 
        teamtree.column("firstname", width = 100, anchor = CENTER)
        teamtree.column("lastname", width = 100, anchor = CENTER)
        teamtree.column("birthyear", width = 70, anchor = CENTER)
        teamtree.column("gender", width = 70, anchor = CENTER)
        teamtree.column("email", width = 150, anchor = CENTER)

        teamtree.heading("#0", text = "", anchor = W)
        teamtree.heading("studentID", text = "studentID", anchor = CENTER)
        teamtree.heading("firstname", text = "firstname", anchor = CENTER)
        teamtree.heading("lastname", text="lastname", anchor = CENTER)
        teamtree.heading("birthyear", text = "birthyear", anchor = CENTER)
        teamtree.heading("gender", text = "gender", anchor = CENTER)
        teamtree.heading("email", text = "email address", anchor = CENTER)

        teamtree.bind("<ButtonRelease-1>", teamselectedrecord)


MainProgramStart()

ClientDatabase()

LoginFrame()


    
