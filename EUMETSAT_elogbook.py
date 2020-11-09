# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:58:22 2020

@author: Nicoli
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:23:55 2020

@author: matteo
"""
import os

import tkinter as tk
from tkinter import Frame, messagebox, scrolledtext 
from tkcalendar import Calendar, DateEntry

import math

import datetime
import calendar

from pandas import concat




from EPS_I_gen.wimpy_manager import *
from EPS_I_gen.wimpy_manager_N19 import *
#from py_support_files.wimpy_pdf import *
#from EPS_I_gen.wimpy_csv import *
from EPS_I_gen.wimpy_csv_2 import *
from EPS_I_gen.wimpy_XTTC_FBK import *
from EPS_I_gen.EPS_Shif_mag import *


from GEMS.GUI_GEMS import *
from MCS_OOL.GUI_MCS_OOL import *




class GUI_EUMETSAT(Frame):
    SW_title = "EUMETSAT e-logbook tool"
    SW_version = "1.4.1" # Initial release
    
    #
    OS_UserName = os.getlogin()
    UserName = OS_UserName
    
    OS_Sys_sep = '\\'
    DesktopPath = 'C:'+OS_Sys_sep+'Users'+OS_Sys_sep+''+OS_UserName+''+OS_Sys_sep+'Desktop'+OS_Sys_sep+''
    filePath='P:'+OS_Sys_sep+'groups'+OS_Sys_sep+'OPS'+OS_Sys_sep+'EPS System Ops'+OS_Sys_sep+''
    
    #
    now_UTC =datetime.datetime.utcnow()
    now_local =datetime.datetime.now()
    
# =============================================================================
#     UserName = 'DelMonte'
# =============================================================================
# =============================================================================
#     now_local =datetime.datetime(2020, 11, 9, 12, 0, 0, 0*1000)
#     now_UTC =datetime.datetime(now_local.year, now_local.month, now_local.day, now_local.hour, now_local.minute, now_local.second, now_local.microsecond*1000)-datetime.timedelta(hours=1)
# =============================================================================
    
    #filePath = 'files''+OS_Sys_sep+''
# =============================================================================
#     filePath = 'C:'+OS_Sys_sep+'Users'+OS_Sys_sep+'matte'+OS_Sys_sep+'Dropbox'+OS_Sys_sep+'Job'+OS_Sys_sep+'EUMETSAT'+OS_Sys_sep+'Project'+OS_Sys_sep+'Wimpy_Manager'+OS_Sys_sep+'files'+OS_Sys_sep
# =============================================================================
# =============================================================================
#     filePath = 'C:'+OS_Sys_sep+'Users'+OS_Sys_sep+'matte0'+OS_Sys_sep+'Dropbox'+OS_Sys_sep+'Job'+OS_Sys_sep+'EUMETSAT'+OS_Sys_sep+'Project'+OS_Sys_sep+'Wimpy_Manager'+OS_Sys_sep+'files'+OS_Sys_sep
# =============================================================================
    
    
    #
    nWeek=now_UTC.isocalendar()[1]
    
    
    
    def __init__(self):
        super().__init__()

        self.init_GUI()
    # end def
    
    
    
    
    
    
    
    
    
    
    
    def init_GUI(self):

        self.master.title(self.SW_title+" ("+self.SW_version+")")
        #self.master.iconbitmap('')
        
        #=========================================================================================================================================
        # Creating Menubar 
        
        # 
# =============================================================================
#         self.btn_GEMS_Manager = tk.ttk.Button(self.master, text = "GEMS", width=20, command = lambda: self.btn_GEMS_Mang())
#         self.btn_GEMS_Manager.pack(side="top", padx=20, pady=20)
#         
#         
#         self.btn_GEMS_Manager = tk.ttk.Button(self.master, text = "MCS", width=20, command = lambda: self.btn_MCS_OLL())
#         self.btn_GEMS_Manager.pack(side="top", padx=20, pady=20)
# =============================================================================
        
        
        menubar = tk.Menu(self.master) 
        self.master.config(menu=menubar)
        
        # Adding File Menu and commands 
        file = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='File', menu = file)
        #=====================================================================
        file.add_command(label ='New File', command = None)
        file.add_command(label ='Open...', command = None)
        file.add_command(label ='Save as', command = None)
        file.add_separator()
        file.add_command(label ='Exit', command = self.onExit)
          
        # Adding Edit Menu and commands 
        edit = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Edit', menu = edit)
        #=====================================================================
        edit.add_command(label ='Cut', command = None)
        edit.add_command(label ='Copy', command = None)
        edit.add_command(label ='Paste', command = None)
        edit.add_command(label ='Select All', command = None)
        edit.add_separator()
        edit.add_command(label ='Find...', command = None)
        edit.add_command(label ='Find again', command = None)
          
        # Adding Help Menu 
        help_ = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Help', menu = help_)
        #=====================================================================
        help_.add_command(label ='Tk Help', command = None)
        help_.add_command(label ='Demo', command = None)
        help_.add_separator()
        help_.add_command(label ='About '+self.SW_title, command=self.HelpInfo)
        
        
        
        
        #=========================================================================================================================================
        self.Mission = tk.StringVar(value="Choose Mission")
        self.menubutton_Mission = tk.Menubutton(self.master, textvariable=self.Mission, indicatoron=True, borderwidth=1, relief="raised", width=20)
        self.menu_Mission = tk.Menu(self.menubutton_Mission, tearoff=False)
        self.menubutton_Mission.configure(menu=self.menu_Mission)
        
        self.Mission_list = [['EPS',["EPS I gen.",'EPS_I'],["EPS II gen.",'EPS_II']],['Sentinel',["Sentinel 3",'Sentinel_3'],["Sentinel 6",'Sentinel_6']]]
        for item in (("EPS", "EPS I gen.", "EPS II gen."),
                     ("Sentinel", "Sentinel 3", "Sentinel 6")):
            self.menu_M = tk.Menu(self.menu_Mission, tearoff=False)
            self.menu_Mission.add_cascade(label=item[0], menu=self.menu_M)
            for value_item in item[1:]:
                self.menu_M.add_radiobutton(value=value_item, label=value_item, variable=self.Mission, command = lambda: self.ChooseMission() )
            # end for
        # end for
        #self.menubutton_Mission.pack(side="top")
        self.menubutton_Mission.pack(side="top", padx=20, pady=20)

# =============================================================================
#         time.sleep(1)
#         self.Mission.set("EPS I gen.")
#         self.ChooseMission()
# =============================================================================
        
    # end def
    
    
    
    
    
    
    
    
    
    
    
    def btn_GEMS_Mang(self):
        self.Destroy_All()
        self.Mission.set("Choose Mission")
        self = Layout_GEMS_Mang(self)
    # end def

    
    def btn_MCS_OLL(self):
        self.Destroy_All()
        self.Mission.set("Choose Mission")
        self = Layout_MCS_OOL(self)
    # end def
    
    
    
    
    
    
    
    
    
    
    def ChooseMission(self):
        self.Destroy_All()
        Mission = self.Mission.get()
        if ( Mission == "EPS I gen." ):
            #self.ToolChoice_EPS_I()
            self.e_logbook_EPS_I()
            
        elif ( Mission == "EPS II gen." ):
            self.Destroy_EPS_I()
            self.Layout_not_ready()
        elif ( Mission == "Sentinel 3" ):
            self.Destroy_EPS_I()
            self.Layout_not_ready()
        elif ( Mission == "Sentinel 6" ):
            self.Destroy_EPS_I()
            self.Layout_not_ready()
        # end if
    # end def
    
    
    
    
    
    
    
    
    
    
    
    def Destroy_All(self):
        self.Destroy_EPS_I()
        self.Destroy_not_ready()
        self = Destroy_GEMS_Manager(self)
        self = Destroy_MCS_OOL(self)
    # end def
    
    
    
    
    
    
    
    
    
    
    
    def Destroy_EPS_I(self):
        if (hasattr(self, 'PW_EPS_I_Layout_title') == True):
                self.PW_EPS_I_Layout_title.destroy()
        # end if
        if (hasattr(self, 'PW_EPS_I_Layout') == True):
                self.PW_EPS_I_Layout.destroy()
        # end if
        if (hasattr(self, 'PW_EPS_I_Gen') == True):
            self.PW_EPS_I_Gen.destroy()
        # end if
        if (hasattr(self, 'PW_EPS_I_Summary_title') == True):
            self.PW_EPS_I_Summary_title.destroy()
        # end if
        if (hasattr(self, 'PW_EPS_I_Summary') == True):
            self.PW_EPS_I_Summary.destroy()
        # end if
        if (hasattr(self, 'PW_EPS_I_LogWin') == True):
            self.PW_EPS_I_LogWin.destroy()
        # end if
        if (hasattr(self, 'PW_EPS_I_ToolChoice') == True):
            self.PW_EPS_I_ToolChoice.destroy()
        # end if
    # end def
    
    
    
    
    
    
    
    
    
    
    
    def Destroy_not_ready(self):
        if (hasattr(self, 'PW_not_readyn') == True):
            self.PW_not_readyn.destroy()
        # end if
    # end def
    
    
    
    
    
    
    
    
    
    
    
    def Layout_not_ready(self):
        self.PW_not_readyn = tk.PanedWindow(self.master, orient = 'vertical')
        self.PW_not_readyn.pack(fill = tk.X )
        
        btn_PW_not_readyn = tk.Label(self.PW_not_readyn, text = "The Tool for this particular mission is not ready yet")
        btn_PW_not_readyn.pack(fill = tk.X)
    # end def
    
    
    
    
    
    
    
    
    
    
    
    def ToolChoice_EPS_I(self):
        self.PW_EPS_I_ToolChoice = tk.PanedWindow(self.master, orient = 'vertical')
        self.PW_EPS_I_ToolChoice.pack(fill = tk.X )
        
        btn_EPS_I_elogbook = tk.ttk.Button(self.PW_EPS_I_ToolChoice, text = "e-logbook", width=20, command = lambda: self.e_logbook_EPS_I())
        btn_EPS_I_elogbook.pack(side="top", padx=20, pady=20)
        
        btn_EPS_I_ShiftPlan = tk.ttk.Button(self.PW_EPS_I_ToolChoice, text = "Shift Plan", width=20, command = None)
        btn_EPS_I_ShiftPlan.pack(side="top", padx=20, pady=20)
    # end def
    
    def e_logbook_EPS_I(self):
        if (hasattr(self, 'PW_EPS_I_ToolChoice') == True):
            self.PW_EPS_I_ToolChoice.destroy()
        # end if
        self.EPS_I_logEvents = []
        
        self.Data_EPS_I()
        self.Layout_EPS_I()
        self.Generate_EPS_I()
        self.LogWin_EPS_I()
    # end def
    
    def Data_EPS_I(self):
        
        # creating tkinter window 
        PW_EPS_I_Loadingbar = tk.PanedWindow(self.master, orient = 'vertical')
        PW_EPS_I_Loadingbar.pack(fill = tk.X )
        
        
        Style_EPS_I_DataLoadingbar = tk.ttk.Style(self.master)
        Style_EPS_I_DataLoadingbar.layout('text.Horizontal.TProgressbar', 
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}), 
              ('Horizontal.Progressbar.label', {'sticky': ''})])
        
        lbl_EPS_I_Loadingbar = tk.Label(PW_EPS_I_Loadingbar, text="The data acquisition process will take a few moments (no more than 2 min)")
        lbl_EPS_I_Loadingbar.pack()
        ProgressBar_EPS_I_Loadingbar = tk.ttk.Progressbar(PW_EPS_I_Loadingbar, orient = "horizontal", length = 500, mode = 'determinate', style="text.Horizontal.TProgressbar")
        ProgressBar_EPS_I_Loadingbar.pack(pady = 10)
        # Function responsible for the updation 
        # of the progress bar value 
        
        self.LogWin_EPS_I()
        
        
        proges_per100 = 0
        ProgressBar_EPS_I_Loadingbar['value'] = int(proges_per100)
        #lbl_EPS_I_Loadingbar.configure(text= "The data acquisition process will take a few moments (no more than 2 min), Loading ("+str(proges_per100)+"%) [EPS Shift Plan]")
        Style_EPS_I_DataLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [Path file] ('+str(proges_per100)+'%)')
        PW_EPS_I_Loadingbar.update_idletasks()
        
        
        #
        filePath = self.filePath
        OS_Sys_sep = self.OS_Sys_sep
        
        #
        filePath_OpsSup = filePath+'Ops Support file'+OS_Sys_sep+''
        fileName = 'Path_List.txt'
        filePathNamePath_List = filePath_OpsSup + fileName
        
        Path_List=[]
        if (os.path.isfile(filePathNamePath_List) == True):
            fp=open(filePathNamePath_List,'r')
            Path_List=fp.readlines()
            fp.close()
        else:
            for i_Path in range(0,8):
                Path_List.append('')
        
        #
        filePath_Shift = Path_List[0][:-1]
        fileName_Shift = 'EPS Shift List '+str(self.now_UTC.year)+'.xlsm'
        file_Path_Name_Shift = filePath_Shift+fileName_Shift
        
        #
        filePath_Controller = Path_List[0][:-1]
        fileName_Controller = 'Controllers_Users.csv'
        file_Path_Name_Controller = filePath_Controller+fileName_Controller
        
        #
        filePath_OpsSch = filePath
        file_Path_OpsSch = Path_List[1][:-1]
        file_Name_OpsSch = 'Operations Weekly Schedule ('+str(self.now_UTC.year)+').xlsm'
        file_Path_Name_OpsSch = [file_Path_OpsSch,file_Path_OpsSch+file_Name_OpsSch]
        
        #
        filePath_MS = Path_List[3][:-1]
        fileName_MS = 'Mission Swap Schedule.xlsx'
        file_Path_Name_MS = filePath_MS+fileName_MS
        
        #
        filePath_MPF_PGF = Path_List[4][:-1]
        fileName_MPF_PGF = 'PGFDumpSynchSchedule_e_D335_00h30_D344_00h00__01.mpf'
        file_Path_Name_MPF_PGF  = filePath_MPF_PGF+fileName_MPF_PGF
        
        #
        filePath_iCDA = Path_List[5][:-1]
        fileName_iCDA = 'Main_CDA.txt'
        file_Path_Name_iCDA  = filePath_iCDA+fileName_iCDA
        
        #
        filePath_Wimpy = Path_List[6][:-1]
        filePath_TCHIST = filePath+'TCHIST'+OS_Sys_sep+''
        
        self.EPS_I_SC = [['B',int(1)],['A',int(2)],['C',int(3)]]
        filePathName_Wimpy_List =[]
        filePathName_TCHIST_List =[]
        for i_SC in range(0,len(self.EPS_I_SC)):
            file_Path_Name_Wimpy = filePath_Wimpy+'wimpy_m0'+str(int(self.EPS_I_SC[i_SC][1]))
            file_Path_Name_TCHIST = filePath_TCHIST+'M0'+str(int(self.EPS_I_SC[i_SC][1]))+'TCHIST'
            filePathName_Wimpy_List.append(file_Path_Name_Wimpy)
            filePathName_TCHIST_List.append(file_Path_Name_TCHIST)
        # end for
        
        filePath_NOAA_week_OLD = filePath_OpsSup+'NOAA_BOS.csv'
        file_Path_Name_Wimpy_N19 = filePath_Wimpy+'wimpy_n19'
        file_Path_Name_Wimpy_N18 = filePath_Wimpy+'wimpy_n18'
        
        self.file_dir_EPS_I = [file_Path_Name_Shift, file_Path_Name_Controller, file_Path_Name_OpsSch, file_Path_Name_MS, file_Path_Name_MPF_PGF, file_Path_Name_iCDA, filePathName_Wimpy_List, filePathName_TCHIST_List, filePath_NOAA_week_OLD, file_Path_Name_Wimpy_N19, file_Path_Name_Wimpy_N18 ]
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'Path file loaded successfully', True )
        
        
        proges_per100 = 5
        ProgressBar_EPS_I_Loadingbar['value'] = int(proges_per100)
        #lbl_EPS_I_Loadingbar.configure(text= "The data acquisition process will take a few moments (no more than 2 min), Loading ("+str(proges_per100)+"%) [EPS Shift Plan]")
        Style_EPS_I_DataLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [EPS Shift Plan] ('+str(proges_per100)+'%)')
        PW_EPS_I_Loadingbar.update_idletasks()
        
        self.EPS_I_ShiftSide = [0,0,'Controller']
        self.EPS_I_Controller_XTTC_PreBrief=[0,0,0]
        if (os.path.isfile(self.file_dir_EPS_I[0]) and os.path.isfile(self.file_dir_EPS_I[1])):
            now_local_HH = self.now_local.hour
            if (now_local_HH<5):
                now_local2 = datetime.datetime(self.now_local.year, self.now_local.month, self.now_local.day, now_local_HH, self.now_local.minute, self.now_local.second, 0*1000)-datetime.timedelta(hours=24)
            else:
                now_local2 = self.now_local
            # end if
            self.EPS_I_ShiftSide, self.EPS_I_Controller_XTTC_PreBrief, self.Controllers = EPS_Shift_List_Rec(now_local2, self.UserName, self.file_dir_EPS_I[0], self.file_dir_EPS_I[1])
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'EPS Shift Plan loaded successfully', True )
        else:
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'EPS Shift Plan NOT loaded', True )
        # end if
        
        
        proges_per100 = 20
        ProgressBar_EPS_I_Loadingbar['value'] = int(proges_per100)
        Style_EPS_I_DataLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [EPS Weekly Schedule] ('+str(proges_per100)+'%)')
        #lbl_EPS_I_Loadingbar.configure(text= "The data acquisition process will take a few moments (no more than 2 min), Loading ("+str(proges_per100)+"%) [EPS Weekly Schedule]")
        PW_EPS_I_Loadingbar.update_idletasks()
        
        self.EPS_I_Dates_MS=[]
        self.EPS_XTTC=[]
        if (os.path.isfile(self.file_dir_EPS_I[2][1])):
            1
            self.EPS_I_Dates_MS, self.EPS_I_XTTC, self.EPS_I_Manouver = OpsSch_Schedule(self.file_dir_EPS_I[2][1], self.EPS_I_SC)
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'EPS Weekly Schedule loaded successfully', True )
        else:
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'EPS Weekly Schedule NOT loaded', True )
        # end if
        
        proges_per100 = 45
        ProgressBar_EPS_I_Loadingbar['value'] = int(proges_per100)
        Style_EPS_I_DataLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [Manual Mission Swap Schedule] ('+str(proges_per100)+'%)')
        #lbl_EPS_I_Loadingbar.configure(text= "The data acquisition process will take a few moments (no more than 2 min), Loading ("+str(proges_per100)+"%) [MPF PGF Schedule]")
        PW_EPS_I_Loadingbar.update_idletasks()
        
        
        self.MS_Scheduled = []
        if (os.path.isfile(file_Path_Name_MS)):
            self.MS_Scheduled = EPS_MS_Scheduled(file_Path_Name_MS)
        
        proges_per100 = 70
        ProgressBar_EPS_I_Loadingbar['value'] = int(proges_per100)
        Style_EPS_I_DataLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [MPF PGF Schedule] ('+str(proges_per100)+'%)')
        #lbl_EPS_I_Loadingbar.configure(text= "The data acquisition process will take a few moments (no more than 2 min), Loading ("+str(proges_per100)+"%) [MPF PGF Schedule]")
        PW_EPS_I_Loadingbar.update_idletasks()
        
        
        self.EPS_I_PGFDSS = [0,0]
        if (os.path.isfile(self.file_dir_EPS_I[4])):
            #PGFDumpSynchSchedule = MPF_PGFDumpSynchSchedule(MPF_PGFfilepath)
            #PGFDSS = [1,PGFDumpSynchSchedule]
            self.EPS_I_PGFDSS = [0,0]
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'MPF PGF Schedule loaded successfully', True )
        else:
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'MPF PGF Schedule NOT loaded', True )
        # end if
        
        proges_per100 = 100
        ProgressBar_EPS_I_Loadingbar['value'] = int(proges_per100)
        Style_EPS_I_DataLoadingbar.configure("text.Horizontal.TProgressbar", text='Data loading [End] ('+str(proges_per100)+'%)')
        #lbl_EPS_I_Loadingbar.configure(text= "The data acquisition process will take a few moments (no more than 2 min), Loading ("+str(proges_per100)+"%), End")
        PW_EPS_I_Loadingbar.update_idletasks()
        
        
        Style_EPS_I_DataLoadingbar.configure("text.Horizontal.TProgressbar", text='')
        PW_EPS_I_Loadingbar.destroy()
        if (hasattr(self, 'PW_EPS_I_LogWin') == True):
            self.PW_EPS_I_LogWin.destroy()
        # end if
    # end def
    
    def Layout_EPS_I(self):
        #
        self.PW_EPS_I_Layout_title = tk.PanedWindow(self.master, orient = 'vertical')
        self.PW_EPS_I_Layout_title.pack(fill = tk.X )
        
        #
        self.PW_EPS_I_Layout = tk.PanedWindow(self.master, orient = 'vertical')
        self.PW_EPS_I_Layout.pack(fill = tk.X )
        
        
        self.Summary_EPS_I()
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = 0
        i_column_PW_EPS_I_Layout = 0
        
        lbl_Side = tk.Label(self.PW_EPS_I_Layout, text="Controller Side")
        lbl_Side.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.selected_EPS_I_SideS = tk.BooleanVar()
        self.selected_EPS_I_SideS.set(False)
        if (self.EPS_I_ShiftSide[1]=='S' or self.EPS_I_ShiftSide[1]=='SG'):
            self.selected_EPS_I_SideS.set(True)
        # end if
        chk_SideContrS = tk.ttk.Checkbutton(self.PW_EPS_I_Layout, text='SpaCon', var=self.selected_EPS_I_SideS, command = lambda: self.Summary_EPS_I_Side(True) )
        chk_SideContrS.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.selected_EPS_I_SideG = tk.BooleanVar()
        self.selected_EPS_I_SideG.set(False)
        if (self.EPS_I_ShiftSide[1]=='G' or self.EPS_I_ShiftSide[1]=='SG'):
            self.selected_EPS_I_SideG.set(True)
        # end if
        chk_SideContrG = tk.ttk.Checkbutton(self.PW_EPS_I_Layout, text='GrndCon', var=self.selected_EPS_I_SideG, command = lambda: self.Summary_EPS_I_Side(True) )
        chk_SideContrG.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.selected_EPS_I_SHO = tk.BooleanVar()
        self.selected_EPS_I_SHO.set(True) #set check state
        chk_SHO = tk.ttk.Checkbutton(self.PW_EPS_I_Layout, text='SHO', var=self.selected_EPS_I_SHO)
        chk_SHO.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        
# =============================================================================
#         self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'Controller Side loaded', False )
# =============================================================================
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = i_row_PW_EPS_I_Layout + 1
        i_column_PW_EPS_I_Layout = 0
        
        lbl_Shift = tk.Label(self.PW_EPS_I_Layout, text="MetOp Antenna")
        lbl_Shift.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        CDA_cur = 0
        if (self.EPS_I_PGFDSS[0]==1):
            CDA_cur=1
        else:
            if (os.path.isfile(self.file_dir_EPS_I[5])==True):
                fp=open(self.file_dir_EPS_I[5],'r')
                lines=fp.readlines()
                fp.close()
                if ( len(lines)==1 ): 
                    if ( (lines[0]=='1' or lines[0]=='2' ) ):
                        CDA_cur = int(lines[0])+1
                    # end if
                # end if
            # end if
        # end if
        self.SVL_Antenna_List = ['CDA1', 'CDA2']
        self.MPF_Antenna_List = ['AUTO']+self.SVL_Antenna_List
        self.XTTC_Antenna_List = ['KOU', 'VL1', 'MAS']
        self.NOAA_Anetnna_List = ['FBK', 'WAL']
        self.Sup_Antenna_List = self.XTTC_Antenna_List + self.NOAA_Anetnna_List
        self.Antenna_List = self.MPF_Antenna_List+self.Sup_Antenna_List
        
        EPS_I_CDA_List = [''] + self.Antenna_List
        self.combo_EPS_I_CDA = tk.ttk.Combobox(self.PW_EPS_I_Layout, state="readonly", width=17, values=EPS_I_CDA_List )
        self.combo_EPS_I_CDA.bind("<<ComboboxSelected>>", self.Summary_EPS_I_Antenna )
        self.combo_EPS_I_CDA.current(CDA_cur) #set the selected item
        self.combo_EPS_I_CDA.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        btn_EPS_I_MissSwap = tk.ttk.Button(self.PW_EPS_I_Layout, width=12, text="Mission Swap", command = lambda: self.Summary_EPS_I_MissionSwap())
        btn_EPS_I_MissSwap.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'MetOp antenna setted', False )
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = i_row_PW_EPS_I_Layout + 1
        i_column_PW_EPS_I_Layout = 0
        
        self.lbl_EPS_I_SC = tk.Label(self.PW_EPS_I_Layout, text="S/C")
        self.lbl_EPS_I_SC.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.MetOp_List = []
        for i_SC in range(0,len(self.EPS_I_SC)):
            self.MetOp_List.append('MetOp-'+self.EPS_I_SC[i_SC][0])
        # end for
        SC_list = ['', 'All MetOp']+self.MetOp_List+[ 'N19', 'N18']
        self.combo_EPS_I_SC = tk.ttk.Combobox(self.PW_EPS_I_Layout, state="readonly", width=17, values=SC_list)
        self.combo_EPS_I_SC.bind("<<ComboboxSelected>>", self.Summary_EPS_I_SC )
        self.combo_EPS_I_SC.current(1) #set the selected item
        self.combo_EPS_I_SC.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        btn_EPS_I_Manoeuvre = tk.ttk.Button(self.PW_EPS_I_Layout, width=12, text="Manoeuvre", command = lambda: self.Summary_EPS_I_Manoeuvre())
        btn_EPS_I_Manoeuvre.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'S/C setted', False )
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = i_row_PW_EPS_I_Layout + 1
        i_column_PW_EPS_I_Layout = 1
        
        self.selected_EPS_I_NOAA_BOS = tk.BooleanVar()
        self.selected_EPS_I_NOAA_BOS.set(True) #set check state
        chk_NOAA_BOS = tk.ttk.Checkbutton(self.PW_EPS_I_Layout, text='NOAA BOS', var=self.selected_EPS_I_NOAA_BOS)
        chk_NOAA_BOS.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.selected_EPS_I_Weekly = tk.BooleanVar()
        self.selected_EPS_I_Weekly.set(True) #set check state
        chk_Weekly = tk.ttk.Checkbutton(self.PW_EPS_I_Layout, text='Daily Events', var=self.selected_EPS_I_Weekly)
        chk_Weekly.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        btn_EPS_I_XTTCFBK = tk.ttk.Button(self.PW_EPS_I_Layout, width=12, text="XTTC or FBK", command = lambda: self.Summary_EPS_I_XTTCFBK())
        btn_EPS_I_XTTCFBK.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        
        
# =============================================================================
#         self.XTTCFBK = tk.StringVar(value="XTTC or FBK")
#         self.menubutton_XTTCFBK = tk.Menubutton(PW1, textvariable=self.XTTCFBK, indicatoron=True, borderwidth=1, relief="raised", width=20)
#         self.menu_Mission = tk.Menu(self.menubutton_XTTCFBK, tearoff=False)
#         self.menubutton_XTTCFBK.configure(menu=self.menu_Mission)
#         
#         for item in (("Standard support"),
#                      ("pre-pass briefing")):
#             self.menu_M = tk.Menu(self.menu_Mission, tearoff=False)
#             self.menu_Mission.add_cascade(label=item[0], menu=self.menu_M)
#             for value_item in item[1:]:
#                 self.menu_M.add_radiobutton(value=value_item, label=value_item, variable=self.XTTCFBK, command = lambda: self.ChooseMission() )
#             # end for
#         # end for
#         self.menubutton_XTTCFBK.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
# =============================================================================
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = i_row_PW_EPS_I_Layout + 1
        i_column_PW_EPS_I_Layout = 0
        
        lbl_Shift = tk.Label(self.PW_EPS_I_Layout, text="Shift")
        lbl_Shift.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        Shift_List = ["Morning","Evening","Night"]
        self.combo_EPS_I_Shift = tk.ttk.Combobox(self.PW_EPS_I_Layout, state="readonly", width=17, values=Shift_List)
        self.combo_EPS_I_Shift.bind("<<ComboboxSelected>>", self.Summary_EPS_I_Shift )
        if (self.EPS_I_ShiftSide[0] != 0):
            self.combo_EPS_I_Shift.current(self.EPS_I_ShiftSide[0]-1)
        else:
            if (self.now_local.hour>=6  and self.now_local.hour<12):
                self.combo_EPS_I_Shift.current(0) #set the selected item
            elif (self.now_local.hour>=12  and self.now_local.hour<20):
                self.combo_EPS_I_Shift.current(1) #set the selected item
            else:
                self.combo_EPS_I_Shift.current(2) #set the selected item
            # end if
        # end if
        self.combo_EPS_I_Shift.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
# =============================================================================
#         i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
#         btn_EPS_I_Shift = tk.ttk.Button(self.PW_EPS_I_Layout, text="Update")
#         btn_EPS_I_Shift.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
# =============================================================================
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'Shift setted', False )

        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = i_row_PW_EPS_I_Layout + 1
        i_column_PW_EPS_I_Layout = 0
        
        self.strv_EPS_I_flagDataStart = False
        self.strv_EPS_I_DataStart = tk.StringVar()
        lbl_EPS_I_DataStart = tk.Label(self.PW_EPS_I_Layout, text="Date Start: YYYY-MM-DD hh:mm:ss [UTC]")
        lbl_EPS_I_DataStart.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.entry_EPS_I_DataStart = tk.Entry(self.PW_EPS_I_Layout, width=20, textvariable=self.strv_EPS_I_DataStart, validate="focusout", validatecommand=self.Summary_EPS_I_UpadateDataStart)
        self.entry_EPS_I_DataStart.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        btn_EPS_I_DataStartCalendar = tk.ttk.Button(self.PW_EPS_I_Layout, width=12, text="Calendar", command = lambda: self.Summary_EPS_I_CalendarDateStart() )
        btn_EPS_I_DataStartCalendar.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = i_row_PW_EPS_I_Layout + 1
        i_column_PW_EPS_I_Layout = 0
        
        self.strv_EPS_I_flagDataEnd = False
        self.strv_EPS_I_DataEnd = tk.StringVar()
        lbl_EPS_I_DataEnd = tk.Label(self.PW_EPS_I_Layout, text="Date End: YYYY-MM-DD hh:mm:ss [UTC]")
        lbl_EPS_I_DataEnd.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.entry_EPS_I_DataEnd = tk.Entry(self.PW_EPS_I_Layout, width=20, textvariable=self.strv_EPS_I_DataEnd, validate="focusout", validatecommand=self.Summary_EPS_I_UpadateDataEnd)
        self.entry_EPS_I_DataEnd.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        btn_EPS_I_DataEndCalendar = tk.ttk.Button(self.PW_EPS_I_Layout, width=12, text="Calendar", command = lambda: self.Summary_EPS_I_CalendarDateEnd() )
        btn_EPS_I_DataEndCalendar.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Layout = i_row_PW_EPS_I_Layout + 1
        i_column_PW_EPS_I_Layout = 0
        
        lbl_file = tk.Label(self.PW_EPS_I_Layout, text="File format")
        lbl_file.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout, sticky="W")
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.selected_EPS_I_filecsv = tk.BooleanVar()
        self.selected_EPS_I_filecsv.set(True) #set check state
        chk_SideContrG = tk.ttk.Checkbutton(self.PW_EPS_I_Layout, text='Uberlog (.csv)', var=self.selected_EPS_I_filecsv)
        chk_SideContrG.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        
        i_column_PW_EPS_I_Layout = i_column_PW_EPS_I_Layout + 1
        self.selected_EPS_I_fileXTTCPDF = tk.BooleanVar()
        self.selected_EPS_I_fileXTTCPDF.set(False) #set check state
        self.chk_EPS_I_fileXTTCPDF = tk.ttk.Checkbutton(self.PW_EPS_I_Layout, text='XTTC & FBK (.pdf)', var=self.selected_EPS_I_fileXTTCPDF, command = lambda: self.Summary_EPS_I_XTTC_PreBrief())
        self.chk_EPS_I_fileXTTCPDF.grid(row=i_row_PW_EPS_I_Layout, column=i_column_PW_EPS_I_Layout)
        self.chk_EPS_I_fileXTTCPDF.config(state=tk.DISABLED)

        if (self.EPS_I_Controller_XTTC_PreBrief[0]==1):
            self.chk_EPS_I_fileXTTCPDF.config(state=tk.NORMAL)
            if (self.EPS_I_Controller_XTTC_PreBrief[1]==1):
                self.selected_EPS_I_fileXTTCPDF.set(True)
        # end if
        
        
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, 'file format setted', False )
        
        
        #=========================================================================================================================================
        if (self.combo_EPS_I_Shift.get()=='Morning'):
            lbl_Side = tk.Label(self.PW_EPS_I_Layout_title, text='Goooood '+self.combo_EPS_I_Shift.get()+' '+self.EPS_I_ShiftSide[2]+'!, have a nice shift :)')
        else:
            lbl_Side = tk.Label(self.PW_EPS_I_Layout_title, text='Hi '+self.EPS_I_ShiftSide[2]+'!, have a nice '+self.combo_EPS_I_Shift.get()+' shift :)')
        lbl_Side.pack()
        
        
        #=========================================================================================================================================
        self.Summary_EPS_I_Side(False)
        self.Summary_EPS_I_Antenna(1 )
        self.Summary_EPS_I_SC(1 )
        self.Summary_EPS_I_Shift(1 )
    # end def
    
    def Generate_EPS_I(self):
        #
        self.PW_EPS_I_Gen = tk.PanedWindow(self.master, orient = 'vertical')
        self.PW_EPS_I_Gen.pack(fill = tk.X )
        
        btn_EPS_I_Gen = tk.ttk.Button(self.PW_EPS_I_Gen, text = "Generate", command = lambda: self.btn_EPS_I_Generate())
        btn_EPS_I_Gen.pack(fill = tk.X)
        
        self.Style_EPS_I_DataGenLoadingbar = tk.ttk.Style(self.PW_EPS_I_Gen)
        self.Style_EPS_I_DataGenLoadingbar.layout('text.Horizontal.TProgressbar', 
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}), 
              ('Horizontal.Progressbar.label', {'sticky': ''})])
        
        self.ProgressBar_EPS_I_DataGenLoadingbar = tk.ttk.Progressbar(self.PW_EPS_I_Gen, orient = "horizontal", length = 500, mode = 'determinate', style="text.Horizontal.TProgressbar")
        self.ProgressBar_EPS_I_DataGenLoadingbar.pack()
    # end def
    
    def Summary_EPS_I(self):
        #
        self.PW_EPS_I_Summary_title = tk.PanedWindow(self.master, orient = 'vertical')
        self.PW_EPS_I_Summary_title.pack(fill = tk.X )
        
        
        sep_EPS_I_Gen_Summary_Title = tk.ttk.Separator(self.PW_EPS_I_Summary_title, orient='horizontal')
        sep_EPS_I_Gen_Summary_Title.pack(side='top', fill='x')
        lbl_EPS_I_Gen_Summary_Title = tk.Label(self.PW_EPS_I_Summary_title, text="Setting Summary")
        lbl_EPS_I_Gen_Summary_Title.pack()
        
        #
        self.PW_EPS_I_Summary = tk.PanedWindow(self.master, orient = 'vertical')
        self.PW_EPS_I_Summary.pack(fill = tk.X )
        
        
        #=========================================================================================================================================
        row_PW_EPS_I_Summay = []
        column_PW_EPS_I_Summay = []
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = 0
        
        lbl_EPS_I_Gen_Summary = tk.Label(self.PW_EPS_I_Summary, text="e-lobook:")
        lbl_EPS_I_Gen_Summary.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_Side = tk.Label(self.PW_EPS_I_Summary, text="Side:")
        lbl_EPS_I_Gen_Side.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_Anatenna = tk.Label(self.PW_EPS_I_Summary, text="Antenna:")
        lbl_EPS_I_Gen_Anatenna.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_SC = tk.Label(self.PW_EPS_I_Summary, text="S/C:")
        lbl_EPS_I_Gen_SC.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_DateStart = tk.Label(self.PW_EPS_I_Summary, text="Date Start:")
        lbl_EPS_I_Gen_DateStart.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_DateEnd = tk.Label(self.PW_EPS_I_Summary, text="Date End:")
        lbl_EPS_I_Gen_DateEnd.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        
        self.lbl_EPS_I_Gen_Summary = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_Summary.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_Side = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_Side.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_Anatenna = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_Anatenna.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_SC = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_SC.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_DateStart = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_DateStart.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_DateEnd = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_DateEnd.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        row_PW_EPS_I_Summay.append(i_row_PW_EPS_I_Summay+1)
        column_PW_EPS_I_Summay.append(i_column_PW_EPS_I_Summay)
         
        #=========================================================================================================================================
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        
        lbl_EPS_I_Gen_Summary_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="XTTC or FBK Support:")
        lbl_EPS_I_Gen_Summary_XTTC_Sup.grid(row = i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_nEvent_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="n° Support:")
        lbl_EPS_I_Gen_nEvent_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_CDA_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="Antenna:")
        lbl_EPS_I_Gen_CDA_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_CooVis_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="Coo-Visibility:")
        lbl_EPS_I_Gen_CooVis_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_SC_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="S/C:")
        lbl_EPS_I_Gen_SC_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_nOrbit_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="n° Orbit:")
        lbl_EPS_I_Gen_nOrbit_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
# =============================================================================
#         i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
#         lbl_EPS_I_Gen_AOS_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="AOS:")
#         lbl_EPS_I_Gen_AOS_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
#         
#         i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
#         lbl_EPS_I_Gen_LOS_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="LOS:")
#         lbl_EPS_I_Gen_LOS_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
# =============================================================================
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        
        self.lbl_EPS_I_Gen_Summary_XTTCFBK = tk.Label(self.PW_EPS_I_Summary, text="NO")
        self.lbl_EPS_I_Gen_Summary_XTTCFBK.grid(row = i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_nEvent_XTTCFBK = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_nEvent_XTTCFBK.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_CDA_XTTCFBK = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_CDA_XTTCFBK.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.chk_EPS_I_Gen_CooVis_XTTCFBK = tk.BooleanVar()
        self.chk_EPS_I_Gen_CooVis_XTTCFBK.set(False)
        self.lbl_EPS_I_Gen_CooVis_XTTCFBK = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_CooVis_XTTCFBK.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_SC_XTTCFBK = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_SC_XTTCFBK.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.strv_EPS_I_Gen_nOrbit_XTTCFBK = tk.StringVar()
        self.lbl_EPS_I_Gen_nOrbit_XTTCFBK = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
# =============================================================================
#         i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
#         self.lbl_EPS_I_Gen_AOS_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="")
#         self.lbl_EPS_I_Gen_AOS_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
#         
#         i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
#         self.lbl_EPS_I_Gen_LOS_XTTC_Sup = tk.Label(self.PW_EPS_I_Summary, text="")
#         self.lbl_EPS_I_Gen_LOS_XTTC_Sup.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
# =============================================================================
        
        self.Controller_XTTC_PreBrief = []
        
        
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        row_PW_EPS_I_Summay.append(i_row_PW_EPS_I_Summay+1)
        column_PW_EPS_I_Summay.append(i_column_PW_EPS_I_Summay)
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        
        
        
        lbl_EPS_I_Gen_Summary_MSW = tk.Label(self.PW_EPS_I_Summary, text="Mission Swap:")
        lbl_EPS_I_Gen_Summary_MSW.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_DateStart_MSW = tk.Label(self.PW_EPS_I_Summary, text="Date Start:")
        lbl_EPS_I_Gen_DateStart_MSW.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_DateEnd_MSW = tk.Label(self.PW_EPS_I_Summary, text="Date End:")
        lbl_EPS_I_Gen_DateEnd_MSW.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        
        self.lbl_EPS_I_Gen_Summary_MSW = tk.Label(self.PW_EPS_I_Summary, text="NO")
        self.lbl_EPS_I_Gen_Summary_MSW.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.strv_EPS_I_DataStart_MSW = tk.StringVar()
        self.lbl_EPS_I_Gen_DateStart_MSW = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_DateStart_MSW.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.strv_EPS_I_DataEnd_MSW = tk.StringVar()
        self.lbl_EPS_I_Gen_DateEnd_MSW = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_DateEnd_MSW.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        
        
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        row_PW_EPS_I_Summay.append(i_row_PW_EPS_I_Summay+1)
        column_PW_EPS_I_Summay.append(i_column_PW_EPS_I_Summay)
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        
        
        lbl_EPS_I_Gen_Summary_Man = tk.Label(self.PW_EPS_I_Summary, text="Manoeuvre:")
        lbl_EPS_I_Gen_Summary_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_SC_Man = tk.Label(self.PW_EPS_I_Summary, text="SC:")
        lbl_EPS_I_Gen_SC_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_Type_Man = tk.Label(self.PW_EPS_I_Summary, text="Type:")
        lbl_EPS_I_Gen_Type_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        lbl_EPS_I_Gen_BurnTime_Man = tk.Label(self.PW_EPS_I_Summary, text="Burn time:")
        lbl_EPS_I_Gen_BurnTime_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        
        #=========================================================================================================================================
        i_row_PW_EPS_I_Summay = 0
        i_column_PW_EPS_I_Summay = i_column_PW_EPS_I_Summay + 1
        
        self.lbl_EPS_I_Gen_Summary_Man = tk.Label(self.PW_EPS_I_Summary, text="NO")
        self.lbl_EPS_I_Gen_Summary_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_SC_Man = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_SC_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.lbl_EPS_I_Gen_Type_Man = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_Type_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        i_row_PW_EPS_I_Summay = i_row_PW_EPS_I_Summay + 1
        self.strv_EPS_I_BurnTime_Man = tk.StringVar()
        self.lbl_EPS_I_Gen_BurnTime_Man = tk.Label(self.PW_EPS_I_Summary, text="")
        self.lbl_EPS_I_Gen_BurnTime_Man.grid(row=i_row_PW_EPS_I_Summay, column=i_column_PW_EPS_I_Summay, sticky="W")
        
        self.Controller_Manoeuvre = [0,]
        
        #=========================================================================================================================================
        tk.ttk.Separator(self.PW_EPS_I_Summary, orient='vertical').grid(column=column_PW_EPS_I_Summay[0], row=0, rowspan=max(row_PW_EPS_I_Summay), sticky='ns')
        tk.ttk.Separator(self.PW_EPS_I_Summary, orient='vertical').grid(column=column_PW_EPS_I_Summay[1], row=0, rowspan=max(row_PW_EPS_I_Summay), sticky='ns')
        tk.ttk.Separator(self.PW_EPS_I_Summary, orient='vertical').grid(column=column_PW_EPS_I_Summay[2], row=0, rowspan=max(row_PW_EPS_I_Summay), sticky='ns')
    # end def
    
    def LogWin_EPS_I(self):
        #
        1
# =============================================================================
#         self.PW_EPS_I_LogWin = tk.PanedWindow(self.master, orient = 'vertical')
#         self.PW_EPS_I_LogWin.pack(fill = tk.X )
#         
#         #
#         self.lbl_EPS_I_LogArea = tk.Label(self.PW_EPS_I_LogWin, text="Events Log")
#         self.lbl_EPS_I_LogArea.pack()
# =============================================================================
        
# =============================================================================
#         self.scrlbar_EPS_I_LogArea = Scrollbar(self.PW_EPS_I_LogWin) 
#         self.scrlbar_EPS_I_LogArea.pack( side = RIGHT, fill = Y ) 
#            
#        self.mylist_EPS_I_LogArea = Listbox(self.PW_EPS_I_LogWin, yscrollcommand = self.scrlbar_EPS_I_LogAre.set ) 
# =============================================================================
        
# =============================================================================
#         self.scrtx_EPS_I_LogArea = tk.scrolledtext..ScrolledText( self.PW_EPS_I_LogWin )
#         self.scrtx_EPS_I_LogArea.pack()
#         
#         self.LogArea_EPS_I(self.EPS_I_logEvents, 2 )
# =============================================================================
        
    # end def
    
    def LogArea_EPS_I(self, logEvents, allogEvents ):
        if (allogEvents == 1):
            head = '\n'
            queue = head
            ilogEvents = head + logEvents[-1]
            ilogEvents = logEvents[-1] + queue
            self.scrtx_EPS_I_LogArea.insert(tk.INSERT, ilogEvents)
        else:
            ilogEvents = '\n'.join(logEvents)
            self.scrtx_EPS_I_LogArea.insert(tk.INSERT, ilogEvents)
        
        self.PW_EPS_I_LogWin.update_idletasks()
    # end def
    
    def Add_LogInfo(self, fcn_LogArea, logEvents, newstrEvent, flag_LogArea ):
        newEvent = '['+str(datetime.datetime.utcnow())[0:23]+']'+ newstrEvent
        logEvents = logEvents + [newEvent]
# =============================================================================
#         if (flag_LogArea == True):
#             fcn_LogArea( logEvents, 1 )
# =============================================================================
        return logEvents
    # end def
    
    def Summary_EPS_I_Side(self, flag_LogArea ):
        if (self.selected_EPS_I_SideS.get()==True and self.selected_EPS_I_SideG.get()==True):
            Side = "SpaCon & GrndCon"
            SideColor = 'orange'
            self.selected_EPS_I_NOAA_BOS.set(True)
        elif (self.selected_EPS_I_SideS.get()==True):
            Side = "SpaCon"
            SideColor = 'blue'
            self.selected_EPS_I_NOAA_BOS.set(False)
        elif (self.selected_EPS_I_SideG.get()==True):
            Side = "GrndCon"
            SideColor = 'green'
            self.selected_EPS_I_NOAA_BOS.set(True)
        else:
            SideColor = 'black'
            Side = ""
        # end if
        
        #
        nwemsg = 'Controlled Side setted ['+Side+']'
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, nwemsg, flag_LogArea )
        
        #
        self.Summary_EPS_I_UpadateDataStart()
        self.Summary_EPS_I_UpadateDataEnd()
        self.lbl_EPS_I_Gen_Side.configure(text = Side, fg=SideColor )
    # end def
    
    def Summary_EPS_I_Antenna(self, event ):
        self.lbl_EPS_I_Gen_Anatenna.configure(text = self.combo_EPS_I_CDA.get())
        
        #
        flag_LogArea = False
        newmsg = 'Antenna setted ['+self.combo_EPS_I_CDA.get()+']'
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
    # end def
    
    def Summary_EPS_I_SC(self, event ):
        self.lbl_EPS_I_Gen_SC.configure(text = self.combo_EPS_I_SC.get())
        
        #
        flag_LogArea = False
        newmsg = 'S/C setted ['+self.combo_EPS_I_SC.get()+']'
        self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
    # end def
    
    def Solar_Legal_Clock(self, anno):
        month = calendar.monthcalendar(anno, 3)
        giorno_di_marzo = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
        month = calendar.monthcalendar(anno, 10)
        giorno_di_ottobre = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
        return giorno_di_marzo, giorno_di_ottobre
    # end def
    
    def Summary_EPS_I_Shift(self, event ):
        if (self.combo_EPS_I_Shift.get()!=''):
            delta=(self.now_local-self.now_UTC).seconds
            delta =datetime.timedelta(seconds=delta)
            if (self.combo_EPS_I_Shift.get()=='Morning'):
                DS=datetime.datetime(self.now_local.year, self.now_local.month, self.now_local.day, 6, 0, 0, 0)-delta
                DE=datetime.datetime(self.now_local.year, self.now_local.month, self.now_local.day, 12, 29, 59, 0)-delta
            elif (self.combo_EPS_I_Shift.get()=='Evening'):
                DS=datetime.datetime(self.now_local.year, self.now_local.month, self.now_local.day, 12, 30, 0, 0)-delta
                DE=datetime.datetime(self.now_local.year, self.now_local.month, self.now_local.day, 20, 14, 59, 0)-delta
            elif (self.combo_EPS_I_Shift.get()=='Night'):
                now_local_HH = self.now_local.hour
                if (now_local_HH<6):
                    now_local2 = datetime.datetime(self.now_local.year, self.now_local.month, self.now_local.day, self.now_local.hour, self.now_local.minute, self.now_local.second, 0*1000)-datetime.timedelta(hours=24)
                else:
                    now_local2 = self.now_local
                # end if
                DS=datetime.datetime(now_local2.year, now_local2.month, now_local2.day, 20, 15, 0, 0)-delta
                giorno_di_marzo, giorno_di_ottobre = self.Solar_Legal_Clock(now_local2.year)
                DE=datetime.datetime(now_local2.year, now_local2.month, now_local2.day, 5, 59, 59, 0)+datetime.timedelta(days=1)-delta
                if (DE.month==3 and DE.day==giorno_di_marzo):
                    DE=DE-datetime.timedelta(hours=1)
                # end if
                if (DE.month==10 and DE.day==giorno_di_ottobre):
                    DE=DE+datetime.timedelta(hours=1)
                # end if
            # end if
            
            self.DateEnd = DE
            self.DateStart = DS
            
            self.strv_EPS_I_flagDataEnd = True
            self.strv_EPS_I_DataEnd.set(DE)
            self.lbl_EPS_I_Gen_DateEnd.configure(text= self.entry_EPS_I_DataEnd.get())
            
            self.strv_EPS_I_flagDataStart = True            
            self.strv_EPS_I_DataStart.set(DS)
            self.lbl_EPS_I_Gen_DateStart.configure(text= self.entry_EPS_I_DataStart.get())
            
            
            #
            flag_LogArea = False
            newmsg = 'Shift setted ['+self.combo_EPS_I_Shift.get()+']'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            #
            self.Summary_EPS_I_Auto_MSW_XTTCFBK()
    # end def
    
    def CheckCharInt(self, char):
        CharInt = 1
        if ( char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9' ):
            CharInt = 0
        return CharInt
    # end def
    
    def Summary_EPS_I_DateFormatCheck(self, str_date):
        DateFormatCheck = True
        if (len(str_date) == 19):
            CharInt0 = self.CheckCharInt(str_date[0])
            CharInt1 = self.CheckCharInt(str_date[1])
            CharInt2 = self.CheckCharInt(str_date[2])
            CharInt3 = self.CheckCharInt(str_date[3])
            CharInt4 = 1
            if (str_date[4]=='-'):
                CharInt4 = 0
            CharInt5 = self.CheckCharInt(str_date[5])
            CharInt6 = self.CheckCharInt(str_date[6])
            CharInt7 = 1
            if (str_date[7]=='-'):
                CharInt7 = 0
            CharInt8 = self.CheckCharInt(str_date[8])
            CharInt9 = self.CheckCharInt(str_date[9])
            CharInt10 = 1
            if (str_date[10]==' '):
                CharInt10 = 0
            CharInt11 = self.CheckCharInt(str_date[11])
            CharInt12 = self.CheckCharInt(str_date[12])
            CharInt13 = 1
            if (str_date[13]==':'):
                CharInt13 = 0
            CharInt14 = self.CheckCharInt(str_date[14])
            CharInt15 = self.CheckCharInt(str_date[15])
            CharInt16 = 1
            if (str_date[16]==':'):
                CharInt16 = 0
            CharInt17 = self.CheckCharInt(str_date[17])
            CharInt18 = self.CheckCharInt(str_date[18])
            CharInt = CharInt0 + CharInt1 + CharInt2 + CharInt3 + CharInt4 + CharInt5 + CharInt6 + CharInt7 + CharInt8 + CharInt9 + CharInt10 + CharInt11 + CharInt12 + CharInt13 + CharInt14 + CharInt15 + CharInt16 + CharInt17 + CharInt18
            if (CharInt != 0):
                DateFormatCheck = False
        else:
            DateFormatCheck = False
        return DateFormatCheck
    #end def
    
    def Summary_EPS_I_UpadateDataStart(self):
        self.strv_EPS_I_DataStart.set(self.entry_EPS_I_DataStart.get())
        self.strv_EPS_I_flagDataStart = False
        if (len(self.strv_EPS_I_DataStart.get())!=0):
            DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.entry_EPS_I_DataStart.get())
            if (DateFormatCheck == False):
                messagebox.showerror('error', 'Date Start format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                
                #
                flag_LogArea = True
                newmsg = 'Date Start format not correct'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            else:
                self.strv_EPS_I_flagDataStart = True
                self.lbl_EPS_I_Gen_DateStart.configure(text= self.entry_EPS_I_DataStart.get())
                self.DateStart = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateStart.cget("text"), '%Y-%m-%d %H:%M:%S')
                
                #
                flag_LogArea = True
                newmsg = 'Date Start setted ['+self.entry_EPS_I_DataStart.get()+']'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
                #
                if (self.strv_EPS_I_flagDataEnd == True):
                    if ( len(self.strv_EPS_I_DataEnd.get())!=0 ):
                        DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.entry_EPS_I_DataEnd.get())
                        if (DateFormatCheck == False):
                            messagebox.showerror('error', 'Date End format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                            
                            #
                            flag_LogArea = True
                            newmsg = 'Date End format not correct'
                            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                        else:
                            self.DateEnd = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateEnd.cget("text"), '%Y-%m-%d %H:%M:%S')
                            
                            if (self.DateEnd>=self.DateStart):
                                self.Summary_EPS_I_Auto_MSW_XTTCFBK()
        return True
    # end def
    
    def Summary_EPS_I_UpadateDataEnd(self):
        self.strv_EPS_I_DataEnd.set(self.entry_EPS_I_DataEnd.get())
        self.strv_EPS_I_flagDataEnd = False
        if (len(self.strv_EPS_I_DataEnd.get())!=0):
            DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.entry_EPS_I_DataEnd.get())
            if (DateFormatCheck == False):
                messagebox.showerror('error', 'Date End format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                
                #
                flag_LogArea = True
                newmsg = 'Date End format not correct'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            else:
                self.strv_EPS_I_flagDataEnd = True
                self.lbl_EPS_I_Gen_DateEnd.configure(text= self.entry_EPS_I_DataEnd.get())
                self.DateEnd = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateEnd.cget("text"), '%Y-%m-%d %H:%M:%S')
                
                #
                flag_LogArea = True
                newmsg = 'Date End setted ['+self.entry_EPS_I_DataEnd.get()+']'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
                #
                if (self.strv_EPS_I_flagDataStart == True):
                    if ( len(self.strv_EPS_I_DataStart.get())!=0 ):
                        DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.entry_EPS_I_DataStart.get())
                        if (DateFormatCheck == False):
                            messagebox.showerror('error', 'Date Start format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                            
                            #
                            flag_LogArea = True
                            newmsg = 'Date Start format not correct'
                            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                        else:
                            self.DateStart = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateStart.cget("text"), '%Y-%m-%d %H:%M:%S')
                            if (self.DateEnd>=self.DateStart):
                                self.Summary_EPS_I_Auto_MSW_XTTCFBK()
        return True
    # end def
    
    def Summary_EPS_I_CalendarDateStart(self):
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
            self.DateStart = res1
            self.strv_EPS_I_DataStart.set(res1)
            self.lbl_EPS_I_Gen_DateStart.configure(text= self.entry_EPS_I_DataStart.get())
            self.DateStart = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateStart.cget("text"), '%Y-%m-%d %H:%M:%S')
            self.Summary_EPS_I_Auto_MSW_XTTCFBK()
            #
            flag_LogArea = True
            newmsg = 'Date Start setted ['+self.entry_EPS_I_DataStart.get()+']'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        def clicked_btn_now_UTC():
            now_UTC_nos1=datetime.datetime.utcnow()
            now_UTC_nos=datetime.datetime(now_UTC_nos1.year, now_UTC_nos1.month, now_UTC_nos1.day, now_UTC_nos1.hour, now_UTC_nos1.minute, now_UTC_nos1.second, 0)
            
            self.DateStart = now_UTC_nos
            self.strv_EPS_I_DataStart.set(now_UTC_nos)
            self.lbl_EPS_I_Gen_DateStart.configure(text= self.entry_EPS_I_DataStart.get())
            self.DateStart = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateStart.cget("text"), '%Y-%m-%d %H:%M:%S')
            self.Summary_EPS_I_Auto_MSW_XTTCFBK()
            #
            flag_LogArea = True
            newmsg = 'Date Start setted ['+self.entry_EPS_I_DataStart.get()+']'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            #
            combo_M.current(now_UTC_nos.minute+1)
            combo_H.current(now_UTC_nos.hour+1)
            
        top = tk.Toplevel(self.PW_EPS_I_Layout)
        top.title("Calendar Date Start")
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=self.now_UTC.year, month=self.now_UTC.month, day=self.now_UTC.day)
        cal.pack(fill="both", expand=True)
        
        frame1 = Frame(top)
        frame1.pack(fill=tk.X)
            
        combo_M = tk.ttk.Combobox(frame1, state="readonly", width=5)
        combo_M['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
        combo_M.current(self.now_UTC.minute) #set the selected item
        combo_M.pack(side='right')
        lbl_Minutes = tk.Label(frame1, text="Minutes:")
        lbl_Minutes.pack(side='right')
        
        combo_H = tk.ttk.Combobox(frame1, state="readonly", width=5)
        combo_H['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
        combo_H.current(self.now_UTC.hour) #set the selected item
        combo_H.pack(side='right')
        lbl_Hours = tk.Label(frame1, text="Hours:")
        lbl_Hours.pack(side='right')
        
        frame2 = Frame(top)
        frame2.pack()
            
        tk.ttk.Button(frame2, text="Update", command=print_update).pack(side='right')
        tk.ttk.Button(frame2, text="now UTC", command=clicked_btn_now_UTC).pack(side='right')
    # end def
    
    def Summary_EPS_I_CalendarDateEnd(self):
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
            self.DateEnd = res1
            self.strv_EPS_I_DataEnd.set(res1)
            self.lbl_EPS_I_Gen_DateEnd.configure(text= self.entry_EPS_I_DataEnd.get())
            self.DateEnd = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateEnd.cget("text"), '%Y-%m-%d %H:%M:%S')
            self.Summary_EPS_I_Auto_MSW_XTTCFBK()
            #
            flag_LogArea = True
            newmsg = 'Date End setted ['+self.entry_EPS_I_DataEnd.get()+']'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
        
        def clicked_btn_UpdateShift():
            if (combo_pS.get()!=''):
                DS=datetime.datetime.strptime( self.strv_EPS_I_DataStart.get(), '%Y-%m-%d %H:%M:%S')
                giorno_di_marzo, giorno_di_ottobre = self.Solar_Legal_Clock(DS.year)
                if (DS>=datetime.datetime(DS.year, 3, giorno_di_marzo, 1, 0, 0, 0) and DS<datetime.datetime(DS.year, 10, giorno_di_ottobre, 1, 0, 0, 0)):
                    deltatime_SL=datetime.timedelta(hours=2)
                else:
                    deltatime_SL=datetime.timedelta(hours=1)
                
                if (combo_pS.get()=='Morning'):
                    DE=datetime.datetime(DS.year, DS.month, DS.day, 12, 30, 0, 0)-deltatime_SL
                elif (combo_pS.get()=='Evening'):
                    DE=datetime.datetime(DS.year, DS.month, DS.day, 20, 0, 0, 0)-deltatime_SL
                elif (combo_pS.get()=='Night'):
                    deltaNight = datetime.timedelta(days=0)
                    if (self.now_local.hour>6):
                        deltaNight = datetime.timedelta(days=1)
                    DE=datetime.datetime(DS.year, DS.month, DS.day, 6, 0, 0, 0)+deltaNight-deltatime_SL
                    if (DE.month==3 and DE.day==giorno_di_marzo and DS<datetime.datetime(2020, 3, giorno_di_marzo, 1, 0, 0, 0)):
                        DE=DE-datetime.timedelta(hours=1)
                    if (DE.month==10 and DE.day==giorno_di_ottobre and DS<datetime.datetime(2020, 10, giorno_di_ottobre, 1, 0, 0, 0)):
                        DE=DE+datetime.timedelta(hours=1)
                self.DateEnd = DE
                self.strv_EPS_I_DataEnd.set(DE)
                self.lbl_EPS_I_Gen_DateEnd.configure(text= self.entry_EPS_I_DataEnd.get())
                self.DateEnd = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateEnd.cget("text"), '%Y-%m-%d %H:%M:%S')
                self.Summary_EPS_I_Auto_MSW_XTTCFBK()
                #
                flag_LogArea = True
                newmsg = 'Date End setted ['+self.entry_EPS_I_DataEnd.get()+']'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
        
        def clicked_btn_UpdateDateStartp():
            if (combo_ph.get()!=''):
                res=int(combo_ph.get())
                D1=datetime.datetime.strptime( self.strv_EPS_I_DataStart.get(), '%Y-%m-%d %H:%M:%S')
                dD=datetime.timedelta(hours=res)
                DE=D1+dD
                self.DateEnd = DE
                self.strv_EPS_I_DataEnd.set(DE)
                self.lbl_EPS_I_Gen_DateEnd.configure(text= self.entry_EPS_I_DataEnd.get())
                self.DateEnd = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateEnd.cget("text"), '%Y-%m-%d %H:%M:%S')
                self.Summary_EPS_I_Auto_MSW_XTTCFBK()
                #
                flag_LogArea = True
                newmsg = 'Date End setted ['+self.entry_EPS_I_DataEnd.get()+']'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
        
        top = tk.Toplevel(self.PW_EPS_I_Layout)
        top.title("Calendar Date End")
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=self.now_UTC.year, month=self.now_UTC.month, day=self.now_UTC.day)
        cal.pack(fill="both", expand=True)
        
        frame1 = Frame(top)
        frame1.pack()
        
        tk.ttk.Button(frame1, text="Update", command=print_update).pack(side='right')
        
        combo_M = tk.ttk.Combobox(frame1, state="readonly", width=5)
        combo_M['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
        combo_M.current(self.now_UTC.minute+1) #set the selected item
        combo_M.pack(side='right')
        lbl_Minutes = tk.Label(frame1, text="Minutes:")
        lbl_Minutes.pack(side='right')
        
        combo_H = tk.ttk.Combobox(frame1, state="readonly", width=5)
        combo_H['values']= ('', '00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
        combo_H.current(self.now_UTC.hour+1) #set the selected item
        combo_H.pack(side='right')
        lbl_Hours = tk.Label(frame1, text="Hours:")
        lbl_Hours.pack(side='right')
        
        frame2 = Frame(top)
        frame2.pack()
        
        tk.ttk.Button(frame2, text="Update", command=clicked_btn_UpdateDateStartp).pack(side='right')
        lbl_hour = tk.Label(frame2, text="Hours")
        lbl_hour.pack(side='right')    
        combo_ph = tk.ttk.Combobox(frame2, state="readonly", width=10)
        combo_ph['values']= ('', '1', '2', '3', '4', '5', '6', '7' , '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36')
        combo_ph.current(0) #set the selected item
        combo_ph.pack(side='right')
        lbl_hours = tk.Label(frame2, text="Data Start +:")
        lbl_hours.pack(side='right')
        
        frame3 = Frame(top)
        frame3.pack()
        
        tk.ttk.Button(frame3, text="Update", command=clicked_btn_UpdateShift).pack(side='right')
        lbl_hour = tk.Label(frame3, text="shift")
        lbl_hour.pack(side='right')    
        combo_pS = tk.ttk.Combobox(frame3, state="readonly", width=10)
        combo_pS['values']= ('', 'Morning', 'Evening', 'Night')
        combo_pS.current(0) #set the selected item
        combo_pS.pack(side='right')
        lbl_hours = tk.Label(frame3, text="Data Start until:")
        lbl_hours.pack(side='right')
    # end def
    
    def Summary_EPS_I_MissionSwap(self):
        top = tk.Toplevel(self.PW_EPS_I_Layout)
        top.title("Mission Swap")
        
        lbl_DataFormat_MSW = tk.Label(top, text="Date Format: YYYY-MM-DD hh:mm:ss [UTC]")
        #lbl_DataFormat_MSW.grid(column=0, row=0, columnspan = 2, sticky = tk.W+tk.E)
        lbl_DataFormat_MSW.grid(column=0, row=0)
        
        def view_MSW_FAQ():
            top = tk.Toplevel(self.PW_EPS_I_Layout)
            top.title("Mission Swap FAQ")
            lbl_PreGenerate_FAQ_MSW = tk.Label(top, text="Date Start: after LOS shadow pass but before AOS of 1st pass on new CDA")
            lbl_PreGenerate_FAQ_MSW.grid(column=0, row=0, sticky="W")
            lbl_PreGenerate_FAQ_MSW = tk.Label(top, text="Date End: after LOS shadow pass but before AOS of the 1st pass on old CDA")
            lbl_PreGenerate_FAQ_MSW.grid(column=0, row=1, sticky="W")
        # end def
        
        btn_FAQ_MSW = tk.ttk.Button(top, text="?", command=view_MSW_FAQ)
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
                self.strv_EPS_I_DataStart_MSW.set(res1)
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: Date Start setted ['+self.strv_EPS_I_DataStart_MSW.get()+']'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            top = tk.Toplevel(self.PW_EPS_I_Layout)
            top.title("Calendar Date Start")
            cal = Calendar(top,
                           font="Arial 14", selectmode='day',
                           cursor="hand1", year=self.now_UTC.year, month=self.now_UTC.month, day=self.now_UTC.day)
            cal.pack(fill="both", expand=True)
            
            frame1 = Frame(top)
            frame1.pack()
                
            combo_M = tk.ttk.Combobox(frame1, state="readonly", width=5)
            combo_M['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
            combo_M.current(self.now_UTC.minute) #set the selected item
            combo_M.pack(side='right')
            lbl_Minutes = tk.Label(frame1, text="Minutes:")
            lbl_Minutes.pack(side='right')
            
            combo_H = tk.ttk.Combobox(frame1, state="readonly", width=5)
            combo_H['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
            combo_H.current(self.now_UTC.hour) #set the selected item
            combo_H.pack(side='right')
            lbl_Hours = tk.Label(frame1, text="Hours:")
            lbl_Hours.pack(side='right')
            
            frame2 = Frame(top)
            frame2.pack()
                
            tk.ttk.Button(frame2, text="Update", command=print_update_cal_MSW).pack(side='top')
        
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
                self.strv_EPS_I_DataEnd_MSW.set(res1)
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: Date End setted ['+self.strv_EPS_I_DataEnd_MSW.get()+']'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            top = tk.Toplevel(self.PW_EPS_I_Layout)
            top.title("Calendar Date Start")
            cal = Calendar(top,
                           font="Arial 14", selectmode='day',
                           cursor="hand1", year=self.now_UTC.year, month=self.now_UTC.month, day=self.now_UTC.day)
            cal.pack(fill="both", expand=True)
            
            frame1 = Frame(top)
            frame1.pack()
                
            combo_M = tk.ttk.Combobox(frame1, state="readonly", width=5)
            combo_M['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
            combo_M.current(self.now_UTC.minute) #set the selected item
            combo_M.pack(side='right')
            lbl_Minutes = tk.Label(frame1, text="Minutes:")
            lbl_Minutes.pack(side='right')
            
            combo_H = tk.ttk.Combobox(frame1, state="readonly", width=5)
            combo_H['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
            combo_H.current(self.now_UTC.hour) #set the selected item
            combo_H.pack(side='right')
            lbl_Hours = tk.Label(frame1, text="Hours:")
            lbl_Hours.pack(side='right')
            
            frame2 = Frame(top)
            frame2.pack()
                
            tk.ttk.Button(frame2, text="Update", command=print_update_cal_MSW).pack(side='top')
            
        def Apply_MSW():
            flagMSW = 1
            if (entry_EPS_I_DataStart_MSW.get()== ""):
                messagebox.showerror('error', 'Mission Swap: NO Date Start choice')
                flagMSW = 0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: NO Date Start choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            if (flagMSW==1 and entry_EPS_I_DataEnd_MSW.get()==""):
                messagebox.showerror('error', 'Mission Swap: NO Date End choice')
                flagMSW=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: NO Date End choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(entry_EPS_I_DataStart_MSW.get())
            if (flagMSW==1 and DateFormatCheck == False):
                messagebox.showerror('error', 'Mission Swap: Date Start format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                flagMSW=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: Date Start format not corect'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(entry_EPS_I_DataEnd_MSW.get())
            if (flagMSW==1 and DateFormatCheck == False):
                messagebox.showerror('error', 'Mission Swap: Date End format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                flagMSW=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: Date End format not corect'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            if (flagMSW==1):
                self.lbl_EPS_I_Gen_Summary_MSW.configure(text= 'YES', fg = "red")
                self.lbl_EPS_I_Gen_DateStart_MSW.configure(text= entry_EPS_I_DataStart_MSW.get())
                
                DS_MSW=datetime.datetime.strptime(self.strv_EPS_I_DataStart_MSW.get(), '%Y-%m-%d %H:%M:%S')
                DE_MSW=datetime.datetime.strptime(self.strv_EPS_I_DataEnd_MSW.get(), '%Y-%m-%d %H:%M:%S')
                
                if (DE_MSW<DS_MSW):
                    messagebox.showerror('error', 'Missin Swap: Date End greater than Data Start one')
                    
                    #
                    flag_LogArea = True
                    newmsg = 'Missin Swap: Date End greater than Data Start one'
                    self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                    
                else:
                    self.lbl_EPS_I_Gen_DateEnd_MSW.configure(text= entry_EPS_I_DataEnd_MSW.get())
                    self.MSW_info = [1,DS_MSW,DE_MSW,0]
                    
                    #
                    flag_LogArea = True
                    newmsg = 'Mission Swap: setted'
                    self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
        def Reset_MSW():
            self.lbl_EPS_I_Gen_Summary_MSW.configure(text= 'NO', fg = "black")
            self.lbl_EPS_I_Gen_DateStart_MSW.configure(text= '')
            self.lbl_EPS_I_Gen_DateEnd_MSW.configure(text= '')
            self.MSW_info = [0,0,0,0]
            
            #
            flag_LogArea = True
            newmsg = 'Mission Swap: removed'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
        
        lbl_DataStart_MSW = tk.Label(top, text="Date Start")
        lbl_DataStart_MSW.grid(column=0, row=1)
        entry_EPS_I_DataStart_MSW = tk.Entry(top, width=20, textvariable=self.strv_EPS_I_DataStart_MSW)
        entry_EPS_I_DataStart_MSW.grid(column=0, row=3)
        btn_DS_MSW = tk.ttk.Button(top, text="Calendar", command=calendar_view_MSW_DS).grid(column=0, row=4)
        
        
        lbl_DataEnd_MSW = tk.Label(top, text="Date End")
        lbl_DataEnd_MSW.grid(column=1, row=1)
        entry_EPS_I_DataEnd_MSW = tk.Entry(top, width=20, textvariable=self.strv_EPS_I_DataEnd_MSW)
        entry_EPS_I_DataEnd_MSW.grid(column=1, row=3)
        btn_DE_MSW = tk.ttk.Button(top, text="Calendar", command=calendar_view_MSW_DE)
        btn_DE_MSW.grid(column=1, row=4)
        
        
        btn_AP_MSW = tk.ttk.Button(top, text="Apply", command=Apply_MSW)
        btn_AP_MSW.grid(column=0, row=5, sticky = tk.W+tk.E)
        btn_Re_MSW = tk.ttk.Button(top, text="Reset", command=Reset_MSW)
        btn_Re_MSW.grid(column=1, row=5, sticky = tk.W+tk.E)
    # end def
    
    def Summary_EPS_I_Manoeuvre(self):
        top_Manoeuvre = tk.Toplevel(self.PW_EPS_I_Layout)
        top_Manoeuvre.title("Manoeuvre")
        
        #
        lbl_SC_Manoeuvre = tk.Label(top_Manoeuvre, text="S/C")
        lbl_SC_Manoeuvre.grid(row=0, column=0, sticky="W")
        combo_SC_Manoeuvre = tk.ttk.Combobox(top_Manoeuvre, state="readonly", width=12, value = ['']+self.MetOp_List )
        combo_SC_Manoeuvre.current(0) #set the selected item
        combo_SC_Manoeuvre.grid(row=0, column=1, sticky="W")
        
        #
        lbl_SC_Manoeuvre = tk.Label(top_Manoeuvre, text="Type")
        lbl_SC_Manoeuvre.grid(row=1, column=0, sticky="W")
        combo_Type_Manoeuvre = tk.ttk.Combobox(top_Manoeuvre, state="readonly", width=17, value = ['']+['IP - In Plane', 'OOP - Out Off Plane'] )
        combo_Type_Manoeuvre.current(0) #set the selected item
        combo_Type_Manoeuvre.grid(row=1, column=1, sticky="W")
        
        
        def calendar_view_Man_DT():
            def print_update_cal_Man():
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
                self.strv_EPS_I_BurnTime_Man.set(res1)
                
                #
                flag_LogArea = True
                newmsg = 'Manoeuvre: Burn Time setted ['+self.strv_EPS_I_BurnTime_Man.get()+']'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            top = tk.Toplevel(self.PW_EPS_I_Layout)
            top.title("Calendar Date Start")
            cal = Calendar(top,
                           font="Arial 14", selectmode='day',
                           cursor="hand1", year=self.now_UTC.year, month=self.now_UTC.month, day=self.now_UTC.day)
            cal.pack(fill="both", expand=True)
            
            frame1 = Frame(top)
            frame1.pack()
                
            combo_M = tk.ttk.Combobox(frame1, state="readonly", width=5)
            combo_M['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
            combo_M.current(self.now_UTC.minute) #set the selected item
            combo_M.pack(side='right')
            lbl_Minutes = tk.Label(frame1, text="Minutes:")
            lbl_Minutes.pack(side='right')
            
            combo_H = tk.ttk.Combobox(frame1, state="readonly", width=5)
            combo_H['values']= ('00', '01', '02', '03', '04', '05', '06', '07' , '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
            combo_H.current(self.now_UTC.hour) #set the selected item
            combo_H.pack(side='right')
            lbl_Hours = tk.Label(frame1, text="Hours:")
            lbl_Hours.pack(side='right')
            
            frame2 = Frame(top)
            frame2.pack()
                
            tk.ttk.Button(frame2, text="Update", command=print_update_cal_Man).pack(side='top')
        
        
        lbl_BurnTime_Manoeuvre  = tk.Label(top_Manoeuvre, text="Burn Time")
        lbl_BurnTime_Manoeuvre.grid(row=2, column=0, sticky="W")
        entry_EPS_I_BurnTime_Manoeuvre = tk.Entry(top_Manoeuvre, width=20, textvariable=self.strv_EPS_I_BurnTime_Man)
        entry_EPS_I_BurnTime_Manoeuvre.grid(row=2, column=1)
        btn_BT_Manoeuvre = tk.ttk.Button(top_Manoeuvre, text="Calendar", command=calendar_view_Man_DT)
        btn_BT_Manoeuvre.grid(row=2, column=2)
        
        def Apply_Manoeuvre():
            flagMan = 1
            if (combo_SC_Manoeuvre.get()== ""):
                messagebox.showerror('error', 'Manoeuvre: NO S/C choice')
                flagMan = 0
                
                #
                flag_LogArea = True
                newmsg = 'Manoeuvre: NO S/C choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            if (flagMan==1 and combo_Type_Manoeuvre.get()==""):
                messagebox.showerror('error', 'Manoeuvre: NO Manoeuvre Type choice')
                flagMan=0
                
                #
                flag_LogArea = True
                newmsg = 'Manoeuvre: NO Manoeuvre Type choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            
            if (flagMan==1 and entry_EPS_I_BurnTime_Manoeuvre.get()==""):
                messagebox.showerror('error', 'Manoeuvre: NO Burn Time choice')
                flagMan=0
                
                #
                flag_LogArea = True
                newmsg = 'Manoeuvre: NO Burn Time choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            else:
                DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(entry_EPS_I_BurnTime_Manoeuvre.get())
                if (flagMan==1 and DateFormatCheck == False):
                    messagebox.showerror('error', 'Manoeuvre: Burn Time format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                    flagMan=0
                    
                    #
                    flag_LogArea = True
                    newmsg = 'Manoeuvre: Burn Time format not corect'
                    self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            if (flagMan==1):
                self.lbl_EPS_I_Gen_Summary_Man.configure(text= 'YES', fg = "red")
                self.lbl_EPS_I_Gen_SC_Man.configure(text= combo_SC_Manoeuvre.get())
                self.lbl_EPS_I_Gen_Type_Man.configure(text= combo_Type_Manoeuvre.get())
                self.lbl_EPS_I_Gen_BurnTime_Man.configure(text= entry_EPS_I_BurnTime_Manoeuvre.get())
                self.EPS_I_Manoeuvre_Info()
                
                #
                flag_LogArea = True
                newmsg = 'Manoeuvre: setted'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
        
        def Reset_Manoeuvre():
            self.lbl_EPS_I_Gen_Summary_Man.configure(text= 'NO', fg = "black")
            self.lbl_EPS_I_Gen_SC_Man.configure(text= '')
            self.lbl_EPS_I_Gen_Type_Man.configure(text= '')
            self.lbl_EPS_I_Gen_BurnTime_Man.configure(text= '')
            self.Man_info = [0,0,0,0,0,0]
            
            #
            flag_LogArea = True
            newmsg = 'Manoeuvre: removed'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
        
        btn_AP_Manoeuvre = tk.ttk.Button(top_Manoeuvre, text="Apply", command=Apply_Manoeuvre)
        btn_AP_Manoeuvre.grid(row=3, column=0, sticky = tk.W+tk.E)
        btn_Re_Manoeuvre = tk.ttk.Button(top_Manoeuvre, text="Reset", command=Reset_Manoeuvre)
        btn_Re_Manoeuvre.grid(row=3, column=2, sticky = tk.W+tk.E)
    # end def
    
    def Summary_EPS_I_XTTCFBK(self):
        top_XTTCFBK = tk.Toplevel(self.PW_EPS_I_Layout)
        top_XTTCFBK.title("XTTC and FBK Support")
        
        chk_CooVis = tk.ttk.Checkbutton(top_XTTCFBK, text='CooVis', var=self.chk_EPS_I_Gen_CooVis_XTTCFBK)
        chk_CooVis.grid(column=2, row=0)
        
        def AntennaCooVis(event):
            chk_CooVis.config(state=tk.NORMAL)
            if ( combo_CDA_XTTCFBK.get() != 'FBK' ):
                self.chk_EPS_I_Gen_CooVis_XTTCFBK.set(False)
                chk_CooVis.config(state=tk.DISABLED)
            # end if
        # end def
        lbl_CDA_XTTCFBK = tk.Label(top_XTTCFBK, text="Antenna")
        lbl_CDA_XTTCFBK.grid(column=0, row=0, sticky="W")
        combo_CDA_XTTCFBK = tk.ttk.Combobox(top_XTTCFBK, state="readonly", width=12, value = ['']+self.Sup_Antenna_List )
        combo_CDA_XTTCFBK.bind("<<ComboboxSelected>>", AntennaCooVis )
        combo_CDA_XTTCFBK.current(0) #set the selected item
        combo_CDA_XTTCFBK.grid(column=1, row=0, sticky="W")
        AntennaCooVis(1)
        
        lbl_SC_XTTCFBK = tk.Label(top_XTTCFBK, text="S/C")
        lbl_SC_XTTCFBK.grid(column=0, row=1, sticky="W")
        combo_SC_XTTCFBK = tk.ttk.Combobox(top_XTTCFBK, state="readonly", width=12, value = ['']+self.MetOp_List )
        combo_SC_XTTCFBK.current(0) #set the selected item
        combo_SC_XTTCFBK.grid(column=1, row=1, sticky="W")
        
        lbl_nSC_XTTCFBK = tk.Label(top_XTTCFBK, text="n° Orbit")
        lbl_nSC_XTTCFBK.grid(column=0, row=2, sticky="W")
        txt_XTTCFBK_nOrbit = tk.Entry(top_XTTCFBK, width=15, textvariable=self.strv_EPS_I_Gen_nOrbit_XTTCFBK)
        txt_XTTCFBK_nOrbit.grid(column=1, row=2, sticky="W")
        
        def Apply_XTTCFBK():
            flag_apply_XTTCFBK = 1
            if (combo_CDA_XTTCFBK.get()==''):
                messagebox.showerror('error', 'XTTC or FBK: NO Antenna choice')
                flag_apply_XTTCFBK=0
                
                #
                flag_LogArea = True
                newmsg = 'XTTC or FBK: NO Antenna choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            # end if
            
            if (flag_apply_XTTCFBK==1 and combo_SC_XTTCFBK.get()==''):
                messagebox.showerror('error', 'XTTC or FBK: NO Antenna choice')
                flag_apply_XTTCFBK=0
                
                #
                flag_LogArea = True
                newmsg = 'XTTC or FBK: NO Antenna choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            # end if
            
            if (flag_apply_XTTCFBK==1 and txt_XTTCFBK_nOrbit.get()==''):
                messagebox.showerror('error', 'XTTC or FBK: NO n° Orbit choice')
                flag_apply_XTTCFBK=0
                
                #
                flag_LogArea = True
                newmsg = 'XTTC or FBK: NO n° Orbit choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            # end if
            
            if (flag_apply_XTTCFBK==1):
                n = 0
                info = txt_XTTCFBK_nOrbit.get()
                for i_info in range(0,len(info)+1):
                    let = info[i_info-1:i_info]
                    if (let=='0' or let=='1' or let=='2' or let=='3' or let=='4' or let=='5' or let=='6' or let=='7' or let=='8' or let=='9'):
                        n = n + 1
                    # end if
                # end for
                if (n != len(info) ):   
                    messagebox.showerror('error', 'XTTC or FBK: n° Orbit is not a number')
                    flag_apply_XTTCFBK=0
                    
                    #
                    flag_LogArea = True
                    newmsg = 'XTTC or FBK: n° Orbit is not a number'
                    self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                # end if
            # end if
            if (flag_apply_XTTCFBK==1):
                self.lbl_EPS_I_Gen_Summary_XTTCFBK.configure(text= 'YES', fg="red")
                self.lbl_EPS_I_Gen_nEvent_XTTCFBK.configure(text= '1')
                self.lbl_EPS_I_Gen_CDA_XTTCFBK.configure(text= combo_CDA_XTTCFBK.get())                
                self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= 'NO')
                if (self.chk_EPS_I_Gen_CooVis_XTTCFBK.get()==True):
                    self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= 'YES')
                # end if                
                self.lbl_EPS_I_Gen_SC_XTTCFBK.configure(text= combo_SC_XTTCFBK.get())
                self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.configure(text= txt_XTTCFBK_nOrbit.get())
                self.chk_EPS_I_fileXTTCPDF.config(state=tk.NORMAL)
                self.EPS_I_Controller_XTTC_PreBrief[0]=1
                self.EPS_I_XTTC_Info()
                
                flag_LogArea = True
                newmsg = 'XTTC or FBK: setted'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            # end if
        # end def
        def Reset_XTTCFBK():
            self.lbl_EPS_I_Gen_Summary_XTTCFBK.configure(text= 'NO', fg = "black")
            self.lbl_EPS_I_Gen_nEvent_XTTCFBK.configure(text= '')
            self.lbl_EPS_I_Gen_CDA_XTTCFBK.configure(text= '')
            self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= '')
            self.lbl_EPS_I_Gen_SC_XTTCFBK.configure(text= '')
            self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.configure(text= '')
            
            self.selected_EPS_I_fileXTTCPDF.set(False)
            self.chk_EPS_I_fileXTTCPDF.config(state=tk.DISABLED)
            self.EPS_I_Controller_XTTC_PreBrief[0]=0
            self.XTTC_FBK_info = [0,0,0,0,0,0,1]
            
            #
            flag_LogArea = True
            newmsg = 'XTTC or FBK: removed'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        # end def
        btn_AP_XTTCFBK = tk.ttk.Button(top_XTTCFBK, text="Apply", command=Apply_XTTCFBK)
        btn_AP_XTTCFBK.grid(column=0, row=3, sticky = tk.W+tk.E)
        btn_Re_XTTCFBK = tk.ttk.Button(top_XTTCFBK, text="Reset", command=Reset_XTTCFBK)
        btn_Re_XTTCFBK.grid(column=2, row=3, sticky = tk.W+tk.E)
    # end def
    
    def Summary_EPS_I_Auto_MSW_XTTCFBK(self):
        self.XTTC_FBK_info = [0,0,0,0,0,0,1]
        self.DateStart = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateStart.cget("text"), '%Y-%m-%d %H:%M:%S')
        self.DateEnd = datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateEnd.cget("text"), '%Y-%m-%d %H:%M:%S')
        print('Summary_EPS_I_Auto_MSW_XTTCFBK',self.DateStart,self.DateEnd)
        if (self.DateEnd<self.DateStart):
            messagebox.showerror('error', 'Date End greater than start one')
            
        else:
            if (self.selected_EPS_I_SideS.get()==True):
                if (len(self.EPS_I_XTTC)!=0):
                    flag_XTTC_now = False
                    self.ESTRACK_passlist = METOPCONT_Info(self.file_dir_EPS_I[2][0],self.file_dir_EPS_I[6],self.OS_Sys_sep,self.EPS_I_SC,self.DateStart,self.DateEnd)
                    ii_XTTC = 0
                    for i_XTTC in range(0,len(self.ESTRACK_passlist)):
                        if ( self.ESTRACK_passlist[i_XTTC][6] == 1 ):
                            if (self.ESTRACK_passlist[i_XTTC][3]>=self.DateStart and self.ESTRACK_passlist[i_XTTC][3]<=self.DateEnd):
                                flag_XTTC_now = True
                                ii_XTTC = ii_XTTC+1
                                ii_XTTC_str = str(ii_XTTC)
                                self.lbl_EPS_I_Gen_Summary_XTTCFBK.configure(text= 'YES', fg="red")
                                self.lbl_EPS_I_Gen_nEvent_XTTCFBK.configure(text= ii_XTTC_str)
                                self.lbl_EPS_I_Gen_CDA_XTTCFBK.configure(text= self.ESTRACK_passlist[i_XTTC][2])
                                self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= 'NO')               
                                self.lbl_EPS_I_Gen_SC_XTTCFBK.configure(text= self.ESTRACK_passlist[i_XTTC][0])
                                self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.configure(text= str(self.ESTRACK_passlist[i_XTTC][5]))
                                self.chk_EPS_I_fileXTTCPDF.config(state=tk.NORMAL)
                                self.EPS_I_Controller_XTTC_PreBrief[0]=1
                                
                    
                    for i_XTTC in range(0,len(self.EPS_I_XTTC)):
                        if ( ((self.EPS_I_XTTC[i_XTTC][0]=='FBK') or (self.EPS_I_XTTC[i_XTTC][0]=='WAL')) or (ii_XTTC==0) ):
                            if (self.EPS_I_XTTC[i_XTTC][1]>=self.DateStart and self.EPS_I_XTTC[i_XTTC][1]<=self.DateEnd):
                                flag_XTTC_now = True
                                
                                self.lbl_EPS_I_Gen_Summary_XTTCFBK.configure(text= 'YES', fg="red")
                                self.lbl_EPS_I_Gen_nEvent_XTTCFBK.configure(text= '1')
                                self.lbl_EPS_I_Gen_CDA_XTTCFBK.configure(text= self.EPS_I_XTTC[i_XTTC][0])
                                self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= 'NO')
                                if (self.EPS_I_XTTC[i_XTTC][4]=='CoVis'):
                                    self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= 'YES')
                                # end if                
                                self.lbl_EPS_I_Gen_SC_XTTCFBK.configure(text= self.EPS_I_XTTC[i_XTTC][2])
                                self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.configure(text= self.EPS_I_XTTC[i_XTTC][3])
                                self.chk_EPS_I_fileXTTCPDF.config(state=tk.NORMAL)
                                self.EPS_I_Controller_XTTC_PreBrief[0]=1
                                
                        # end if
                    # end for
                    if (flag_XTTC_now == False):
                        self.XTTC_FBK_info = [0,0,0,0,0,0,1]
                        self.lbl_EPS_I_Gen_Summary_XTTCFBK.configure(text= 'NO', fg = "black")
                        self.lbl_EPS_I_Gen_nEvent_XTTCFBK.configure(text= '')
                        self.lbl_EPS_I_Gen_CDA_XTTCFBK.configure(text= '')
                        self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= '')             
                        self.lbl_EPS_I_Gen_SC_XTTCFBK.configure(text= '')
                        self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.configure(text='')
                        self.chk_EPS_I_fileXTTCPDF.config(state=tk.DISABLED)
                        self.EPS_I_Controller_XTTC_PreBrief[0]=0
                    else:
                        self.EPS_I_XTTC_Info()
                        
                # end if
            else:
                self.lbl_EPS_I_Gen_Summary_XTTCFBK.configure(text= 'NO', fg = "black")
                self.lbl_EPS_I_Gen_nEvent_XTTCFBK.configure(text= '')
                self.lbl_EPS_I_Gen_CDA_XTTCFBK.configure(text= '')
                self.lbl_EPS_I_Gen_CooVis_XTTCFBK.configure(text= '')             
                self.lbl_EPS_I_Gen_SC_XTTCFBK.configure(text= '')
                self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.configure(text='')
                self.chk_EPS_I_fileXTTCPDF.config(state=tk.DISABLED)
                self.EPS_I_Controller_XTTC_PreBrief[0]=0
            # end if
                
            file_Path_Name_MS = self.file_dir_EPS_I[3]
            self.MSW_info = [0,0,0,0]
            
            if (len(self.EPS_I_Dates_MS)!=0):
                flag_MSW_today = False
                flag_MSW_Info_today = False
                for i_MS in range(0,len(self.EPS_I_Dates_MS)):
                    DS_test = datetime.datetime(self.DateStart.year, self.DateStart.month, self.DateStart.day, 0, 0, 0, 0*1000)
                    DE_test = datetime.datetime(self.DateEnd.year, self.DateEnd.month, self.DateEnd.day, 0, 0, 0, 0*1000)
                    DateStar_Flag = self.EPS_I_Dates_MS[i_MS] >= DS_test
                    DateEnd_Flag = self.EPS_I_Dates_MS[i_MS] <= DE_test
                    if (DateStar_Flag and DateEnd_Flag):
                        flag_MSW_today = True
                        self.lbl_EPS_I_Gen_Summary_MSW.configure(text= 'YES', fg="red")
                        if (os.path.isfile(file_Path_Name_MS)):
                            self.MSW_info[3]=0
                            
                            MS_Scheduled = self.MS_Scheduled
                            if (len(MS_Scheduled)!=0):
                                DMS2_test = datetime.datetime(self.MS_Scheduled[2].year, self.MS_Scheduled[2].month, self.MS_Scheduled[2].day, 0, 0, 0, 0*1000)
                                DMS3_test = datetime.datetime(self.MS_Scheduled[3].year, self.MS_Scheduled[3].month, self.MS_Scheduled[3].day, 0, 0, 0, 0*1000)
                                DateStar_S_Flag = DMS2_test == self.EPS_I_Dates_MS[i_MS]
                                DateEnd_S_Flag = DMS3_test == self.EPS_I_Dates_MS[i_MS]
                                if ((MS_Scheduled[2]>=self.DateStart and MS_Scheduled[2]<=self.DateEnd) or (MS_Scheduled[3]>=self.DateStart and MS_Scheduled[3]<=self.DateEnd)):
                                    flag_MSW_Info_today = True
                                    self.strv_EPS_I_DataStart_MSW.set(MS_Scheduled[0])
                                    self.lbl_EPS_I_Gen_DateStart_MSW.configure(text= self.strv_EPS_I_DataStart_MSW.get())
                                    DS_MSW=datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateStart_MSW.cget("text"), '%Y-%m-%d %H:%M:%S')
                                    self.strv_EPS_I_DataEnd_MSW.set(MS_Scheduled[1])
                                    self.lbl_EPS_I_Gen_DateEnd_MSW.configure(text= self.strv_EPS_I_DataEnd_MSW.get())
                                    DE_MSW=datetime.datetime.strptime(self.lbl_EPS_I_Gen_DateEnd_MSW.cget("text"), '%Y-%m-%d %H:%M:%S')
                                    self.MSW_info = [1,DS_MSW,DE_MSW,0]
                                elif ( DateStar_S_Flag and DateEnd_S_Flag ):
                                    self.MSW_info[3]=0
                                    flag_MSW_today = False
                                else:
                                    self.MSW_info[3] = 1
                            else:
                              self.MSW_info[3]=1  
                        else:
                            self.MSW_info[3]=1
                    else:
                        self.MSW_info[3]=0
                    if (flag_MSW_today==False):
                        self.lbl_EPS_I_Gen_Summary_MSW.configure(text= 'NO', fg = "black")
                        self.MSW_info[0] = 0
                        flag_MSW_Info_today = False
                    if (flag_MSW_Info_today==False):
                        self.strv_EPS_I_DataStart_MSW.set('')
                        self.lbl_EPS_I_Gen_DateStart_MSW.configure(text= self.strv_EPS_I_DataStart_MSW.get())
                        self.strv_EPS_I_DataEnd_MSW.set('')
                        self.lbl_EPS_I_Gen_DateEnd_MSW.configure(text= self.strv_EPS_I_DataEnd_MSW.get())
                        self.MSW_info[1] = 0
                        self.MSW_info[2] = 0
            else:
                self.MSW_info[3]=0
            
            self.Man_info = [0,0,0,0,0,0]
    # end def
    
    def EPS_I_Manoeuvre_Info(self):
        for i_SC in range(0,len(self.EPS_I_SC)):
            if (self.EPS_I_SC[i_SC][0]==self.lbl_EPS_I_Gen_SC_Man.cget("text")[-1:]):
                nMetop = i_SC
        nMetop_str = 'M0'+str(int(self.EPS_I_SC[nMetop][1]))
        Wimpyfilepath = self.file_dir_EPS_I[6][nMetop]
        
        DT_Man=datetime.datetime.strptime(self.strv_EPS_I_BurnTime_Man.get(), '%Y-%m-%d %H:%M:%S')
        
        Man_info = fcn_Manoeuvre(DTBurn, Wimpyfilepath)
        self.Man_info = [1,nMetop_str,Wimpyfilepath,self.lbl_EPS_I_Gen_Type_Man.cget("text"),DT_Man,Man_info]
    # end def
    
    def EPS_I_XTTC_Info(self):
        
        chk_CooVis = False
        if (self.lbl_EPS_I_Gen_CooVis_XTTCFBK.cget("text")=='YES'):
            chk_CooVis = True
        Antenna_XTTC_FBK = self.lbl_EPS_I_Gen_CDA_XTTCFBK.cget("text")
        nOrbit_cust = int(self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.cget("text"))
        for i_SC in range(0,len(self.EPS_I_SC)):
            if (self.EPS_I_SC[i_SC][0]==self.lbl_EPS_I_Gen_SC_XTTCFBK.cget("text")[-1:]):
                nMetop = i_SC
        nMetop_str = 'M0'+str(int(self.EPS_I_SC[nMetop][1]))
        Wimpyfilepath = self.file_dir_EPS_I[6][nMetop]
        
        
        XTTC_FBK, ErrorMsg = fcn_XTTC_FBK(Wimpyfilepath, nOrbit_cust)
        
        self.XTTC_FBK_info =[1,chk_CooVis,Antenna_XTTC_FBK,nMetop_str,nOrbit_cust,XTTC_FBK,1]
        
        if (self.XTTC_FBK_info[0]==1):
            time_list_XTTC = ['AOS','AOSM','AOS5','Mid','LOS5','LOSM', 'LOS']
            niter = 0
            for i_XTTC_FBK in range(0,XTTC_FBK.shape[0]):
                if (self.XTTC_FBK_info[5].loc[time_list_XTTC[i_XTTC_FBK],[self.XTTC_FBK_info[2]]][self.XTTC_FBK_info[2]]=='N/A'):
                    niter = niter + 1
            
            if (niter!=0):
                result = messagebox.askquestion(title='warning', message="The information, for XTTC or FBK support, are incorrect or inconsistent.\nDo you want to continue anyway?", icon='warning')
                if (result == 'yes'):
                    self.XTTC_FBK_info = [0,0,0,0,0,0,1]
                else:
                    self.XTTC_FBK_info[6]=0
            else:
                1
                #self.lbl_EPS_I_Gen_AOS_XTTC_Sup.configure(text= '')
                #self.lbl_EPS_I_Gen_LOS_XTTC_Sup.configure(text= '')
            
            
            if (self.XTTC_FBK_info[6]==1):
                XTTC_Date = self.XTTC_FBK_info[5].loc['AOS',[self.XTTC_FBK_info[2]]][self.XTTC_FBK_info[2]]
                if (XTTC_Date>=self.DateStart and XTTC_Date<=self.DateEnd):
                    self.XTTC_FBK_info[6] = self.XTTC_FBK_info[6]
                else:
                    result = messagebox.askquestion(title='warning', message="The information, for XTTC or FBK support, are related to a pass, not within the indicated timeframe.\nDo you want to continue anyway?", icon='warning')
                    if (result == 'yes'):
                        self.XTTC_FBK_info = [0,0,0,0,0,0,1]
                    else:
                        self.XTTC_FBK_info[6] = 0
    # end def
    
    def Summary_EPS_I_XTTC_PreBrief(self):
        if (self.EPS_I_Controller_XTTC_PreBrief[0]==1):
            if (self.selected_EPS_I_fileXTTCPDF.get() == False and self.EPS_I_Controller_XTTC_PreBrief[1]==0):
                result1 = messagebox.askquestion(title='warning', message="XTTC or FBK exist.\nDo you want generate a Pre-Pass briefing?", icon='warning')
                if (result1 == 'yes'):
                    self.selected_EPS_I_fileXTTCPDF.set(True)
                    
                    #
                    flag_LogArea = True
                    newmsg = 'XTTC or FBK: exist'
                    self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
                
                result2 = messagebox.askquestion(title='question', message="Do you want save your setting about XTTC or FBK Pre-Pass briefing?", icon='question')
                if (result2 == 'yes'):
                    if (self.selected_EPS_I_fileXTTCPDF.get()==True):
                        self.Controllers.at[self.EPS_I_Controller_XTTC_PreBrief[2],'XTTC_PreBrief']=int(1)
                    else:
                        self.Controllers.at[self.EPS_I_Controller_XTTC_PreBrief[2],'XTTC_PreBrief']=int(-1)
                    self.Controllers.to_csv (r''+self.file_dir_EPS_I[1], index = False, header=True)
            
            self.EPS_I_Controller_XTTC_PreBrief[1] = self.Controllers.loc[self.EPS_I_Controller_XTTC_PreBrief[2],['XTTC_PreBrief']]['XTTC_PreBrief']
            
            if ( (self.EPS_I_Controller_XTTC_PreBrief[1]==1 and self.selected_EPS_I_fileXTTCPDF.get()==False) or (self.EPS_I_Controller_XTTC_PreBrief[1]==-1 and self.selected_EPS_I_fileXTTCPDF.get()==True) or (self.EPS_I_Controller_XTTC_PreBrief[1]==0 and self.selected_EPS_I_fileXTTCPDF.get()==True) ):
                result2 = messagebox.askquestion(title='question', message="Do you want save your new setting about XTTC or FBK Pre-Pass briefing?", icon='question')
                if (result2 == 'yes'):
                    if (self.selected_EPS_I_fileXTTCPDF.get()==True):
                        self.Controllers.at[self.EPS_I_Controller_XTTC_PreBrief[2],'XTTC_PreBrief']=int(1)
                    else:
                        self.Controllers.at[self.EPS_I_Controller_XTTC_PreBrief[2],'XTTC_PreBrief']=int(-1)
                    self.Controllers.to_csv (r''+self.file_dir_EPS_I[1], index = False, header=True)
    # end def
    
    def messageerror(self):
        flag=1
        if (self.selected_EPS_I_SideS.get()==False and self.selected_EPS_I_SideG.get()==False):
            messagebox.showerror('error', 'NO side choice')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'NO side choice'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        if (flag==1 and self.lbl_EPS_I_Gen_Anatenna.cget("text")==''):
            messagebox.showerror('error', 'NO Antenna choice')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'NO Antenna choice'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        if (flag==1 and self.lbl_EPS_I_Gen_SC.cget("text")==''):
            messagebox.showerror('error', 'NO S/C choice')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'NO S/C choice'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        if (flag==1 and self.lbl_EPS_I_Gen_DateStart.cget("text")==''):
            messagebox.showerror('error', 'NO Date Start choice')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'NO Data Start choice'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.entry_EPS_I_DataStart.get())
        if (flag==1 and DateFormatCheck == False):
            messagebox.showerror('error', 'Date Start format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'Date Start format not corect'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        if (flag==1 and self.lbl_EPS_I_Gen_DateEnd.cget("text")==''):
            messagebox.showerror('error', 'NO Date End choice')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'NO Date End choice'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.entry_EPS_I_DataEnd.get())
        if (flag==1 and DateFormatCheck == False):
            messagebox.showerror('error', 'Date End format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'Date End format not corect'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        if (flag==1 and self.DateEnd<self.DateStart):
            messagebox.showerror('error', 'Date End greater than start one')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'Date End greater than start one'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        if (flag==1 and self.selected_EPS_I_filecsv.get()==False):
        #if (flag==1 and selected_filePDF.get()==False and selected_filecsv.get()==False):
            messagebox.showerror('error', 'NO file choice')
            flag=0
            
            #
            flag_LogArea = True
            newmsg = 'NO file choice'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        
        
        #
        if (flag==1 and self.MSW_info[3]==1):
            flag = 0
            result = messagebox.askquestion(title='Warning', message="Today there is a Mission Swap.\nYou have not set it yet.\nAre you sure you want to continue?", icon='warning')
            if (result == 'yes'):
                flag = 1
                self.lbl_EPS_I_Gen_Summary_MSW.configure(text= 'NO', fg = "black")
            else:
                messagebox.showinfo(title='Info', message ='Click "Mission Swap" button to add or reset it')
            
            #
            flag_LogArea = True
            newmsg = 'Mission Swap: exist but not setted'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
        if (self.lbl_EPS_I_Gen_Summary_MSW.cget("text")== "YES"):
            if (flag==1 and self.lbl_EPS_I_Gen_DateStart_MSW.cget("text")== ""):
                messagebox.showerror('error', 'Mission Swap: NO Date Start choice')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: NO Date Start choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            if (flag==1 and self.lbl_EPS_I_Gen_DateEnd_MSW.cget("text")==""):
                messagebox.showerror('error', 'Mission Swap: NO Date End choice')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: NO Date End choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.lbl_EPS_I_Gen_DateStart_MSW.cget("text"))
            if (flag==1 and DateFormatCheck == False):
                messagebox.showerror('error', 'Mission Swap: Date Start format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: Date Start format not corect'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            DateFormatCheck = self.Summary_EPS_I_DateFormatCheck(self.lbl_EPS_I_Gen_DateEnd_MSW.cget("text"))
            if (flag==1 and DateFormatCheck == False):
                messagebox.showerror('error', 'Mission Swap: Date End format not corect.\nRemenber, the format must be: [YYYY-MM-DD hh:mm:ss].\nIf you are not sure, you use the "Calendar" button.')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: Date End format not corect'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            if (flag==1 and self.MSW_info[2]<self.MSW_info[1]):
                messagebox.showerror('error', 'Mission Swap: Date End greater than Date Start one')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'Mission Swap: Date End greater than Date Start one'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
        
        
        
        #
        if (self.EPS_I_Controller_XTTC_PreBrief[0]==1):  
            if (flag==1 and self.lbl_EPS_I_Gen_CDA_XTTCFBK.cget("text")==''):
                messagebox.showerror('error', 'XTTC or FBK: NO Antenna choice')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'XTTC or FBK: NO Antenna choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            # end if
            if (flag==1 and self.lbl_EPS_I_Gen_SC_XTTCFBK.cget("text")==''):
                messagebox.showerror('error', 'XTTC or FBK: NO S/C choice')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'XTTC or FBK: NO S/C choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            # end if
            if (flag==1 and self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.cget("text")==''):
                messagebox.showerror('error', 'XTTC or FBK: NO n° Orbit choice')
                flag=0
                
                #
                flag_LogArea = True
                newmsg = 'XTTC or FBK: NO n° Orbit choice'
                self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                
            # end if
            if (flag==1):
                n = 0
                info = self.lbl_EPS_I_Gen_nOrbit_XTTCFBK.cget("text")
                for i_info in range(0,len(info)+1):
                    let = info[i_info-1:i_info]
                    if (let=='0' or let=='1' or let=='2' or let=='3' or let=='4' or let=='5' or let=='6' or let=='7' or let=='8' or let=='9'):
                        n = n + 1
                    # end if
                # end for
                if (n != len(info) ):   
                    messagebox.showerror('error', 'XTTC or FBK: n° Orbit is not a number')
                    flag=0
                    
                    #
                    flag_LogArea = True
                    newmsg = 'XTTC or FBK: NO  n° Orbit is not a number'
                    self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
                    
                # end if
                #self.Summary_EPS_I_XTTC_PreBrief()
            # end if
        return flag
    # end def
    
    def msg_wimpyerror(self, error_line):
        flag_wimpyerror = 1
        if ( error_line[0] == 1 ):
            messagebox.showerror('wimpy error', 'Possible event inversion in the wimpy file:\n\n'+error_line[1]+'\n\nPlease check line between: '+str(error_line[2])+' (Date: '+error_line[4]+') and '+str(error_line[3])+' (Date: '+error_line[5]+') and correct it.\n\nOpen the wimpy file (mentioned above) with a text editor.\nGo to the line/date (inticated above).\nInvert the 2 lines' )
            
            #
            flag_LogArea = True
            newmsg = 'Possible event inversion in the wimpy file'
            self.EPS_I_logEvents = self.Add_LogInfo(self.LogArea_EPS_I, self.EPS_I_logEvents, newmsg, flag_LogArea )
            
            flag_wimpyerror=0
        return flag_wimpyerror
    # end def
    
    def btn_EPS_I_Generate(self):
        flag = self.messageerror()
        
        
        # Function responsible for the updation 
        # of the progress bar value 
        if (flag==1):
            proges_per100 = int(0)
            self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
            self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading ('+str(proges_per100)+'%)')
            self.PW_EPS_I_Gen.update_idletasks()
            
            CDAn = self.lbl_EPS_I_Gen_Anatenna.cget("text")
            
            flag_wimpyerrors = [0,0,0,0,0]
            Global_frame_TC = []
            i_proges_per100 = 0
            for i_SC in range(0,len(self.EPS_I_SC)):
                if (self.lbl_EPS_I_Gen_SC.cget("text")=='MetOp-'+self.EPS_I_SC[i_SC][0] or self.lbl_EPS_I_Gen_SC.cget("text")=='All MetOp'):
                    Wimpyfilepath_Mi = self.file_dir_EPS_I[6][i_SC]
                    
                    if (os.path.isfile(Wimpyfilepath_Mi) == True):
                        
                        proges_per100 = int(i_proges_per100)
                        self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                        self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [Wimpy MetOp-'+self.EPS_I_SC[i_SC][0]+'] ('+str(proges_per100)+'%)')
                        self.PW_EPS_I_Gen.update_idletasks()
                        i_proges_per100 = proges_per100 + 10
                        
                        FDF_Pass_Mi, ErrorMsg = fcn_Wimpy_Maga(self.DateStart, self.DateEnd, Wimpyfilepath_Mi, 'MetOp-'+self.EPS_I_SC[i_SC][0], CDAn )
                        flag_wimpyerror = self.msg_wimpyerror(ErrorMsg)
                        if (flag_wimpyerror==0):
                            flag_wimpyerrors[i_SC] = 1
                        
                        FDF_MPF_Pass_Mi, MPF_Pass_Mi = fcn_MPF_mang(FDF_Pass_Mi, self.EPS_I_PGFDSS)
                        
                        #print (FDF_MPF_Pass_Mi.loc[:,['TM_Format']]['TM_Format'])
                        
                        Global_frame_TC = Global_frame_TC + [FDF_MPF_Pass_Mi]
            
            if (self.XTTC_FBK_info[6] == 1):
                if (CDAn[0:3]=='CDA'):
                    CDAn_N = CDAn[0:3]
                    if (CDAn[3:4]=='1'):
                        CDAn_N = CDAn_N+'2'
                    else:
                        CDAn_N = CDAn_N+'1'
                else:
                    CDAn_N = CDAn
                
                Wimpyfilepath_N19 = self.file_dir_EPS_I[9]
                if (os.path.isfile(Wimpyfilepath_N19) == True):
                    if (self.lbl_EPS_I_Gen_SC.cget("text")=='N19' or self.selected_EPS_I_NOAA_BOS.get()==True):
                        
                        proges_per100 = int(30)
                        self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                        self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [Wimpy N19] ('+str(proges_per100)+'%)')
                        self.PW_EPS_I_Gen.update_idletasks()
                        
                        FDF_Pass_N19, ErrorMsg = fcn_Wimpy_Maga(self.DateStart, self.DateEnd, Wimpyfilepath_N19, 'N19', CDAn_N)
                        flag_wimpyerror = self.msg_wimpyerror(ErrorMsg)
                        if (flag_wimpyerror==0):
                            flag_wimpyerrors[3] = 1
                        
                        FDF_MPF_Pass_N19, MPF_Pass_N19 = fcn_MPF_mang(FDF_Pass_N19, self.EPS_I_PGFDSS)
                
                Wimpyfilepath_N18 = self.file_dir_EPS_I[10]
                if (os.path.isfile(Wimpyfilepath_N18) == True):
                    if (self.lbl_EPS_I_Gen_SC.cget("text")=='N18' or self.selected_EPS_I_NOAA_BOS.get()==True):
                        
                        proges_per100 = int(40)
                        self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                        self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [Wimpy N18] ('+str(proges_per100)+'%)')
                        self.PW_EPS_I_Gen.update_idletasks()
                        
                        FDF_Pass_N18, ErrorMsg = fcn_Wimpy_Maga(self.DateStart, self.DateEnd, Wimpyfilepath_N18, 'N18', CDAn_N)
                        flag_wimpyerror = self.msg_wimpyerror(ErrorMsg)
                        if (flag_wimpyerror==0):
                            flag_wimpyerrors[4] = 1
                        
                        FDF_MPF_Pass_N18, MPF_Pass_N18 = fcn_MPF_mang(FDF_Pass_N18, self.EPS_I_PGFDSS)
                
                
                sumflag_wimpyerror = 0
                for num in flag_wimpyerrors:
                    sumflag_wimpyerror += int(num)
                if ( sumflag_wimpyerror == 0 ):
                    if (self.selected_EPS_I_NOAA_BOS.get()==True):
                        
                        proges_per100 = int(50)
                        self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                        self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading [NOAA BOS] ('+str(proges_per100)+'%)')
                        self.PW_EPS_I_Gen.update_idletasks()
                        
                        frames_N19_N18 = [FDF_MPF_Pass_N19, FDF_MPF_Pass_N18]
                        result = concat(frames_N19_N18)
                        FDF_N = result.sort_values(by=['CDA_AOS'])
                        FDF_N = FDF_N.reset_index()
                        FDF_MPF_Pass_N19_N18 = FDF_N.drop(columns='index')
                        filePath_NOAA_week_OLD = self.file_dir_EPS_I[8]
                        FDF_Pass_N19_N18 = NOAA_BOS_shift(FDF_MPF_Pass_N19_N18,self.DateStart, self.DateEnd, filePath_NOAA_week_OLD)
                        
                        Global_frame_TC = Global_frame_TC + [FDF_Pass_N19_N18]
                    
                    proges_per100 = int(65)
                    self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                    self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Merge Wimpys ('+str(proges_per100)+'%)')
                    self.PW_EPS_I_Gen.update_idletasks()
                    
                    TC_Pass_M = mergeWimpy( Global_frame_TC, 1, self.DateStart, self.DateEnd, self.MSW_info)
                    
                    
                    
                    
                    if ( self.EPS_I_Controller_XTTC_PreBrief[1]==1 and self.selected_EPS_I_fileXTTCPDF.get()==True ):
                        1
                    
                    
                    
                    if (self.selected_EPS_I_filecsv.get()==True):      
                        if (self.selected_EPS_I_Weekly.get()==True):
                            opts = 3
                        else:
                            opts = 2
                        
                        SHOfalg = 0
                        if (self.selected_EPS_I_SHO.get()==True):
                            SHOfalg = 1
                        
                        new_DS = self.DateStart
                        new_DE = self.DateEnd
                        Dt = (new_DE-new_DS)
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
                        
                        proges_per100 = int(75)
                        self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                        self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Generation Uberlog file (.csv) ('+str(proges_per100)+'%)')
                        self.PW_EPS_I_Gen.update_idletasks()
                        
                        nfile = math.ceil( DT / (24*3600) )
                        for ifile in range(1,nfile+1):
                            
                            new_DS = self.DateStart + datetime.timedelta(hours = (ifile-1) * 24)
                            new_DE = self.DateStart + datetime.timedelta(hours = (ifile) * 24)
                            if ( new_DE >= self.DateEnd ):
                                new_DE = self.DateEnd
                            
                            strShiftfilename_from = strShiftfilename_fromto(new_DS)
                            strShiftfilename_to = strShiftfilename_fromto(new_DE)
                            
                            if (self.selected_EPS_I_SideS.get()==True and self.selected_EPS_I_SideG.get()==True):
                                strEPSSide = 'EPS_Combine'
                                Folder = 'Combine'+self.OS_Sys_sep+''
                                SpaGrndCon=1
                            elif (self.selected_EPS_I_SideS.get()==True):
                                strEPSSide = 'EPS_SpaCon'
                                Folder = 'SpaCon'+self.OS_Sys_sep+''
                                SpaGrndCon=2
                            elif (self.selected_EPS_I_SideG.get()==True):
                                strEPSSide = 'EPS_GrndCon'
                                Folder = 'GrndCon'+self.OS_Sys_sep+''
                                SpaGrndCon=3
                            else:
                                SpaGrndCon=0
                            strInfo = ''
                            if (SHOfalg == 1):
                                strInfo = strInfo+'_SHO'
                            strInfo = strInfo+'_'+self.lbl_EPS_I_Gen_SC.cget("text")
                            
                            if (self.selected_EPS_I_NOAA_BOS.get()==True):
                                strInfo = strInfo+'_NOAA_BOS'
                            if (self.selected_EPS_I_Weekly.get()==True):
                                strInfo = strInfo+'_DailyEvents'
                            if (self.MSW_info[0]==1):
                                strInfo = strInfo+'_MissionSwap'
                            if (self.XTTC_FBK_info[0]==1):
                                strInfo = strInfo+'_XTTCFBK'
                            i_filename ='uberlogBatch_from_'+strShiftfilename_from+'_to_'+strShiftfilename_to+'_'+strEPSSide+''+strInfo
                            i_TC_Pass_M = mergeWimpy( Global_frame_TC, 1, new_DS, new_DE , self.MSW_info)
                            
                            
                            file_Path_Name_csv = self.DesktopPath+i_filename+'.csv'
                            fcn_wimpy_csv( i_TC_Pass_M, file_Path_Name_csv, new_DS, new_DE, SpaGrndCon, opts , SHOfalg, self.XTTC_FBK_info, self.Man_info )
# =============================================================================
#                             file_Path_Name_csv = self.+Folder+i_filename+'.csv'
#                             fcn_wimpy_csv( i_TC_Pass_M, file_Path_Name_csv, new_DS, new_DE, SpaGrndCon, opts , SHOfalg, self.XTTC_FBK_info, self.Man_info )
# =============================================================================
                        
                        proges_per100 = int(100)
                        self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                        self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Generation completed successfully ('+str(proges_per100)+'%)')
                        self.PW_EPS_I_Gen.update_idletasks()
                else:
                    proges_per100 = int(0)
                    self.ProgressBar_EPS_I_DataGenLoadingbar['value'] = proges_per100
                    self.Style_EPS_I_DataGenLoadingbar.configure("text.Horizontal.TProgressbar", text='Loading ('+str(proges_per100)+'%)')
                    self.PW_EPS_I_Gen.update_idletasks()
    # end def
    
    
    def onExit(self):
        self.quit()
    # end def
    
    def HelpInfo(self):
        messagebox.showinfo(title="About "+self.SW_title, message='Developed by Matteo Nicoli')
    # end def
    
# end class









def main():
    root = tk.Tk()
    root.geometry("620x550+300+300")
    app = GUI_EUMETSAT()
    root.mainloop()
# end def











if __name__ == '__main__':
    main()
# end if