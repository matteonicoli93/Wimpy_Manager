#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:14:30 2020

@author: matteo
"""
import os
import csv
import datetime
from datetime import timezone

import pandas as pd
import numpy as np










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











def fcn_MPF_events_csv(FDF_Pass_M, DS, DE, SpaGrndCon, opts, SHOfalg, XTTC_FBK_info ):
    if ( SpaGrndCon == 1 ):
        LogbookID = '5e7c9f51a585c67a02eeed0d'
    elif ( SpaGrndCon == 2 ):
        LogbookID = '5ad5c6b7a585c614bac889cd'
    elif ( SpaGrndCon == 3 ):
        LogbookID = '5ad5c6b7a585c614bac889cc'
    
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
        Metop = FDF_Pass_M.loc[wrow,['M01']]['M01']
        intnOrbit = FDF_Pass_M.loc[wrow,['CDA_nOrbit']]['CDA_nOrbit']
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
                        
                        AOSlineText='AOS '+CDAn+'/TTC1     Az/ACU: '+Azstrsin+'.000°('+Azstr+'° expected)/2LT       TM:  OK      TC: OK'
                        MtOp=str(Metop)
                        GAC_type = FDF_Pass_M.loc[wrow,['GDS_GAC']]['GDS_GAC'][0:2]
                        GAC_Frame = FDF_Pass_M.loc[wrow,['GDS_GAC']]['GDS_GAC'][3:10]
                        LOSlineText='LOS     GAC: /'+GAC_Frame+' ('+GAC_type+') Frames'
                        
                        csv_DateT.append(AOS)
                        datastr=datatime2str_csv(AOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('N'+MtOp)
                        csv_PassOrbit.append('Pass Orbit '+nOrbit)
                        csv_Text.append(AOSlineText)
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(LOS)
                        datastr=datatime2str_csv(LOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('N'+MtOp)
                        csv_PassOrbit.append('Pass Orbit '+nOrbit)
                        csv_Text.append(LOSlineText)
                        csv_LogbookID.append(LogbookID)
                        
            else:
                AOSM=FDF_Pass_M.loc[wrow,['CDA_AOSM']]['CDA_AOSM']
                RPF=AOSM+datetime.timedelta(minutes=5)
                MtOp='0'+str(Metop)
                DEFPass = FDF_Pass_M.loc[wrow,['TM_Format']]['TM_Format']
                AOCSPass = FDF_Pass_M.loc[wrow,['AOCS']]['AOCS']
                
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
                AOSlineText='AOS    '+CDAn+'/TTC1     TM: OK      TC: OK     XBAND: OK'
                
                #==================================================================
                #
                if (DEFPass=='DEF_PLM'):
                    RPFlineText="All RPF's received and reset"
                elif (DEFPass=='DEF_ROUT'):
                    RPFlineText = 'SVM and TEXTR received and reset'
                
                #==================================================================
                #    
                nextAz=FDF_Pass_M.loc[wrow,['Next_Az_MetOp']]['Next_Az_MetOp']
                nextAzstr=str(nextAz)
                if (nextAz>=360-100):
                    nextAz = nextAz-360
                    nextAzstr=str(nextAz)

                if (len(str(abs(nextAz)))==1):
                    nextAzstrsin = '0'
                elif (len(str(abs(nextAz)))==2):
                    nextAzstrsin = '00'
                else:
                    nextAzstrsin = '000'
                
                nextAzstrsin1 = nextAzstr[0:1]
                if (nextAzstrsin1 != '-'):
                    nextAzstrsin = ''+nextAzstrsin
                else:
                    nextAzstrsin = nextAzstrsin1+nextAzstrsin
                #
                RD=FDF_Pass_M.loc[wrow,['RNGDOP']]['RNGDOP']
                
                if (SpaGrndCon==1):
                    if ( opts >= 2 ):
                        LOSlineText='LOS     Az/ACU: '+nextAzstrsin+'.000°('+nextAzstr+'° expected)/2LT       TC Count:        R/D: '+str(RD)+'/'+str(RD)+''
                    else:
                        LOSlineText='LOS     Az/ACU: '+nextAzstrsin+'.000('+nextAzstr+' expected)/2LT       TC Count:        R/D: '+str(RD)+'/'+str(RD)+''
                elif (SpaGrndCon==2):
                    LOSlineText='LOS        TC Count:        R/D: '+str(RD)+'/'+str(RD)+''
                elif (SpaGrndCon==3):
                    if ( opts >= 2 ):
                        LOSlineText='LOS     Az/ACU: '+nextAzstrsin+'.000°('+nextAzstr+'° expected)/2LT'
                    else:
                        LOSlineText='LOS     Az/ACU: '+nextAzstrsin+'.000('+nextAzstr+' expected)/2LT'
                
                #==================================================================
                if (XTTC_FBK_info[0]==1):
                    if (XTTC_FBK_info[1]==False):
                        csv_DateT.append(AOS)
                        datastr=datatime2str_csv(AOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('M'+MtOp)
                        csv_PassOrbit.append('Pass Orbit '+nOrbit)
                        csv_Text.append(AOSlineText)
                        csv_LogbookID.append(LogbookID)
                        
                        if (SpaGrndCon==1 or SpaGrndCon==2):
                            csv_DateT.append(RPF)
                            datastr=datatime2str_csv(RPF)
                            csv_Date.append(datastr)
                            csv_Entry.append('Entry')
                            csv_SC.append('M'+MtOp)
                            csv_PassOrbit.append('Pass Orbit '+nOrbit)
                            csv_Text.append(RPFlineText)
                            csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(LOS)
                        datastr=datatime2str_csv(LOS)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('M'+MtOp)
                        csv_PassOrbit.append('Pass Orbit '+nOrbit)
                        csv_Text.append(LOSlineText)
                        csv_LogbookID.append(LogbookID)
                    else:
                        if (intnOrbit!=XTTC_FBK_info[4]):
                            csv_DateT.append(AOS)
                            datastr=datatime2str_csv(AOS)
                            csv_Date.append(datastr)
                            csv_Entry.append('Entry')
                            csv_SC.append('M'+MtOp)
                            csv_PassOrbit.append('Pass Orbit '+nOrbit)
                            csv_Text.append(AOSlineText)
                            csv_LogbookID.append(LogbookID)
                            
                            if (SpaGrndCon==1 or SpaGrndCon==2):
                                csv_DateT.append(RPF)
                                datastr=datatime2str_csv(RPF)
                                csv_Date.append(datastr)
                                csv_Entry.append('Entry')
                                csv_SC.append('M'+MtOp)
                                csv_PassOrbit.append('Pass Orbit '+nOrbit)
                                csv_Text.append(RPFlineText)
                                csv_LogbookID.append(LogbookID)
                            
                            csv_DateT.append(LOS)
                            datastr=datatime2str_csv(LOS)
                            csv_Date.append(datastr)
                            csv_Entry.append('Entry')
                            csv_SC.append('M'+MtOp)
                            csv_PassOrbit.append('Pass Orbit '+nOrbit)
                            csv_Text.append(LOSlineText)
                            csv_LogbookID.append(LogbookID)
                else:
                    csv_DateT.append(AOS)
                    datastr=datatime2str_csv(AOS)
                    csv_Date.append(datastr)
                    csv_Entry.append('Entry')
                    csv_SC.append('M'+MtOp)
                    csv_PassOrbit.append('Pass Orbit '+nOrbit)
                    csv_Text.append(AOSlineText)
                    csv_LogbookID.append(LogbookID)
                    
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(RPF)
                        datastr=datatime2str_csv(RPF)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('M'+MtOp)
                        csv_PassOrbit.append('Pass Orbit '+nOrbit)
                        csv_Text.append(RPFlineText)
                        csv_LogbookID.append(LogbookID)
                    
                    csv_DateT.append(LOS)
                    datastr=datatime2str_csv(LOS)
                    csv_Date.append(datastr)
                    csv_Entry.append('Entry')
                    csv_SC.append('M'+MtOp)
                    csv_PassOrbit.append('Pass Orbit '+nOrbit)
                    csv_Text.append(LOSlineText)
                    csv_LogbookID.append(LogbookID)
                        
            
    flag_DE=0
    iminute=0
    while (flag_DE==0):
        iDate=DS+datetime.timedelta(minutes=iminute)
        if (iDate==DS and SHOfalg == 1):
            csv_DateT.append(iDate)
            datastr=datatime2str_csv(iDate)
            csv_Date.append(datastr)
            csv_Entry.append('Entry')
            csv_SC.append('CR')
            csv_PassOrbit.append('SHO')
            csv_Text.append('SHO completed, off, on-console, LAMON/LACON= /, CFS= //')
            csv_LogbookID.append(LogbookID)
            
        if (iDate >= DS and iDate <= DE ):
            if ( opts >= 3 ):
                if (iDate.weekday()==1-1 and iDate.hour==5 and iDate.minute==30):
                    csv_DateT.append(iDate)
                    datastr=datatime2str_csv(iDate)
                    csv_Date.append(datastr)
                    csv_Entry.append('Entry')
                    csv_SC.append('CDA')
                    csv_PassOrbit.append('Daily Event')
                    csv_Text.append('RNG/DOP Calibration')
                    csv_LogbookID.append(LogbookID)
                    
                if (iDate.weekday()==5-1 and iDate.hour==6 and iDate.minute==30 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('DIF')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('Weekly UNS check')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==7 and iDate.minute==50 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('OBT to UTC Check')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==7 and iDate.minute==50 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('PGF')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('PGF Aux file Check')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('CDA short period pointing file Check')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==5-1 and iDate.hour==8 and iDate.minute==10 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('Delay MMAMs')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==8 and iDate.minute==20 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('MMAMs')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==13 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('CDA long period pointing file Check')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==3-1 and iDate.hour==16 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('JASON')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('J3 pointing file check')
                        csv_LogbookID.append('5b0e8a6fa585c614bac88a0a')
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('JASON')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('J3 pass planning file check')
                        csv_LogbookID.append('5b0e8a6fa585c614bac88a0a')
                        
                if (iDate.hour==17 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('OBT to UTC Check')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==17 and iDate.minute==15 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('PGF')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('PGF Aux file Check')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==18 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CDA')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('CDA short period pointing file Check')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.hour==19 and iDate.minute==0 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('ALL METOP')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('MMAMs')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==6-1 and iDate.hour==23 and iDate.minute==59 ):
                    if (SpaGrndCon==1 or SpaGrndCon==2):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('Print schedule')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('Load CHRONOPS')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('Check ESTRACK Pass List')
                        csv_LogbookID.append(LogbookID)
                        
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('Load countdown tool')
                        csv_LogbookID.append(LogbookID)
                        
                if (iDate.weekday()==6-1 and iDate.hour==23 and iDate.minute==59 ):
                    if (SpaGrndCon==1 or SpaGrndCon==3):
                        csv_DateT.append(iDate)
                        datastr=datatime2str_csv(iDate)
                        csv_Date.append(datastr)
                        csv_Entry.append('Entry')
                        csv_SC.append('CR')
                        csv_PassOrbit.append('Daily Event')
                        csv_Text.append('Print WOTIS file')
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
                        iDate_AOS =XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]
                        iDate_AOS5=XTTC_FBK_info[5].loc['AOS5',[Antenna]][Antenna]
                    else:
                        iDate_AOS =XTTC_FBK_info[5].loc['LOS','CDA']['CDA']
                        iDate_AOS5=iDate_AOS+datetime.timedelta(seconds=2*60)
                    
                    iDate_AOS5=iDate_AOS5+datetime.timedelta(seconds=60)
                    #if (XTTC_FBK_info[2]=='KOU'):
                    iDate_LOS=XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]
                    #else:
                    #    iDate_LOS=XTTC_FBK_info[5].loc['AOS',['CDA']]['CDA']-datetime.timedelta(seconds=60+30)
                else:
                    iDate_AOS=XTTC_FBK_info[5].loc['LOS',['CDA']]['CDA']+datetime.timedelta(seconds=30)
                    iDate_AOS5=XTTC_FBK_info[5].loc['LOS',['CDA']]['CDA']+datetime.timedelta(seconds=2*60)+datetime.timedelta(minutes=1)
                    iDate_LOS=XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]
                
                csv_DateT.append(iDate_AOS)
                csv_Date.append(datatime2str_csv(iDate_AOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Pass Orbit '+XTTCFBK_nOrbit_chr)
                csv_Text.append('AOS    '+Ant+'/TTC1     TM: OK      TC: OK')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_AOS5)
                csv_Date.append(datatime2str_csv(iDate_AOS5))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Pass Orbit '+XTTCFBK_nOrbit_chr)
                csv_Text.append('NOP')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_LOS)
                csv_Date.append(datatime2str_csv(iDate_LOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Pass Orbit '+XTTCFBK_nOrbit_chr)
                csv_Text.append('LOS        TC Count:        ')
                csv_LogbookID.append(LogbookID)
            else:
                iDate_AOS=XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]
                iDate_AOS5=XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]+datetime.timedelta(minutes=1)
                iDate_LOS=XTTC_FBK_info[5].loc['LOS',[Antenna]][Antenna]
                
                csv_DateT.append(iDate_AOS)
                csv_Date.append(datatime2str_csv(iDate_AOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Pass Orbit '+XTTCFBK_nOrbit_chr)
                csv_Text.append('AOS    '+Ant+'/TTC1     TM: OK      TC: OK')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_AOS5)
                csv_Date.append(datatime2str_csv(iDate_AOS5))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Pass Orbit '+XTTCFBK_nOrbit_chr)
                csv_Text.append('NOP')
                csv_LogbookID.append(LogbookID)
                
                csv_DateT.append(iDate_LOS)
                csv_Date.append(datatime2str_csv(iDate_LOS))
                csv_Entry.append('Entry')
                csv_SC.append(XTTC_FBK_info[3])
                csv_PassOrbit.append('Pass Orbit '+XTTCFBK_nOrbit_chr)
                csv_Text.append('LOS        TC Count:        ')
                csv_LogbookID.append(LogbookID)
                
    data = {'Date_T': csv_DateT,
            'Date_str': csv_Date,
            'Entry': csv_Entry,
            'S/C': csv_SC,
            'Pass_Orbit': csv_PassOrbit,
            'Text': csv_Text,
            'LogBook_ID': csv_LogbookID
            }
    
    Data_csv_vet = pd.DataFrame (data, columns = ['Date_T','Date_str','Entry','S/C','Pass_Orbit','Text','LogBook_ID'])
    Data_csv_vet = Data_csv_vet.sort_values(by=['Date_T'])
    Data_csv_vet = Data_csv_vet.reset_index()
    Data_csv_vet = Data_csv_vet.drop(columns='index')
    
    return Data_csv_vet











def fcn_wimpy_csv(FDF_Pass_M,filename, DS, DE, SpaGrndCon, opts , SHOfalg, XTTC_FBK_info):
    
    Data_csv_vet = fcn_MPF_events_csv(FDF_Pass_M, DS, DE, SpaGrndCon, opts, SHOfalg, XTTC_FBK_info)
    
    Data_csv_vet = Data_csv_vet.drop(columns='Date_T')
    
    Data_csv_vet.to_csv (r''+filename+'.csv', index = False, header=False)
    