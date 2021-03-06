# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:47:19 2020

@author: Nicoli
"""

import tkinter as tk
from tkinter import Frame, messagebox, scrolledtext 

from GEMS.GEMS_Mang import *


def Destroy_GEMS_Manager(self):
    if (hasattr(self, 'PW_GEMS_Manager') == True):
        self.PW_GEMS_Manager.destroy()
    # end if
    if (hasattr(self, 'PW_GEMS_Event') == True):
        self.PW_GEMS_Event.destroy()
    # end if
    if (hasattr(self, 'PW_GEMS_Gen') == True):
        self.PW_GEMS_Gen.destroy()
    # end if
    if (hasattr(self, 'PW_GEMS_ManagerLog') == True):
        self.PW_GEMS_ManagerLog.destroy()
    # end if
    return self
# end def











def Layout_GEMS_Mang(self):
    self.PW_GEMS_Manager = tk.PanedWindow(self.master, orient = 'vertical')
    self.PW_GEMS_Manager.pack(fill = tk.X )
    
    
    
    self.Fr_GEMS_Side = tk.Frame(self.PW_GEMS_Manager)
    self.Fr_GEMS_Side.pack(fill = tk.X, expand=True)
    
    #
    self.Fr_GEMS_SideS = tk.Frame(self.Fr_GEMS_Side)
    self.Fr_GEMS_SideS.pack(fill = tk.X, side='left', expand=True)
    
    self.sel_SideS = tk.BooleanVar()
    self.sel_SideS.set(False)
# =============================================================================
#     if (self.EPS_I_ShiftSide[1]=='S' or self.EPS_I_ShiftSide[1]=='SG'):
#         self.selected_EPS_I_SideS.set(True)
#     # end if
# =============================================================================
    chk_SideContrS = tk.ttk.Checkbutton(self.Fr_GEMS_SideS, text='SpaCon', var=self.sel_SideS, command = None )
    chk_SideContrS.pack()
    
    
    #
    self.Fr_GEMS_SideG = tk.Frame(self.Fr_GEMS_Side)
    self.Fr_GEMS_SideG.pack(fill = tk.X, side='right', expand=True)
    
    self.sel_GEMS_SideG = tk.BooleanVar()
    self.sel_GEMS_SideG.set(False)
# =============================================================================
#     if (self.EPS_I_ShiftSide[1]=='G' or self.EPS_I_ShiftSide[1]=='SG'):
#         self.selected_EPS_I_SideG.set(True)
#     # end if
# =============================================================================
    chk_SideContrG = tk.ttk.Checkbutton(self.Fr_GEMS_SideG, text='GrndCon', var=self.sel_GEMS_SideG, command = None )
    chk_SideContrG.pack()
    
    
    
    
    
    #
    self.Fr_GEMS_URL = tk.Frame(self.PW_GEMS_Manager)
    self.Fr_GEMS_URL.pack(fill = tk.X, expand=True)
    
    lbl_GEMS_URL = tk.Label(self.Fr_GEMS_URL, text="GEMS URL:", anchor='w')
    lbl_GEMS_URL.pack(side='left')
    
    #self.Fr_GEMS_URL2 = tk.Frame(self.Fr_GEMS_URL)
    #self.Fr_GEMS_URL2.pack(fill = tk.X, expand=True)
    
    self.strv_GEMS_URL = tk.StringVar()
    self.entry_GEMS_URL = tk.Entry(self.Fr_GEMS_URL , textvariable=self.strv_GEMS_URL, validate="focusout")
    #self.entry_GEMS_URL = tk.Entry(self.PW_GEMS, width=20, textvariable=self.GEMS_URL, validate="focusout", validatecommand=self.Summary_EPS_I_UpadateDataEnd)
    self.entry_GEMS_URL.pack( side='left', fill = tk.X, expand=True)
    
    
    
    #
    self.Fr_GEMS_Res = tk.Frame(self.PW_GEMS_Manager)
    self.Fr_GEMS_Res.pack(fill = tk.X, expand=True)
    
    
    self.data_Response = {} # dictionary to store all the IntVars
    self.Response_list = ['Logged','e-mail','Call']
    self.Response_list_Bool = [False]*len(self.Response_list)
    def GEMS_update_Response(var_name, *args):
        str_Res = ''
        for idata in range(0,len(self.data_Response)):
            # Get the actual var from the dict
            iResponse = self.Response_list[idata]
            var_Response = self.data_Response[iResponse]
            if ( var_Response.get() == True ):
                str_Res = str_Res + iResponse+'+'
                self.Response_list_Bool[idata] = True
            else:
                self.Response_list_Bool[idata] = False
            
            if (self.Response_list_Bool[1] == True):
                self.mb_email.config(state=tk.NORMAL)
                self.mb_emailCC.config(state=tk.NORMAL)
            else:
                self.mb_email.config(state=tk.DISABLED)
                self.mb_emailCC.config(state=tk.DISABLED)
            
            if (self.Response_list_Bool[2] == True):
                self.mb_call.config(state=tk.NORMAL)
            else:
                self.mb_call.config(state=tk.DISABLED)
                
                
        self.Response.set("Response")
    
    self.Response = tk.StringVar(value="Response")
    self.mb_Response = tk.Menubutton ( self.Fr_GEMS_Res, textvariable=self.Response, width=9, relief=tk.RAISED )
    self.mb_Response.menu  =  tk.Menu ( self.mb_Response, tearoff = 0 )
    self.mb_Response["menu"]  =  self.mb_Response.menu
    for iResponse_list in self.Response_list:
        var = tk.BooleanVar(name = iResponse_list)
        var.trace("w", GEMS_update_Response)
        self.mb_Response.menu.add_checkbutton(label=iResponse_list, variable=var)
        self.data_Response[iResponse_list] = var
    self.mb_Response.pack(side='left')
    
    
    
    self.selected_GEMS_Merge = tk.BooleanVar()
    self.selected_GEMS_Merge.set(False)
    chk_GEMS_Merge = tk.ttk.Checkbutton(self.Fr_GEMS_Res, text='Merge', var=self.selected_GEMS_Merge )
    chk_GEMS_Merge.pack(side='left')
    
    
    
    #
    self.Fr_GEMS_email = tk.Frame(self.PW_GEMS_Manager)
    self.Fr_GEMS_email.pack(fill = tk.X, expand=True)
    
    
    self.data_email = {} # dictionary to store all the IntVars
    self.email_list = ['e-mail Controller','e-mail Analyst']
    self.email_list_Bool = [False]*len(self.email_list)
    def GEMS_update_email(var_name, *args):
        str_Res = ''
        for idata in range(0,len(self.data_email)):
            var_email = self.data_email[self.email_list[idata]]
            if var_email.get() == True:
                self.email_list_Bool[idata] = True
            else:
                self.email_list_Bool[idata] = False
    self.email = tk.StringVar(value="e-mail")
    self.mb_email = tk.Menubutton ( self.Fr_GEMS_email, textvariable=self.email, width=9, relief=tk.RAISED )
    self.mb_email.menu  =  tk.Menu ( self.mb_email, tearoff = 0 )
    self.mb_email["menu"]  =  self.mb_email.menu
    for iemail_list in self.email_list:
        variemail_list = tk.BooleanVar(name = iemail_list)
        variemail_list.trace("w", GEMS_update_email)
        self.mb_email.menu.add_checkbutton(label=iemail_list, variable=variemail_list)
        self.data_email[iemail_list] = variemail_list
    self.mb_email.pack(side='left')
    self.mb_email.config(state=tk.DISABLED)
    #self.mb_email.config(state=tk.NORMAL)
    
    self.strv_GEMS_email = tk.StringVar()
    self.entry_GEMS_email = tk.Entry(self.Fr_GEMS_email , textvariable=self.strv_GEMS_email, validate="focusout")
    #self.entry_GEMS_URL = tk.Entry(self.PW_GEMS, width=20, textvariable=self.GEMS_URL, validate="focusout", validatecommand=self.Summary_EPS_I_UpadateDataEnd)
    self.entry_GEMS_email.pack( side='left', fill = tk.X, expand=True)
    
    
    
    
    #
    self.Fr_GEMS_emailCC = tk.Frame(self.PW_GEMS_Manager)
    self.Fr_GEMS_emailCC.pack(fill = tk.X, expand=True)
    
    
    self.data_emailCC = {} # dictionary to store all the IntVars
    self.emailCC_list = ['e-mail Controller','Controller']
    self.emailCC_list_Bool = [False]*len(self.emailCC_list)
    def GEMS_update_emailCC(var_name, *args):
        str_Res = ''
        for idata in range(0,len(self.data_emailCC)):
            var_emailCC = self.data_emailCC[self.emailCC_list[idata]]
            if var_emailCC.get() == True:
                self.emailCC_list_Bool[idata] = True
            else:
                self.emailCC_list_Bool[idata] = False
    self.emailCC = tk.StringVar(value="e-mail CC")
    self.mb_emailCC = tk.Menubutton ( self.Fr_GEMS_emailCC, textvariable=self.emailCC, width=9, relief=tk.RAISED )
    self.mb_emailCC.menu  =  tk.Menu ( self.mb_emailCC, tearoff = 0 )
    self.mb_emailCC["menu"]  =  self.mb_emailCC.menu
    for iemailCC_list in self.emailCC_list:
        variemailCC_list = tk.BooleanVar(name = iemailCC_list)
        variemailCC_list.trace("w", GEMS_update_emailCC)
        self.mb_emailCC.menu.add_checkbutton(label=iemailCC_list, variable=variemailCC_list)
        self.data_emailCC[iemailCC_list] = variemailCC_list
    self.mb_emailCC.pack(side='left')
    self.mb_emailCC.config(state=tk.DISABLED)
    #self.mb_emailCC.config(state=tk.NORMAL)
    
    self.strv_GEMS_emailCC = tk.StringVar()
    self.entry_GEMS_emailCC = tk.Entry(self.Fr_GEMS_emailCC , textvariable=self.strv_GEMS_emailCC, validate="focusout")
    #self.entry_GEMS_URL = tk.Entry(self.PW_GEMS, width=20, textvariable=self.GEMS_URL, validate="focusout", validatecommand=self.Summary_EPS_I_UpadateDataEnd)
    self.entry_GEMS_emailCC.pack( side='left', fill = tk.X, expand=True)
    
    
    #
    self.Fr_GEMS_Call = tk.Frame(self.PW_GEMS_Manager)
    self.Fr_GEMS_Call.pack(fill = tk.X, expand=True)
    
    self.data_call = {} # dictionary to store all the IntVars
    self.call_list = ['Duty analyst','Duty SOE', 'Duty MCS']
    self.call_list_Bool = [False]*len(self.call_list)
    def GEMS_update_call(var_name, *args):
        str_Res = ''
        for idata in range(0,len(self.data_call)):
            var_call = self.data_call[self.call_list[idata]]
            if var_call.get() == True:
                self.call_list_Bool[idata] = True
            else:
                self.call_list_Bool[idata] = False
    self.call = tk.StringVar(value="Call")
    self.mb_call = tk.Menubutton ( self.Fr_GEMS_Call, textvariable=self.call, width=9, relief=tk.RAISED  )
    self.mb_call.menu  =  tk.Menu ( self.mb_call, tearoff = 0 )
    self.mb_call["menu"]  =  self.mb_call.menu
    for icall_list in self.call_list:
        var = tk.BooleanVar(name = icall_list)
        var.trace("w", GEMS_update_call)
        self.mb_call.menu.add_checkbutton(label=icall_list, variable=var)
        self.data_call[icall_list] = var
    self.mb_call.pack(side='left')
    self.mb_call.config(state=tk.DISABLED)
    
    
    
    
    #
    self.PW_GEMS_Event = tk.PanedWindow(self.master, orient = 'vertical')
    self.PW_GEMS_Event.pack(fill = tk.X )
    
    self.Fr_GEMS_Event_btn = tk.Frame(self.PW_GEMS_Event)
    self.Fr_GEMS_Event_btn.pack(fill = tk.X, side='left')
    
    self.lbl_GEMS_Comment = tk.Label(self.Fr_GEMS_Event_btn, text="")
    self.lbl_GEMS_Comment.pack(fill = tk.X)
    
    
    
    
    
    
    
    
    
    
    
    
    self.GEMS_Info = []
    self.selected_GEMS = []
    self.nlist_chk_iGEMS = -1
    self.list_chk_iGEMS = {}
    #btn_GEMS_URL_p = tk.ttk.Button(self.Fr_GEMS_URL, text = "+", width=3 )
    btn_GEMS_URL_p = tk.ttk.Button(self.Fr_GEMS_Event_btn, text = "+", width=10, command = lambda: btn_GEMS_URLp(self) )
    btn_GEMS_URL_p.pack()
    
    
    
    self.Fr_GEMS_Event_scrtx = tk.Frame(self.PW_GEMS_Event)
    self.Fr_GEMS_Event_scrtx.pack(fill = tk.X, side='right', expand=True)
    
    
    self.lbl_GEMS_Comment = tk.Label(self.Fr_GEMS_Event_scrtx, text="Comment")
    self.lbl_GEMS_Comment.pack(fill = tk.X)
    
    self.scrtx_GEMS_Event = scrolledtext.ScrolledText( self.Fr_GEMS_Event_scrtx, height=8)
    self.scrtx_GEMS_Event.pack(fill = tk.X)
    
    
    
    
    
    #
    self.PW_GEMS_Gen = tk.PanedWindow(self.master, orient = 'vertical')
    self.PW_GEMS_Gen.pack(fill = tk.X )
    
    btn_GEMS_Gen = tk.ttk.Button(self.PW_GEMS_Gen, text = "GEMS Generate", command = lambda: btn_GEMS_Generate(self))
    #btn_GEMS_Gen = tk.ttk.Button(self.PW_GEMS_Manager, text = "GEMS Generate")
    btn_GEMS_Gen.pack(fill = tk.X)
    
    
    self.lbl_GEMS_LogArea = tk.Label(self.PW_GEMS_Gen, text="Events Log")
    self.lbl_GEMS_LogArea.pack(fill = tk.X)
    
    
    
    
    self.PW_GEMS_ManagerLog = tk.PanedWindow(self.master, orient = 'vertical')
    self.PW_GEMS_ManagerLog.pack(fill = tk.X )
    self.i_row_PW_GEMS_Manager = 0
    i_column_PW_GEMS_Manager = 0
    
    
    self.selected_allGEMS = tk.BooleanVar()
    self.selected_allGEMS.set(True)
    chk_SideContrS = tk.ttk.Checkbutton(self.PW_GEMS_ManagerLog, text='All', var=self.selected_allGEMS, command = lambda: All_GEMS_sel(self) )
    chk_SideContrS.grid(row = self.i_row_PW_GEMS_Manager, column = i_column_PW_GEMS_Manager )
    
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_fac = tk.Label(self.PW_GEMS_ManagerLog, text="Facility")
    lbl_GEMS_fac.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_fac = tk.Label(self.PW_GEMS_ManagerLog, text="Sev.")
    lbl_GEMS_fac.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_ST = tk.Label(self.PW_GEMS_ManagerLog, text="Start Date")
    lbl_GEMS_ST.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_ET = tk.Label(self.PW_GEMS_ManagerLog, text="End Date")
    lbl_GEMS_ET.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_ET = tk.Label(self.PW_GEMS_ManagerLog, text="Merge")
    lbl_GEMS_ET.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
# =============================================================================
#         i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
#         lbl_GEMS_ET = tk.Label(self.PW_GEMS_ManagerLog, text="Response")
#         lbl_GEMS_ET.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
# =============================================================================
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_ET = tk.Label(self.PW_GEMS_ManagerLog, text="e-mail")
    lbl_GEMS_ET.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_ET = tk.Label(self.PW_GEMS_ManagerLog, text="Call")
    lbl_GEMS_ET.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
    i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
    lbl_GEMS_ET = tk.Label(self.PW_GEMS_ManagerLog, text="Comment")
    lbl_GEMS_ET.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
    
    self.i_row_PW_GEMS_Manager = self.i_row_PW_GEMS_Manager + 1
    
    #self.scrtx_GEMS_LogArea = scrolledtext.ScrolledText( self.PW_GEMS_Manager , state="disabled" )
    #self.scrtx_GEMS_LogArea.pack(fill = tk.BOTH)
    
    return self
# end def











def i_GEMS_info(self, GEMS_info_list):
    GEMS_Merge = self.selected_GEMS_Merge.get()
    GEMS_Log   = self.data_Response[self.Response_list[0]].get()
    
    
    iGEMS_email = []
    for idata in range(0,len(self.data_email)):
        var = self.data_email[self.email_list[idata]]
        if var.get() == True:
            iGEMS_email.append(self.email_list[idata])
            self.data_email[self.email_list[idata]].set(False)
    GEMS_email = [ self.data_Response[self.Response_list[1]].get(), iGEMS_email ]
    
    iGEMS_call = []
    for idata in range(0,len(self.data_call)):
        var = self.data_call[self.call_list[idata]]
        if var.get() == True:
            iGEMS_call.append(self.call_list[idata])
            self.data_call[self.call_list[idata]].set(False)
    GEMS_call  = [ self.data_Response[self.Response_list[2]].get(), iGEMS_call ]
    
    GEMS_comme = self.scrtx_GEMS_Event.get("1.0", tk.END)
    
    iGEMS_info_list = GEMS_info_list + [
        GEMS_Merge,
        GEMS_Log,
        GEMS_email,
        GEMS_call,
        GEMS_comme ]
    
    
    self.GEMS_Info.append( iGEMS_info_list )
    
    for idata in range(0,len(self.data_Response)):
        self.data_Response[self.Response_list[idata]].set(False)
    
    self.selected_GEMS_Merge.set(False)
    
    return iGEMS_info_list
# end def











def btn_GEMS_URLp(self):
    GEMS_URL = self.strv_GEMS_URL.get()
    
    #GEMS_info_list = acq_GEMS_Info(GEMS_URL)
    GEMS_info_list = [True, GEMS_URL, GEMS_URL, 'A+W+I', GEMS_URL, GEMS_URL , '' ]
    
    Flag_GEMS_URL = True
    
    if ( Flag_GEMS_URL == True ):
        
        iGEMS_info_list = i_GEMS_info(self, GEMS_info_list)
        print(iGEMS_info_list)
        
        i_column_PW_GEMS_Manager = 0
        
        selected_iGEMS = tk.BooleanVar()
        selected_iGEMS.set(True)
        self.selected_GEMS.append(selected_iGEMS)
        
        self.nlist_chk_iGEMS = self.nlist_chk_iGEMS + 1
        self.list_chk_iGEMS[self.nlist_chk_iGEMS] = tk.ttk.Checkbutton(self.PW_GEMS_ManagerLog, text='', var=selected_iGEMS )
        self.list_chk_iGEMS[self.nlist_chk_iGEMS].grid(row = self.i_row_PW_GEMS_Manager, column = i_column_PW_GEMS_Manager )
        
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        lbl_GEMS_fac = tk.Label(self.PW_GEMS_ManagerLog, text=iGEMS_info_list[2])
        lbl_GEMS_fac.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        lbl_GEMS_sev = tk.Label(self.PW_GEMS_ManagerLog, text=iGEMS_info_list[3])
        lbl_GEMS_sev.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager)
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        lbl_GEMS_ST = tk.Label(self.PW_GEMS_ManagerLog, text=iGEMS_info_list[4])
        lbl_GEMS_ST.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        lbl_GEMS_ET = tk.Label(self.PW_GEMS_ManagerLog, text=iGEMS_info_list[5])
        lbl_GEMS_ET.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager, sticky="W")
        
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        Text_lbl_GEMS_Merge = 'NO'
        if (iGEMS_info_list[7] == True):
            Text_lbl_GEMS_Merge = 'YES'
        lbl_GEMS_Merge = tk.Label(self.PW_GEMS_ManagerLog, text=Text_lbl_GEMS_Merge)
        lbl_GEMS_Merge.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager)
        
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        Text_lbl_GEMS_email = 'NO'
        if (iGEMS_info_list[9][0] == True):
            Text_lbl_GEMS_email = 'YES'
        lbl_GEMS_email = tk.Label(self.PW_GEMS_ManagerLog, text=Text_lbl_GEMS_email)
        lbl_GEMS_email.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager)
        
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        Text_lbl_GEMS_call = 'NO'
        if (iGEMS_info_list[10][0] == True):
            Text_lbl_GEMS_call = 'YES'
        lbl_GEMS_call = tk.Label(self.PW_GEMS_ManagerLog, text=Text_lbl_GEMS_call)
        lbl_GEMS_call.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager)
        
        
        i_column_PW_GEMS_Manager = i_column_PW_GEMS_Manager + 1
        Text_lbl_GEMS_comm = 'NO'
        if (iGEMS_info_list[11] != '\n' ):
            Text_lbl_GEMS_comm = 'YES'
        lbl_GEMS_comm = tk.Label(self.PW_GEMS_ManagerLog, text=Text_lbl_GEMS_comm)
        lbl_GEMS_comm.grid(row = self.i_row_PW_GEMS_Manager, column=i_column_PW_GEMS_Manager)
        
        
        self.i_row_PW_GEMS_Manager = self.i_row_PW_GEMS_Manager + 1
    
# end def











def btn_GEMS_Generate(self):
    GEMS_URL = self.strv_GEMS_URL.get()
    #GEMS_info_list = acq_GEMS_Info(GEMS_URL)
    GEMS_info_list = [True, GEMS_URL]
    
    Flag_GEMS_URL = True
    
    if ( Flag_GEMS_URL == True ):
        self.i_GEMS_info(GEMS_info_list)
        if (len(self.GEMS_Info) == 0 and GEMS_URL > 0 ):
            GEMS_info_list = GEMS_URL
            
    
# end def











def All_GEMS_sel( self ):
    for iGEMS in range(0,len(self.list_chk_iGEMS)):
        self.selected_GEMS[iGEMS].set(self.selected_allGEMS.get())
# end def