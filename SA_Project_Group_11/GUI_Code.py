############################################
#   Author : Ashok Jangir (19CE10012)      #
############################################

import numpy as np 
import tkinter
import math
import os

# to create the root 

root = tkinter.Tk()


# Define the geometry of the screen to be displayed

root.geometry('1280x700')


# to stop re-shapeness


root.maxsize(1280,700)
root.minsize(1280,700)

#find current location of a folder

current_location = os.getcwd()

#title and icon of game

root.title('Frame Structure')
try:
    path = current_location + r'\ico1.ico'
    root.wm_iconbitmap(path)
except:
    pass


#background-image for first page

try:
    path = current_location + r'\p1.png'
    filename = tkinter.PhotoImage(file = path)
    background_label = tkinter.Label(image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass


#to destroy the screen widgets

def remove_children():
    for remove_root_child1 in root.winfo_children():
        remove_root_child1.destroy()


# function for first start button click

def start_structure():
    remove_children()
    second_page()


#to make access to the other functions
A_val = tkinter.StringVar()
B_val = tkinter.StringVar()
C_val = tkinter.StringVar()
D_val = tkinter.StringVar()
E_val = tkinter.StringVar()
F_val = tkinter.StringVar()
G_val = tkinter.StringVar()
H_val = tkinter.StringVar()
I_val = tkinter.StringVar()
J_val = tkinter.StringVar()
mat_E_val = tkinter.StringVar()
mat_I_val = tkinter.StringVar()
mat_A_val = tkinter.StringVar()

#after on click the start button or second page

def second_page():
    #for background
    try:
        path = current_location + r'\p2.png'
        filename1 = tkinter.PhotoImage(file = path)
        background_label1 = tkinter.Label(image=filename1)
        background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        pass
    #main code
    tkinter.Label(text='Enter following values :',font='comicsansms 25 bold',fg='#202b2a',bg='#e5f5d5',padx=50,pady=10,borderwidth=0).pack(pady=20)
    try:
        path = current_location + r'\struct1.png'
        filename2 = tkinter.PhotoImage(file = path)
        background_label2 = tkinter.Label(image=filename2,bg='#202b2a',padx=100,pady=0,borderwidth=0)
        background_label2.place(x=20, y=150, relwidth=0.55, relheight=0.525)  #0.525
    except:
        tkinter.Label(text="Error! Image not found \nResasons:\nSource folder is not present at location : C:\ \nOr image name has changed\nOr source folder name has changed \nMake sure source folder name is: \nSA_Project_Group_11",font='comicsansms 14 bold',padx=10,pady=10,fg='#202b2a',bg='#e5f5d5').place(x=20,y=200)
    tkinter.Label(text=" Enter the length 'A' value (in meter) : ",font='comicsansms 14 bold',padx=10,pady=10,fg='#202b2a',bg='#e5f5d5').place(x=800,y=100)
    tkinter.Entry(root,textvariable=A_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=150,relwidth=0.35, relheight=0.06)
    tkinter.Label(text=" Enter the length 'B' value (in meter) : ",font='comicsansms 14 bold',padx=10,pady=10,fg='#202b2a',bg='#e5f5d5').place(x=800,y=250)
    tkinter.Entry(root,textvariable=B_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=300,relwidth=0.35, relheight=0.06)
    tkinter.Label(text=" Enter the uniformly distributed load 'H' value\n (in KN/m) : ",font='comicsansms 14 bold',padx=10,pady=10,fg='#202b2a',bg='#e5f5d5').place(x=800,y=400)
    tkinter.Entry(root,textvariable=H_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=472.5,relwidth=0.35, relheight=0.06)
    tkinter.Button(text='Continue ->',padx=15,pady=10,font='comicsansms 15 bold',bg='#a33333',fg='white',command=second_page_validation).place(x=950,y=565)
    root.mainloop()

#for check data validation
warn_A = tkinter.Label()
warn_B = tkinter.Label()
warn_H = tkinter.Label()
warn_A_B = tkinter.Label()

def second_page_validation():
    A_valid = False
    B_valid = False
    H_valid = False
    sum_valid = True
    global warn_A
    warn_A.destroy()
    global warn_B
    warn_B.destroy()
    global warn_H
    warn_H.destroy()
    global warn_A_B
    warn_A_B.destroy()
    temp1 = 1
    temp2 = 1

    try:
        is_poss1 = float(A_val.get())
        temp1 = is_poss1
        A_valid = True
    except:
        warn_A = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_A.place(x=800,y=200)

    try:
        is_poss2 = float(B_val.get())
        temp2 = is_poss2
        B_valid = True
    except:
        warn_B = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_B.place(x=800,y=350)

    if((temp1==0)and(temp2==0)):
        sum_valid = False
        warn_A_B = tkinter.Label(text="*Provide either A or B non-zero.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_A_B.place(x=800,y=350)
        warn_A_B.place(x=800,y=200)

    try:
        is_poss3 = float(H_val.get())
        H_valid = True
    except:
        warn_H = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_H.place(x=800,y=515)
    if((A_valid==True)and(B_valid==True)and(H_valid==True)and(sum_valid==True)):
        third_page()


#Third page :

def third_page():
    remove_children()
    #for background
    try:
        path = current_location + r'\p3.png'
        filename1 = tkinter.PhotoImage(file = path)
        background_label1 = tkinter.Label(image=filename1)
        background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        pass
    #main code
    tkinter.Label(text='Enter following values :',font='comicsansms 25 bold',bg='#202b2a',fg='#e5f5d5',padx=50,pady=10,borderwidth=0).pack(pady=20)
    try:
        path = current_location + r'\struct1.png'
        filename2 = tkinter.PhotoImage(file = path)
        background_label2 = tkinter.Label(image=filename2,bg='#202b2a',padx=100,pady=0,borderwidth=0)
        background_label2.place(x=20, y=150, relwidth=0.55, relheight=0.525)  #0.525
    except:
        tkinter.Label(text="Please put source folder at location :\n C:'\'",font='comicsansms 14 bold',padx=10,pady=10,fg='#202b2a',bg='#e5f5d5').place(x=20,y=200)
    tkinter.Label(text=" Enter the length 'C' value (in meter) : ",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='#e5f5d5').place(x=800,y=100)
    tkinter.Entry(root,textvariable=C_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=150,relwidth=0.35, relheight=0.06)
    tkinter.Label(text=" Enter the length 'D' value (in meter) : ",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='#e5f5d5').place(x=800,y=250)
    tkinter.Entry(root,textvariable=D_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=300,relwidth=0.35, relheight=0.06)
    tkinter.Label(text=" Enter the uniformly varying load 'I' value\n (in KN/m) : ",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='#e5f5d5').place(x=800,y=400)
    tkinter.Entry(root,textvariable=I_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=472.5,relwidth=0.35, relheight=0.06)
    tkinter.Button(text='<- back',padx=35,pady=10,font='comicsansms 15 bold',bg='#a33333',fg='white',command=start_structure).place(x=800,y=575)
    tkinter.Button(text='Continue ->',padx=15,pady=10,font='comicsansms 15 bold',bg='#a33333',fg='white',command=third_page_validation).place(x=1090,y=575)
    root.mainloop()

#for check data validation
warn_C = tkinter.Label()
warn_D = tkinter.Label()
warn_I = tkinter.Label()

def third_page_validation():
    C_valid = False
    D_valid = False
    I_valid = False
    global warn_C
    warn_C.destroy()
    global warn_D
    warn_D.destroy()
    global warn_I
    warn_I.destroy()
    try:
        is_poss1 = float(C_val.get())
        if(is_poss1>0):
            C_valid = True
        else:
            warn_C = tkinter.Label(text="*Enter a positive value greater than zero for length.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
            warn_C.place(x=800,y=200)
    except:
        warn_C = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_C.place(x=800,y=200)
    try:
        is_poss2 = float(D_val.get())
        if(is_poss2>0):
            D_valid = True
        else:
           warn_D = tkinter.Label(text="*Enter a positive value greater than zero for length.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
           warn_D.place(x=800,y=350)
    except:
        warn_D = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_D.place(x=800,y=350) 

    try:
        is_poss3 = float(I_val.get())
        I_valid = True
    except:
        warn_I = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_I.place(x=800,y=518)

    if((C_valid==True)and(D_valid==True)and(I_valid==True)):
        fourth_page()


#fourth page

def fourth_page():
    remove_children()
    #for background
    try:
        path = current_location + r'\p4.png'
        filename1 = tkinter.PhotoImage(file = path)
        background_label1 = tkinter.Label(image=filename1)
        background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        pass
    #main code
    tkinter.Label(text='Enter following values :',font='comicsansms 25 bold',bg='#202b2a',fg='#e5f5d5',padx=50,pady=10,borderwidth=0).pack(pady=20)
    try:
        path = current_location + r'\struct1.png'
        filename2 = tkinter.PhotoImage(file = path)
        background_label2 = tkinter.Label(image=filename2,bg='#202b2a',padx=100,pady=0,borderwidth=0)
        background_label2.place(x=20, y=150, relwidth=0.55, relheight=0.525)  #0.525
    except:
        tkinter.Label(text="Please put source folder at location :\n C:'\'",font='comicsansms 14 bold',padx=10,pady=10,fg='#202b2a',bg='#e5f5d5').place(x=20,y=200)
    tkinter.Label(text=" Enter the length 'E' value (in meter) : ",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='#e5f5d5').place(x=800,y=100)
    tkinter.Entry(root,textvariable=E_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=150,relwidth=0.35, relheight=0.06)
    tkinter.Label(text=" Enter the length 'F' value (in meter) : ",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='#e5f5d5').place(x=800,y=250)
    tkinter.Entry(root,textvariable=F_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=300,relwidth=0.35, relheight=0.06)
    tkinter.Label(text=" Enter the point load 'J' value (in KN) : ",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='#e5f5d5').place(x=800,y=400)
    tkinter.Entry(root,textvariable=J_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=450,relwidth=0.35, relheight=0.06)
    tkinter.Label(text=" Enter the length 'G' value (in meter) : ",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='#e5f5d5').place(x=800,y=550)
    tkinter.Entry(root,textvariable=G_val,font='comicsansms 14 bold',justify='center',bd=3,width=75).place(x=800,y=600,relwidth=0.35, relheight=0.06)
    tkinter.Button(text='<- Back',padx=35,pady=10,font='comicsansms 15 bold',bg='#a33333',fg='white',command=third_page).place(x=20,y=585)
    tkinter.Button(text='Continue ->',padx=15,pady=10,font='comicsansms 15 bold',bg='#a33333',fg='white',command=fourth_page_validation).place(x=570,y=585)
    root.mainloop()

#for check data validation
warn_E = tkinter.Label()
warn_F = tkinter.Label()
warn_G = tkinter.Label()
warn_J = tkinter.Label()

def fourth_page_validation():
    E_valid = False
    F_valid = False
    G_valid = False
    J_valid = False
    global warn_E
    warn_E.destroy()
    global warn_F
    warn_F.destroy()
    global warn_G
    warn_G.destroy()
    global warn_J
    warn_J.destroy()
    try:
        is_poss1 = float(E_val.get())
        if(is_poss1>0):
            E_valid = True
        else:
            warn_E = tkinter.Label(text="*Enter a positive value greater than zero for length.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
            warn_E.place(x=800,y=200)
    except:
        warn_E = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_E.place(x=800,y=200)

    try:
        is_poss2 = float(F_val.get())
        if(is_poss2>0):
            F_valid = True
        else:
           warn_F = tkinter.Label(text="*Enter a positive value greater than zero for length.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
           warn_F.place(x=800,y=350)
    except:
        warn_F = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_F.place(x=800,y=350) 

    try:
        is_poss3 = float(J_val.get())
        J_valid = True
    except:
        warn_J = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_J.place(x=800,y=500)
    
    try:
        is_poss4 = float(G_val.get())
        if(is_poss4>0):
            G_valid = True
        else:
           warn_G = tkinter.Label(text="*Enter a positive value greater than zero for length.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
           warn_G.place(x=800,y=650)
    except:
        warn_G = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_G.place(x=800,y=650) 

    if((E_valid==True)and(F_valid==True)and(G_valid==True)and(J_valid==True)):
        fifth_page()


#fifth page

def fifth_page():
    remove_children()
    try:
        path = current_location + r'\p5.png'
        filename3 = tkinter.PhotoImage(file = path)
        background_label3 = tkinter.Label(image=filename3)
        background_label3.place(x=0, y=0, relwidth=1, relheight=1) 
    except:
        pass
    #main code
    tkinter.Label(text='Enter Material Properties :',font='comicsansms 25 bold',bg='#202b2a',fg='#e5f5d5',padx=50,pady=10,borderwidth=0).place(x=380,y=50)
    tkinter.Label(text=" Enter the E value of material (in GPa) : ",font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=50,y=200)
    tkinter.Entry(root,textvariable=mat_E_val,font='comicsansms 15 bold',justify='center',bd=3,width=75).place(x=500,y=200,relwidth=0.55, relheight=0.055)
    tkinter.Label(text=" Enter the A value of material (in m^2) : ",font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=50,y=300)
    tkinter.Entry(root,textvariable=mat_A_val,font='comicsansms 15 bold',justify='center',bd=3,width=75).place(x=500,y=300,relwidth=0.55, relheight=0.055)
    tkinter.Label(text=" Enter the I value of material (in m^4) : ",font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=50,y=400)
    tkinter.Entry(root,textvariable=mat_I_val,font='comicsansms 15 bold',justify='center',bd=3,width=75).place(x=500,y=400,relwidth=0.55, relheight=0.055)
    tkinter.Button(text='<- Back',padx=35,pady=10,font='comicsansms 15 bold',bg='#a33333',fg='white',command=fourth_page).place(x=200,y=500)
    tkinter.Button(text='Solve ->',padx=35,pady=10,font='comicsansms 15 bold',bg='#a33333',fg='white',command=fifth_page_validation).place(x=900,y=500)
    root.mainloop()

#for check data validation
warn_E_mat = tkinter.Label()
warn_A_mat = tkinter.Label()
warn_I_mat = tkinter.Label()

def fifth_page_validation():
    mat_E_valid = False
    mat_A_valid = False
    mat_I_valid = False
    global warn_E_mat
    warn_E_mat.destroy()
    global warn_A_mat
    warn_A_mat.destroy()
    global warn_I_mat
    warn_I_mat.destroy()
    try:
        is_poss1 = float(mat_E_val.get())
        if(is_poss1>0):
            mat_E_valid = True
        else:
            warn_E_mat = tkinter.Label(text="*Enter a positive value greater than zero.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
            warn_E_mat.place(x=500,y=250)
    except:
        warn_E_mat = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_E_mat.place(x=500,y=250)
    try:
        is_poss2 = float(mat_A_val.get())
        if(is_poss2>0):
            mat_A_valid = True
        else:
           warn_A_mat = tkinter.Label(text="*Enter a positive value greater than zero.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
           warn_A_mat.place(x=500,y=350)
    except:
        warn_A_mat = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_A_mat.place(x=500,y=350) 

    try:
        is_poss3 = float(mat_I_val.get())
        if(is_poss3>0):
            mat_I_valid = True
        else:
           warn_I_mat = tkinter.Label(text="*Enter a positive value greater than zero.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
           warn_I_mat.place(x=500,y=450)
    except:
        warn_I_mat = tkinter.Label(text="*Enter a numerical value.",font='comicsansms 14 bold',padx=10,pady=10,bg='#202b2a',fg='red')
        warn_I_mat.place(x=500,y=450)

    if((mat_E_valid==True)and(mat_A_valid==True)and(mat_I_valid==True)):
        input_data_members()

#main problem solve using global matrix

give_input = [[0,0,0,0,0,0,''],[0,0,0,0,0,0,''],[0,0,0,0,0,0,''],[0,0,0,0,0,0,''],[0,0,0,0,0,0,''],[0,0,0,0,0,0,'']]
def input_data_members():
    l_0 = math.sqrt((float(A_val.get()))*(float(A_val.get()))+(float(B_val.get()))*(float(B_val.get())))
    give_input[0][0] = (float(mat_E_val.get()))*1000000000
    give_input[0][1] = float(mat_A_val.get())
    give_input[0][2] = float(mat_I_val.get())
    give_input[0][3] = l_0
    give_input[0][4] = (float(A_val.get()))/l_0
    give_input[0][5] = (float(B_val.get()))/l_0
    give_input[0][6] = "19 20 21 1 2 3"
    give_input[1][0] = (float(mat_E_val.get()))*1000000000
    give_input[1][1] = float(mat_A_val.get())
    give_input[1][2] = float(mat_I_val.get())
    give_input[1][3] = float(C_val.get())
    give_input[1][4] = 1
    give_input[1][5] = 0
    give_input[1][6] = "1 2 3 4 5 6"
    give_input[2][0] = (float(mat_E_val.get()))*1000000000
    give_input[2][1] = float(mat_A_val.get())
    give_input[2][2] = float(mat_I_val.get())
    give_input[2][3] = float(D_val.get())
    give_input[2][4] = 1
    give_input[2][5] = 0
    give_input[2][6] = "4 5 6 7 8 9"
    give_input[3][0] = (float(mat_E_val.get()))*1000000000
    give_input[3][1] = float(mat_A_val.get())
    give_input[3][2] = float(mat_I_val.get())
    give_input[3][3] = float(E_val.get())
    give_input[3][4] = 0
    give_input[3][5] = -1
    give_input[3][6] = "7 8 9 10 11 12"
    give_input[4][0] = (float(mat_E_val.get()))*1000000004
    give_input[4][1] = float(mat_A_val.get())
    give_input[4][2] = float(mat_I_val.get())
    give_input[4][3] = float(F_val.get())
    give_input[4][4] = 0
    give_input[4][5] = -1
    give_input[4][6] = "10 11 12 14 15 13"
    give_input[5][0] = (float(mat_E_val.get()))*1000000000
    give_input[5][1] = float(mat_A_val.get())
    give_input[5][2] = float(mat_I_val.get())
    give_input[5][3] = float(G_val.get())
    give_input[5][4] = 1
    give_input[5][5] = 0
    give_input[5][6] = "7 8 9 16 17 18"
    solve_global_matrix()


global_matrix = []
def solve_global_matrix():
    node_number = 7

    for p1 in range(0,3*node_number):
        one_row = []
        for p2 in range(0,3*node_number):
            one_row.append(0)
        global_matrix.append(one_row)

    tot_member = 6

    for a in range(1,tot_member+1):
        E_val = give_input[a-1][0]
        A_val = give_input[a-1][1]
        I_val = give_input[a-1][2]
        L_val = give_input[a-1][3]
        lembda_x = give_input[a-1][4]
        lembda_y = give_input[a-1][5]
        dof = (give_input[a-1][6]).split()
        matrix_input_to_global_matrix = [[A_val*E_val*lembda_x*lembda_x/L_val+12*E_val*I_val*lembda_y*lembda_y/(L_val*L_val*L_val),A_val*E_val*lembda_x*lembda_y/L_val-12*E_val*I_val*lembda_y*lembda_x/(L_val*L_val*L_val),-6*E_val*I_val*lembda_y/(L_val*L_val),-A_val*E_val*lembda_x*lembda_x/L_val-12*E_val*I_val*lembda_y*lembda_y/(L_val*L_val*L_val),-A_val*E_val*lembda_x*lembda_y/L_val+12*E_val*I_val*lembda_x*lembda_y/(L_val*L_val*L_val),-6*E_val*I_val*lembda_y/(L_val*L_val)],[A_val*E_val*lembda_y*lembda_x/L_val-12*E_val*I_val*lembda_x*lembda_y/(L_val*L_val*L_val),A_val*E_val*lembda_y*lembda_y/L_val+12*E_val*I_val*lembda_x*lembda_x/(L_val*L_val*L_val),6*E_val*I_val*lembda_x/(L_val*L_val),-A_val*E_val*lembda_x*lembda_y/L_val+12*E_val*I_val*lembda_x*lembda_y/(L_val*L_val*L_val),-A_val*E_val*lembda_y*lembda_y/L_val-12*E_val*I_val*lembda_x*lembda_x/(L_val*L_val*L_val),6*E_val*I_val*lembda_x/(L_val*L_val)],[-6*E_val*I_val*lembda_y/(L_val*L_val),6*E_val*I_val*lembda_x/(L_val*L_val),4*E_val*I_val/L_val,6*E_val*I_val*lembda_y/(L_val*L_val),-6*E_val*I_val*lembda_x/(L_val*L_val),2*E_val*I_val/L_val],[-A_val*E_val*lembda_x*lembda_x/L_val-12*E_val*I_val*lembda_y*lembda_y/(L_val*L_val*L_val),-A_val*E_val*lembda_y*lembda_x/L_val+12*E_val*I_val*lembda_x*lembda_y/(L_val*L_val*L_val),6*E_val*I_val*lembda_y/(L_val*L_val),A_val*E_val*lembda_x*lembda_x/L_val+12*E_val*I_val*lembda_y*lembda_y/(L_val*L_val*L_val),A_val*E_val*lembda_x*lembda_y/L_val-12*E_val*I_val*lembda_x*lembda_y/(L_val*L_val*L_val),6*E_val*I_val*lembda_y/(L_val*L_val)],[-A_val*E_val*lembda_x*lembda_y/L_val+12*E_val*I_val*lembda_x*lembda_y/(L_val*L_val*L_val),-A_val*E_val*lembda_y*lembda_y/L_val-12*E_val*I_val*lembda_x*lembda_x/(L_val*L_val*L_val),-6*E_val*I_val*lembda_x/(L_val*L_val),A_val*E_val*lembda_x*lembda_y/L_val-12*E_val*I_val*lembda_x*lembda_y/(L_val*L_val*L_val),A_val*E_val*lembda_y*lembda_y/L_val+12*E_val*I_val*lembda_x*lembda_x/(L_val*L_val*L_val),-6*E_val*I_val*lembda_x/(L_val*L_val)],[-6*E_val*I_val*lembda_y/(L_val*L_val),6*E_val*I_val*lembda_x/(L_val*L_val),2*E_val*I_val/L_val,6*E_val*I_val*lembda_y/(L_val*L_val),-6*E_val*I_val*lembda_x/(L_val*L_val),4*E_val*I_val/L_val]]
        for b in range(0,6):
            ind_1 = int(dof[b])
            for c in range(0,6):
                ind_2 = int(dof[c])
                global_matrix[ind_1-1][ind_2-1] += matrix_input_to_global_matrix[b][c]
    FEM_and_FEF()

dis_1 = 0
dis_2 = 0
dis_3 = 0
dis_4 = 0
dis_5 = 0
dis_6 = 0
dis_7 = 0
dis_8 = 0
dis_9 = 0
dis_10 = 0
dis_11 = 0
dis_12 = 0
dis_13 = 0
For_14 = 0
For_15 = 0
For_16 = 0
For_17 = 0
For_18 = 0
For_19 = 0
For_20 = 0
For_21 = 0

def FEM_and_FEF():
    known_force = []
    l_0 = math.sqrt((float(A_val.get()))*(float(A_val.get()))+(float(B_val.get()))*(float(B_val.get())))
    fem_fef = [((float(H_val.get()))*1000)*l_0*((float(B_val.get()))/l_0)/2,-(((float(H_val.get()))*1000)*l_0*((float(A_val.get()))/l_0)/2),((float(H_val.get()))*1000*l_0*l_0/12),0,-((float(I_val.get()))*9000*(float(D_val.get()))/60),-((float(I_val.get()))*1000*(float(D_val.get()))*(float(D_val.get()))/30),0,-((float(I_val.get()))*21000*(float(D_val.get()))/60),((float(I_val.get()))*1000*(float(D_val.get()))*(float(D_val.get()))/20),(float(J_val.get()))*1000,0,0,0,0,0,0,0,0,-((float(H_val.get()))*1000)*l_0*((float(B_val.get()))/l_0)/2,(((float(H_val.get()))*1000)*l_0*((float(A_val.get()))/l_0)/2),((float(H_val.get()))*1000*l_0*l_0/12)]
    for line1 in range(0,13):
        known_force.append(fem_fef[line1])
    known_part_of_matrix = []
    for no1 in range(0,13):
        temp_arr = []
        for no2 in range(0,13):
            temp_arr.append(global_matrix[no1][no2])
        known_part_of_matrix.append(temp_arr)

    sol_dis = np.linalg.solve(known_part_of_matrix,known_force)

    global dis_1 
    dis_1 = sol_dis[0]
    global dis_2
    dis_2 = sol_dis[1]
    global dis_3
    dis_3 = sol_dis[2]
    global dis_4
    dis_4 = sol_dis[3]
    global dis_5
    dis_5 = sol_dis[4]
    global dis_6
    dis_6 = sol_dis[5]
    global dis_7
    dis_7 = sol_dis[6]
    global dis_8
    dis_8 = sol_dis[7]
    global dis_9
    dis_9 = sol_dis[8]
    global dis_10
    dis_10 = sol_dis[9]
    global dis_11
    dis_11 = sol_dis[10]
    global dis_12
    dis_12 = sol_dis[11]
    global dis_13
    dis_13 = sol_dis[12]

    force_find = []

    for ni1 in range(13,21):
        temp_var = 0
        for ni2 in range(0,13):
            temp_var += (global_matrix[ni1][ni2])*(sol_dis[ni2])
        temp_var += fem_fef[ni1]
        force_find.append(temp_var)

    global For_14
    For_14 = force_find[0]
    global For_15
    For_15 = force_find[1]
    global For_16
    For_16 = force_find[2]
    global For_17
    For_17 = force_find[3]
    global For_18
    For_18 = force_find[4]
    global For_19
    For_19 = force_find[5]
    global For_20
    For_20 = force_find[6]
    global For_21
    For_21 = force_find[7]

    sixth_page()
   

#sixth page

def sixth_page():
    remove_children()
    try:
        path = current_location + r'\p6.png'
        filename1 = tkinter.PhotoImage(file = path)
        background_label1 = tkinter.Label(image=filename1)
        background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        pass
    #main code
    tkinter.Label(text='$$ Result $$',font='comicsansms 25 bold',bg='#202b2a',fg='#e5f5d5',padx=50,pady=10,borderwidth=0).pack(pady=10)
    try:
        path = current_location + r'\struct2.png'
        filename2 = tkinter.PhotoImage(file = path)
        background_label2 = tkinter.Label(image=filename2,bg='#202b2a',padx=100,pady=0,borderwidth=0)
        background_label2.place(x=20, y=80, relwidth=0.55, relheight=0.525)
    except:
        tkinter.Label(text="Please put source folder at location :\n C:'\'",font='comicsansms 14 bold',padx=10,pady=10,fg='#202b2a',bg='#e5f5d5').place(x=20,y=100)
    dis_1_Q = "Horizontal displacement (\u2192) of Node Q (in mm): "+str(round(dis_1*1000,3))
    dis_2_Q = "Vertical displacement (\u2191) of Node Q (in mm): "+str(round(dis_2*1000,3))
    rot_Q = "Rotation (\u21BA) at Node Q (in 10^-3 radian): "+str(round(dis_3*1000,3))
    dis_1_R = "Horizontal displacement (\u2192) of Node R (in mm): "+str(round(dis_4*1000,3))
    dis_2_R = "Vertical displacement (\u2191) of Node R (in mm): "+str(round(dis_5*1000,3))
    rot_R = "Rotation (\u21BA) at Node R (in 10^-3 radian): "+str(round(dis_6*1000,3))
    dis_1_S = "Horizontal displacement (\u2192) of Node S (in mm): "+str(round(dis_7*1000,3))
    dis_2_S = "Vertical displacement (\u2191) of Node S (in mm): "+str(round(dis_8*1000,3))
    rot_S = "Rotation (\u21BA) at Node S (in 10^-3 radian): "+str(round(dis_9*1000,3))
    dis_1_T = "Horizontal displacement (\u2192) of Node T (in mm): "+str(round(dis_10*1000,3))
    dis_2_T = "Vertical displacement (\u2191) of Node T (in mm): "+str(round(dis_11*1000,3))
    rot_T = "Rotation (\u21BA) at Node T (in 10^-3 radian): "+str(round(dis_12*1000,3))
    rot_W = "Rotation (\u21BA) at node W (in 10^-3 radian): "+str(round(dis_13*1000,3))
    Force_1_W = "Horizontal Force in \u2192 at Node W (in KN): "+str(round(For_14/1000,3))
    Force_2_W = 'Vertical Force in \u2191 at Node W (in KN):'+str(round(For_15/1000,3))
    Force_1_P = "Horizontal Force in \u2192 at Node P (in KN): "+str(round(For_19/1000,3))
    Force_2_P = "Vertical Force in \u2191 at Node P (in KN): "+str(round(For_20/1000,3))
    Moment_P = "Moment in \u21BA at P (in KN-m): "+str(round(For_21/1000,3))
    Force_1_X = "Horizontal Force in \u2192 at Node X (in KN): "+str(round(For_16/1000,3))
    Force_2_X = "Vertical Force in \u2191 at Node X (in KN): "+str(round(For_17/1000,3))
    Moment_X = "Moment in \u21BA at X (in KN-m): "+str(round(For_18/1000,3))
    tkinter.Label(text=dis_1_Q,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=100)
    tkinter.Label(text=dis_2_Q,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=140)
    tkinter.Label(text=rot_Q,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=180)
    tkinter.Label(text=dis_1_R,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=220)
    tkinter.Label(text=dis_2_R,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=260)
    tkinter.Label(text=rot_R,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=300)
    tkinter.Label(text=dis_1_S,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=340)
    tkinter.Label(text=dis_2_S,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=380)
    tkinter.Label(text=rot_S,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=420)
    tkinter.Label(text=dis_1_T,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=460)
    tkinter.Label(text=dis_2_T,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=20,y=460)
    tkinter.Label(text=rot_T,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=500)
    tkinter.Label(text=Force_1_W,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=20,y=500)
    tkinter.Label(text=Force_2_W,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=20,y=540)
    tkinter.Label(text=Force_1_P,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=540)
    tkinter.Label(text=Force_2_P,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=20,y=580)
    tkinter.Label(text=Moment_P,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=580)
    tkinter.Label(text=Force_1_X,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=20,y=620)
    tkinter.Label(text=Force_2_X,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=620)
    tkinter.Label(text=Moment_X,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=20,y=660)
    tkinter.Label(text=rot_W,font='comicsansms 15 bold',padx=10,pady=5,bg='#202b2a',fg='#e5f5d5').place(x=750,y=660)
    root.mainloop()

#first heading after click on game

tkinter.Label(text='Welcome !\n\n    To the Frame Structure   ',font='comicsansms 25 bold',bg='#202b2a',padx=130,pady=50,fg='#e5f5d5').place(x=300,y=100)

#start button of first page

tkinter.Button(text="Let's Start !",font='comicsansms 20 bold',padx=5,pady=10,relief='ridge',command=start_structure,bg='#a33333',fg='#fcf7f7').place(x=800,y=400)

#Exit button of first page

tkinter.Button(text='Exit !',font='comicsansms 20 bold',padx=20,pady=10,relief='ridge',bg='#a33333',fg='#fcf7f7',command=root.destroy).place(x=300,y=400)

#start the main loop

root.mainloop()