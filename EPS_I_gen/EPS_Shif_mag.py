# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:28:17 2020

@author: Nicoli
"""
from os import path
import time
import datetime
#from datetime import timezone
import calendar

import xlwings as xw

#import pandas as pd
from pandas import read_csv


def EPS_Shift_List_Rec(now_local, WinUserName, file_Path_Name_Shift, file_Path_Name_Controller):
    Controllers = read_csv(file_Path_Name_Controller)
    
    Worksheet = calendar.month_name[now_local.month]+' '+str(now_local.year)    
    Name_Cell_Col = 'B'
    Months_Day_Cell_Col = ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG']
    Month_Day_Cell_Col = Months_Day_Cell_Col[now_local.day-1]
    
    flag_CN = 0
    
    Controller_XTTC_PreBrief = [0,0,0]
    for i_Name in range(0,Controllers.shape[0]):
        if (WinUserName == Controllers.loc[i_Name,['Users']]['Users']):
            ControllerName = Controllers.loc[i_Name,['Name']]['Name']+' '+Controllers.loc[i_Name,['Surname']]['Surname']
            CN = Controllers.loc[i_Name,['Name']]['Name']
            flag_CN = 1
            Controller_XTTC_PreBrief[1] = Controllers.loc[i_Name,['XTTC_PreBrief']]['XTTC_PreBrief']
            Controller_XTTC_PreBrief[2] = i_Name
            
            
    if (flag_CN==1):
        app = xw.App(visible=False) # IF YOU WANT EXCEL TO RUN IN BACKGROUND
        
        xlwb = xw.Book(file_Path_Name_Shift)
        xlws = {}
        xlws['ws1'] = xlwb.sheets[Worksheet]
        
        
        
        
        cel_row = 0
        flag_Name = 1
        while (flag_Name == 1):
            cel_row = cel_row + 1
            Name_Cell = Name_Cell_Col+str(cel_row)
            NameControllers = xlws['ws1'].range(Name_Cell).value
            if (NameControllers == ControllerName):
                flag_Name = 0
            if (cel_row > 40):
                flag_Name = 0
            
        Month_Day_Cell = Month_Day_Cell_Col+str(cel_row)
        Shift_Time = xlws['ws1'].range(Month_Day_Cell).value
        if (Shift_Time=='M'):
            Shift = 1
        elif (Shift_Time=='E'):
            Shift = 2
        elif (Shift_Time=='N1' or Shift_Time=='N2', Shift_Time=='N'):
            Shift = 3
        else:
            Shift = 0
        
        
        Shift_Side = xlws['ws1'].range(Month_Day_Cell).color
        
        if (Shift_Side==(146, 208, 80)):
            Side = 'G'
        elif (Shift_Side==(0, 176, 240)):
            Side = 'S'
        elif (Shift_Side==(255, 192, 0) or Shift_Side==(237, 125, 49) ):
            Side = 'SG'
        else:
            Side = 0
        
        EPS_ShiftSide = [Shift, Side, CN]
        
        app.kill()
        del xlws
    else:
        EPS_ShiftSide = [0, 0, 'Controller']
    
    return EPS_ShiftSide, Controller_XTTC_PreBrief, Controllers












def EPS_MS_Scheduled(file_Path_Name_MS):
    Worksheet = 'Schedule'
    app = xw.App(visible=False) # IF YOU WANT EXCEL TO RUN IN BACKGROUND
    
    xlwb = xw.Book(file_Path_Name_MS)
    Worksheet_n = 0
    sheet = xlwb.sheets[Worksheet_n]
    Worksheet = sheet.name
    
    xlws = {}
    xlws['ws1'] = xlwb.sheets[Worksheet]
    
    Title = xlws['ws1'].range('A1').value
    
    def Date_Time(Title1,Cell_CDA_Time):
        Datestr_YYYY = int(Title[-11:-7])
        Datestr_mm = int(Title[-14:-12])
        Datestr_DD = int(Title[-17:-15])
        
        CDA1_AOS = xlws['ws1'].range(Cell_CDA_Time).value
        
        Datestr_HH = int(CDA1_AOS*24)
        Datestr_MM = int((CDA1_AOS*24-Datestr_HH)*60)
        Datestr_SS = int(((CDA1_AOS*24-Datestr_HH)*60-Datestr_MM)*60)
        
        date = datetime.datetime(Datestr_YYYY, Datestr_mm, Datestr_DD, Datestr_HH, Datestr_MM, Datestr_SS, 0*1000)
        return date
    
    def Date_Time_str(date):
        mm = str(date.month)
        if (date.month<10):
            mm = '0'+mm
        DD = str(date.day)
        if (date.day<10):
            DD = '0'+DD
        HH = str(date.hour)
        if (date.hour<10):
            HH = '0'+HH
        MM = str(date.minute)
        if (date.minute<10):
            MM = '0'+MM
        SS = str(date.second)
        if (date.second<10):
            SS = '0'+SS
        datestr = str(date.year)+'-'+mm+'-'+DD+' '+HH+':'+MM+':'+SS
        return datestr
    
    cel_row = 3
    flag_MS_SE = 1
    flag_MS_S = 1
    flag_MS_E = 0
    while (flag_MS_SE == 1):
        cel_row = cel_row + 1
        Cell_SC = 'A'+str(cel_row)
        Name_SC = xlws['ws1'].range(Cell_SC).value
        
        Cell_CDA1_AOS = 'B'+str(cel_row)
        CDA1_color = xlws['ws1'].range(Cell_CDA1_AOS).color
        
        Cell_CDA2_AOS = 'E'+str(cel_row)
        CDA2_color = xlws['ws1'].range(Cell_CDA2_AOS).color
        
        if (flag_MS_E==1):
            if (CDA1_color==(255, 255, 0) or CDA2_color==(255, 255, 0)):
                flag_MS_E = 0
                Cell_CDA1_LOS = 'C'+str(cel_row)
                Date_MS_E = Date_Time(Title,Cell_CDA1_LOS)
                Date_MS_E = Date_MS_E + datetime.timedelta(minutes=1)
                Date_MS_E_str = Date_Time_str(Date_MS_E)
                flag_MS_SE = 0
        if (flag_MS_S==1):
            if (CDA1_color==(255, 255, 0) or CDA2_color==(255, 255, 0)):
                flag_MS_S = 0
                flag_MS_E = 1
                Cell_CDA1_LOS = 'C'+str(cel_row)
                Date_MS_S = Date_Time(Title,Cell_CDA1_LOS)
                Date_MS_S = Date_MS_S + datetime.timedelta(minutes=1)
                Date_MS_S_str = Date_Time_str(Date_MS_S)
        
        if (Name_SC == None or cel_row > 40):
            flag_MS_SE = 0
            
    
    MS_Scheduled = [Date_MS_S_str, Date_MS_E_str,Date_MS_S,Date_MS_E]
    app.kill()
    del xlws
    return MS_Scheduled











def OpsSch_Schedule(file_Path_Name_OpsSch,SC_Name):
    #Worksheet1 = 'Current Week'
    #Worksheet2 = 'Weekly Schedule'
    
    def XTTC_info(info, date):
        
# =============================================================================
#         flag = 1
#         niter = 0
#         breakp = [0]
#         while (flag==1):
#             niter = niter + 1
#             test = info[niter-1:niter]
#             if (niter!=breakp[-1]+1):
#                 if (test ==' ' or test =='\n' or test ==':' or test =='-'):
#                     breakp.append(niter)
#             if (niter>=len(info)):
#                 flag = 0
# =============================================================================
        n = []
        for i_info in range(0,len(info)+1):
            let = info[i_info-1:i_info]
            if (let=='0' or let=='1' or let=='2' or let=='3' or let=='4' or let=='5' or let=='6' or let=='7' or let=='8' or let=='9'):
                n.append(let)
        
        
        Metop2 = n[1]
        if (Metop2[-1:]=='1' or Metop2[-1:]=='2' or Metop2[-1:]=='3'):
            for i_SC in range(0,len(SC_Name)):
                if (int(Metop2[-1:])==SC_Name[i_SC][1]):
                    Metop1 = 'MetOp-'+SC_Name[i_SC][0]
        else:
            Metop1 = ''
            
        nOrbitstr =  n[-len(n)+2:-8]
        nOrbit = ''
        for i_nOrbit in range(0,len(nOrbitstr)):
            nOrbit = nOrbit + nOrbitstr[i_nOrbit]
        
        
        nHHstr =  n[-8:-6]
        HHstr = ''
        for i_HHstr in range(0,len(nHHstr)):
            HHstr = HHstr + nHHstr[i_HHstr]
        
        
        nMMstr =  n[-6:-4]
        MMstr = ''
        for i_MMstr in range(0,len(nMMstr)):
            MMstr = MMstr + nMMstr[i_MMstr]
        
        
        HH=int(HHstr)
        MM=int(MMstr)
        date = date +datetime.timedelta(hours=HH)+ datetime.timedelta(minutes=MM)
        return Metop1, nOrbit, date
    
    def Date_Manouver(info):
        n = []
        for i_info in range(0,len(info)+1):
            let = info[i_info-1:i_info]
            if (let=='0' or let=='1' or let=='2' or let=='3' or let=='4' or let=='5' or let=='6' or let=='7' or let=='8' or let=='9'):
                n.append(let)
        HH = int("".join(map(str, n[:2])))
        MM = int("".join(map(str, n[2:])))
        return HH, MM
    
    def OPSSCH(Worksheet_n):
        app = xw.App(visible=False) # IF YOU WANT EXCEL TO RUN IN BACKGROUND
        xlwb = xw.Book(r''+file_Path_Name_OpsSch)
        your_macro = xlwb.macro('EPS Schedule')
        sheet = xlwb.sheets[Worksheet_n]
        Worksheet = sheet.name
        
        xlws = {}
        
        xlws['ws1'] = xlwb.sheets[Worksheet]
        
        Cell_date = ['E','F','G','H','I','J','K','L']
        Cell_Col_Fac = 'B'
        Cell_Col_Ops = 'C'
        Dates_MS = []
        
        cel_row = 0
        flag_SVLPSF = 1
        flag_MS = 1
        flag_XTTC = 1
                
        Manouver=[]        
        flag_MA = 1
        flag_MB = 1
        flag_MC = 1
        while (flag_SVLPSF == 1):
            cel_row = cel_row + 1
            Cell_Fac = Cell_Col_Fac+str(cel_row)
            Facility = xlws['ws1'].range(Cell_Fac).value
            if (Facility!=None):
                if (Facility.lower().find('metop a') != -1):
                    SC = 'MetOp-A'
                    i_cel_row = cel_row
                    while (flag_MA==1):
                        i_cel_row = i_cel_row + 1
                        Cell_Fac = Cell_Col_Fac+str(i_cel_row)
                        Facility_iM = xlws['ws1'].range(Cell_Fac).value
                        Cell_Ops = Cell_Col_Ops+str(i_cel_row)
                        Ops = xlws['ws1'].range(Cell_Ops).value
                        if (Ops!=None):
                            if (Ops.lower().find('ip') != -1):
                                flag_MA = 0
                                for i_date in range(0,len(Cell_date)):
                                    Cell_Day = Cell_date[i_date]
                                    Cell_iM_Day = Cell_Day+str(i_cel_row)
                                    Date_iM = xlws['ws1'].range(Cell_iM_Day).value
                                    #if (Date_MS=='Working Hours' or Date_MS=='All Day'):
                                    if (Date_iM != None ):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        HH, MM = Date_Manouver(Date_iM)
                                        DATE = Date + datetime.timedelta(hours=HH) + datetime.timedelta(minutes=MM)
                                        i_Manouver = [SC,'IP',DATE]
                                        Manouver.append(i_Manouver)
                                
                            if (Ops.lower().find('oop') != -1):
                                flag_MA = 0
                                for i_date in range(0,len(Cell_date)):
                                    Cell_Day = Cell_date[i_date]
                                    Cell_iM_Day = Cell_Day+str(i_cel_row)
                                    Date_iM = xlws['ws1'].range(Cell_iM_Day).value
                                    #if (Date_MS=='Working Hours' or Date_MS=='All Day'):
                                    if (Date_iM != None ):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        HH, MM = Date_Manouver(Date_iM)
                                        DATE = Date + datetime.timedelta(hours=HH) + datetime.timedelta(minutes=MM)
                                        i_Manouver = [SC,'OOP',DATE]
                                        Manouver.append(i_Manouver)
                        else:
                            if (Facility_iM!=None):
                                flag_MA = 0
                if (Facility.lower().find('metop b') != -1):
                    SC = 'MetOp-B'
                    i_cel_row = cel_row
                    while (flag_MB==1):
                        i_cel_row = i_cel_row + 1
                        Cell_Fac = Cell_Col_Fac+str(i_cel_row)
                        Facility_iM = xlws['ws1'].range(Cell_Fac).value
                        Cell_Ops = Cell_Col_Ops+str(i_cel_row)
                        Ops = xlws['ws1'].range(Cell_Ops).value
                        if (Ops!=None):
                            if (Ops.lower().find('ip') != -1):
                                flag_MB = 0
                                for i_date in range(0,len(Cell_date)):
                                    Cell_Day = Cell_date[i_date]
                                    Cell_iM_Day = Cell_Day+str(i_cel_row)
                                    Date_iM = xlws['ws1'].range(Cell_iM_Day).value
                                    #if (Date_MS=='Working Hours' or Date_MS=='All Day'):
                                    if (Date_iM != None ):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        HH, MM = Date_Manouver(Date_iM)
                                        DATE = Date + datetime.timedelta(hours=HH) + datetime.timedelta(minutes=MM)
                                        i_Manouver = [SC,'IP',DATE]
                                        Manouver.append(i_Manouver)
                                
                            if (Ops.lower().find('oop') != -1):
                                flag_MB = 0
                                for i_date in range(0,len(Cell_date)):
                                    Cell_Day = Cell_date[i_date]
                                    Cell_iM_Day = Cell_Day+str(i_cel_row)
                                    Date_iM = xlws['ws1'].range(Cell_iM_Day).value
                                    #if (Date_MS=='Working Hours' or Date_MS=='All Day'):
                                    if (Date_iM != None ):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        HH, MM = Date_Manouver(Date_iM)
                                        DATE = Date + datetime.timedelta(hours=HH) + datetime.timedelta(minutes=MM)
                                        i_Manouver = [SC,'OOP',DATE]
                                        Manouver.append(i_Manouver)
                        else:
                            if (Facility_iM!=None):
                                flag_MB = 0
                if (Facility.lower().find('metop c') != -1):
                    SC = 'MetOp-C'
                    i_cel_row = cel_row
                    while (flag_MC==1):
                        i_cel_row = i_cel_row + 1
                        Cell_Fac = Cell_Col_Fac+str(i_cel_row)
                        Facility_iM = xlws['ws1'].range(Cell_Fac).value
                        Cell_Ops = Cell_Col_Ops+str(i_cel_row)
                        Ops = xlws['ws1'].range(Cell_Ops).value
                        if (Ops!=None):
                            if (Ops.lower().find('ip') != -1):
                                flag_MC = 0
                                for i_date in range(0,len(Cell_date)):
                                    Cell_Day = Cell_date[i_date]
                                    Cell_iM_Day = Cell_Day+str(i_cel_row)
                                    Date_iM = xlws['ws1'].range(Cell_iM_Day).value
                                    #if (Date_MS=='Working Hours' or Date_MS=='All Day'):
                                    if (Date_iM != None ):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        HH, MM = Date_Manouver(Date_iM)
                                        DATE = Date + datetime.timedelta(hours=HH) + datetime.timedelta(minutes=MM)
                                        i_Manouver = [SC,'IP',DATE]
                                        Manouver.append(i_Manouver)
                                
                            if (Ops.lower().find('oop') != -1):
                                flag_MC = 0
                                for i_date in range(0,len(Cell_date)):
                                    Cell_Day = Cell_date[i_date]
                                    Cell_iM_Day = Cell_Day+str(i_cel_row)
                                    Date_iM = xlws['ws1'].range(Cell_iM_Day).value
                                    #if (Date_MS=='Working Hours' or Date_MS=='All Day'):
                                    if (Date_iM != None ):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        HH, MM = Date_Manouver(Date_iM)
                                        DATE = Date + datetime.timedelta(hours=HH) + datetime.timedelta(minutes=MM)
                                        i_Manouver = [SC,'OOP',DATE]
                                        Manouver.append(i_Manouver)
                        else:
                            if (Facility_iM!=None):
                                flag_MC = 0
                if (Facility.lower().find('svl psf') != -1):
                    flag_SVLPSF=0
                    while (flag_MS==1):
                        cel_row = cel_row + 1
                        Cell_Fac = Cell_Col_Fac+str(cel_row)
                        Facility = xlws['ws1'].range(Cell_Fac).value
                        Cell_Ops = Cell_Col_Ops+str(cel_row)
                        Ops = xlws['ws1'].range(Cell_Ops).value
                        
                        if (Ops!=None):
                            if ( Ops.lower().find('manual') != -1):
                                flag_MS=0
                                for i_date in range(0,len(Cell_date)):
                                    Cell_Day = Cell_date[i_date]
                                    Cell_MS_Day = Cell_Day+str(cel_row)
                                    Date_MS = xlws['ws1'].range(Cell_MS_Day).value
                                    #if (Date_MS=='Working Hours' or Date_MS=='All Day'):
                                    if (Date_MS != None ):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        Dates_MS.append(Date)
                        else:
                            if (Facility!=None):
                                flag_MS=0
        
        
        
        
        XTTC_type = 'NorSup'
        XTTC=[]
        cel_row = 0
        flag_SVLPSF = 1
        flag_StaSup = 1
        flag_XTTC = 1
        while (flag_SVLPSF == 1):
            cel_row = cel_row + 1
            Cell_Fac = Cell_Col_Fac+str(cel_row)
            Facility = xlws['ws1'].range(Cell_Fac).value
            if (Facility!=None):
                if ( Facility.lower().find('xttc') != -1 ):
                    flag_SVLPSF=0
                    Facility_iM = Facility
                    i_cel_row = cel_row
                    while ( flag_StaSup == 1 ):
                        i_cel_row = i_cel_row + 1
                        Cell_Fac = Cell_Col_Fac+str(i_cel_row)
                        Facility_iM = xlws['ws1'].range(Cell_Fac).value
                        Cell_Ops = Cell_Col_Ops+str(i_cel_row)
                        Ops = xlws['ws1'].range(Cell_Ops).value
                        
                        if (Facility_iM != None ):
                            if ( Facility_iM.lower().find('eps links') != -1 ):
                                flag_StaSup = 0
                        
                        for i_date in range(0,len(Cell_date)):
                            Cell_Day = Cell_date[i_date]
                            
                            if ( Facility_iM != None):
                                if ( Facility_iM.lower().find('kou') != -1 ):
                                    # KOU
                                    Cell_XTTC_Day = Cell_Day+str(i_cel_row)
                                    Date_XTTC = xlws['ws1'].range(Cell_XTTC_Day).value
                                    if (Date_XTTC!=None):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        Metop, nOrbit, Date = XTTC_info(Date_XTTC, Date)
                                        XTTC.append(['KOU',Date,Metop, nOrbit,XTTC_type])
                            
                                if ( Facility_iM.lower().find('vil1') != -1 ):
                                    # VIL1
                                    Cell_XTTC_Day = Cell_Day+str(i_cel_row)
                                    Date_XTTC = xlws['ws1'].range(Cell_XTTC_Day).value
                                    if (Date_XTTC!=None):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        Metop, nOrbit, Date = XTTC_info(Date_XTTC, Date)
                                        XTTC.append(['VL1',Date,Metop, nOrbit,XTTC_type])
                                        
                                if ( Facility_iM.lower().find('mas') != -1 ):
                                    # MAS
                                    Cell_XTTC_Day = Cell_Day+str(i_cel_row)
                                    Date_XTTC = xlws['ws1'].range(Cell_XTTC_Day).value
                                    if (Date_XTTC!=None):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        Metop, nOrbit, Date = XTTC_info(Date_XTTC, Date)
                                        XTTC.append(['MAS',Date,Metop, nOrbit,XTTC_type])
                            
                            if ( Ops != None):
                                if ( Ops.lower().find('fbk') != -1  ):
                                    # FBK
                                    Cell_XTTC_Day = Cell_Day+str(i_cel_row)
                                    Date_FBK = xlws['ws1'].range(Cell_XTTC_Day).value
                                    if (Date_FBK!=None):
                                        Date = xlws['ws1'].range(Cell_Day+'4').value
                                        Metop, nOrbit, Date = XTTC_info(Date_FBK, Date)
                                        Ops = xlws['ws1'].range(Cell_Col_Ops+str(i_cel_row)).value
                                        if ( Ops.lower().find('covis') != -1):
                                            FBK_type = 'CoVis'
                                        else:
                                            FBK_type = XTTC_type
                                        XTTC.append(['FBK',Date,Metop, nOrbit,FBK_type])
                        
        if ( len(XTTC) >= 2 ):
            for iXTTC_d1 in range(0,len(XTTC)):
                count = 0
                iXTTC_d_Date = XTTC[iXTTC_d1][1]
                for iXTTC_d2 in range(0,len(XTTC)):
                    if ( XTTC[iXTTC_d2][1] == iXTTC_d_Date ):
                        count = count + 1
                        if ( count > 1 ):
                            XTTC.pop(iXTTC_d2)
                
                    
                
                
        
        app.kill()
        del xlws
        return Dates_MS, XTTC, Manouver
    
    
    Dates_MS1, XTTC1, Manouver1 = OPSSCH(0)
    time.sleep(0.006)
    Dates_MS2, XTTC2, Manouver2 = OPSSCH(1)
    
    Dates_MS_all = Dates_MS1 + Dates_MS2
    XTTC_all = XTTC1 + XTTC2
    Manouver_all = Manouver1 + Manouver2
    
    
    return Dates_MS_all, XTTC_all, Manouver_all











def METOPCONT_Info(filePath_OpsSch,filePathName_Wimpy_List,OS_Sys_sep,EPS_I_SC,DS,DE):
    
    ESTRACK_passlist=[]
    nWeek_DE = DE.isocalendar()[1]
    iD = DS
    List_Year_Week=[]
    flag = True
    while (flag==True):
        nDate = iD-datetime.timedelta(days=7)
        nYear = nDate.year
        nWeek = nDate.isocalendar()[1]
        if (nWeek==nWeek_DE):
            flag=False
        else:
            List_Year_Week.append([nYear,nWeek])
            iD=iD+datetime.timedelta(days=7)
    
    for i_Week in range(0,len(List_Year_Week)):
        iYear = List_Year_Week[i_Week][0]
        iWeek = List_Year_Week[i_Week][1]
        file_Name_METOPCONT_filtered = 'METOPCONT'+OS_Sys_sep+str(iYear)+OS_Sys_sep+'ESTRACK_passlist_'+str(iYear)+'-'+str(iWeek)+'-filtered.csv'
        file_Name_METOPCONT_updated = 'METOPCONT'+OS_Sys_sep+str(iYear)+OS_Sys_sep+'ESTRACK_passlist_'+str(iYear)+'-'+str(iWeek)+'-updated.csv'
        file_Path_METOPCONT = [filePath_OpsSch+file_Name_METOPCONT_filtered, filePath_OpsSch+file_Name_METOPCONT_updated]
        
        flag = False
        if (path.isfile(file_Path_METOPCONT[1])==True):
            METOPCONT = read_csv(r''+file_Path_METOPCONT[1])
            flag = True
        elif (path.isfile(file_Path_METOPCONT[0])==True):
            METOPCONT = read_csv(r''+file_Path_METOPCONT[0])
            flag = True
        
        
        if (flag == True):
            for i_ESTRACK_passlist in range(0,METOPCONT.shape[0]):
                Metop = METOPCONT.loc[i_ESTRACK_passlist,['Spacecraft']]['Spacecraft'][-1:]
                Antstr = METOPCONT.loc[i_ESTRACK_passlist,['Station']]['Station']
                if (Antstr=='KRU'):
                    Ant = 'KOU'
                elif (Antstr=='MSP1'):
                    Ant = 'MAS'
                elif (Antstr=='VIL1'):
                    Ant = 'VL1'
                AOSstr = METOPCONT.loc[i_ESTRACK_passlist,['BOT']]['BOT']
                info = AOSstr
                n = []
                for i_info in range(0,len(info)+1):
                    let = info[i_info-1:i_info]
                    if (let=='0' or let=='1' or let=='2' or let=='3' or let=='4' or let=='5' or let=='6' or let=='7' or let=='8' or let=='9'):
                        n.append(let)
                AOS = datetime.datetime(int(''.join(n[0:4])), int(''.join(n[4:6])), int(''.join(n[6:8])), int(''.join(n[8:10])), int(''.join(n[10:12])), int(''.join(n[12:14])), 0*1000)
                AOS2 = datetime.datetime(int(''.join(n[0:4])), int(''.join(n[4:6])), int(''.join(n[6:8])), int(''.join(n[8:10])), int(''.join(n[10:12])), 0, 0*1000)
                
                for i_SC in range(0,len(EPS_I_SC)):
                    if (EPS_I_SC[i_SC][0]==Metop):
                        nMetop = EPS_I_SC[i_SC][1]
                        inMetop = i_SC
                Wimpyfilepath = filePathName_Wimpy_List[inMetop]
                
                fp=open(Wimpyfilepath,'r')
                lines=fp.readlines()
                fp.close()
                ii_RowNow=22
                flagline = 1
                flagDD1=1
                YYMM = lines[ii_RowNow-7-1].strip()
                YYYYPageDate = int(YYMM[20:24])
                MMPageDate = int(YYMM[25:27])
                strPageDate=lines[ii_RowNow-1].strip()
                Dhmss = strPageDate[0:26]
                DD_date=int(Dhmss[0:2])
                hh_date=int(Dhmss[3:5])
                mm_date=int(Dhmss[6:8])
                #ss_date=float(Dhmss[9:15])
                s1ss_date=int(Dhmss[9:11])
                s2ss_date=int(Dhmss[12:15])
                iDD_date = DD_date
                iDate_old=datetime.datetime(YYYYPageDate, MMPageDate, iDD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
                ErrorMsg=[]
                if (iDate_old<AOS):
                    while (flagline == 1):
                        for i_RowNow in range(ii_RowNow,ii_RowNow+52):
                            if (i_RowNow<=len(lines)):
                                strPageDate=lines[i_RowNow-1].strip()
                                
                                i_nOrbit = int(strPageDate[21:26])
                                Dhmss = strPageDate[0:26]
                                
                                DD_date = int(Dhmss[0:2])
                                if (flagDD1 == 1):
                                    DD_date_old = DD_date
                                
                                hh_date=int(Dhmss[3:5])
                                mm_date=int(Dhmss[6:8])
                                #ss_date=float(Dhmss[9:15])
                                s1ss_date=int(Dhmss[9:11])
                                s2ss_date=int(Dhmss[12:15])
                                
                                iDD_date = DD_date
                                if (DD_date != DD_date_old):
                                    Date_date=datetime.datetime(iDate_old.year, iDate_old.month, DD_date_old, hh_date, mm_date, s1ss_date, s2ss_date*1000)+datetime.timedelta(days=1)
                                    Date_date_XTTC=datetime.datetime(iDate_old.year, iDate_old.month, DD_date_old, hh_date, mm_date, s1ss_date, 0*1000)+datetime.timedelta(days=1)
                                    Date_date_XTTC2=datetime.datetime(iDate_old.year, iDate_old.month, DD_date_old, hh_date, mm_date, 0, 0*1000)+datetime.timedelta(days=1)
                                    flagDD1 = 1
                                else:
                                    Date_date=datetime.datetime(iDate_old.year, iDate_old.month, iDD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
                                    Date_date_XTTC=datetime.datetime(iDate_old.year, iDate_old.month, iDD_date, hh_date, mm_date, s1ss_date, 0*1000)
                                    Date_date_XTTC2=datetime.datetime(iDate_old.year, iDate_old.month, iDD_date, hh_date, mm_date, s1ss_date, 0*1000)
                                    if (flagDD1 == 1):
                                        iDate_old = Date_date
                                        flagDD1 = 0
                                
                                if (Date_date<iDate_old):
                                    flagline = 0
                                    ErrorMsg=[1,Wimpyfilepath,i_RowNow-1,i_RowNow]
                                    flagErrorMsg = 1
                                #print(ErrorMsg,Date_date_XTTC, AOS)
                                if (Date_date_XTTC2 == AOS2):
                                    AOSTrue = Date_date
                                    nOrbit_cust = i_nOrbit
                                    flagline = 0
                                
                                DD_date_old = DD_date
                                iDate_old = Date_date
                        
                        if ( i_RowNow >= len(lines) ):
                            flagline = 0
                        ii_RowNow = i_RowNow + 8
                    
    # =============================================================================
    #                 XTTC_FBK, ErrorMsg = fcn_XTTC_FBK(Wimpyfilepath, nOrbit_cust)
    # =============================================================================
                    #print('MetOp-'+Metop, 'M0'+str(int(nMetop)), Ant, AOS)
                    ESTRACK_passlist.append(['MetOp-'+Metop, 'M0'+str(int(nMetop)), Ant, AOS, AOSTrue, nOrbit_cust, 1])
                else:
                    ESTRACK_passlist.append([0, 0, 0, 0, 0, 0, 0])
                
                
    return ESTRACK_passlist