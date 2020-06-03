# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:27:21 2020

@author: matte
"""
import os
from os import path
from tkinter import *

from tkinter.ttk import *
from tkinter import Menu

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

import math

#from datetime import datetime
import datetime
from datetime import timezone
import calendar

#
from py_support_files.wimpy_manager import *
from py_support_files.wimpy_manager_N19 import *
#from py_support_files.wimpy_pdf import *
from py_support_files.wimpy_csv import *
# =============================================================================
# from wimpy_manager import *
# from wimpy_manager_N19 import *
# from wimpy_pdf import *
# from wimpy_csv import *
# =============================================================================

#
now_UTC =datetime.datetime.utcnow()
now_local =datetime.datetime.now()
timestamp = datetime.datetime.timestamp(now_UTC)

window = Tk()

window.title("Wimpy Manager app")
window.geometry('1241x700')
#window.geometry('500x300')


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)




lbl_Side = Label(window, text="Controller Side")
lbl_Side.grid(column=0, row=0)



selected_SideS = BooleanVar()
selected_SideS.set(False) #set check state
chk_SideContrS = Checkbutton(window, text='SpaCon', var=selected_SideS)
chk_SideContrS.grid(column=1, row=0)
selected_SideG = BooleanVar()
selected_SideG.set(False) #set check state
chk_SideContrG = Checkbutton(window, text='GrndCon', var=selected_SideG)
chk_SideContrG.grid(column=2, row=0)

#selected_SideContr = IntVar()
#rad_SG = Radiobutton(window,text='SpaCon & GrndCon', value=1, variable=selected_SideContr)
#rad_S = Radiobutton(window,text='SpaCon', value=2, variable=selected_SideContr)
#rad_G = Radiobutton(window,text='GrndCon', value=3, variable=selected_SideContr)
#rad_SG.grid(column=1, row=0)
#rad_S.grid(column=2, row=0)
#rad_G.grid(column=3, row=0)


lbl_Shift = Label(window, text="MetOp Antenna")
lbl_Shift.grid(column=0, row=1)

CDA_cur = 1
CDAfp = 'files'
CDAf = CDAfp+'/Main_CDA.txt'
Wfis_CDA = path.isfile(CDAf)
if (Wfis_CDA==True):
    fp=open(CDAf,'r')
    lines=fp.readlines()
    if (len(lines)==1 and (lines[0]=='1' or lines[0]=='2' )):
        CDA_cur = int(lines[0])
combo_CDA = Combobox(window, width=10)
combo_CDA['values']= ('', 'CDA1', 'CDA2', 'MAS', 'VL1', 'KOU', 'FBK', 'WAL')
combo_CDA.current(CDA_cur) #set the selected item
combo_CDA.grid(column=1, row=1, sticky="W")


DataStart_MSW = StringVar()
DataEnd_MSW = StringVar()
lbl_PreGenerate_Summary_MSW = Label(window, text="Mission Swap:")
lbl_PreGenerate_Summary_MSW.grid(column=1, row=9, sticky="W")

lbl_PreGenerate_DateStart_MSW = Label(window, text="")
lbl_PreGenerate_DateStart_MSW.grid(column=1, row=10, sticky="W")
lbl_PreGenerate_DateEnd_MSW = Label(window, text="")
lbl_PreGenerate_DateEnd_MSW.grid(column=1, row=11, sticky="W")

def clicked_btn_MissionSwap():
    top = tk.Toplevel(window)
    top.title("Mission Swap")
    
    lbl_DataFormat_MSW = Label(top, text="Date Format: YYYY-MM-DD hh:mm:ss [UTC]")
    #lbl_DataFormat_MSW.grid(column=0, row=0, columnspan = 2, sticky = tk.W+tk.E)
    lbl_DataFormat_MSW.grid(column=0, row=0)
    
    def view_MSW_FAQ():
        top = tk.Toplevel(window)
        top.title("Mission Swap FAQ")
        lbl_PreGenerate_FAQ_MSW = Label(top, text="Date Start: after LOS shadow pass but before AOS of 1st pass on new CDA")
        lbl_PreGenerate_FAQ_MSW.grid(column=0, row=0, sticky="W")
        lbl_PreGenerate_FAQ_MSW = Label(top, text="Date End: after LOS shadow pass but before AOS of the 1st pass on old CDA")
        lbl_PreGenerate_FAQ_MSW.grid(column=0, row=1, sticky="W")
        
    btn_FAQ_MSW = Button(top, text="?", command=view_MSW_FAQ)
    btn_FAQ_MSW.grid(column=1, row=0)
    
    def calendar_view_MSW_DS():
        def print_update_cal_MSW():
            res=format(cal.selection_get())
            if (combo_H.get()==''):
                hr=0
            else:
                hr=int(combo_H.get())
            if (combo_M.get()==''):
                mint=0
            else:
                mint=int(combo_M.get())
            res1=datetime.datetime(int(res[0:4]), int(res[5:7]), int(res[8:10]), hr, mint, 0, 0)
            DataStart_MSW.set(res1)
        top = tk.Toplevel(window)
        top.title("Calendar Date Start")
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=now_UTC.year, month=now_UTC.month, day=now_UTC.day)
        cal.pack(fill="both", expand=True)
        
        frame1 = Frame(top)
        frame1.pack(fill=X)
            
        combo_M = Combobox(frame1, width=5)
        combo_M['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
        combo_M.current(now_UTC.minute+1) #set the selected item
        combo_M.pack(side=RIGHT)
        lbl_Minutes = Label(frame1, text="Minutes:")
        lbl_Minutes.pack(side=RIGHT)
        
        combo_H = Combobox(frame1, width=5)
        combo_H['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
        combo_H.current(now_UTC.hour+1) #set the selected item
        combo_H.pack(side=RIGHT)
        lbl_Hours = Label(frame1, text="Hours:")
        lbl_Hours.pack(side=RIGHT)
        
        frame2 = Frame(top)
        frame2.pack(fill=X)
            
        ttk.Button(frame2, text="Update", command=print_update_cal_MSW).pack(side=TOP)
    
    def calendar_view_MSW_DE():
        def print_update_cal_MSW():
            res=format(cal.selection_get())
            if (combo_H.get()==''):
                hr=0
            else:
                hr=int(combo_H.get())
            if (combo_M.get()==''):
                mint=0
            else:
                mint=int(combo_M.get())
            res1=datetime.datetime(int(res[0:4]), int(res[5:7]), int(res[8:10]), hr, mint, 0, 0)
            DataEnd_MSW.set(res1)
        top = tk.Toplevel(window)
        top.title("Calendar Date Start")
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=now_UTC.year, month=now_UTC.month, day=now_UTC.day)
        cal.pack(fill="both", expand=True)
        
        frame1 = Frame(top)
        frame1.pack(fill=X)
            
        combo_M = Combobox(frame1, width=5)
        combo_M['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
        combo_M.current(now_UTC.minute+1) #set the selected item
        combo_M.pack(side=RIGHT)
        lbl_Minutes = Label(frame1, text="Minutes:")
        lbl_Minutes.pack(side=RIGHT)
        
        combo_H = Combobox(frame1, width=5)
        combo_H['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
        combo_H.current(now_UTC.hour+1) #set the selected item
        combo_H.pack(side=RIGHT)
        lbl_Hours = Label(frame1, text="Hours:")
        lbl_Hours.pack(side=RIGHT)
        
        frame2 = Frame(top)
        frame2.pack(fill=X)
            
        ttk.Button(frame2, text="Update", command=print_update_cal_MSW).pack(side=TOP)
        
    def Apply_MSW():
        res_PreGenerate_DateStart = "Date Start: " + txt_DataStart_MSW.get()
        lbl_PreGenerate_DateStart_MSW.configure(text= res_PreGenerate_DateStart)
        
        DS=datetime.datetime.strptime(DataStart_MSW.get(), '%Y-%m-%d %H:%M:%S')
        DE=datetime.datetime.strptime(DataEnd_MSW.get(), '%Y-%m-%d %H:%M:%S')
        
        if (DE<DS):
            messagebox.showerror('error', 'Date end Missin Swap greater than start one')
        else:
            res_PreGenerate_DateEnd = "Date End: " + txt_DataEnd_MSW.get()
            lbl_PreGenerate_DateEnd_MSW.configure(text= res_PreGenerate_DateEnd) 
    
    def Reset_MSW():
        res_PreGenerate_DateStart = ""
        lbl_PreGenerate_DateStart_MSW.configure(text= res_PreGenerate_DateStart)
        res_PreGenerate_DateEnd = ""
        lbl_PreGenerate_DateEnd_MSW.configure(text= res_PreGenerate_DateEnd) 
            
    lbl_DataStart_MSW = Label(top, text="Date Start")
    lbl_DataStart_MSW.grid(column=0, row=1)
    txt_DataStart_MSW = Entry(top, width=20, textvariable=DataStart_MSW)
    txt_DataStart_MSW.grid(column=0, row=3)
    btn_DS_MSW = Button(top, text="Calendar", command=calendar_view_MSW_DS).grid(column=0, row=4)
    
    
    lbl_DataEnd_MSW = Label(top, text="Date End")
    lbl_DataEnd_MSW.grid(column=1, row=1)
    txt_DataEnd_MSW = Entry(top, width=20, textvariable=DataEnd_MSW)
    txt_DataEnd_MSW.grid(column=1, row=3)
    btn_DE_MSW = Button(top, text="Calendar", command=calendar_view_MSW_DE)
    btn_DE_MSW.grid(column=1, row=4)
    
    
    btn_AP_MSW = Button(top, text="Apply", command=Apply_MSW)
    btn_AP_MSW.grid(column=0, row=5, sticky = tk.W+tk.E)
    btn_Re_MSW = Button(top, text="Reset", command=Reset_MSW)
    btn_Re_MSW.grid(column=1, row=5, sticky = tk.W+tk.E)

clicked_btn_MissSwap = Button(window, text="Mission Swap", command=clicked_btn_MissionSwap)
clicked_btn_MissSwap.grid(column=2, row=1)

lbl_Shift = Label(window, text="Shift")
lbl_Shift.grid(column=0, row=3)


combo_Shift = Combobox(window, width=10)
combo_Shift['values']= ('', 'Morning', 'Evening', 'Night')
if (now_local.hour>6  and now_local.hour<12):
    combo_Shift.current(1) #set the selected item
elif (now_local.hour>=12  and now_local.hour<20):
    combo_Shift.current(2) #set the selected item
else:
    combo_Shift.current(3) #set the selected item    
combo_Shift.grid(column=1, row=3, sticky="W")


def Solar_Legal_Clock(anno):
    month = calendar.monthcalendar(anno, 3)
    giorno_di_marzo = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
    month = calendar.monthcalendar(anno, 10)
    giorno_di_ottobre = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
    return giorno_di_marzo, giorno_di_ottobre

def clicked_btn_Shift():
    if (combo_Shift.get()!=''):
        delta=(now_local-now_UTC).seconds
        delta =datetime.timedelta(seconds=delta)
        if (combo_Shift.get()=='Morning'):
            DS=datetime.datetime(now_local.year, now_local.month, now_local.day, 6, 0, 0, 0)-delta
            DE=datetime.datetime(now_local.year, now_local.month, now_local.day, 12, 45, 0, 0)-delta
        elif (combo_Shift.get()=='Evening'):
            DS=datetime.datetime(now_local.year, now_local.month, now_local.day, 12, 30, 0, 0)-delta
            DE=datetime.datetime(now_local.year, now_local.month, now_local.day, 20, 15, 0, 0)-delta
        elif (combo_Shift.get()=='Night'):
            DS=datetime.datetime(now_local.year, now_local.month, now_local.day, 20, 00, 0, 0)-delta
            giorno_di_marzo, giorno_di_ottobre = Solar_Legal_Clock(now_local.year)
            DE=datetime.datetime(now_local.year, now_local.month, now_local.day, 6, 15, 0, 0)+datetime.timedelta(days=1)-delta
            if (DE.month==3 and DE.day==giorno_di_marzo):
                DE=DE-datetime.timedelta(hours=1)
            if (DE.month==10 and DE.day==giorno_di_ottobre):
                DE=DE+datetime.timedelta(hours=1)
        DataStart.set(DS)
        DataEnd.set(DE)
clicked_btn_Shift = Button(window, text="Update", command=clicked_btn_Shift)
clicked_btn_Shift.grid(column=2, row=3)


lbl_SC = Label(window, text="S/C")
lbl_SC.grid(column=0, row=2)

combo_SC = Combobox(window, width=10)
combo_SC['values']= ( '', 'All MetOp','MetOp-A', 'MetOp-B', 'MetOp-C', 'N19', 'N18')
combo_SC.current(1) #set the selected item
combo_SC.grid(column=1, row=2, sticky="W")

selected_NOAA_BOS = BooleanVar()
selected_NOAA_BOS.set(True) #set check state
chk_NOAA_BOS = Checkbutton(window, text='NOAA BOS', var=selected_NOAA_BOS)
chk_NOAA_BOS.grid(column=2, row=2)
selected_Weekly = BooleanVar()
selected_Weekly.set(True) #set check state
chk_Weekly = Checkbutton(window, text='Weekly', var=selected_Weekly)
chk_Weekly.grid(column=3, row=2)
#chk_state_M01 = BooleanVar()
#chk_state_M01.set(True) #set check state
#chk_M01 = Checkbutton(window, text='M01', var=chk_state_M01)
#chk_M01.grid(column=2, row=2)












lbl_DataFormat = Label(window, text="Date Format: YYYY-MM-DD hh:mm:ss [UTC]")
lbl_DataFormat.grid(column=0, row=4)

DataStart = StringVar()
lbl_DataStart = Label(window, text="Date Start")
lbl_DataStart.grid(column=0, row=5)
txt_DataStart = Entry(window, width=20, textvariable=DataStart)
txt_DataStart.grid(column=1, row=5)



def calendar_view():
    def print_update():
        res=format(cal.selection_get())
        if (combo_H.get()==''):
            hr=0
        else:
            hr=int(combo_H.get())
        if (combo_M.get()==''):
            mint=0
        else:
            mint=int(combo_M.get())
        res1=datetime.datetime(int(res[0:4]), int(res[5:7]), int(res[8:10]), hr, mint, 0, 0)
        DataStart.set(res1)
    def clicked_btn_now_UTC():
        now_UTC_nos1=datetime.datetime.utcnow()
        now_UTC_nos=datetime.datetime(now_UTC_nos1.year, now_UTC_nos1.month, now_UTC_nos1.day, now_UTC_nos1.hour, now_UTC_nos1.minute, now_UTC_nos1.second, 0)
        DataStart.set(now_UTC_nos)
        combo_M.current(now_UTC_nos.minute+1)
        combo_H.current(now_UTC_nos.hour+1)
        
    top = tk.Toplevel(window)
    top.title("Calendar Date Start")
    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=now_UTC.year, month=now_UTC.month, day=now_UTC.day)
    cal.pack(fill="both", expand=True)
    
    frame1 = Frame(top)
    frame1.pack(fill=X)
        
    combo_M = Combobox(frame1, width=5)
    combo_M['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    combo_M.current(now_UTC.minute+1) #set the selected item
    combo_M.pack(side=RIGHT)
    lbl_Minutes = Label(frame1, text="Minutes:")
    lbl_Minutes.pack(side=RIGHT)
    
    combo_H = Combobox(frame1, width=5)
    combo_H['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
    combo_H.current(now_UTC.hour+1) #set the selected item
    combo_H.pack(side=RIGHT)
    lbl_Hours = Label(frame1, text="Hours:")
    lbl_Hours.pack(side=RIGHT)
    
    frame2 = Frame(top)
    frame2.pack(fill=X)
        
    ttk.Button(frame2, text="Update", command=print_update).pack(side=RIGHT)
    ttk.Button(frame2, text="now UTC", command=clicked_btn_now_UTC).pack(side=LEFT)
    
btn_now_UTC = Button(window, text="Calendar", command=calendar_view)
btn_now_UTC.grid(column=2, row=5)


DataEnd = StringVar()
lbl_DataEnd = Label(window, text="Date End")
lbl_DataEnd.grid(column=0, row=6)
txt_DataEnd = Entry(window, width=20, textvariable=DataEnd)
txt_DataEnd.grid(column=1, row=6)


def clicked_btn_Calendar2():
    def print_update():
        res=format(cal.selection_get())
        if (combo_H.get()==''):
            hr=0
        else:
            hr=int(combo_H.get())
        if (combo_M.get()==''):
            mint=0
        else:
            mint=int(combo_M.get())
        res1=datetime.datetime(int(res[0:4]), int(res[5:7]), int(res[8:10]), hr, mint, 0, 0)
        DataEnd.set(res1)
    
    def clicked_btn_UpdateShift():
        if (combo_pS.get()!=''):
            DS=datetime.datetime.strptime(DataStart.get(), '%Y-%m-%d %H:%M:%S')
            giorno_di_marzo, giorno_di_ottobre = Solar_Legal_Clock(DS.year)
            if (DS>=datetime.datetime(DS.year, 3, giorno_di_marzo, 1, 0, 0, 0) and DS<datetime.datetime(DS.year, 10, giorno_di_ottobre, 1, 0, 0, 0)):
                deltatime_SL=datetime.timedelta(hours=2)
            else:
                deltatime_SL=datetime.timedelta(hours=1)
            
            if (combo_pS.get()=='Morning'):
                DE=datetime.datetime(DS.year, DS.month, DS.day, 12, 45, 0, 0)-deltatime_SL
                DataEnd.set(DE)
            elif (combo_pS.get()=='Evening'):
                DE=datetime.datetime(DS.year, DS.month, DS.day, 20, 15, 0, 0)-deltatime_SL
                DataEnd.set(DE)
            elif (combo_pS.get()=='Night'):
                DE=datetime.datetime(DS.year, DS.month, DS.day, 6, 15, 0, 0)+datetime.timedelta(days=1)-deltatime_SL
                if (DE.month==3 and DE.day==giorno_di_marzo and DS<datetime.datetime(2020, 3, giorno_di_marzo, 1, 0, 0, 0)):
                    DE=DE-datetime.timedelta(hours=1)
                if (DE.month==10 and DE.day==giorno_di_ottobre and DS<datetime.datetime(2020, 10, giorno_di_ottobre, 1, 0, 0, 0)):
                    DE=DE+datetime.timedelta(hours=1)
                DataEnd.set(DE)
    
    def clicked_btn_UpdateDateStartp():
        if (combo_ph.get()!=''):
            res=int(combo_ph.get())
            D1=datetime.datetime.strptime(DataStart.get(), '%Y-%m-%d %H:%M:%S')
            dD=datetime.timedelta(hours=res)
            DE=D1+dD
            DataEnd.set(DE)
    
    top = tk.Toplevel(window)
    top.title("Calendar Date End")
    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=now_UTC.year, month=now_UTC.month, day=now_UTC.day)
    cal.pack(fill="both", expand=True)
    
    frame1 = Frame(top)
    frame1.pack(fill=X)
    
    ttk.Button(frame1, text="Update", command=print_update).pack(side=RIGHT)
    
    combo_M = Combobox(frame1, width=5)
    combo_M['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    combo_M.current(now_UTC.minute+1) #set the selected item
    combo_M.pack(side=RIGHT)
    lbl_Minutes = Label(frame1, text="Minutes:")
    lbl_Minutes.pack(side=RIGHT)
    
    combo_H = Combobox(frame1, width=5)
    combo_H['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
    combo_H.current(now_UTC.hour+1) #set the selected item
    combo_H.pack(side=RIGHT)
    lbl_Hours = Label(frame1, text="Hours:")
    lbl_Hours.pack(side=RIGHT)
    
    
    
    
    frame2 = Frame(top)
    frame2.pack(fill=X)
    
    ttk.Button(frame2, text="Update", command=clicked_btn_UpdateDateStartp).pack(side=RIGHT)
    lbl_hour = Label(frame2, text="Hours")
    lbl_hour.pack(side=RIGHT)    
    combo_ph = Combobox(frame2, width=10)
    combo_ph['values']= ('', '1', '2', '3', '4', '5', '6', '7' , '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36')
    combo_ph.current(0) #set the selected item
    combo_ph.pack(side=RIGHT)
    lbl_hours = Label(frame2, text="Data Start +:")
    lbl_hours.pack(side=RIGHT)
    
    frame3 = Frame(top)
    frame3.pack(fill=X)
    
    ttk.Button(frame3, text="Update", command=clicked_btn_UpdateShift).pack(side=RIGHT)
    lbl_hour = Label(frame3, text="shift")
    lbl_hour.pack(side=RIGHT)    
    combo_pS = Combobox(frame3, width=10)
    combo_pS['values']= ('', 'Morning', 'Evening', 'Night')
    combo_pS.current(0) #set the selected item
    combo_pS.pack(side=RIGHT)
    lbl_hours = Label(frame3, text="Data Start until:")
    lbl_hours.pack(side=RIGHT)
    

        
clicked_btn_Update = Button(window, text="Calendar", command=clicked_btn_Calendar2)
clicked_btn_Update.grid(column=2, row=6)







lbl_file = Label(window, text="File format")
lbl_file.grid(column=0, row=7)

#selected_fileContr = IntVar()
#rad_pdfcsv = Radiobutton(window,text='.pdf & .csv', value=1, variable=selected_fileContr)
#rad_pdf = Radiobutton(window,text='.pdf', value=2, variable=selected_fileContr)
#rad_csv = Radiobutton(window,text='.csv', value=3, variable=selected_fileContr)
#rad_pdfcsv.grid(column=1, row=7)
#rad_pdf.grid(column=2, row=7)
#rad_csv.grid(column=3, row=7)


#selected_filePDF = BooleanVar()
#selected_filePDF.set(False) #set check state
#chk_SideContrS = Checkbutton(window, text='.pdf', var=selected_filePDF)
#chk_SideContrS.grid(column=1, row=7)
selected_filecsv = BooleanVar()
selected_filecsv.set(True) #set check state
chk_SideContrG = Checkbutton(window, text='.csv', var=selected_filecsv)
chk_SideContrG.grid(column=2, row=7)






lbl_PreGenerate_Summary = Label(window, text="Summary:")
lbl_PreGenerate_Summary.grid(column=0, row=9, sticky="W")
lbl_PreGenerate_Side = Label(window, text="")
lbl_PreGenerate_Side.grid(column=0, row=10, sticky="W")
lbl_PreGenerate_SC = Label(window, text="")
lbl_PreGenerate_SC.grid(column=0, row=11, sticky="W")
lbl_PreGenerate_DateStart = Label(window, text="")
lbl_PreGenerate_DateStart.grid(column=0, row=12, sticky="W")
lbl_PreGenerate_DateEnd = Label(window, text="")
lbl_PreGenerate_DateEnd.grid(column=0, row=13, sticky="W")



def messageerror():
    flag=1
    if (selected_SideS.get()==False and selected_SideG.get()==False):
        messagebox.showerror('error', 'NO side choice')
        flag=0
    if (flag==1 and combo_CDA.get()==''):
        messagebox.showerror('error', 'NO Antenna choice')
        flag=0
    if (flag==1 and combo_SC.get()==''):
        messagebox.showerror('error', 'NO S/C choice')
        flag=0
    if (flag==1 and DataStart.get()==''):
        messagebox.showerror('error', 'NO Data Start choice')
        flag=0
    if (flag==1 and len(DataStart.get())!=19):
        messagebox.showerror('error', 'Data Start format')
        flag=0
    if (flag==1 and DataEnd.get()==''):
        messagebox.showerror('error', 'NO Data End choice')
        flag=0
    if (flag==1 and len(DataEnd.get())!=19):
        messagebox.showerror('error', 'Data Start format')
        flag=0
    if (flag==1 and selected_filePDF.get()==False and selected_filecsv.get()==False):
        messagebox.showerror('error', 'NO file choice')
        flag=0
    return flag

def msg_wimpyerror(error_line, wimpy_path):
    flag_wimpyerror = 1
    if ( error_line != 0 ):
        messagebox.showerror('wimpy error', 'possible event inversion in the wimpy file: '+wimpy_path+'. please check line: '+str(error_line)+' and correct it' )
        
        flag_wimpyerror=0
    return flag_wimpyerror

def clicked_PreGenerate():
    flag = messageerror()  
        
    if (flag==1):
        if (selected_SideS.get()==True and selected_SideG.get()==True):
            res_PreGenerate_Side = "Side: SpaCon & GrndCon"
        elif (selected_SideS.get()==True):
            res_PreGenerate_Side = "Side: SpaCon"
        elif (selected_SideG.get()==True):
            res_PreGenerate_Side = "Side: GrndCon"
        else:
            res_PreGenerate_Side = "Side: "
        lbl_PreGenerate_Side.configure(text= res_PreGenerate_Side)
        res_PreGenerate_SC = "S/C: " + combo_SC.get()
        lbl_PreGenerate_SC.configure(text= res_PreGenerate_SC)
        res_PreGenerate_DateStart = "Date Start: " + txt_DataStart.get()
        lbl_PreGenerate_DateStart.configure(text= res_PreGenerate_DateStart)
        
        DS=datetime.datetime.strptime(DataStart.get(), '%Y-%m-%d %H:%M:%S')
        DE=datetime.datetime.strptime(DataEnd.get(), '%Y-%m-%d %H:%M:%S')
        
        if (DE<DS):
            messagebox.showerror('error', 'Date end greater than start one')
        else:
            res_PreGenerate_DateEnd = "Date End: " + txt_DataEnd.get()
            lbl_PreGenerate_DateEnd.configure(text= res_PreGenerate_DateEnd)    

#btn_PreGenerate = Button(window, text="Pre-Generate", command=clicked_PreGenerate)
#btn_PreGenerate.grid(column=1, row=8)

def Click_Gen_Pdf(SC,PassM_36h):
    if (selected_SideS.get()==True and selected_SideG.get()==True):
        fileName_SpaGrndCon = 'SpaGrndCon_Wimpy_'+SC+'.pdf'
        fcn_WimpySpaGrndConpdf(fileName_SpaGrndCon,PassM_36h)
    elif (selected_SideS.get()==True):
        fileName_SpaCon = 'SpaCon_Wimpy_'+SC+'.pdf'
        fcn_WimpySpaConpdf(fileName_SpaCon,PassM_36h)
    elif (selected_SideG.get()==True):
        fileName_GrndCon = 'GrndCon_Wimpy_'+SC+'.pdf'
        fcn_WimpyGrndConpdf(fileName_GrndCon,PassM_36h)
        
        
def clicked_Generate():
    flag = messageerror()
    
    if (flag==1):
        if (selected_SideS.get()==True and selected_SideG.get()==True):
            res_PreGenerate_Side = "Side: SpaCon & GrndCon"
            SpaGrndCon=1
        elif (selected_SideS.get()==True):
            res_PreGenerate_Side = "Side: SpaCon"
            SpaGrndCon=2
        elif (selected_SideG.get()==True):
            res_PreGenerate_Side = "Side: GrndCon"
            SpaGrndCon=3
        else:
            res_PreGenerate_Side = "Side: "
        
        lbl_PreGenerate_Side.configure(text= res_PreGenerate_Side)
        res_PreGenerate_SC = "S/C: " + combo_SC.get()
        lbl_PreGenerate_SC.configure(text= res_PreGenerate_SC)
        res_PreGenerate_DateStart = "Date Start: " + txt_DataStart.get()
        lbl_PreGenerate_DateStart.configure(text= res_PreGenerate_DateStart)
        
        DS=datetime.datetime.strptime(DataStart.get(), '%Y-%m-%d %H:%M:%S')
        DE=datetime.datetime.strptime(DataEnd.get(), '%Y-%m-%d %H:%M:%S')
        
        flag_MSW = 0
        if (lbl_PreGenerate_DateStart_MSW.cget("text")!= "" and lbl_PreGenerate_DateStart_MSW.cget("text")!=""):
            DS_MSW=datetime.datetime.strptime(lbl_PreGenerate_DateStart_MSW.cget("text")[12:31], '%Y-%m-%d %H:%M:%S')
            DE_MSW=datetime.datetime.strptime(lbl_PreGenerate_DateEnd_MSW.cget("text")[10:29], '%Y-%m-%d %H:%M:%S')
            if (DE_MSW<DS_MSW):
                flag_MSW = 1
            MSW_info = [1,DS_MSW,DE_MSW]
        else:
            MSW_info = [0,0,0]
        
        if (DE<DS or flag_MSW==1):
            flag_DEDS_MSW = 0
            if (DE<DS):
                messagebox.showerror('error', 'Date end greater than start one')
                flag_DEDS_MSW = 1
            if (flag_DEDS_MSW==0 and flag_MSW==1):
                messagebox.showerror('error', 'Date end Mission Swap greater than start one')
        else:
            res_PreGenerate_DateEnd = "Date End: " + txt_DataEnd.get()
            lbl_PreGenerate_DateEnd.configure(text= res_PreGenerate_DateEnd)
            #Wfp='P:\\groups\\OPS\\EPS System Ops\\Wimpys'
            Wfp = 'files'
            #Wfp = 'C:\\Users\\matte\\Dropbox\\Job\\Wimpy\\files'
            TCHfp='H:\DesktopW10\MyDocument\wimpys'
            
            Wimpyfilepath1 = Wfp+'/wimpy_m01'
            Wimpyfilepath2 = Wfp+'/wimpy_m02'
            Wimpyfilepath3 = Wfp+'/wimpy_m03'
            Wimpyfilepath_N19 = Wfp+'/wimpy_n19'
            Wimpyfilepath_N18 = Wfp+'/wimpy_n18'
            
            Wfis_M01 = path.isfile(Wimpyfilepath1)
            Wfis_M02 = path.isfile(Wimpyfilepath2)
            Wfis_M03 = path.isfile(Wimpyfilepath3)
            Wfis_N19 = path.isfile(Wimpyfilepath_N19)
            Wfis_N18 = path.isfile(Wimpyfilepath_N18)
            
            CDAn=combo_CDA.get()
            
            if (Wfis_M01 == True):
                if (combo_SC.get()=='MetOp-B' or combo_SC.get()=='All MetOp'):
                    
                    TCHISTfilepath1 = TCHfp+'/M01TCHIST'
                    
                    FDF_Pass_MB, error_line_MB = fcn_Wimpy_Maga(DS, DE, Wimpyfilepath1,'MetOp-B',CDAn)
                    flag_wimpyerror = msg_wimpyerror(error_line_MB, Wimpyfilepath1)
                    
                    FDF_MPF_PassB, MPF_Pass_MB = fcn_MPF_mang(FDF_Pass_MB)
    #                TC_Pass_MB, draft = fcn_TCHIST_mang(FDF_MPF_PassB, TCHISTfilepath1)
                    
                    frames_FDF_B = [FDF_Pass_MB]
                    frames_MPF_B = [FDF_MPF_PassB]
                    FDF_MPFD_Pass = FDF_MPF_PassB
    #                frames_TC_B = [TC_Pass_MB]
                    frame_TC=frames_MPF_B
            
            if (Wfis_M02 == True):
                if (combo_SC.get()=='MetOp-A' or combo_SC.get()=='All MetOp'):
                    TCHISTfilepath2 = TCHfp+'/M02TCHIST'
                    
                    FDF_Pass_MA, error_line_MA = fcn_Wimpy_Maga(DS, DE, Wimpyfilepath2,'MetOp-A',CDAn)
                    flag_wimpyerror = msg_wimpyerror(error_line_MA, Wimpyfilepath2)
                    
                    FDF_MPF_PassA, MPF_Pass_MA = fcn_MPF_mang(FDF_Pass_MA)
    #                TC_Pass_MA, draft = fcn_TCHIST_mang(FDF_MPF_PassA, TCHISTfilepath2)
                    
                    
                    frames_FDF_A = [FDF_Pass_MA]
                    frames_MPF_A = [FDF_MPF_PassA]
                    FDF_MPFD_Pass = FDF_MPF_PassA
    #                frames_TC_A = [TC_Pass_MA]
                    
                    frame_TC=frames_MPF_A
            
            if (Wfis_M03 == True):
                if (combo_SC.get()=='MetOp-C' or combo_SC.get()=='All MetOp'):
                    TCHISTfilepath3 = TCHfp+'/M03TCHIST'
                    
                    FDF_Pass_MC, error_line_MC = fcn_Wimpy_Maga(DS, DE, Wimpyfilepath3,'MetOp-C',CDAn)
                    flag_wimpyerror = msg_wimpyerror(error_line_MC, Wimpyfilepath3)
                    
                    FDF_MPF_PassC, MPF_Pass_MC = fcn_MPF_mang(FDF_Pass_MC)
    #                TC_Pass_MC, draft = fcn_TCHIST_mang(FDF_MPF_PassC, TCHISTfilepath3)
                    
                    frames_FDF_C = [FDF_Pass_MC]
                    frames_MPF_C = [FDF_MPF_PassC]
                    FDF_MPFD_Pass = FDF_MPF_PassC
    #                frames_TC_C = [TC_Pass_MC]
                    frame_TC=frames_MPF_C
            
            if (CDAn[0:3]=='CDA'):
                CDAn_N = CDAn[0:3]
                if (CDAn[3:4]=='1'):
                    CDAn_N = CDAn_N+'2'
                else:
                    CDAn_N = CDAn_N+'1'
            else:
                CDAn_N = CDAn
            
            if (Wfis_N19 == True):
                if (combo_SC.get()=='N19' or selected_NOAA_BOS.get()==True):
                    
                    FDF_Pass_N19, error_line_N19 = fcn_Wimpy_N19_Maga(DS,DE,Wimpyfilepath_N19,'N19',CDAn_N)
                    flag_wimpyerror = msg_wimpyerror(error_line_N19, Wimpyfilepath_N19)
                    
                    FDF_MPF_Pass_N19, MPF_Pass_N19 = fcn_MPF_mang(FDF_Pass_N19)
                    
                    frames_FDF_N19 = [FDF_Pass_N19]
                    frames_MPF_N19 = [FDF_MPF_Pass_N19]
                    frame_TC=frames_MPF_N19
            
            if (Wfis_N18 == True):
                if (combo_SC.get()=='N18' or selected_NOAA_BOS.get()==True):
                    
                    FDF_Pass_N18, error_line_N18 = fcn_Wimpy_N19_Maga(DS,DE,Wimpyfilepath_N18,'N18',CDAn_N)
                    flag_wimpyerror = msg_wimpyerror(error_line_N18, Wimpyfilepath_N18)
                    
                    FDF_MPF_Pass_N18, MPF_Pass_N18 = fcn_MPF_mang(FDF_Pass_N18)
                    
                    frames_FDF_N18 = [FDF_Pass_N18]
                    frames_MPF_N18 = [FDF_MPF_Pass_N18]
                    frame_TC=frames_MPF_N18
            
            if ( flag_wimpyerror == 1 ):
                if (selected_NOAA_BOS.get()==True):
                    frames_N19_N18 = [FDF_MPF_Pass_N19, FDF_MPF_Pass_N18]
                    result = pd.concat(frames_N19_N18)
                    FDF_N = result.sort_values(by=['CDA_AOS'])
                    FDF_N = FDF_N.reset_index()
                    FDF_MPF_Pass_N19_N18 = FDF_N.drop(columns='index')
                    FDF_Pass_N19_N18, NOAA_Pass_shift = NOAA_BOS_shift(FDF_MPF_Pass_N19_N18, DS, DE)
                    
                    frames_FDF_N = [FDF_Pass_N19_N18]
                    frames_MPF_N = [FDF_Pass_N19_N18]
    #                frames_TC_N = [TC_Pass_N]
                    #frame_TC  = frames_MPF_N
                
                
                Global_frame_TC = []
                if ('frames_MPF_B' in locals()):
                    Global_frame_TC = Global_frame_TC + frames_MPF_B
                if ('frames_MPF_A' in locals()):
                    Global_frame_TC = Global_frame_TC + frames_MPF_A
                if ('frames_MPF_C' in locals()):
                    Global_frame_TC = Global_frame_TC + frames_MPF_C
                if ('frames_MPF_N' in locals()):
                    Global_frame_TC = Global_frame_TC + frames_MPF_N
                    
                
            
 #           if (selected_filecsv.get()==True):
 #               Click_Gen_Pdf(combo_SC.get(),TC_Pass_M)
                
                if (selected_filecsv.get()==True):      
                    if (combo_Shift.get()=='Morning'):
                        strShiftfilename = '(1)Morning'
                    elif (combo_Shift.get()=='Evening'):
                        strShiftfilename = '(2)Evening'
                    elif (combo_Shift.get()=='Night'):
                        strShiftfilename = '(3)Night'
                    
                    if (selected_Weekly.get()==True):
                        opts = 3
                    else:
                        opts = 2
                    
                    new_DS = DS
                    new_DE = DE
                    Dt = (DE-DS)
                    DT = Dt.days *(24*3600) + Dt.seconds + Dt.microseconds*1e-6
                    
                    def strShiftfilename_fromto(new_D):
                        D_yyyy=str(new_D.year)
                        D_mm=str(new_D.month)
                        if (new_D.month<10):
                           D_mm = '0'+D_mm 
                        D_dd=str(new_D.day)
                        if (new_D.day<10):
                           D_dd = '0'+D_dd
                        D_HH=str(new_D.hour)
                        if (new_D.hour<10):
                           D_HH = '0'+D_HH
                        D_MM=str(new_D.minute)
                        if (new_D.minute<10):
                           D_MM = '0'+D_MM
                        D_SS=str(new_D.second)
                        if (new_D.second<10):
                           D_SS = '0'+D_SS
                        strShiftfilename = D_yyyy+''+D_mm+''+D_dd+''+D_HH+''+D_MM+''+D_SS
                        return strShiftfilename
                        
                    
                    nfile = math.ceil( DT / (24*3600) )
                    for ifile in range(1,nfile+1):
                        
                        new_DS = DS + datetime.timedelta(hours = (ifile-1) * 24)
                        new_DE = DS + datetime.timedelta(hours = (ifile) * 24)
                        if ( new_DE >= DE ):
                            new_DE = DE
                        
                        strShiftfilename_from = strShiftfilename_fromto(new_DS)
                        strShiftfilename_to = strShiftfilename_fromto(new_DE)
                        
                        if (selected_SideS.get()==True and selected_SideG.get()==True):
                            strEPSSide = 'EPS_Combine'
                        elif (selected_SideS.get()==True):
                            strEPSSide = 'EPS_SpaCon'
                        elif (selected_SideG.get()==True):
                            strEPSSide = 'EPS_GrndCon'
                        strInfo = ''
                        if (combo_SC.get()=='All MetOp'):
                            strInfo = strInfo+'All_MetOp'
                        else:
                            strInfo = strInfo+combo_SC.get()
                        if (selected_NOAA_BOS.get()==True):
                            strInfo = strInfo+'_NOAA_BOS'
                        if (selected_Weekly.get()==True):
                            strInfo = strInfo+'_Weekly'
                        i_filename ='uberlogBatch_from_'+strShiftfilename_from+'_to_'+strShiftfilename_to+'_'+strEPSSide+'_'+strInfo
                        i_TC_Pass_M = mergeWimpy( Global_frame_TC, 1, new_DS, new_DE , MSW_info)
                        fcn_wimpy_csv( i_TC_Pass_M, i_filename, new_DS, new_DE, SpaGrndCon, opts )
                    
                
                
btn_Generate = Button(window, text="Generate", command=clicked_Generate)
btn_Generate.grid(column=0, row=8, columnspan = 5, sticky = tk.W+tk.E)







window.mainloop()






