#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:14:30 2020

@author: matteo
"""
import datetime
from datetime import timezone

#import pandas as pd
from pandas import DataFrame










def datatime2str_csv(date):
    AOSyys = str(date.year)
    mm = date.month
    if (mm<10):
        AOSmms = '0'+str(mm)
    else:
        AOSmms = str(mm)
    dd = date.day
    if (dd<10):
        AOSdds = '0'+str(dd)
    else:
        AOSdds = str(dd)
    hh = date.hour
    if (hh<10):
        AOShhs = '0'+str(hh)
    else:
        AOShhs = str(hh)
    MM = date.minute
    if (MM<10):
        AOSMMs = '0'+str(MM)
    else:
        AOSMMs = str(MM)
    ss = date.second
    if (ss<10):
        AOSsss = '0'+str(ss)
    else:
        AOSsss = str(ss)
    datastr=AOSyys+'-'+AOSmms+'-'+AOSdds+'T'+AOShhs+':'+AOSMMs+':'+AOSsss+'Z'
    return datastr











def XTTC_datatime2str_csv(date):
    hh = date.hour
    if (hh<10):
        AOShhs = '0'+str(hh)
    else:
        AOShhs = str(hh)
    MM = date.minute
    if (MM<10):
        AOSMMs = '0'+str(MM)
    else:
        AOSMMs = str(MM)
    ss = date.second
    if (ss<10):
        AOSsss = '0'+str(ss)
    else:
        AOSsss = str(ss)
    datastr=AOShhs+':'+AOSMMs+':'+AOSsss+'Z'
    return datastr











def fcn_MPF_events_csv(FDF_Pass_M, DS, DE, SpaGrndCon, opts, SHOfalg, XTTC_FBK_info, Man_info ):
    if ( SpaGrndCon == 1 ):
        LogbookID = '5e7c9f51a585c67a02eeed0d'
    elif ( SpaGrndCon == 2 ):
        LogbookID = '5ad5c6b7a585c614bac889cd'
    elif ( SpaGrndCon == 3 ):
        LogbookID = '5ad5c6b7a585c614bac889cc'
    
    flag_metop_list1=1
    flag_metop_list2=1
    flag_metop_list3=1
    metop_list=[]
    
    i_space = '&#09'
    i_space = '&nbsp'
    space = i_space*4
    space = (i_space+' ')*4*2
    
    maxlennOrbit = len(str(max(FDF_Pass_M.loc[:,['CDA_nOrbit']]['CDA_nOrbit'])))
    
    csv_DateT = [datetime.datetime(1900, 1, 1, 00, 00, 0, 0*1000)]
    csv_Date = ['#']
    csv_Entry = ['TRUE']
    csv_SC = ['D']
    csv_PassOrbit = ['']
    csv_Text = ['']
    csv_LogbookID= ['']
    for wrow in range(0,FDF_Pass_M.shape[0]):
        AOS=FDF_Pass_M.loc[wrow,['CDA_AOS']]['CDA_AOS']
        LOS=FDF_Pass_M.loc[wrow,['CDA_LOS']]['CDA_LOS']
        Metop = int(FDF_Pass_M.loc[wrow,['M01']]['M01'])
        if (flag_metop_list1==1 and Metop==1):
            flag_metop_list1 = 0
            metop_list.append(Metop)
        if (flag_metop_list2==1 and Metop==2):
            flag_metop_list2 = 0
            metop_list.append(Metop)
        if (flag_metop_list3==1 and Metop==3):
            flag_metop_list3 = 0
            metop_list.append(Metop)
        intnOrbit = int(FDF_Pass_M.loc[wrow,['CDA_nOrbit']]['CDA_nOrbit'])
        nOrbit = str(intnOrbit)
        
        CDAn = str(FDF_Pass_M.loc[wrow,['CDAn']]['CDAn'])
        if (CDAn=='AUTO'):
            CDAn = str(FDF_Pass_M.loc[wrow,['PGF_MPF_ACQ_SITE']]['PGF_MPF_ACQ_SITE'])
# =============================================================================
#         if (MSW_info[0]==1):
#             if (CDAn[0:3]=='CDA'):
#                 if (AOS>=MSW_info[1] and AOS<=MSW_info[2]):
#                     if (CDAn=='CDA1'):
#                         CDAn = 'CDA2'
#                     else:
#                         CDAn = 'CDA1'
# =============================================================================
        
        if (AOS >= DS and AOS <= DE):
            if ( Metop == 19 or Metop == 18 ):
                if (SpaGrndCon==1 or SpaGrndCon==3):
                    NOAA_BOS = FDF_Pass_M.loc[wrow,['NOAA_BOS']]['NOAA_BOS']
                    if (NOAA_BOS == 'YES'):
                        
                        AzNOAA = FDF_Pass_M.loc[wrow,['CDA_AOS_Azi']]['CDA_AOS_Azi']
                        Azstr = str(AzNOAA)
                        if (AzNOAA>=360-100):
                            AzNOAA = AzNOAA-360
                            Azstr=str(AzNOAA)   
                        
                        if (len(str(abs(AzNOAA)))==1):
                            Azstrsin = '0'
                        elif (len(str(abs(AzNOAA)))==2):
                            Azstrsin = '00'
                        else:
                            Azstrsin = '000'
                        
                        Azstrsin1 = Azstr[0:1]
                        if (Azstrsin1 != '-'):
                            Azstrsin = ''+Azstrsin
                        else:
                            Azstrsin = Azstrsin1+Azstrsin
                        
                        AOSlineText='AOS<br>Az/ACU: '+Azstrsin+'.000°('+Azstr+'° expected)/2LT<br>'+CDAn+'/TTC1 '+space+'TM:  OK '+space+'TC: OK'
                        MtOp=str(Metop)
                        GAC_type = FDF_Pass_M.loc[wrow,['GDS_GAC']]['GDS_GAC'][0:2]
                        GAC_Frame = FDF_Pass_M.loc[wrow,['GDS_GAC']]['GDS_GAC'][3:10]
                        GAC_Frame_0 = '0'*len(GAC_Frame)
                        LOSlineText='LOS'
                        
                        GACStart = FDF_Pass_M.loc[wrow,['Dump_Start']]['Dump_Start']
                        GACEnd = FDF_Pass_M.loc[wrow,['Dump_End']]['Dump_End']
                        
                        csv_DateT.append(AOS)
                        datastr=datatime2str_csv(AOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('N'+MtOp)
                        csv_PassOrbit.append('Orbit '+nOrbit)
                        csv_Text.append('<p>'+AOSlineText+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(GACStart)
                        datastr=datatime2str_csv(GACStart)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('N'+MtOp)
                        csv_PassOrbit.append('Orbit '+nOrbit)
                        csv_Text.append('<p>'+'GAC Start<br>Frames Expected: '+GAC_Frame+' ['+GAC_type+']'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(GACEnd)
                        datastr=datatime2str_csv(GACEnd)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('N'+MtOp)
                        csv_PassOrbit.append('Orbit '+nOrbit)
                        csv_Text.append('<p>'+'GAC End<br>Frames Received: '+GAC_Frame_0+' ['+GAC_type+']'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(LOS)
                        datastr=datatime2str_csv(LOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('N'+MtOp)
                        csv_PassOrbit.append('Orbit '+nOrbit)
                        csv_Text.append('<p>'+LOSlineText+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
            else:
                AOSM=FDF_Pass_M.loc[wrow,['CDA_AOS5']]['CDA_AOS5']
                RPF=AOSM+datetime.timedelta(seconds=3*60+45)
                MtOp='0'+str(Metop)
                
                DEFPass = FDF_Pass_M.loc[wrow,['TM_Format']]['TM_Format']
                AOCSPass = FDF_Pass_M.loc[wrow,['AOCS']]['AOCS']
                
                
                SpanOr = i_space*(maxlennOrbit-len(nOrbit))
                SpanOr = ' '*(maxlennOrbit-len(nOrbit))
                iDEFPass = ''
                #print (Metop, DEFPass)
                if (DEFPass == 'DEF_ROUT' ):
                    
                    iDEFPass = ' - '+DEFPass
                iAOCSPass = ''
                if (AOCSPass == 'AOCS' ):
                    iAOCSPass = ' - '+AOCSPass
                    
                TMF_AOCS = SpanOr + iDEFPass + iAOCSPass
                
                Det = ''
                
                
                #==================================================================
                #
# =============================================================================
#                 if (DEFPass=='DEF_PLM'):
#                     if (AOCSPass == 'AOCS '):
#                         AOSlineText='AOS    '+AOCSPass+'    '+CDAn+'/TTC1     TM: OK      TC: OK     XBAND: OK'
#                     else:
#                         AOSlineText='AOS    '+CDAn+'/TTC1     TM: OK      TC: OK     XBAND: OK'
#                 elif (DEFPass=='DEF_ROUT'):   
#                     AOSlineText='AOS   '+DEFPass+'      '+CDAn+'/TTC1     TM: OK      TC: OK     XBAND: OK'
# =============================================================================
                AOSlineText='AOS<br>'+CDAn+'/TTC1 '+space+'TM: OK '+space+'TC: OK'
                
                #==================================================================
                #
                if (DEFPass=='DEF_PLM'):
                    RPFlineText="All RPF's received and reset"
                elif (DEFPass=='DEF_ROUT'):
                    RPFlineText = 'SVM and TEXTR received and reset'
                
                if (SpaGrndCon==1 or SpaGrndCon==2):
                    Det = Det+''+TMF_AOCS
                    
                #==================================================================
                #    
                nextAz=FDF_Pass_M.loc[wrow,['Next_Az_MetOp']]['Next_Az_MetOp']
                nextAzstr=str(nextAz)
                if (nextAz>=360-100):
                    nextAz = nextAz-360
                    nextAzstr=str(nextAz)
                
                nextAzstrsin = '0'*len(str(abs(nextAz)))
                
                
                nextAzstrsin1 = nextAzstr[0:1]
                if (nextAzstrsin1 != '-'):
                    nextAzstrsin = ''+nextAzstrsin
                else:
                    nextAzstrsin = nextAzstrsin1+nextAzstrsin
                #
                RD=FDF_Pass_M.loc[wrow,['RNGDOP']]['RNGDOP']
                
                if (SpaGrndCon==1):
                    if ( opts >= 2 ):
                        LOSlineText='LOS<br>XBAND: OK '+space+'TC Count: 000/255 '+space+'R/D: '+str(RD)+'/'+str(RD)+'<br>Az/ACU: '+nextAzstrsin+'.000°('+nextAzstr+'° expected)/2LT'
                    else:
                        LOSlineText='LOS<br>XBAND: OK '+space+'TC Count: 000/255 '+space+'R/D: '+str(RD)+'/'+str(RD)+'<br>Az/ACU: '+nextAzstrsin+'.000('+nextAzstr+' expected)/2LT'
                elif (SpaGrndCon==2):
                    LOSlineText='LOS<br>XBAND: OK '+space+'TC Count: 000/255 '+space+'R/D: '+str(RD)+'/'+str(RD)+''
                elif (SpaGrndCon==3):
                    if ( opts >= 2 ):
                        LOSlineText='LOS<br>Az/ACU: '+nextAzstrsin+'.000°('+nextAzstr+'° expected)/2LT'
                    else:
                        LOSlineText='LOS<br>Az/ACU: '+nextAzstrsin+'.000('+nextAzstr+' expected)/2LT'
                
                #==================================================================
                if (XTTC_FBK_info[0]==1):
                    if (XTTC_FBK_info[1]==False):
                        csv_DateT.append(AOS)
                        datastr=datatime2str_csv(AOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('M'+MtOp)
                        csv_PassOrbit.append('Orbit '+nOrbit+Det)
                        csv_Text.append('<p>'+AOSlineText+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        if (SpaGrndCon==1 or SpaGrndCon==2):
                            csv_DateT.append(RPF)
                            datastr=datatime2str_csv(RPF)
                            csv_Date.append(datastr)
                            csv_Entry.append('Entry')
                            csv_SC.append('M'+MtOp)
                            csv_PassOrbit.append('Orbit '+nOrbit+Det)
                            csv_Text.append('<p>'+RPFlineText+'</p>')
                            csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(LOS)
                        datastr=datatime2str_csv(LOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('M'+MtOp)
                        csv_PassOrbit.append('Orbit '+nOrbit+Det)
                        csv_Text.append('<p>'+LOSlineText+'</p>')
                        csv_LogbookID.append(LogbookID)
                    else:
                        if (intnOrbit!=XTTC_FBK_info[4]):
                            csv_DateT.append(AOS)
                            datastr=datatime2str_csv(AOS)
                            csv_Date.append(datastr)
                            csv_Entry.append('Entry')
                            csv_SC.append('M'+MtOp)
                            csv_PassOrbit.append('Orbit '+nOrbit+Det)
                            csv_Text.append('<p>'+AOSlineText+'</p>')
                            csv_LogbookID.append(LogbookID)
                            
                            if (SpaGrndCon==1 or SpaGrndCon==2):
                                csv_DateT.append(RPF)
                                datastr=datatime2str_csv(RPF)
                                csv_Date.append(datastr)
                                csv_Entry.append('Entry')
                                csv_SC.append('M'+MtOp)
                                csv_PassOrbit.append('Orbit '+nOrbit+Det)
                                csv_Text.append('<p>'+RPFlineText+'</p>')
                                csv_LogbookID.append(LogbookID)
                            
                            csv_DateT.append(LOS)
                            datastr=datatime2str_csv(LOS)
                            csv_Date.append(datastr)
                            csv_Entry.append('Entry')
                            csv_SC.append('M'+MtOp)
                            csv_PassOrbit.append('Orbit '+nOrbit+Det)
                            csv_Text.append('<p>'+LOSlineText+'</p>')
                            csv_LogbookID.append(LogbookID)
                        else:
                            if (SpaGrndCon==1 or SpaGrndCon==3):
                                csv_DateT.append(AOS)
                                datastr=datatime2str_csv(AOS)
                                csv_Date.append(datastr)
                                csv_Entry.append('Entry')
                                csv_SC.append('M'+MtOp)
                                csv_PassOrbit.append('Orbit '+nOrbit+Det)
                                csv_Text.append('<p>'+AOSlineText+'</p>')
                                csv_LogbookID.append(LogbookID)
                                
                                csv_DateT.append(LOS)
                                datastr=datatime2str_csv(LOS)
                                csv_Date.append(datastr)
                                csv_Entry.append('Entry')
                                csv_SC.append('M'+MtOp)
                                csv_PassOrbit.append('Orbit '+nOrbit+Det)
                                csv_Text.append('<p>'+LOSlineText+'</p>')
                                csv_LogbookID.append(LogbookID)
                else:
                    csv_DateT.append(AOS)
                    datastr=datatime2str_csv(AOS)
                    csv_Date.append(datastr)
                    csv_Entry.append('Entry')
                    csv_SC.append('M'+MtOp)
                    csv_PassOrbit.append('Orbit '+nOrbit+Det)
                    csv_Text.append('<p>'+AOSlineText+'</p>')
                    csv_LogbookID.append(LogbookID)
                    
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(RPF)
                        datastr=datatime2str_csv(RPF)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('M'+MtOp)
                        csv_PassOrbit.append('Orbit '+nOrbit+Det)
                        csv_Text.append('<p>'+RPFlineText+'</p>')
                        csv_LogbookID.append(LogbookID)
                    
                    csv_DateT.append(LOS)
                    datastr=datatime2str_csv(LOS)
                    csv_Date.append(datastr)
                    csv_Entry.append('Entry')
                    csv_SC.append('M'+MtOp)
                    csv_PassOrbit.append('Orbit '+nOrbit+Det)
                    csv_Text.append('<p>'+LOSlineText+'</p>')
                    csv_LogbookID.append(LogbookID)
                        
    metop_list.sort()
    flag_DE=0
    iminute=0
    while (flag_DE==0):
        iDate=DS+datetime.timedelta(minutes=iminute)
        if (iDate==DS and SHOfalg == 1):
            SHO_Entry = 'SHO completed'
            if (SpaGrndCon==1 or SpaGrndCon==3):
                SHO_Entry = SHO_Entry+'<br>LACOM: 00<br>LAMON: 00'
            if (SpaGrndCon==1 or SpaGrndCon==2):
                for i_metop in range(0,len(metop_list)):
                    SHO_Entry= SHO_Entry + '<br>M0'+str(metop_list[i_metop])+' CFS/PLM/IN: /0/0'
            
            csv_DateT.append(iDate)
            datastr=datatime2str_csv(iDate)
            csv_Date.append(datastr)
            csv_Entry.append('Entry')
            csv_SC.append('CR')
            csv_PassOrbit.append('SHO')
            csv_Text.append('<p>'+SHO_Entry+'</p>')
            csv_LogbookID.append(LogbookID)
            
        if (iDate >= DS and iDate <= DE ):
            if ( opts >= 3 ):
                if (iDate.weekday()==1-1 and iDate.hour==5 and iDate.minute==30):
                    if (SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'RNG/DOP Calibration<br>CDA1/TTC1'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'RNG/DOP Calibration<br>CDA2/TTC1'+'</p>')
                        csv_LogbookID.append(LogbookID)
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'RNG/DOP Calibration<br>CDA1/TTC1: Range 38.000 Time Delay 129000'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'RNG/DOP Calibration<br>CDA2/TTC1: Range 38.000 Time Delay 129000'+'</p>')
                        csv_LogbookID.append(LogbookID)
                    
                if (iDate.weekday()==5-1 and iDate.hour==6 and iDate.minute==30 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('DIF')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'Weekly UNS check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==7 and iDate.minute==50 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'OBT to UTC Check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==7 and iDate.minute==50 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('PGF')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'PGF Aux file Check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'CDA short period pointing file Check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==5-1 and iDate.hour==8 and iDate.minute==10 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'Delay MMAMs'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==8 and iDate.minute==20 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'MMAMs'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==13 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'CDA long period pointing file Check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==3-1 and iDate.hour==16 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('JASON')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'J3 pointing file check'+'</p>')
                        csv_LogbookID.append('5b0e8a6fa585c614bac88a0a')
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('JASON')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'J3 pass planning file check'+'</p>')
                        csv_LogbookID.append('5b0e8a6fa585c614bac88a0a')
                        
                if (iDate.hour==17 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'OBT to UTC Check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==17 and iDate.minute==15 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('PGF')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'PGF Aux file Check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==18 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'CDA short period pointing file Check'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==19 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'MMAMs'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==6-1 and iDate.hour==23 and iDate.minute==59 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'Print schedule'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'Load CHRONOPS'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'Check ESTRACK Pass List'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'Load countdown tool'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==6-1 and iDate.hour==23 and iDate.minute==59 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('<p>'+'Print WOTIS file'+'</p>')
                        csv_LogbookID.append(LogbookID)
                    
        iminute = iminute + 1
        if (iDate>=DE):
            flag_DE=1
    
    
    if (SpaGrndCon==1 or SpaGrndCon==2):
        if (XTTC_FBK_info[0]!=0):
            Antenna = XTTC_FBK_info[2]
            Ant = Antenna
            XTTCFBK_nOrbit = XTTC_FBK_info[4]
            XTTCFBK_nOrbit_chr = str(XTTCFBK_nOrbit)
            if (XTTC_FBK_info[1]==False):
                if (Antenna=='KOU' or Antenna=='VL1' or Antenna=='MAS'):
                    if (XTTC_FBK_info[2]=='KOU'):
                        iDate_AOS =XTTC_FBK_info[5].loc['AOS',[Antenna]][Antenna]
                        iDate_AOS5=XTTC_FBK_info[5].loc['AOS5',[Antenna]][Antenna]
                    else:
                        iDate_AOS = XTTC_FBK_info[5].loc['LOS',['CDA']]['CDA']+datetime.timedelta(seconds=1*60)
                        iDate_AOS5 = iDate_AOS+datetime.timedelta(seconds=1*60)
                    
                    iDate_AOS_NOP=iDate_AOS5+datetime.timedelta(seconds=60)
                    iDate_LOS=XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]
                    
                    SpanOr = i_space*(maxlennOrbit-len(XTTCFBK_nOrbit_chr))
                    SpanOr = ' '*(maxlennOrbit-len(XTTCFBK_nOrbit_chr))
                    Support = 'XTTC'
                    Det = SpanOr+' - '+Support+' - '+Antenna
                    XTTC_AOS_Date = XTTC_FBK_info[5].loc['AOS',[Antenna]][Antenna]
                    XTTC_PPI_Date = XTTC_AOS_Date-datetime.timedelta(hours=1)
                    
                    XTTC_AOS = XTTC_datatime2str_csv(XTTC_AOS_Date)[:-1]
                    XTTC_AOS5 = XTTC_datatime2str_csv(iDate_AOS5)[:-1]
                    XTTC_LOS5 = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['LOS5',[Antenna]][Antenna])[:-1]
                    XTTC_LOS = XTTC_datatime2str_csv(iDate_LOS)[:-1]
                    
                    Pass_det_Pre_Pass_Info = '<b>Pre-Pass Info</b>'
                    Pass_det_SC   ='<br>S/C ID: '+XTTC_FBK_info[3]
                    Pass_det_nO   ='<br>Orbit Number: '+XTTCFBK_nOrbit_chr
                    Pass_det_GS   ='<br>Ground Station ID: '+Antenna
                    Pass_det_AOS  ='<br>AOS: '+XTTC_AOS
                    Pass_det_LOS  ='<br>LOS: '+XTTC_LOS
                    Pass_det_AOS5 ='<br>Uplink Start: '+XTTC_AOS5
                    Pass_det_LOS5 ='<br>Uplink Stop: '+XTTC_LOS5
                    Pass_det_Nat  ='<br>Nature: Normaly Routine XTTC Support'
                    Pass_det_EIT  =''
                    Pass_det = Pass_det_Pre_Pass_Info+Pass_det_SC+Pass_det_nO+Pass_det_GS+Pass_det_AOS+Pass_det_LOS+Pass_det_AOS5+Pass_det_LOS5+Pass_det_Nat+Pass_det_EIT
                else:
                    iDate_AOS=XTTC_FBK_info[5].loc['AOS',[Antenna]][Antenna]
                    iDate_AOS5=XTTC_FBK_info[5].loc['AOS5',[Antenna]][Antenna]
                    iDate_AOS_NOP=iDate_AOS5+datetime.timedelta(minutes=1)
                    iDate_LOS=XTTC_FBK_info[5].loc['AOS',['CDA']]['CDA']-datetime.timedelta(minutes=1)
                    SpanOr = i_space*(maxlennOrbit-len(XTTCFBK_nOrbit_chr))
                    SpanOr = ' '*(maxlennOrbit-len(XTTCFBK_nOrbit_chr))
                    Det = SpanOr+' - '+Antenna
                    
                    XTTC_AOS_Date = iDate_AOS
                    XTTC_PPI_Date = XTTC_AOS_Date-datetime.timedelta(minutes=30)
                    
                    XTTC_AOS = XTTC_datatime2str_csv(XTTC_AOS_Date)[:-1]
                    XTTC_AOS5 = XTTC_datatime2str_csv(iDate_AOS5)[:-1]
                    XTTC_LOS5 = XTTC_datatime2str_csv(iDate_LOS-datetime.timedelta(minutes=1))[:-1]
                    XTTC_LOS = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna])[:-1]
                    
                    XTTC_SVL_AOS = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['AOS',['CDA']]['CDA'])[:-1]
                    XTTC_SVL_AOS5 = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['AOS5',['CDA']]['CDA'])[:-1]
                    XTTC_SVL_LOS5 = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['LOS5',['CDA']]['CDA'])[:-1]
                    XTTC_SVL_LOS = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['LOS',['CDA']]['CDA'])[:-1]
                    
                    Support = Antenna
                    
                    Pass_det_Pre_Pass_Info = '<b>Pre-Pass Info</b>'
                    Pass_det_SC   ='<br>S/C ID: '+XTTC_FBK_info[3]
                    Pass_det_nO   ='<br>Orbit Number: '+XTTCFBK_nOrbit_chr
                    Pass_det_FBK_AOS  ='<br>FBK AOS: '+XTTC_AOS
                    Pass_det_FBK_AOS5 ='<br>FBK Carrier on: '+XTTC_AOS5
                    Pass_det_FBK_LOS5 ='<br>FBK Carrier off: '+XTTC_LOS5
                    Pass_det_SVL_AOS  ='<br>SVL AOS: '+XTTC_SVL_AOS
                    Pass_det_FBK_LOS  ='<br>FBK LOS: '+XTTC_LOS
                    Pass_det_SVL_AOS5 ='<br>SVL Uplink start: '+XTTC_SVL_AOS5
                    Pass_det_SVL_LOS5 ='<br>SVL Uplink start: '+XTTC_SVL_LOS5
                    Pass_det_SVL_LOS  ='<br>SVL LOS: '+XTTC_SVL_LOS
                    Pass_det_Nat  ='<br>Nature of the Pass: '
                    Pass_det_EIT  ='<br>Station: '
                    Pass_det = Pass_det_Pre_Pass_Info+Pass_det_SC+Pass_det_nO+Pass_det_FBK_AOS+Pass_det_FBK_AOS5+Pass_det_FBK_LOS5+Pass_det_SVL_AOS+Pass_det_FBK_LOS+Pass_det_SVL_AOS5+Pass_det_SVL_LOS5+Pass_det_SVL_LOS+Pass_det_Nat+Pass_det_EIT
                 
                
                
                
                
                
                
                
                
                
                
                
                BAOS_Start_pass = 'Activate the relevant "start_pass" procedure (/home/metop/METOP1.0/database/procedure/SC_STREAM_MPF_FCP/start_pass.prc(0,0,0,0,0,0))'
                BAOS_MPF = '<br>MPF Queue opening = manual'
                BAOS_CDA = '<br>Configure the CDA selection for '+Antenna+' station'
                BAOS_TTC = '<br>Configure the TTC selection as required'
                BAOS_TMTC = '<br>Connect TM and TC manually'
                BAOS_LOSSVL = 'Manually disconnect the TM and TC connections'
                
                ALOS_TMTC = 'Disconnect TM and TC from the station'
                ALOS_CDA = '<br>Configure the CDA selection to Auto'
                ALOS_TTC = '<br>Configure the TTC selection as required'
                ALOS_MPF = '<br>Leave the Q opening in Manual'
                ALOS_Start_pass = '<br>Activate the relevant "end_pass" procedure (/home/metop/METOP1.0/database/procedure/SC_STREAM_MPF_FCP/end_pass.prc(0,0,0,0,0,0))'
                    
                if (Antenna=='KOU' or Antenna=='VL1' or Antenna=='MAS'):
                    
                    if (Antenna=='KOU'):
                        BAOS = BAOS_Start_pass+BAOS_MPF+BAOS_CDA+BAOS_TMTC
                        iDate = iDate_AOS-datetime.timedelta(seconds=4*60)
                        csv_DateT.append(iDate)
                        csv_Date.append(datatime2str_csv(iDate))
                        csv_Entry.append('Entry')
                        csv_SC.append(XTTC_FBK_info[3])
                        csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                        csv_Text.append('<p>'+BAOS+'</p>')
                        csv_LogbookID.append(LogbookID)
                    else:
                        iDate = XTTC_FBK_info[5].loc['AOS',['CDA']]['CDA']-datetime.timedelta(seconds=4*60)
                        csv_DateT.append(iDate)
                        csv_Date.append(datatime2str_csv(iDate))
                        csv_Entry.append('Entry')
                        csv_SC.append(XTTC_FBK_info[3])
                        csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                        csv_Text.append('<p>'+'PI suspend the relevant TC and TM disconnections'+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                        BAOS = BAOS_LOSSVL + BAOS_CDA + BAOS_TTC + BAOS_TMTC
                        iDate = iDate_AOS-datetime.timedelta(seconds=30)
                        csv_DateT.append(iDate)
                        csv_Date.append(datatime2str_csv(iDate))
                        csv_Entry.append('Entry')
                        csv_SC.append(XTTC_FBK_info[3])
                        csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                        csv_Text.append('<p>'+BAOS+'</p>')
                        csv_LogbookID.append(LogbookID)
                        
                    ALOS = ALOS_TMTC + ALOS_CDA + ALOS_TTC + ALOS_MPF + ALOS_Start_pass
                    csv_DateT.append(iDate_LOS+datetime.timedelta(minutes=1))
                    csv_Date.append(datatime2str_csv(iDate_LOS+datetime.timedelta(minutes=1)))
                    csv_Entry.append('Entry')
                    csv_SC.append(XTTC_FBK_info[3])
                    csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                    csv_Text.append('<p>'+ALOS+'</p>')
                    csv_LogbookID.append(LogbookID)
                    
                    flag = 1
                    for ipass in range(0,FDF_Pass_M.shape[0]):
                        
                        if ( flag == 1 and FDF_Pass_M.loc[ipass,['M01']]['M01']==int(XTTC_FBK_info[3][-1:]) and FDF_Pass_M.loc[ipass,['CDA_AOS']]['CDA_AOS']>iDate_AOS):
                            flag = 0
                            iDate = FDF_Pass_M.loc[ipass,['CDA_AOS5']]['CDA_AOS5']+datetime.timedelta(seconds=60)
                            csv_DateT.append(iDate)
                            csv_Date.append(datatime2str_csv(iDate))
                            csv_Entry.append('Entry')
                            csv_SC.append(XTTC_FBK_info[3])
                            csv_PassOrbit.append('Orbit '+str(XTTCFBK_nOrbit+1))
                            csv_Text.append('<p>'+'NOP'+'</p>')
                            csv_LogbookID.append(LogbookID)
                else:
                    iDate = XTTC_PPI_Date+datetime.timedelta(minutes=10)
                    csv_DateT.append(iDate)
                    csv_Date.append(datatime2str_csv(iDate))
                    csv_Entry.append('Entry')
                    csv_SC.append(XTTC_FBK_info[3])
                    csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                    csv_Text.append('<p>'+'PI suspend the relevant TC and TM connections for Svalbardb<br>PI suspend the relevant command queue opening for Svalbard'+'</p>')
                    csv_LogbookID.append(LogbookID)
                    
                    iDate = XTTC_PPI_Date+datetime.timedelta(minutes=15)
                    csv_DateT.append(iDate)
                    csv_Date.append(datatime2str_csv(iDate))
                    csv_Entry.append('Entry')
                    csv_SC.append(XTTC_FBK_info[3])
                    csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                    csv_Text.append('<p>'+BAOS_Start_pass+'</p>')
                    csv_LogbookID.append(LogbookID)
                    
                    
                    
                    BAOS_1 = 'The spacecraft command queues are closed'
                    BAOS_2 = '<br>Configure the CDA designation for Fairbanks on the S band viewer'
                    BAOS_ = BAOS_1 + BAOS_2
                    iDate = iDate_AOS-datetime.timedelta(minutes=7)
                    csv_DateT.append(iDate)
                    csv_Date.append(datatime2str_csv(iDate))
                    csv_Entry.append('Entry')
                    csv_SC.append(XTTC_FBK_info[3])
                    csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                    csv_Text.append('<p>'+BAOS_+'</p>')
                    csv_LogbookID.append(LogbookID)
                    
                    ALOS_1 = 'Manually disconnect the TC and TM links from FCDAS using the TC and TM buttons on the S band viewer'
                    ALOS_2 = '<br>Configure the CDA designation for Svalbard on the S band viewer'
                    ALOS_3 = '<br>set CDA selection back to AUTO'
                    ALOS_ = ALOS_1 + ALOS_2 + ALOS_3
                    iDate = iDate_LOS+datetime.timedelta(seconds=30)
                    csv_DateT.append(iDate)
                    csv_Date.append(datatime2str_csv(iDate))
                    csv_Entry.append('Entry')
                    csv_SC.append(XTTC_FBK_info[3])
                    csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                    csv_Text.append('<p>'+ALOS_+'</p>')
                    csv_LogbookID.append(LogbookID)
                    
                
                
                
                
                
                
                
                
                
                
                csv_DateT.append(XTTC_PPI_Date)
                csv_Date.append(datatime2str_csv(XTTC_PPI_Date))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+Pass_det+'</p>')
                csv_LogbookID.append(LogbookID)    
                
                
                if (Antenna=='KOU' or Antenna=='VL1' or Antenna=='MAS'):
                    iDate = iDate_AOS-datetime.timedelta(minutes=15)
                else:
                    iDate = iDate_AOS-datetime.timedelta(minutes=10)
                csv_DateT.append(iDate)
                csv_Date.append(datatime2str_csv(iDate))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                if (Antenna=='KOU' or Antenna=='VL1' or Antenna=='MAS'):
                    csv_Text.append('<p>'+'Pass Briefing with ESOC<br>EIT: '+'</p>')
                else:
                    csv_Text.append('<p>'+'Pass Briefing with '+Antenna+'<br>Station: '+'</p>')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_AOS)
                csv_Date.append(datatime2str_csv(iDate_AOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+'AOS<br>'+Ant+'/TTC1 '+space+'TM: OK '+space+'TC: OK'+'</p>')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_AOS_NOP)
                csv_Date.append(datatime2str_csv(iDate_AOS_NOP))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+'NOP'+'</p>')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_LOS)
                csv_Date.append(datatime2str_csv(iDate_LOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+'LOS<br>TC Count: 000/255'+'</p>')
                csv_LogbookID.append(LogbookID)
            else:
                iDate_AOS=XTTC_FBK_info[5].loc['AOS',[Antenna]][Antenna]
                iDate_AOS5=XTTC_FBK_info[5].loc['AOS5',[Antenna]][Antenna]
                iDate_AOS_NOP = iDate_AOS5+datetime.timedelta(minutes=1)
                iDate_LOS5=XTTC_FBK_info[5].loc['LOS5',[Antenna]][Antenna]
                iDate_LOS=XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]
                SpanOr = i_space*(maxlennOrbit-len(XTTCFBK_nOrbit_chr))
                SpanOr = ' '*(maxlennOrbit-len(XTTCFBK_nOrbit_chr))
                Det = SpanOr+' - '+Antenna
                
                XTTC_PPI_Date = iDate_AOS-datetime.timedelta(hours=1)
                
                XTTC_AOS = XTTC_datatime2str_csv(iDate_AOS)[:-1]
                XTTC_SVL_AOS = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['AOS',['CDA']]['CDA'])[:-1]
                XTTC_AOS5 = XTTC_datatime2str_csv(iDate_AOS5)[:-1]
                XTTC_LOS5 = XTTC_datatime2str_csv(iDate_LOS5)[:-1]
                XTTC_LOS = XTTC_datatime2str_csv(iDate_LOS)[:-1]
                XTTC_SVL_LOS = XTTC_datatime2str_csv(XTTC_FBK_info[5].loc['LOS',['CDA']]['CDA'])[:-1]
                
                
                Pass_det_Pre_Pass_Info = '<b>Pre-Pass Info</b>'
                Pass_det_SC   ='<br>S/C ID: '+XTTC_FBK_info[3]
                Pass_det_nO   ='<br>Orbit Number: '+XTTCFBK_nOrbit_chr
                Pass_det_FBK_AOS  ='<br>FBK AOS: '+XTTC_AOS
                Pass_det_SVL_AOS  ='<br>SVL AOS: '+XTTC_SVL_AOS
                Pass_det_FBK_AOS5 ='<br>FBK Carrier up time: '+XTTC_AOS5
                
                Pass_det_SSR_XBand_LOS121 = 'TT time of LOS121_E01: '
                Pass_det_SSR_XBand_LOX003 = 'TT time of LOX003: '
                Pass_det_SSR_XBand_LOS122 = 'TT time of LOS122_E01: '
                Pass_det_SSR_XBand_LOX004 = 'TT time of LOX004: '
                Pass_det_SSR_XBand = Pass_det_SSR_XBand_LOS121+'<br>'+Pass_det_SSR_XBand_LOX003+'<br>'+Pass_det_SSR_XBand_LOS121+'<br>'+Pass_det_SSR_XBand_LOS122+'<br>'+Pass_det_SSR_XBand_LOX004
                
                Pass_det_FBK_LOS5 ='<br>FBK Carrier down time: '+XTTC_LOS5
                Pass_det_FBK_LOS  ='<br>FBK LOS: '+XTTC_LOS
                Pass_det_SVL_LOS  ='<br>SVL AOS: '+XTTC_SVL_LOS
                Pass_det_Nat  ='<br>Nature: '
                Pass_det_EIT  ='<br>Antenna ID: '
                Pass_det = Pass_det_Pre_Pass_Info+Pass_det_SC+Pass_det_nO+Pass_det_FBK_AOS+Pass_det_SVL_AOS+Pass_det_FBK_AOS5+Pass_det_SSR_XBand+Pass_det_FBK_LOS5+Pass_det_FBK_LOS+Pass_det_SVL_LOS+Pass_det_Nat+Pass_det_EIT
                    
                    
                csv_DateT.append(XTTC_PPI_Date)
                csv_Date.append(datatime2str_csv(XTTC_PPI_Date))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+Pass_det+'</p>')
                csv_LogbookID.append(LogbookID)
                
                
                BAOS_1 = 'PI suspend "TM connect" procedures for the following Svalbard pass'
                BAOS_2 = '<br>PI suspend "TC connect" procedures for the following Svalbard pass'
                BAOS_3 = '<br>PI suspend "Command queue opening" procedures for the following Svalbard pass'
                BAOS_4 = '<br>PI suspend "Ranging measurements" procedures for the following Svalbard pass'
                BAOS_5 = '<br>PI suspend "Doppler measurements" procedures for the following Svalbard pass'
                BAOS_6 = '<br>PI suspend "TM disconnect" procedures for the following Svalbard pass'
                BAOS_7 = '<br>PI suspend "TC disconnect" procedures for the following Svalbard pass'
                BAOS_ = BAOS_1 + BAOS_2 + BAOS_3 + BAOS_4 + BAOS_5 + BAOS_6 + BAOS_7
                iDate = iDate_AOS-datetime.timedelta(minutes=20)
                csv_DateT.append(iDate_AOS)
                csv_Date.append(datatime2str_csv(iDate))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+BAOS_+'</p>')
                csv_LogbookID.append(LogbookID)
                
                
                iDate = iDate_AOS-datetime.timedelta(minutes=10)
                csv_DateT.append(iDate)
                csv_Date.append(datatime2str_csv(iDate))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+'Pass Briefing with '+Antenna+'<br>Station: '+'</p>')
                csv_LogbookID.append(LogbookID)
                
                
                BAOS_1 = 'The spacecraft command queues are closed'
                BAOS_2 = '<br>Configure the CDA designation for Fairbanks on the S band viewer'
                BAOS_ = BAOS_1 + BAOS_2
                iDate = iDate_AOS-datetime.timedelta(minutes=7)
                csv_DateT.append(iDate)
                csv_Date.append(datatime2str_csv(iDate))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+BAOS_+'</p>')
                csv_LogbookID.append(LogbookID)
                
                
                
                csv_DateT.append(iDate_AOS)
                csv_Date.append(datatime2str_csv(iDate_AOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+'AOS<br>'+Ant+'/TTC1 '+space+'TM: OK '+space+'TC: OK'+'</p>')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_AOS_NOP)
                csv_Date.append(datatime2str_csv(iDate_AOS_NOP))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+'NOP'+'</p>')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_LOS)
                csv_Date.append(datatime2str_csv(iDate_LOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+'LOS<br>TC Count: 000/255'+'</p>')
                csv_LogbookID.append(LogbookID)
                
                
                ALOS_1 = 'Manually disconnect the TC and TM links from FCDAS using the TC and TM buttons on the S band viewer'
                ALOS_2 = '<br>Configure the CDA designation for Svalbard on the S band viewer'
                ALOS_3 = '<br>set CDA selection back to AUTO'
                ALOS_ = ALOS_1 + ALOS_2 + ALOS_3
                iDate = iDate_LOS+datetime.timedelta(minutes=1)
                csv_DateT.append(iDate)
                csv_Date.append(datatime2str_csv(iDate))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+ALOS_+'</p>')
                csv_LogbookID.append(LogbookID)
        
        if (Man_info[0]==1):
            Day_m1 = Man_info[4] - datetime.timedelta(hours=24)
            if (Day_m1 >= DS and Day_m1 <= DE):
                csv_DateT.append(Day_m1)
                csv_Date.append(datatime2str_csv(Day_m1))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[1])
                csv_PassOrbit.append(Man_info[3]+' Day-1')
                csv_Text.append('<p>'+''+'</p>')
                csv_LogbookID.append(LogbookID)
    
    if (SpaGrndCon==1 or SpaGrndCon==3):
        if (XTTC_FBK_info[0]!=0):
            Antenna = XTTC_FBK_info[2]
            Ant = Antenna
            XTTCFBK_nOrbit = XTTC_FBK_info[4]
            XTTCFBK_nOrbit_chr = str(XTTCFBK_nOrbit)
            SpanOr = i_space*(maxlennOrbit-len(XTTCFBK_nOrbit_chr))
            Det = SpanOr+' - '+Antenna
            if (XTTC_FBK_info[1]==True):
                BAOS_Gr_1 = 'On the MCS Ground Pass Viewer delete the PMON Pass configuration'
                BAOS_Gr_2 = '<br>Set the TC operational global on the MCS ground to OFF'
                BAOS_Gr_3 = '<br>Set the Auto MPF to the relevant CDA'
                BAOS_Gr_4 = '<br>Identify the pass configuration on the PI for the relevant pass and resend to the CDA'
                BAOS_Gr_5 = '<br>Set the TC operational global on the MCS to on'
                BAOS_Gr_6 = '<br>Set the Auto MPF back to auto or its previous setting'
                BAOS_Gr = BAOS_Gr_1 + BAOS_Gr_2 +BAOS_Gr_3 + BAOS_Gr_4 + BAOS_Gr_5 + BAOS_Gr_6
                iDate = XTTC_PPI_Date
                csv_DateT.append(iDtae)
                csv_Date.append(datatime2str_csv(iDtae))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Orbit '+XTTCFBK_nOrbit_chr+Det)
                csv_Text.append('<p>'+BAOS_Gr+'</p>')
                csv_LogbookID.append(LogbookID)
            
    
    
    data = {'Date_T': csv_DateT,
            'Date_str': csv_Date,
            'Entry': csv_Entry,
            'S/C': csv_SC,
            'Pass_Orbit': csv_PassOrbit,
            'Text': csv_Text,
            'LogBook_ID': csv_LogbookID
            }
    
    Data_csv_vet = DataFrame (data, columns = ['Date_T','Date_str','Entry','S/C','Pass_Orbit','Text','LogBook_ID'])
    Data_csv_vet = Data_csv_vet.sort_values(by=['Date_T'])
    Data_csv_vet = Data_csv_vet.reset_index()
    Data_csv_vet = Data_csv_vet.drop(columns='index')
    
    return Data_csv_vet











def fcn_wimpy_csv(FDF_Pass_M, file_Path_Name_csv, DS, DE, SpaGrndCon, opts , SHOfalg, XTTC_FBK_info, Man_info):
    
    Data_csv_vet = fcn_MPF_events_csv(FDF_Pass_M, DS, DE, SpaGrndCon, opts, SHOfalg, XTTC_FBK_info, Man_info)
    
    Data_csv_vet = Data_csv_vet.drop(columns='Date_T')
    
    Data_csv_vet.to_csv (r''+file_Path_Name_csv, index = False, header=False)
    