#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:02:57 2020

@author: matteo
"""

#import urllib
import requests
import datetime
from datetime import timezone

import pandas as pd

def fcn_Wimpy_N19_Maga(DS,DE,Wimpyfilepath,MetOp,CDAn):
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
    if (MetOp=='N19'):
        M01flag = 19#int(metop[6:7])
    elif (MetOp=='N18'):
        M01flag = 18
    
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
            MCMURDO_AOS_Date.append(0)
            MCMURDO_AOS_Azi.append(0)
            MCMURDO_AOSM_Date.append(0)
            MCMURDO_AOS5_Date.append(0)
            MCMURDO_M_Date.append(0)
            MCMURDO_LOS5_Date.append(0)
            MCMURDO_LOSM_Date.append(0)
            MCMURDO_LOS_Date.append(0)
            CDA_AOS_DEFPass.append(0)
            CDA_AOS_AOCS.append(0)
            
            
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























def readNOAAwebsite(link):
    url = link
    r = requests.get(url, stream=True)
    Date = []
    SC = []
    Text = []
    for line in r.iter_lines():
        if ( line ):
            lineASCII = line[26:29].decode("utf-8")
            if ( lineASCII == 'SVL' ):
                n = len(line.decode("utf-8"))
                datestr = line[0:17].decode("utf-8")
                YY = int(datestr[0:4])
                DOY = int(datestr[5:8])
                YYmmdd = datetime.datetime.strptime(str(YY)+'+'+str(DOY), "%Y+%j")
                
                HH = int(datestr[9:11])
                MM = int(datestr[12:14])
                SS = int(datestr[15:17])
                Date_date = datetime.datetime(YY, YYmmdd.month, YYmmdd.day, HH, MM, SS, 0*1000)
                
                SC_ID = int(line[23:25].decode("utf-8"))
                Text_str = line[34:n].decode("utf-8")
                
                Date.append(Date_date)
                SC.append(SC_ID)
                Text.append(Text_str)
    
    data = {'Date': Date,
            'S/C': SC,
            'Text': Text
            }
    
    NOAA_Pass = pd.DataFrame (data, columns = ['Date','S/C','Text'])
    return NOAA_Pass











def NOAA_week_sch():
    link_mon = "https://noaasis.noaa.gov/socc/polrrec.mon"
    link_tue = "https://noaasis.noaa.gov/socc/polrrec.tue"
    link_web = "https://noaasis.noaa.gov/socc/polrrec.web"
    link_thu = "https://noaasis.noaa.gov/socc/polrrec.thu"
    link_fri = "https://noaasis.noaa.gov/socc/polrrec.fri"
    link_sat = "https://noaasis.noaa.gov/socc/polrrec.sat"
    link_sun = "https://noaasis.noaa.gov/socc/polrrec.sun"
    NOAA_Pass_mon = readNOAAwebsite(link_mon)
    NOAA_Pass_tue = readNOAAwebsite(link_tue)
    NOAA_Pass_web = readNOAAwebsite(link_web)
    NOAA_Pass_thu = readNOAAwebsite(link_thu)
    NOAA_Pass_fri = readNOAAwebsite(link_fri)
    NOAA_Pass_sat = readNOAAwebsite(link_sat)
    NOAA_Pass_sun = readNOAAwebsite(link_sun)
    
    frames = [NOAA_Pass_mon, NOAA_Pass_tue, NOAA_Pass_web, NOAA_Pass_thu, NOAA_Pass_fri, NOAA_Pass_sat, NOAA_Pass_sun]
    
    result = pd.concat(frames)
    NOAA_week = result.sort_values(by=['Date'])
    NOAA_week = NOAA_week.reset_index()
    NOAA_week = NOAA_week.drop(columns='index')
    return NOAA_week











def NOAA_BOS_shift(FDF_Pass_N19, DS, DE):
    NOAA_week = NOAA_week_sch()
    Date = []
    SC = []
    Text = []
    for wrow in range(0,NOAA_week.shape[0]):
        iDate = NOAA_week.loc[wrow,['Date']]['Date']
        if (iDate >= DS and iDate <= DE):
            Date.append(iDate)
            SC.append(NOAA_week.loc[wrow,['S/C']]['S/C'])
            Text.append(NOAA_week.loc[wrow,['Text']]['Text'])
    
    data = {'Date': Date,
            'S/C': SC,
            'Text': Text
            }
        
    NOAA_Pass_shift = pd.DataFrame (data, columns = ['Date','S/C','Text'])
    
    npass = NOAA_Pass_shift.shape[0]/10
    iBOS=0
    wrow = 0
    flag = 1
    if (npass!=0):
        while (flag == 1):
            nOrbit_FDF = FDF_Pass_N19.loc[wrow,['CDA_nOrbit']]['CDA_nOrbit']
            Text_BOS_str = NOAA_Pass_shift.loc[iBOS*10,['Text']]['Text']
            nOrbit_BOS_str = Text_BOS_str[13:19]
            nOrbit_BOS = int(nOrbit_BOS_str)
            if (nOrbit_FDF == nOrbit_BOS):
                FDF_Pass_N19.at[wrow,'CDA_AOS']=NOAA_Pass_shift.loc[iBOS*10+3,['Date']]['Date']
                FDF_Pass_N19.at[wrow,'CDA_LOS']=NOAA_Pass_shift.loc[iBOS*10+9,['Date']]['Date']
                GAC_Type = (NOAA_Pass_shift.loc[iBOS*10+2,['Text']]['Text'])[12:14]
                GAC_Frame = int((NOAA_Pass_shift.loc[iBOS*10+2,['Text']]['Text'])[31:36])*2
                FDF_Pass_N19.at[wrow,'GDS_GAC']=GAC_Type+','+str(GAC_Frame)
                FDF_Pass_N19.at[wrow,'NOAA_BOS']='YES'
                iBOS = iBOS + 1
                if (iBOS == npass):
                    flag = 0
            wrow = wrow + 1
            if (wrow >= FDF_Pass_N19.shape[0]):
                flag = 0
    return FDF_Pass_N19, NOAA_Pass_shift