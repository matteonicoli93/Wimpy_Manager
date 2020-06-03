# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:16:26 2020

@author: Nicoli
"""

import datetime
from datetime import timezone

import pandas as pd

#from M01_CDA_XBand_Dump_Processing_MS import *


def fcn_Wimpy_Maga(DS,DE,Wimpyfilepath,MetOp,CDAn):
    def Date_Str2Datetime(YMD,Dhmss):
        YYYYPageDate=int(YMD[20:24])
        MMPageDate=int(YMD[25:27])
        DDPageDate=int(YMD[28:30])
        
        DD_date=int(Dhmss[0:2])
        hh_date=int(Dhmss[3:5])
        mm_date=int(Dhmss[6:8])
        #ss_date=float(Dhmss[9:15])
        s1ss_date=int(Dhmss[9:11])
        s2ss_date=int(Dhmss[12:15])
        Date_date=datetime.datetime(YYYYPageDate, MMPageDate, DD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
        return Date_date
    def Date_Str2Datetime2(YMD, Dhmss, DD_date_Old):
        YYYYPageDate=int(YMD[20:24])
        MMPageDate=int(YMD[25:27])
        DDPageDate=int(YMD[28:30])
        
        DD_date=int(Dhmss[0:2])
        hh_date=int(Dhmss[3:5])
        mm_date=int(Dhmss[6:8])
        #ss_date=float(Dhmss[9:15])
        s1ss_date=int(Dhmss[9:11])
        s2ss_date=int(Dhmss[12:15])
        
        Date_date=datetime.datetime(YYYYPageDate, MMPageDate, DD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
        if (Date_date<DD_date_Old):
            if (MMPageDate==12):
                MMPageDate=1
                YYYYPageDate=YYYYPageDate+1
            else:
                MMPageDate=MMPageDate+1
            Date_date=datetime.datetime(YYYYPageDate, MMPageDate, DD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
        return Date_date
    
    error_line = 0
    now_custm16=DS-datetime.timedelta(minutes=16)
    now_cust=now_custm16-datetime.timedelta(minutes=20)
    timestamp = datetime.datetime.timestamp(now_cust)
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    
    DEp16=DE+datetime.timedelta(minutes=16)
    nowp36=DE+datetime.timedelta(minutes=101+70)
    
    fp=open(Wimpyfilepath,'r')
    lines=fp.readlines()
    
    metop=lines[17-1].strip()
    M01flag = int(metop[6:7])
    
    strPageDate=lines[15-1].strip()
    Page1date=lines[15+7-1].strip()
    Date1date=Date_Str2Datetime(strPageDate,Page1date)
    strPageDate2=lines[15+59-1].strip()
    Page2date=lines[15+7+59-1].strip()
    Date2date=Date_Str2Datetime(strPageDate2,Page2date)
    for row in range(15,len(lines),59):
        strPageDate=lines[row-1].strip()
        Page1date=lines[row+7-1].strip()
        Date1date = Date_Str2Datetime2(strPageDate,Page1date, Date1date)
        
        if (row+7+59-1<=len(lines)):
            strPageDate2=lines[row+59-1].strip()
            Page2date=lines[row+7+59-1].strip()
            Date2date = Date_Str2Datetime2(strPageDate2,Page2date, Date2date)
        else:
            strPageDate2=lines[row-1].strip()
            Page2date=lines[len(lines)-1].strip()
            Date2date = Date_Str2Datetime2(strPageDate2,Page2date,Date2date)
        if (Date1date<=now_cust and Date2date>=now_cust):
            RowNow=row
        Dflag=1
    
    ii_RowNow = RowNow
    flag=1
    flag59=0
    flagCDA=1
    flag_CDA_Pass_old=0
    flag_CDA_Pass_new=0
    flag_CDA_mPass_old=0
    flag_CDA_mPass_new=0
    i_AOS=0
    i_LOS=0
    i_ANX=[]
    i_CDA_AOS_i_Datedate=[]
    i_CDA_AOS_nOrbit=[]
    i_CDA_AOS_Azi=[]
    i_CDA_AOSM_i_Datedate=[]
    i_CDA_AOSM_nOrbit=[]
    i_CDA_AOSM_Azi=[]
    i_CDA_AOS5_i_Datedate=[]
    i_CDA_AOS5_nOrbit=[]
    i_CDA_AOS5_Azi=[]
    i_CDA_M_i_Datedate=[]
    i_CDA_M_nOrbit=[]
    i_CDA_M_Azi=[]
    i_CDA_M_El=[]
    i_CDA_LOSM_i_Datedate=[]
    i_CDA_LOSM_nOrbit=[]
    i_CDA_LOSM_Azi=[]
    i_CDA_LOS5_i_Datedate=[]
    i_CDA_LOS5_nOrbit=[]
    i_CDA_LOS5_Azi=[]
    i_CDA_LOS_i_Datedate=[]
    i_CDA_LOS_nOrbit=[]
    i_CDA_LOS_Azi=[]
    
    flagMCMURDO=1
    flag_MCMURDO_Pass_old=0
    flag_MCMURDO_Pass_new=0
    flag_MCMURDO_mPass_old=0
    flag_MCMURDO_mPass_new=0
    i_AOS=0
    i_LOS=0
    i_MCMURDO_AOS_i_Datedate=[]
    i_MCMURDO_AOS_nOrbit=[]
    i_MCMURDO_AOS_Azi=[]
    i_MCMURDO_AOSM_i_Datedate=[]
    i_MCMURDO_AOSM_nOrbit=[]
    i_MCMURDO_AOSM_Azi=[]
    i_MCMURDO_AOS5_i_Datedate=[]
    i_MCMURDO_AOS5_nOrbit=[]
    i_MCMURDO_AOS5_Azi=[]
    i_MCMURDO_M_i_Datedate=[]
    i_MCMURDO_M_nOrbit=[]
    i_MCMURDO_M_Azi=[]
    i_MCMURDO_LOS5_i_Datedate=[]
    i_MCMURDO_LOS5_nOrbit=[]
    i_MCMURDO_LOS5_Azi=[]
    i_MCMURDO_LOSM_i_Datedate=[]
    i_MCMURDO_LOSM_nOrbit=[]
    i_MCMURDO_LOSM_Azi=[]
    i_MCMURDO_LOS_i_Datedate=[]
    i_MCMURDO_LOS_nOrbit=[]
    i_MCMURDO_LOS_Azi=[]
    
    while (flag==1):
        strPageDate=lines[ii_RowNow-1].strip()
        Page1date=lines[ii_RowNow+7-1].strip()
        i_Datedate=Date_Str2Datetime(strPageDate,Page1date)
        i_Datedate_2 = i_Datedate
        for i_RowNow in range(ii_RowNow+7-1,ii_RowNow+59-1):
            i_strPageDate=lines[ii_RowNow-1].strip()
            
            iii_RowNow =i_RowNow
            i_Pagedate=lines[iii_RowNow].strip()
            i_Datedate_OLD = i_Datedate
            i_Datedate = Date_Str2Datetime2(i_strPageDate,i_Pagedate,i_Datedate)
            if (i_Datedate > i_Datedate_OLD + datetime.timedelta(hours=2)):
                error_line = i_RowNow
            i_chr_ANX=i_Pagedate[16:17]
            
            if (i_chr_ANX=='A'):
                i_ANX.append(i_Datedate)
            
            
            i_nOrbit=int(i_Pagedate[21:26])
            i_chr_CDA_Azi=i_Pagedate[29:32]
            if (i_chr_CDA_Azi!='   ' and i_chr_CDA_Azi!=''):
                i_chr_CDA_M=i_Pagedate[36:37]
                i_CDA_Azi=int(i_Pagedate[29:32])
                i_CDA_El=int(i_Pagedate[33:35])
                if (flag_CDA_mPass_old==0 and i_CDA_El==0):
                    flag_AOS=1
                    i_CDA_AOS_i_Datedate.append(i_Datedate)
                    i_CDA_AOS_nOrbit.append(i_nOrbit)
                    i_CDA_AOS_Azi.append(i_CDA_Azi)
                    i_AOS = i_AOS+1
                    flag_CDA_Pass_new=1
                if (i_chr_CDA_M=='M'):
                    i_CDA_M_i_Datedate.append(i_Datedate)
                    i_CDA_M_nOrbit.append(i_nOrbit)
                    i_CDA_M_Azi.append(i_CDA_Azi)
                    i_CDA_M_El.append(i_CDA_El)
                if (i_chr_CDA_M=='a'):
                    i_CDA_AOSM_i_Datedate.append(i_Datedate)
                    i_CDA_AOSM_nOrbit.append(i_nOrbit)
                    i_CDA_AOSM_Azi.append(i_CDA_Azi)
                if (i_chr_CDA_M=='A'):
                    i_CDA_AOS5_i_Datedate.append(i_Datedate)
                    i_CDA_AOS5_nOrbit.append(i_nOrbit)
                    i_CDA_AOS5_Azi.append(i_CDA_Azi)
                if (i_chr_CDA_M=='L'):
                    i_CDA_LOS5_i_Datedate.append(i_Datedate)
                    i_CDA_LOS5_nOrbit.append(i_nOrbit)
                    i_CDA_LOS5_Azi.append(i_CDA_Azi)
                if (i_chr_CDA_M=='l'):
                    i_CDA_LOSM_i_Datedate.append(i_Datedate)
                    i_CDA_LOSM_nOrbit.append(i_nOrbit)
                    i_CDA_LOSM_Azi.append(i_CDA_Azi)
                flag_CDA_mPass_new=1
            else:
                if (flag_CDA_Pass_old==1 and i_CDA_El==0 and flag59==1):
                    i_strPageDate_2 = lines[ii_RowNow-59-1].strip()
                    i_Pagedate_2=lines[iii_RowNow-8].strip()
                    i_Datedate_2 = Date_Str2Datetime2(i_strPageDate_2,i_Pagedate_2,i_CDA_AOS_i_Datedate[-1])
                    
                    i_CDA_Azi_2=int(i_Pagedate_2[29:32])
                    i_CDA_El_2=int(i_Pagedate_2[33:35])
                    
                    flag_LOS=1
                    i_CDA_LOS_i_Datedate.append(i_Datedate_2)
                    i_CDA_LOS_nOrbit.append(i_nOrbit)
                    i_CDA_LOS_Azi.append(i_CDA_Azi_2)
                    i_LOS = i_LOS+1
                elif (flag_CDA_Pass_old==1 and i_CDA_El==0):
                    i_Pagedate_2=lines[iii_RowNow-1].strip()
                    i_Datedate_2 = Date_Str2Datetime2(i_strPageDate,i_Pagedate_2,i_CDA_AOS_i_Datedate[-1])
                    
                    i_CDA_Azi_2=int(i_Pagedate_2[29:32])
                    i_CDA_El_2=int(i_Pagedate_2[33:35])
                    
                    flag_LOS=1
                    i_CDA_LOS_i_Datedate.append(i_Datedate_2)
                    i_CDA_LOS_nOrbit.append(i_nOrbit)
                    i_CDA_LOS_Azi.append(i_CDA_Azi_2)
                    i_LOS = i_LOS+1
                flag_CDA_Pass_new=0
                flag_CDA_mPass_new=0
            flag_CDA_Pass_old =flag_CDA_Pass_new
            flag_CDA_mPass_old=flag_CDA_mPass_new
            
            i_chr_MCMURDO_Azi=i_Pagedate[40:43]
            if (i_chr_MCMURDO_Azi!='   ' and i_chr_MCMURDO_Azi!=''):
                i_chr_MCMURDO_M=i_Pagedate[47:48]
                i_MCMURDO_Azi=int(i_Pagedate[40:43])
                i_MCMURDO_El=int(i_Pagedate[45:46])
                if (flag_MCMURDO_mPass_old==0 and i_MCMURDO_El==0):
                    flag_AOS=1
                    i_MCMURDO_AOS_i_Datedate.append(i_Datedate)
                    i_MCMURDO_AOS_nOrbit.append(i_nOrbit)
                    i_MCMURDO_AOS_Azi.append(i_MCMURDO_Azi)
                    i_AOS = i_AOS+1
                    flag_MCMURDO_Pass_new=1
                if (i_chr_MCMURDO_M=='M'):
                    i_MCMURDO_M_i_Datedate.append(i_Datedate)
                    i_MCMURDO_M_nOrbit.append(i_nOrbit)
                    i_MCMURDO_M_Azi.append(i_MCMURDO_Azi)
                if (i_chr_MCMURDO_M=='a'):
                    i_MCMURDO_AOSM_i_Datedate.append(i_Datedate)
                    i_MCMURDO_AOSM_nOrbit.append(i_nOrbit)
                    i_MCMURDO_AOSM_Azi.append(i_MCMURDO_Azi)
                if (i_chr_MCMURDO_M=='A'):
                    i_MCMURDO_AOS5_i_Datedate.append(i_Datedate)
                    i_MCMURDO_AOS5_nOrbit.append(i_nOrbit)
                    i_MCMURDO_AOS5_Azi.append(i_MCMURDO_Azi)
                if (i_chr_MCMURDO_M=='L'):
                    i_MCMURDO_LOS5_i_Datedate.append(i_Datedate)
                    i_MCMURDO_LOS5_nOrbit.append(i_nOrbit)
                    i_MCMURDO_LOS5_Azi.append(i_MCMURDO_Azi)
                if (i_chr_MCMURDO_M=='l'):
                    i_MCMURDO_LOSM_i_Datedate.append(i_Datedate)
                    i_MCMURDO_LOSM_nOrbit.append(i_nOrbit)
                    i_MCMURDO_LOSM_Azi.append(i_MCMURDO_Azi)
                
                flag_MCMURDO_mPass_new=1
            else:
                if (flag_MCMURDO_Pass_old==1 and i_MCMURDO_El==0 and flag59==1):
                    i_strPageDate_2 = lines[ii_RowNow-59-1].strip()
                    i_Pagedate_2=lines[iii_RowNow-8].strip()
                    i_Datedate_2 = Date_Str2Datetime2(i_strPageDate_2,i_Pagedate_2,i_MCMURDO_AOS_i_Datedate[-1])
                    
                    i_MCMURDO_Azi_2=int(i_Pagedate_2[40:43])
                    i_MCMURDO_El_2=int(i_Pagedate_2[45:46])
                    
                    flag_LOS=1
                    i_MCMURDO_LOS_i_Datedate.append(i_Datedate_2)
                    i_MCMURDO_LOS_nOrbit.append(i_nOrbit)
                    i_MCMURDO_LOS_Azi.append(i_MCMURDO_Azi_2)
                    i_LOS = i_LOS+1
                elif (flag_MCMURDO_Pass_old==1 and i_MCMURDO_El==0):
                    i_Pagedate_2=lines[iii_RowNow-1].strip()
                    i_Datedate_2 = Date_Str2Datetime2(i_strPageDate,i_Pagedate_2,i_MCMURDO_AOS_i_Datedate[-1])
                    
                    i_MCMURDO_Azi_2=int(i_Pagedate_2[40:43])
                    i_MCMURDO_El_2=int(i_Pagedate_2[45:46])
                    
                    flag_LOS=1
                    i_MCMURDO_LOS_i_Datedate.append(i_Datedate_2)
                    i_MCMURDO_LOS_nOrbit.append(i_nOrbit)
                    i_MCMURDO_LOS_Azi.append(i_MCMURDO_Azi_2)
                    i_LOS = i_LOS+1
                flag_MCMURDO_Pass_new=0
                flag_MCMURDO_mPass_new=0
            flag_MCMURDO_Pass_old =flag_MCMURDO_Pass_new
            flag_MCMURDO_mPass_old =flag_MCMURDO_mPass_new
            flag59=0
            
            if (i_Datedate>nowp36 ):
                flag=0
        
        ii_RowNow=ii_RowNow+59
        flag59=1
    
    fp.close()
    
    ANX=[]
    NOAA_BOS = []
    GDS_GAC = []
    CDA_AOS_SC=[]
    CDA_AOS_DEFPass=[]
    CDA_AOS_AOCSPass=[]
    CDA_AOS_AOCS=[]
    CDA_AOS_M01=[]
    CDA_n=[]
    CDA_RNGDOP=[]
    CDA_AOS_Date=[]
    CDA_AOS_Azi=[]
    CDA_AOS_nOrbit=[]
    CDA_AOSM_Date=[]
    CDA_AOS5_Date=[]
    CDA_M_Date=[]
    CDA_M_El=[]
    CDA_LOS5_Date=[]
    CDA_LOSM_Date=[]
    CDA_LOS_Date=[]
    MCMURDO_AOS_Date=[]
    MCMURDO_AOS_Azi=[]
    MCMURDO_AOSM_Date=[]
    MCMURDO_AOS5_Date=[]
    MCMURDO_M_Date=[]
    MCMURDO_LOS5_Date=[]
    MCMURDO_LOSM_Date=[]
    MCMURDO_LOS_Date=[]
#    CDA_CONF_PI=[]
#    CDA_CONF_S=[]
#    CDA_CONF_E=[]
#    CDA_STANDBY_S=[]
#    CDA_STANDBY_E=[]
    ii_AOS=-1
    for i_AOS in range(0,len(i_CDA_AOS_i_Datedate)-1):
        if (i_CDA_AOS_i_Datedate[i_AOS]>=now_custm16):
            CDA_AOS_Date.append(i_CDA_AOS_i_Datedate[i_AOS])
            CDA_AOS_Azi.append(i_CDA_AOS_Azi[i_AOS])
            CDA_AOS_nOrbit.append(i_CDA_AOS_nOrbit[i_AOS])
            CDA_AOS_SC.append(MetOp)
            CDA_AOS_M01.append(M01flag)
            CDA_n.append(CDAn)
            NOAA_BOS.append('N/A')
            GDS_GAC.append('N/A')
            
            AOS_horsmm=i_CDA_AOS_i_Datedate[i_AOS].hour+i_CDA_AOS_i_Datedate[i_AOS].minute/60
            if ( (AOS_horsmm>2+(15/60) and AOS_horsmm<3+(48/60)) ):
                CDA_AOS_DEFPass.append('DEF_ROUT')
            else:
                CDA_AOS_DEFPass.append('DEF_PLM')
            
            CDA_AOS_AOCS.append('AOCS')
 #           if (AOS_horsmm>9+(24/60) and AOS_horsmm<11):
                
#            else:
#                CDA_AOS_AOCS.append(0)
            
#            if (AOS_horsmm>21+(26/60) and AOS_horsmm<23+(4/60)):
#                CDA_AOS_AOCS.append('AOCS')
#            else:
#                CDA_AOS_AOCS.append(0)
            
            
            ii_AOS=ii_AOS+1
            
            flag_ANX=0
            ii_ANX=-1
            while (flag_ANX==0):
                ii_ANX=ii_ANX+1
                if (i_ANX[ii_ANX]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=40)):
                    ANX.append(i_ANX[ii_ANX])
                    flag_ANX=1
            flag_CDA_LOS=0
            i_CDA_LOS=-1
            while (flag_CDA_LOS==0):
                i_CDA_LOS=i_CDA_LOS+1
                if (i_CDA_LOS_i_Datedate[i_CDA_LOS]>CDA_AOS_Date[ii_AOS]):
                    CDA_LOS_Date.append(i_CDA_LOS_i_Datedate[i_CDA_LOS])
                    flag_CDA_LOS=1
            flag_CDA_AOSM=0
            i_CDA_AOSM=-1
            while (flag_CDA_AOSM==0):
                i_CDA_AOSM=i_CDA_AOSM+1
                if (i_CDA_AOSM_i_Datedate[i_CDA_AOSM]>CDA_AOS_Date[ii_AOS]):
                    CDA_AOSM_Date.append(i_CDA_AOSM_i_Datedate[i_CDA_AOSM])
                    flag_CDA_AOSM=1
            flag_CDA_AOS5=0
            i_CDA_AOS5=-1
            while (flag_CDA_AOS5==0):
                i_CDA_AOS5=i_CDA_AOS5+1
                if (i_CDA_AOS5_i_Datedate[i_CDA_AOS5]>CDA_AOS_Date[ii_AOS]):
                    CDA_AOS5_Date.append(i_CDA_AOS5_i_Datedate[i_CDA_AOS5])
                    flag_CDA_AOS5=1
            flag_CDA_M=0
            i_CDA_M=-1
            while (flag_CDA_M==0):
                i_CDA_M=i_CDA_M+1
                if (i_CDA_M_i_Datedate[i_CDA_M]>CDA_AOS_Date[ii_AOS]):
                    CDA_M_Date.append(i_CDA_M_i_Datedate[i_CDA_M])
                    CDA_M_El.append(i_CDA_M_El[i_CDA_M])
                    flag_CDA_M=1
            flag_CDA_LOS5=0
            i_CDA_LOS5=-1
            while (flag_CDA_LOS5==0):
                i_CDA_LOS5=i_CDA_LOS5+1
                if (i_CDA_LOS5_i_Datedate[i_CDA_LOS5]>CDA_AOS_Date[ii_AOS]):
                    CDA_LOS5_Date.append(i_CDA_LOS5_i_Datedate[i_CDA_LOS5])
                    flag_CDA_LOS5=1
            flag_CDA_LOSM=0
            i_CDA_LOSM=-1
            while (flag_CDA_LOSM==0):
                i_CDA_LOSM=i_CDA_LOSM+1
                if (i_CDA_LOSM_i_Datedate[i_CDA_LOSM]>CDA_AOS_Date[ii_AOS]):
                    CDA_LOSM_Date.append(i_CDA_LOSM_i_Datedate[i_CDA_LOSM])
                    flag_CDA_LOSM=1
            flag_MCMURDO_AOS=0
            i_MCMURDO_AOS=-1
            while (flag_MCMURDO_AOS==0):
                i_MCMURDO_AOS=i_MCMURDO_AOS+1
                if (i_MCMURDO_AOS_i_Datedate[i_MCMURDO_AOS]>CDA_AOS_Date[ii_AOS]):
                    MCMURDO_AOS_Date.append(i_MCMURDO_AOS_i_Datedate[i_MCMURDO_AOS])
                    MCMURDO_AOS_Azi.append(i_MCMURDO_AOS_Azi[i_MCMURDO_AOS])
                    flag_MCMURDO_AOS=1
            flag_MCMURDO_AOSM=0
            i_MCMURDO_AOSM=-1
            while (flag_MCMURDO_AOSM==0):
                i_MCMURDO_AOSM=i_MCMURDO_AOSM+1
                if (i_MCMURDO_AOSM_i_Datedate[i_MCMURDO_AOSM]>CDA_AOS_Date[ii_AOS]):
                    MCMURDO_AOSM_Date.append(i_MCMURDO_AOSM_i_Datedate[i_MCMURDO_AOSM])
                    flag_MCMURDO_AOSM=1
            flag_MCMURDO_AOS5=0
            i_MCMURDO_AOS5=-1
            while (flag_MCMURDO_AOS5==0):
                i_MCMURDO_AOS5=i_MCMURDO_AOS5+1
                if (i_MCMURDO_AOS5_i_Datedate[i_MCMURDO_AOS5]>CDA_AOS_Date[ii_AOS]):
                    MCMURDO_AOS5_Date.append(i_MCMURDO_AOS5_i_Datedate[i_MCMURDO_AOS5])
                    flag_MCMURDO_AOS5=1
            flag_MCMURDO_M=0
            i_MCMURDO_M=-1
            while (flag_MCMURDO_M==0):
                i_MCMURDO_M=i_MCMURDO_M+1
                if (i_MCMURDO_M_i_Datedate[i_MCMURDO_M]>CDA_AOS_Date[ii_AOS]):
                    MCMURDO_M_Date.append(i_MCMURDO_M_i_Datedate[i_MCMURDO_M])
                    flag_MCMURDO_M=1
            flag_MCMURDO_LOS5=0
            i_MCMURDO_LOS5=-1
            while (flag_MCMURDO_LOS5==0):
                i_MCMURDO_LOS5=i_MCMURDO_LOS5+1
                if (i_MCMURDO_LOS5_i_Datedate[i_MCMURDO_LOS5]>CDA_AOS_Date[ii_AOS]):
                    MCMURDO_LOS5_Date.append(i_MCMURDO_LOS5_i_Datedate[i_MCMURDO_LOS5])
                    flag_MCMURDO_LOS5=1
            flag_MCMURDO_LOSM=0
            i_MCMURDO_LOSM=-1
            while (flag_MCMURDO_LOSM==0):
                i_MCMURDO_LOSM=i_MCMURDO_LOSM+1
                if (i_MCMURDO_LOSM_i_Datedate[i_MCMURDO_LOSM]>CDA_AOS_Date[ii_AOS]):
                    MCMURDO_LOSM_Date.append(i_MCMURDO_LOSM_i_Datedate[i_MCMURDO_LOSM])
                    flag_MCMURDO_LOSM=1
            flag_MCMURDO_LOS=0
            i_MCMURDO_LOS=-1
            while (flag_MCMURDO_LOS==0):
                i_MCMURDO_LOS=i_MCMURDO_LOS+1
                if (i_MCMURDO_LOS_i_Datedate[i_MCMURDO_LOS]>CDA_AOS_Date[ii_AOS]):
                    MCMURDO_LOS_Date.append(i_MCMURDO_LOS_i_Datedate[i_MCMURDO_LOS])
                    flag_MCMURDO_LOS=1
            
            TC_len_s = (CDA_LOS5_Date[-1]-CDA_AOS5_Date[-1]).seconds
            TC_len_ms = (CDA_LOS5_Date[-1]-CDA_AOS5_Date[-1]).microseconds
            TC_len = TC_len_s + TC_len_ms*1e-6
            C_O = 65
            Window = TC_len-2*C_O
            FIX = (TC_len/2-C_O)/3
            OFFSET_1=FIX+C_O
            OFFSET_2=TC_len/2
            OFFSET_3=TC_len-C_O-FIX
            if ( Window > 3*C_O ):
                nRNGDOP = 3
            elif ( Window > 1.5*C_O):
                nRNGDOP = 2
            else:
                nRNGDOP = 1
                
            #if (TC_len <= 397.5):
            #    nRNGDOP = 1
            #elif (TC_len <= 495):
            #    nRNGDOP = 2
            #else:
            #    nRNGDOP = 3
            CDA_RNGDOP.append(nRNGDOP)
                
    data = {'S/C': CDA_AOS_SC,
            'NOAA_BOS': NOAA_BOS,
            'GDS_GAC': GDS_GAC,
            'M01': CDA_AOS_M01,
            'CDAn': CDA_n,
            'TM_Format': CDA_AOS_DEFPass,
            'AOCS': CDA_AOS_AOCS,
            'RNGDOP': CDA_RNGDOP,
            'ANX': ANX,
            'CDA_AOS': CDA_AOS_Date,
            'CDA_nOrbit': CDA_AOS_nOrbit,
            'CDA_AOS_Azi': CDA_AOS_Azi,
            'CDA_AOSM': CDA_AOSM_Date,
            'CDA_AOS5': CDA_AOS5_Date,
            'CDA_Mid': CDA_M_Date,
            'CDA_Mid_El': CDA_M_El,
            'CDA_LOS5': CDA_LOS5_Date,
            'CDA_LOSM': CDA_LOSM_Date,
            'CDA_LOS': CDA_LOS_Date,
            'ADA_AOS': MCMURDO_AOS_Date,
            'ADA_AOS_Azi': MCMURDO_AOS_Azi,
            'ADA_AOSM': MCMURDO_AOSM_Date,
            'ADA_AOS5': MCMURDO_AOS5_Date,
            'ADA_Mid': MCMURDO_M_Date,
            'ADA_LOS5': MCMURDO_LOS5_Date,
            'ADA_LOSM': MCMURDO_LOSM_Date,
            'ADA_LOS': MCMURDO_LOS_Date
#            'CDA_CONF_PI': CDA_CONF_PI,
#            'CDA_CONF_S': CDA_CONF_S,
#            'CDA_CONF_E': CDA_CONF_E,
#            'CDA_PASS_S': CDA_AOS_Date,
#            'CDA_PASS_E': CDA_LOS_Date,
#            'CDA_STANDBY_S': CDA_STANDBY_S,
#            'CDA_STANDBY_E': CDA_STANDBY_E
            }
    
#    FDF_Pass = pd.DataFrame (data, columns = ['S/C','M01','ANX','CDA_AOS','CDA_nOrbit','CDA_AOS_Azi','CDA_AOSM','CDA_AOS5','CDA_Mid','CDA_LOS5','CDA_LOSM','CDA_LOS','ADA_AOS','ADA_AOS_Azi','ADA_AOSM','ADA_AOS5','ADA_Mid','ADA_LOS5','ADA_LOSM','ADA_LOS','CDA_CONF_PI','CDA_CONF_S','CDA_CONF_E','CDA_PASS_S','CDA_PASS_E','CDA_STANDBY_S','CDA_STANDBY_E'])
    FDF_Pass = pd.DataFrame (data, columns = ['S/C','NOAA_BOS','GDS_GAC','M01','CDAn','TM_Format','AOCS','RNGDOP','ANX','CDA_AOS','CDA_nOrbit','CDA_AOS_Azi','CDA_AOSM','CDA_AOS5','CDA_Mid','CDA_Mid_El','CDA_LOS5','CDA_LOSM','CDA_LOS','ADA_AOS','ADA_AOS_Azi','ADA_AOSM','ADA_AOS5','ADA_Mid','ADA_LOS5','ADA_LOSM','ADA_LOS'])
    return FDF_Pass, error_line











def mergeWimpy(frames, delflag, DS, DE, MSW_info ):
    result = pd.concat(frames)
    FDF_Pass_M = result.sort_values(by=['CDA_AOS'])
    FDF_Pass_M = FDF_Pass_M.reset_index()
    FDF_Pass_M = FDF_Pass_M.drop(columns='index')
    
    if (delflag == 1):
        flag=1
        flagDE=1
        wrow = -1
        listwrow=[]
        next_Az_M = []
        while (flag==1):
            wrow = wrow + 1
            DAOS = FDF_Pass_M.loc[wrow,['CDA_AOS']]['CDA_AOS']
            if (DAOS<DS or DAOS>DE):
                listwrow.append(wrow)
                if (DAOS>DE and flagDE==1):
                    nextwrow=wrow
                    flagDE=0
            else:
                AOS=FDF_Pass_M.loc[wrow,['CDA_AOS']]['CDA_AOS']
                CDAn = FDF_Pass_M.loc[wrow,['CDAn']]['CDAn']
                if (MSW_info[0]==1):
                    if (CDAn[0:3]=='CDA'):
                        if (AOS>=MSW_info[1] and AOS<=MSW_info[2]):
                            if (CDAn=='CDA1'):
                                CDAn = 'CDA2'
                            else:
                                CDAn = 'CDA1'
                FDF_Pass_M.at[wrow,'CDAn']=CDAn
                
                if (FDF_Pass_M.loc[wrow,['M01']]['M01'] != 19 and FDF_Pass_M.loc[wrow,['M01']]['M01'] != 18 ):
                    if ( FDF_Pass_M.loc[wrow+1,['M01']]['M01'] == 19 or FDF_Pass_M.loc[wrow+1,['M01']]['M01'] == 18 ):
                        if ( FDF_Pass_M.loc[wrow+2,['M01']]['M01'] == 19 or FDF_Pass_M.loc[wrow+2,['M01']]['M01'] == 18 ):
                            nextAz=FDF_Pass_M.loc[wrow+3,['CDA_AOS_Azi']]['CDA_AOS_Azi']
                            next_Az_M.append(nextAz)
                        else:
                            nextAz=FDF_Pass_M.loc[wrow+2,['CDA_AOS_Azi']]['CDA_AOS_Azi']
                            next_Az_M.append(nextAz)
                    else:
                        nextAz=FDF_Pass_M.loc[wrow+1,['CDA_AOS_Azi']]['CDA_AOS_Azi']
                        next_Az_M.append(nextAz)
                else:
                    next_Az_M.append(0)
                    
                        
            if (wrow>=FDF_Pass_M.shape[0]-1):
                flag=0
        
        
        FDF_Pass_M_c = FDF_Pass_M.drop(index=listwrow)
        FDF_Pass_M_c = FDF_Pass_M_c.reset_index()
        FDF_Pass_M = FDF_Pass_M_c.drop(columns='index')
        
        data = {
                'Next_Az_MetOp': next_Az_M
                }
    
        pd_next_Az_M = pd.DataFrame(data, columns = ['Next_Az_MetOp'])
        
        FDF_Pass_M = pd.concat([FDF_Pass_M, pd_next_Az_M.reindex(pd_next_Az_M.index)], axis=1)
    
    return FDF_Pass_M











def fcn_MPF_mang(FDF_Pass):
    CDA_CONF_PI=[]
    CDA_CONF_S=[]
    CDA_CONF_E=[]
    CDA_AOS_Date = []
    CDA_LOS_Date = []
    CDA_STANDBY_S=[]
    CDA_STANDBY_E=[]
    CDA_FEP=[]
    CDA_PGF=[]
    
    for i_Pass in range(0,FDF_Pass.shape[0]):
        i_CDA_AOS_i_Datedate = FDF_Pass.loc[i_Pass,['CDA_AOS']]['CDA_AOS']
        CDA_CONF_PI.append(i_CDA_AOS_i_Datedate-datetime.timedelta(hours=36))
        CDA_CONF_S.append(i_CDA_AOS_i_Datedate-datetime.timedelta(minutes=4))
        CDA_CONF_E.append(i_CDA_AOS_i_Datedate-datetime.timedelta(minutes=4)+datetime.timedelta(seconds=12))
        CDA_AOS_Date.append(i_CDA_AOS_i_Datedate)
        i_CDA_LOS_i_Datedate = FDF_Pass.loc[i_Pass,['CDA_LOS']]['CDA_LOS']
        CDA_LOS_Date.append(i_CDA_LOS_i_Datedate)
        CDA_STANDBY_S.append(i_CDA_LOS_i_Datedate+datetime.timedelta(seconds=5))
        CDA_STANDBY_E.append(i_CDA_LOS_i_Datedate+datetime.timedelta(seconds=5)+datetime.timedelta(minutes=1)+datetime.timedelta(seconds=30))
        
#        dur_PGF = 0*60
        if (FDF_Pass.loc[i_Pass,['M01']]['M01']!=1):
            
#            FEP_ANX = getFEP_acq_start(FDF_Pass, dur_PGF, i_Pass)
#            D_FEP = FDF_Pass.loc[i_Pass,['ANX']]['ANX']+FEP_ANX
            CDA_FEP.append(0)
            CDA_PGF.append(0)
        else:
            CDA_FEP.append(0)
#            PGF_ANX = getFEP_acq_start(FDF_Pass, dur_PGF, i_Pass)
#            D_PGF = FDF_Pass.loc[i_Pass,['ANX']]['ANX']+PGF_ANX
            CDA_PGF.append(0)
            
        
    data = {
            'CDA_CONF_PI': CDA_CONF_PI,
            'CDA_CONF_S': CDA_CONF_S,
            'CDA_CONF_E': CDA_CONF_E,
            'CDA_PASS_S': CDA_AOS_Date,
            'CDA_PASS_E': CDA_LOS_Date,
            'CDA_STANDBY_S': CDA_STANDBY_S,
            'CDA_STANDBY_E': CDA_STANDBY_E
            }
    
    MPF_Pass = pd.DataFrame(data, columns = ['CDA_CONF_PI','CDA_CONF_S','CDA_CONF_E','CDA_PASS_S','CDA_PASS_E','CDA_STANDBY_S','CDA_STANDBY_E'])
    
    FDF_MPF_Pass = pd.concat([FDF_Pass, MPF_Pass.reindex(MPF_Pass.index)], axis=1)
    return FDF_MPF_Pass, MPF_Pass











def fcn_TCHIST_mang(FDF_Pass, TCHISTfilepath):
    fp=open(TCHISTfilepath,'r')
    TClines=fp.readlines()
    
    SSR_TT=[]
    ADA_Start_TT=[]
    PGFAcquisitionStart=[]
    PGFAcquisitionStop=[]
    PGFTime_Tag_Start=[]
    PGFTime_Tag_Stop=[]
    PGFSensingStart=[]
    PGFSensingStop=[]
    FEPAcquisitionStart=[]
    FEPAcquisitionStop=[]
    FEPTime_Tag_Start=[]
    FEPTime_Tag_Stop=[]
    FEPSensingStart=[]
    FEPSensingStop=[]
    TC_EOA030 = []
    TC_EOA031 = []
    def TCDate_Str2Datetime2(i_line):
        i_year=int(i_line[22:26])
        i_DOY=int(i_line[27:30])
        d = datetime.date(i_year, 1, 1) + datetime.timedelta(i_DOY - 1)
        i_MM=d.month
        i_dd=d.day
        i_hh=int(i_line[31:33])
        i_mm=int(i_line[34:36])
        i_s=int(i_line[37:39])
        i_s2=int(i_line[40:43])
        i_Datedate=datetime.datetime(i_year, i_MM, i_dd, i_hh, i_mm, i_s, i_s2*1000)
        return i_Datedate
    flagTC=0
    TCrow=0
    Wrow = 0
    Wrow_SSR_TT=0
    Wrow_ADA_Start_TT=0
    Wrow_CDA_Start_TT = 0
    flagTTLOS=0
    ADASflag=0
    flagTC_SSR=0
    flagTC_ADA_S=0
    flagTC_CDA_S = 0
    while (flagTC==0):
        TCrow =TCrow+1
        i_line=TClines[TCrow].strip()
        i_Datedate = TCDate_Str2Datetime2(i_line)
        
        if (FDF_Pass.loc[Wrow_CDA_Start_TT,['M01']]['M01'] != 1):
            if (flagTC_CDA_S == 0):
                if (i_Datedate > FDF_Pass.loc[Wrow_CDA_Start_TT,['CDA_AOS']]['CDA_AOS']):
                    TC_CDAStart = i_line[91:97]
                    if (TC_CDAStart == 'LOX003'):
                        PGFAcquisitionStart.append(i_Datedate)
                        PGFTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
                        PGFTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(hours=3))
                        
                        FEPAcquisitionStart.append(i_Datedate)
                        FEPTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
                        PGFTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(seconds=1+60*60+38*60+30))
                    if (TC_CDAStart == 'LOX004'):
                        PGFAcquisitionStop.append(i_Datedate)
                        FEPAcquisitionStop.append(i_Datedate)
                        
                        iPGFSensingStart = i_Datedate - datetime.timedelta(minutes=60+42)
                        iPGFSensingStart_test = iPGFSensingStart.minute % 3
                        iiPGFSensingStart = datetime.datetime(iPGFSensingStart.year, iPGFSensingStart.mouth, iPGFSensingStart.day, iPGFSensingStart.hour, iPGFSensingStart.minute, 0, 0*1000)
                        if (iPGFSensingStart_test != 0):
                            PGFSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                            FEPSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                        else:
                            PGFSensingStart.append(iiPGFSensingStart)
                            FEPSensingStart.append(iiPGFSensingStart)
                        
                        iPGFSensingStop = i_Datedate
                        iPGFSensingStop_test = iPGFSensingStop.minute % 3
                        iiPGFSensingStart = datetime.datetime(iPGFSensingStop.year, iPGFSensingStop.mouth, iPGFSensingStop.day, iPGFSensingStop.hour, iPGFSensingStop.minute, 0, 0*1000)
                        if (iPGFSensingStop_test != 0):
                            PGFSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                            FEPSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                        else:
                            PGFSensingStop.append(iiPGFSensingStop)
                            FEPSensingStop.append(iiPGFSensingStop)
                        
                        Wrow_CDA_Start_TT=Wrow_CDA_Start_TT+1   
                        
        if (FDF_Pass.loc[Wrow_ADA_Start_TT,['M01']]['M01'] == 1):
            if (flagTC_CDA_S == 0):
                if (i_Datedate > FDF_Pass.loc[Wrow_CDA_Start_TT,['CDA_AOS']]['CDA_AOS']):
                    TC_CDAStart = i_line[91:97]
                    if (TC_CDAStart == 'LOX003'):
                        FEPAcquisitionStart.append(i_Datedate)
                        FEPTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
                        PGFTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(seconds=1+60*60+38*60+30))
                    if (TC_CDAStart == 'LOX004'):
                        PGFAcquisitionStop.append(i_Datedate)
                        FEPAcquisitionStop.append(i_Datedate)
                        
                        iPGFSensingStart = i_Datedate - datetime.timedelta(minutes=60+42)
                        iPGFSensingStart_test = iPGFSensingStart.minute % 3
                        iiPGFSensingStart = datetime.datetime(iPGFSensingStart.year, iPGFSensingStart.mouth, iPGFSensingStart.day, iPGFSensingStart.hour, iPGFSensingStart.minute, 0, 0*1000)
                        if (iPGFSensingStart_test != 0):
                            PGFSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                            FEPSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                        else:
                            PGFSensingStart.append(iiPGFSensingStart)
                            FEPSensingStart.append(iiPGFSensingStart)
                        
                        iPGFSensingStop = i_Datedate
                        iPGFSensingStop_test = iPGFSensingStop.minute % 3
                        iiPGFSensingStart = datetime.datetime(iPGFSensingStop.year, iPGFSensingStop.mouth, iPGFSensingStop.day, iPGFSensingStop.hour, iPGFSensingStop.minute, 0, 0*1000)
                        if (iPGFSensingStop_test != 0):
                            PGFSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                            FEPSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                        else:
                            PGFSensingStop.append(iiPGFSensingStop)
                            FEPSensingStop.append(iiPGFSensingStop)
                        
                        Wrow_CDA_Start_TT=Wrow_CDA_Start_TT+1
                        
                        
            if (flagTC_ADA_S == 0):
                if (i_Datedate > FDF_Pass.loc[Wrow_ADA_Start_TT,['ADA_AOS']]['ADA_AOS']):
                    TC_CDAStart = i_line[91:97]
                    if (TC_CDAStart == 'LOX003'):
                        PGFAcquisitionStart.append(i_Datedate)
                        PGFTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
                        PGFTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(minutes=3*60+30))
                        Wrow_ADA_Start_TT=Wrow_ADA_Start_TT+1
                        
                    TC_ADAStart = i_line[91:101]
                    if (TC_ADAStart=='LOS121_E01'):
                        ADA_Start_TT.append(i_Datedate)
                        
            
            if (flagTC_SSR==0):
                if (i_Datedate>FDF_Pass.loc[Wrow_SSR_TT,['CDA_LOS']]['CDA_LOS']):
                    i_line_2=TClines[TCrow-1].strip()
                    i_Datedate_2 = TCDate_Str2Datetime2(i_line_2)
                    
                    if (i_Datedate-i_Datedate_2>datetime.timedelta(seconds=4*60)):
                        
                        if (flagTTLOS==0):
                            ii_TT=FDF_Pass.loc[Wrow_SSR_TT,['CDA_LOS']]['CDA_LOS']
                        else:
                            ii_TT=i_Datedate_2
                        
                        i_TT=datetime.datetime(ii_TT.year, ii_TT.month, ii_TT.day, ii_TT.hour, ii_TT.minute, 0, 0)+datetime.timedelta(seconds=2*60)
                        
                        if (i_TT<i_Datedate-datetime.timedelta(seconds=60) and i_TT <FDF_Pass.loc[Wrow_SSR_TT,['ADA_AOS']]['ADA_AOS']):
                            SSR_TT.append(i_TT)
                            print(i_TT)
                            Wrow_SSR_TT=Wrow_SSR_TT+1
                        else:
                            flagTTLOS=1
        else:
            ADA_Start_TT.append(0)
            SSR_TT.append(0)
            Wrow_SSR_TT=Wrow_SSR_TT+1
            Wrow_ADA_Start_TT=Wrow_ADA_Start_TT+1
        
        TC_EOA = i_line[91:97]
        if (TC_EOA=='EOA030'):
            TC_EOA030.append(i_Datedate)
        elif (TC_EOA=='EOA031'):
            TC_EOA031.append(i_Datedate)
        
        
        if (Wrow_SSR_TT>=FDF_Pass.shape[0]):
            flagTC_SSR=1
        if (Wrow_ADA_Start_TT>=FDF_Pass.shape[0]):
            flagTC_ADA_S=1
        if (Wrow_CDA_Start_TT>=FDF_Pass.shape[0]):
            flagTC_CDA_S=1
        if (Wrow_SSR_TT>=FDF_Pass.shape[0] and Wrow_ADA_Start_TT>=FDF_Pass.shape[0]):
            flagTC=1
        if (TCrow+1>len(TClines)-11):
            flagTC=1   
    
    wrow_EOA030=0
    TC_EOA030_Pass=[]
    iTC_EOA030=-1
    
    wrow_EOA031=0
    TC_EOA031_Pass=[]
    iTC_EOA031=-1
    
    for i_Pass in range(0,FDF_Pass.shape[0]):
        if (len(TC_EOA030)!=0):
            wrow_EOA030=0
            flagEOA030=0
            while (flagEOA030==0):
                if (TC_EOA030[wrow_EOA030]>=FDF_Pass.loc[i_Pass,['CDA_AOS']]['CDA_AOS']-datetime.timedelta(minutes=101) and TC_EOA030[wrow_EOA030]<=FDF_Pass.loc[i_Pass,['CDA_LOS']]['CDA_LOS']+datetime.timedelta(hours=6)):
                    iTC_EOA030_Pass=TC_EOA030[iTC_EOA030]
                    flagEOA030=1
                else:
                    iTC_EOA030_Pass=0
                wrow_EOA030=wrow_EOA030+1
                if (wrow_EOA030>len(TC_EOA030)-1):
                    flagEOA030=1
                
            TC_EOA030_Pass.append(iTC_EOA030_Pass)
        else:
            TC_EOA030_Pass.append(0)
        if (len(TC_EOA031)!=0):
            wrow_EOA031=0
            flagEOA031=0
            while (flagEOA031==0):
                if (TC_EOA031[wrow_EOA031]>=FDF_Pass.loc[i_Pass,['CDA_AOS']]['CDA_AOS']-datetime.timedelta(minutes=101) and TC_EOA031[wrow_EOA031]<=FDF_Pass.loc[i_Pass,['CDA_LOS']]['CDA_LOS']+datetime.timedelta(hours=6)):
                    iTC_EOA031_Pass=TC_EOA031[iTC_EOA031]
                    flagEOA031=1
                else:
                    iTC_EOA031_Pass=0
                wrow_EOA031=wrow_EOA031+1
                if (wrow_EOA031>len(TC_EOA031)-1):
                    flagEOA031=1
                
            TC_EOA031_Pass.append(iTC_EOA031_Pass)
        else:
            TC_EOA031_Pass.append(0)
    
    data = {
        'ADA_Start_TT': ADA_Start_TT,
        'SSR_TT': SSR_TT,
        'EOA030': TC_EOA030_Pass,
        'EOA031': TC_EOA031_Pass
        }
    
    TC_Pass = pd.DataFrame(data, columns = ['ADA_Start_TT','SSR_TT','EOA030','EOA031'])
    
    FDF_TC_Pass = pd.concat([FDF_Pass, TC_Pass.reindex(FDF_Pass.index)], axis=1)
    
    fp.close()
    return FDF_TC_Pass, TC_Pass