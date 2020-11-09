# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:47:35 2020

@author: matte
"""
import tkinter as tk
from tkinter import Frame, messagebox, scrolledtext 







def Destroy_MCS_OOL(self):
    if (hasattr(self, 'PW_MCS_OOL') == True):
        self.PW_MCS_OOL.destroy()
    # end if
    return self
# end def











def Layout_MCS_OOL(self):
    self.PW_MCS_OOL = tk.PanedWindow(self.master, orient = 'vertical')
    self.PW_MCS_OOL.pack(fill = tk.X )
    
    self.Fr_MCS_OOL_SpaCon = tk.Frame(self.PW_MCS_OOL)
    self.Fr_MCS_OOL_SpaCon.pack(fill = tk.X, side='left', expand=True)
    
    
    
    self.selected_MCS_OOL_SideS = tk.BooleanVar()
    self.selected_MCS_OOL_SideS.set(False)
# =============================================================================
#     if (self.EPS_I_ShiftSide[1]=='S' or self.EPS_I_ShiftSide[1]=='SG'):
#         self.selected_EPS_I_SideS.set(True)
#     # end if
# =============================================================================
    chk_SideContrS = tk.ttk.Checkbutton(self.Fr_MCS_OOL_SpaCon, text='SpaCon', var=self.selected_MCS_OOL_SideS, command = None )
    chk_SideContrS.pack()
    
    
    #
    self.Fr_MCS_OOL_Res = tk.Frame(self.PW_MCS_OOL_Manager)
    self.Fr_MCS_OOL_Res.pack(fill = tk.X, expand=True)
    
    
    self.data_Response = {} # dictionary to store all the IntVars
    self.Response_list = ['Logged','e-mail','Call']
    self.Response_list_Bool = [False]*len(self.Response_list)
    def MCS_OOL_update_Response(var_name, *args):
        str_Res = ''
        for idata in range(0,len(self.data_Response)):
            # Get the actual var from the dict
            iResponse = self.Response_list[idata]
            var = self.data_Response[iResponse]
            if var.get() == True:
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
    self.mb_Response = tk.Menubutton ( self.Fr_MCS_OOL_Res, textvariable=self.Response, width=9, relief=tk.RAISED )
    self.mb_Response.menu  =  tk.Menu ( self.mb_Response, tearoff = 0 )
    self.mb_Response["menu"]  =  self.mb_Response.menu
    for iResponse_list in self.Response_list:
        var = tk.BooleanVar(name = iResponse_list)
        var.trace("w", MCS_OOL_update_Response)
        self.mb_Response.menu.add_checkbutton(label=iResponse_list, variable=var)
        self.data_Response[iResponse_list] = var
    self.mb_Response.pack(side='left')
    
    
    
    self.selected_MCS_OOL_Merge = tk.BooleanVar()
    self.selected_MCS_OOL_Merge.set(False)
    chk_MCS_OOL_Merge = tk.ttk.Checkbutton(self.Fr_MCS_OOL_Res, text='Merge', var=self.selected_MCS_OOL_Merge )
    chk_MCS_OOL_Merge.pack(side='left')
    
    
    
    #
    self.Fr_MCS_OOL_email = tk.Frame(self.PW_MCS_OOL_Manager)
    self.Fr_MCS_OOL_email.pack(fill = tk.X, expand=True)
    
    
    self.data_email = {} # dictionary to store all the IntVars
    self.email_list = ['e-mail Controller','e-mail Analyst']
    self.email_list_Bool = [False]*len(self.email_list)
    def MCS_OOL_update_email(var_name, *args):
        str_Res = ''
        for idata in range(0,len(self.data_email)):
            var = self.data_email[self.email_list[idata]]
            if var.get() == True:
                self.email_list_Bool[idata] = True
            else:
                self.email_list_Bool[idata] = False
    self.email = tk.StringVar(value="e-mail")
    self.mb_email = tk.Menubutton ( self.Fr_MCS_OOL_email, textvariable=self.email, width=9, relief=tk.RAISED, state='disable' )
    self.mb_email.menu  =  tk.Menu ( self.mb_email, tearoff = 0 )
    self.mb_email["menu"]  =  self.mb_email.menu
    for iemail_list in self.email_list:
        variemail_list = tk.BooleanVar(name = iemail_list)
        variemail_list.trace("w", MCS_OOL_update_email)
        self.mb_email.menu.add_checkbutton(label=iemail_list, variable=variemail_list)
        self.data_email[iemail_list] = variemail_list
    self.mb_email.pack(side='left')
    self.mb_email.config(state=tk.DISABLED)
    #self.mb_email.config(state=tk.NORMAL)
    
    self.strv_GEMS_email = tk.StringVar()
    self.entry_GEMS_email = tk.Entry(self.Fr_GEMS_email , textvariable=self.strv_GEMS_email, validate="focusout")
    #self.entry_GEMS_URL = tk.Entry(self.PW_GEMS, width=20, textvariable=self.GEMS_URL, validate="focusout", validatecommand=self.Summary_EPS_I_UpadateDataEnd)
    self.entry_GEMS_email.pack( side='left', fill = tk.X, expand=True)
    
    
    
    self.Fr_MCS_OOL_GrnCon = tk.Frame(self.PW_MCS_OOL)
    self.Fr_MCS_OOL_GrnCon.pack(fill = tk.X, side='right', expand=True)
    
    self.selected_MCS_OOL_SideG = tk.BooleanVar()
    self.selected_MCS_OOL_SideG.set(False)
# =============================================================================
#     if (self.EPS_I_ShiftSide[1]=='G' or self.EPS_I_ShiftSide[1]=='SG'):
#         self.selected_EPS_I_SideG.set(True)
#     # end if
# =============================================================================
    chk_SideContrG = tk.ttk.Checkbutton(self.Fr_MCS_OOL_GrnCon, text='GrndCon', var=self.selected_MCS_OOL_SideG, command = None )
    chk_SideContrG.pack()
    
    return self
#end def