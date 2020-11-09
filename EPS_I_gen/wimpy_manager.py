# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:16:26 2020

@author: Nicoli
"""

import datetime
#from datetime import timezone

#import pandas as pd
from pandas import DataFrame, concat


#from M01_CDA_XBand_Dump_Processing_MS import *


# =============================================================================
# def fcn_Wimpy_Maga(DS,DE,Wimpyfilepath,MetOp,CDAn):
#     def Date_Str2Datetime(YMD,Dhmss):
#         YYYYPageDate=int(YMD[20:24])
#         MMPageDate=int(YMD[25:27])
#         DDPageDate=int(YMD[28:30])
#         
#         DD_date=int(Dhmss[0:2])
#         hh_date=int(Dhmss[3:5])
#         mm_date=int(Dhmss[6:8])
#         #ss_date=float(Dhmss[9:15])
#         s1ss_date=int(Dhmss[9:11])
#         s2ss_date=int(Dhmss[12:15])
#         Date_date=datetime.datetime(YYYYPageDate, MMPageDate, DD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
#         return Date_date
#     def Date_Str2Datetime2(YMD, Dhmss, DD_date_Old):
#         YYYYPageDate=int(YMD[20:24])
#         MMPageDate=int(YMD[25:27])
#         DDPageDate=int(YMD[28:30])
#         
#         DD_date=int(Dhmss[0:2])
#         hh_date=int(Dhmss[3:5])
#         mm_date=int(Dhmss[6:8])
#         #ss_date=float(Dhmss[9:15])
#         s1ss_date=int(Dhmss[9:11])
#         s2ss_date=int(Dhmss[12:15])
#         
#         Date_date=datetime.datetime(YYYYPageDate, MMPageDate, DD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
#         if (Date_date<DD_date_Old):
#             if (MMPageDate==12):
#                 MMPageDate=1
#                 YYYYPageDate=YYYYPageDate+1
#             else:
#                 MMPageDate=MMPageDate+1
#             Date_date=datetime.datetime(YYYYPageDate, MMPageDate, DD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
#         return Date_date
#     
#     error_line = 0
#     now_custm16=DS-datetime.timedelta(minutes=16)
#     now_cust=now_custm16-datetime.timedelta(minutes=20)
#     timestamp = datetime.datetime.timestamp(now_cust)
#     dt_object = datetime.datetime.fromtimestamp(timestamp)
#     
#     DEp16=DE+datetime.timedelta(minutes=16)
#     nowp36=DE+datetime.timedelta(minutes=101+70)
#     
#     fp=open(Wimpyfilepath,'r')
#     lines=fp.readlines()
#     
#     metop=lines[17-1].strip()
#     M01flag = int(metop[6:7])
#     
#     strPageDate=lines[15-1].strip()
#     Page1date=lines[15+7-1].strip()
#     Date1date=Date_Str2Datetime(strPageDate,Page1date)
#     strPageDate2=lines[15+59-1].strip()
#     Page2date=lines[15+7+59-1].strip()
#     Date2date=Date_Str2Datetime(strPageDate2,Page2date)
#     for row in range(15,len(lines),59):
#         strPageDate=lines[row-1].strip()
#         Page1date=lines[row+7-1].strip()
#         Date1date = Date_Str2Datetime2(strPageDate,Page1date, Date1date)
#         
#         if (row+7+59-1<=len(lines)):
#             strPageDate2=lines[row+59-1].strip()
#             Page2date=lines[row+7+59-1].strip()
#             Date2date = Date_Str2Datetime2(strPageDate2,Page2date, Date2date)
#         else:
#             strPageDate2=lines[row-1].strip()
#             Page2date=lines[len(lines)-1].strip()
#             Date2date = Date_Str2Datetime2(strPageDate2,Page2date,Date2date)
#         if (Date1date<=now_cust and Date2date>=now_cust):
#             RowNow=row
#         Dflag=1
#     
#     ii_RowNow = RowNow
#     flag=1
#     flag59=0
#     flagCDA=1
#     flag_CDA_Pass_old=0
#     flag_CDA_Pass_new=0
#     flag_CDA_mPass_old=0
#     flag_CDA_mPass_new=0
#     i_AOS=0
#     i_LOS=0
#     i_ANX=[]
#     i_CDA_AOS_i_Datedate=[]
#     i_CDA_AOS_nOrbit=[]
#     i_CDA_AOS_Azi=[]
#     i_CDA_AOSM_i_Datedate=[]
#     i_CDA_AOSM_nOrbit=[]
#     i_CDA_AOSM_Azi=[]
#     i_CDA_AOS5_i_Datedate=[]
#     i_CDA_AOS5_nOrbit=[]
#     i_CDA_AOS5_Azi=[]
#     i_CDA_M_i_Datedate=[]
#     i_CDA_M_nOrbit=[]
#     i_CDA_M_Azi=[]
#     i_CDA_M_El=[]
#     i_CDA_LOSM_i_Datedate=[]
#     i_CDA_LOSM_nOrbit=[]
#     i_CDA_LOSM_Azi=[]
#     i_CDA_LOS5_i_Datedate=[]
#     i_CDA_LOS5_nOrbit=[]
#     i_CDA_LOS5_Azi=[]
#     i_CDA_LOS_i_Datedate=[]
#     i_CDA_LOS_nOrbit=[]
#     i_CDA_LOS_Azi=[]
#     
#     flagMCMURDO=1
#     flag_MCMURDO_Pass_old=0
#     flag_MCMURDO_Pass_new=0
#     flag_MCMURDO_mPass_old=0
#     flag_MCMURDO_mPass_new=0
#     i_AOS=0
#     i_LOS=0
#     i_MCMURDO_AOS_i_Datedate=[]
#     i_MCMURDO_AOS_nOrbit=[]
#     i_MCMURDO_AOS_Azi=[]
#     i_MCMURDO_AOSM_i_Datedate=[]
#     i_MCMURDO_AOSM_nOrbit=[]
#     i_MCMURDO_AOSM_Azi=[]
#     i_MCMURDO_AOS5_i_Datedate=[]
#     i_MCMURDO_AOS5_nOrbit=[]
#     i_MCMURDO_AOS5_Azi=[]
#     i_MCMURDO_M_i_Datedate=[]
#     i_MCMURDO_M_nOrbit=[]
#     i_MCMURDO_M_Azi=[]
#     i_MCMURDO_LOS5_i_Datedate=[]
#     i_MCMURDO_LOS5_nOrbit=[]
#     i_MCMURDO_LOS5_Azi=[]
#     i_MCMURDO_LOSM_i_Datedate=[]
#     i_MCMURDO_LOSM_nOrbit=[]
#     i_MCMURDO_LOSM_Azi=[]
#     i_MCMURDO_LOS_i_Datedate=[]
#     i_MCMURDO_LOS_nOrbit=[]
#     i_MCMURDO_LOS_Azi=[]
#     
#     while (flag==1):
#         strPageDate=lines[ii_RowNow-1].strip()
#         Page1date=lines[ii_RowNow+7-1].strip()
#         i_Datedate=Date_Str2Datetime(strPageDate,Page1date)
#         i_Datedate_2 = i_Datedate
#         
#         for i_RowNow in range(ii_RowNow+7-1,ii_RowNow+59-1):
#             i_strPageDate=lines[ii_RowNow-1].strip()
#             
#             iii_RowNow =i_RowNow
#             i_Pagedate=lines[iii_RowNow].strip()
#             i_Datedate_OLD = i_Datedate
#             i_Datedate = Date_Str2Datetime2(i_strPageDate,i_Pagedate,i_Datedate)
#             
#             if (i_Datedate > i_Datedate_OLD + datetime.timedelta(hours=2)):
#                 error_line = i_RowNow
#             i_chr_ANX=i_Pagedate[16:17]
#             
#             if (i_chr_ANX=='A'):
#                 i_ANX.append(i_Datedate)
#             
#             
#             i_nOrbit=int(i_Pagedate[21:26])
#             i_chr_CDA_Azi=i_Pagedate[29:32]
#             if (i_chr_CDA_Azi!='   ' and i_chr_CDA_Azi!=''):
#                 i_chr_CDA_M=i_Pagedate[36:37]
#                 i_CDA_Azi=int(i_Pagedate[29:32])
#                 i_CDA_El=int(i_Pagedate[33:35])
#                 if (flag_CDA_mPass_old==0 and i_CDA_El==0):
#                     flag_AOS=1
#                     
#                     i_CDA_AOS_i_Datedate.append(i_Datedate)
#                     i_CDA_AOS_nOrbit.append(i_nOrbit)
#                     i_CDA_AOS_Azi.append(i_CDA_Azi)
#                     i_AOS = i_AOS+1
#                     flag_CDA_Pass_new=1
#                 if (i_chr_CDA_M=='M'):
#                     i_CDA_M_i_Datedate.append(i_Datedate)
#                     i_CDA_M_nOrbit.append(i_nOrbit)
#                     i_CDA_M_Azi.append(i_CDA_Azi)
#                     i_CDA_M_El.append(i_CDA_El)
#                 if (i_chr_CDA_M=='a'):
#                     i_CDA_AOSM_i_Datedate.append(i_Datedate)
#                     i_CDA_AOSM_nOrbit.append(i_nOrbit)
#                     i_CDA_AOSM_Azi.append(i_CDA_Azi)
#                 if (i_chr_CDA_M=='A'):
#                     i_CDA_AOS5_i_Datedate.append(i_Datedate)
#                     i_CDA_AOS5_nOrbit.append(i_nOrbit)
#                     i_CDA_AOS5_Azi.append(i_CDA_Azi)
#                 if (i_chr_CDA_M=='L'):
#                     i_CDA_LOS5_i_Datedate.append(i_Datedate)
#                     i_CDA_LOS5_nOrbit.append(i_nOrbit)
#                     i_CDA_LOS5_Azi.append(i_CDA_Azi)
#                 if (i_chr_CDA_M=='l'):
#                     i_CDA_LOSM_i_Datedate.append(i_Datedate)
#                     i_CDA_LOSM_nOrbit.append(i_nOrbit)
#                     i_CDA_LOSM_Azi.append(i_CDA_Azi)
#                 flag_CDA_mPass_new=1
#             else:
#                 if (flag_CDA_Pass_old==1 and i_CDA_El==0 and flag59==1):
#                     i_strPageDate_2 = lines[ii_RowNow-59-1].strip()
#                     i_Pagedate_2=lines[iii_RowNow-8].strip()
#                     i_Datedate_2 = Date_Str2Datetime2(i_strPageDate_2,i_Pagedate_2,i_CDA_AOS_i_Datedate[-1])
#                     
#                     i_CDA_Azi_2=int(i_Pagedate_2[29:32])
#                     i_CDA_El_2=int(i_Pagedate_2[33:35])
#                     
#                     flag_LOS=1
#                     i_CDA_LOS_i_Datedate.append(i_Datedate_2)
#                     i_CDA_LOS_nOrbit.append(i_nOrbit)
#                     i_CDA_LOS_Azi.append(i_CDA_Azi_2)
#                     i_LOS = i_LOS+1
#                 elif (flag_CDA_Pass_old==1 and i_CDA_El==0):
#                     i_Pagedate_2=lines[iii_RowNow-1].strip()
#                     i_Datedate_2 = Date_Str2Datetime2(i_strPageDate,i_Pagedate_2,i_CDA_AOS_i_Datedate[-1])
#                     
#                     i_CDA_Azi_2=int(i_Pagedate_2[29:32])
#                     i_CDA_El_2=int(i_Pagedate_2[33:35])
#                     
#                     flag_LOS=1
#                     i_CDA_LOS_i_Datedate.append(i_Datedate_2)
#                     i_CDA_LOS_nOrbit.append(i_nOrbit)
#                     i_CDA_LOS_Azi.append(i_CDA_Azi_2)
#                     i_LOS = i_LOS+1
#                 flag_CDA_Pass_new=0
#                 flag_CDA_mPass_new=0
#             flag_CDA_Pass_old =flag_CDA_Pass_new
#             flag_CDA_mPass_old=flag_CDA_mPass_new
#             
#             i_chr_MCMURDO_Azi=i_Pagedate[40:43]
#             if (i_chr_MCMURDO_Azi!='   ' and i_chr_MCMURDO_Azi!=''):
#                 i_chr_MCMURDO_M=i_Pagedate[47:48]
#                 i_MCMURDO_Azi=int(i_Pagedate[40:43])
#                 i_MCMURDO_El=int(i_Pagedate[45:46])
#                 if (flag_MCMURDO_mPass_old==0 and i_MCMURDO_El==0):
#                     flag_AOS=1
#                     i_MCMURDO_AOS_i_Datedate.append(i_Datedate)
#                     i_MCMURDO_AOS_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_AOS_Azi.append(i_MCMURDO_Azi)
#                     i_AOS = i_AOS+1
#                     flag_MCMURDO_Pass_new=1
#                 if (i_chr_MCMURDO_M=='M'):
#                     i_MCMURDO_M_i_Datedate.append(i_Datedate)
#                     i_MCMURDO_M_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_M_Azi.append(i_MCMURDO_Azi)
#                 if (i_chr_MCMURDO_M=='a'):
#                     i_MCMURDO_AOSM_i_Datedate.append(i_Datedate)
#                     i_MCMURDO_AOSM_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_AOSM_Azi.append(i_MCMURDO_Azi)
#                 if (i_chr_MCMURDO_M=='A'):
#                     i_MCMURDO_AOS5_i_Datedate.append(i_Datedate)
#                     i_MCMURDO_AOS5_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_AOS5_Azi.append(i_MCMURDO_Azi)
#                 if (i_chr_MCMURDO_M=='L'):
#                     i_MCMURDO_LOS5_i_Datedate.append(i_Datedate)
#                     i_MCMURDO_LOS5_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_LOS5_Azi.append(i_MCMURDO_Azi)
#                 if (i_chr_MCMURDO_M=='l'):
#                     i_MCMURDO_LOSM_i_Datedate.append(i_Datedate)
#                     i_MCMURDO_LOSM_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_LOSM_Azi.append(i_MCMURDO_Azi)
#                 
#                 flag_MCMURDO_mPass_new=1
#             else:
#                 if (flag_MCMURDO_Pass_old==1 and i_MCMURDO_El==0 and flag59==1):
#                     i_strPageDate_2 = lines[ii_RowNow-59-1].strip()
#                     i_Pagedate_2=lines[iii_RowNow-8].strip()
#                     i_Datedate_2 = Date_Str2Datetime2(i_strPageDate_2,i_Pagedate_2,i_MCMURDO_AOS_i_Datedate[-1])
#                     
#                     i_MCMURDO_Azi_2=int(i_Pagedate_2[40:43])
#                     i_MCMURDO_El_2=int(i_Pagedate_2[45:46])
#                     
#                     flag_LOS=1
#                     i_MCMURDO_LOS_i_Datedate.append(i_Datedate_2)
#                     i_MCMURDO_LOS_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_LOS_Azi.append(i_MCMURDO_Azi_2)
#                     i_LOS = i_LOS+1
#                 elif (flag_MCMURDO_Pass_old==1 and i_MCMURDO_El==0):
#                     i_Pagedate_2=lines[iii_RowNow-1].strip()
#                     i_Datedate_2 = Date_Str2Datetime2(i_strPageDate,i_Pagedate_2,i_MCMURDO_AOS_i_Datedate[-1])
#                     
#                     i_MCMURDO_Azi_2=int(i_Pagedate_2[40:43])
#                     i_MCMURDO_El_2=int(i_Pagedate_2[45:46])
#                     
#                     flag_LOS=1
#                     i_MCMURDO_LOS_i_Datedate.append(i_Datedate_2)
#                     i_MCMURDO_LOS_nOrbit.append(i_nOrbit)
#                     i_MCMURDO_LOS_Azi.append(i_MCMURDO_Azi_2)
#                     i_LOS = i_LOS+1
#                 flag_MCMURDO_Pass_new=0
#                 flag_MCMURDO_mPass_new=0
#             flag_MCMURDO_Pass_old =flag_MCMURDO_Pass_new
#             flag_MCMURDO_mPass_old =flag_MCMURDO_mPass_new
#             flag59=0
#             
#             print(i_Datedate,nowp36)
#             if (i_Datedate>nowp36 ):
#                 flag=0
#         
#         ii_RowNow=ii_RowNow+59
#         flag59=1
#     
#     fp.close()
#     
#     print(i_CDA_LOS_nOrbit)
#     
#     ANX=[]
#     NOAA_BOS = []
#     GDS_GAC = []
#     CDA_AOS_SC=[]
#     CDA_AOS_DEFPass=[]
#     CDA_AOS_AOCSPass=[]
#     CDA_AOS_AOCS=[]
#     CDA_AOS_M01=[]
#     CDA_n=[]
#     CDA_RNGDOP=[]
#     CDA_nRNG = []
#     CDA_nDOP = []
#     CDA_AOS_Date=[]
#     CDA_AOS_Azi=[]
#     CDA_AOS_nOrbit=[]
#     CDA_AOSM_Date=[]
#     CDA_AOS5_Date=[]
#     CDA_M_Date=[]
#     CDA_M_El=[]
#     CDA_LOS5_Date=[]
#     CDA_LOSM_Date=[]
#     CDA_LOS_Date=[]
#     MCMURDO_AOS_Date=[]
#     MCMURDO_Next_AOS_Date=[]
#     MCMURDO_AOS_Azi=[]
#     MCMURDO_AOSM_Date=[]
#     MCMURDO_AOS5_Date=[]
#     MCMURDO_M_Date=[]
#     MCMURDO_LOS5_Date=[]
#     MCMURDO_LOSM_Date=[]
#     MCMURDO_LOS_Date=[]
# #    CDA_CONF_PI=[]
# #    CDA_CONF_S=[]
# #    CDA_CONF_E=[]
# #    CDA_STANDBY_S=[]
# #    CDA_STANDBY_E=[]
#     ii_AOS=-1
#     for i_AOS in range(0,len(i_CDA_AOS_i_Datedate)-1):
#         if (i_CDA_AOS_i_Datedate[i_AOS]>=now_custm16):
#             CDA_AOS_Date.append(i_CDA_AOS_i_Datedate[i_AOS])
#             CDA_AOS_Azi.append(i_CDA_AOS_Azi[i_AOS])
#             CDA_AOS_nOrbit.append(i_CDA_AOS_nOrbit[i_AOS])
#             CDA_AOS_SC.append(MetOp)
#             CDA_AOS_M01.append(M01flag)
#             CDA_n.append(CDAn)
#             NOAA_BOS.append('N/A')
#             GDS_GAC.append('N/A')
#             
#             AOS_horsmm=i_CDA_AOS_i_Datedate[i_AOS].hour+i_CDA_AOS_i_Datedate[i_AOS].minute/60
#             if ( (AOS_horsmm>2+(15/60) and AOS_horsmm<3+(48/60)) ):
#                 CDA_AOS_DEFPass.append('DEF_ROUT')
#             else:
#                 CDA_AOS_DEFPass.append('DEF_PLM')
#             
#             CDA_AOS_AOCS.append('AOCS')
#  #           if (AOS_horsmm>9+(24/60) and AOS_horsmm<11):
#                 
# #            else:
# #                CDA_AOS_AOCS.append(0)
#             
# #            if (AOS_horsmm>21+(26/60) and AOS_horsmm<23+(4/60)):
# #                CDA_AOS_AOCS.append('AOCS')
# #            else:
# #                CDA_AOS_AOCS.append(0)
#             
#             
#             ii_AOS=ii_AOS+1
#             
#             flag_ANX=0
#             ii_ANX=-1
#             while (flag_ANX==0):
#                 ii_ANX=ii_ANX+1
#                 if (i_ANX[ii_ANX]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=40)):
#                     ANX.append(i_ANX[ii_ANX])
#                     flag_ANX=1
#             flag_CDA_LOS=0
#             i_CDA_LOS=-1
#             while (flag_CDA_LOS==0):
#                 i_CDA_LOS=i_CDA_LOS+1
#                 if (i_CDA_LOS_i_Datedate[i_CDA_LOS]>CDA_AOS_Date[ii_AOS]):
#                     CDA_LOS_Date.append(i_CDA_LOS_i_Datedate[i_CDA_LOS])
#                     flag_CDA_LOS=1
#             flag_CDA_AOSM=0
#             i_CDA_AOSM=-1
#             while (flag_CDA_AOSM==0):
#                 i_CDA_AOSM=i_CDA_AOSM+1
#                 if (i_CDA_AOSM_i_Datedate[i_CDA_AOSM]>CDA_AOS_Date[ii_AOS]):
#                     CDA_AOSM_Date.append(i_CDA_AOSM_i_Datedate[i_CDA_AOSM])
#                     flag_CDA_AOSM=1
#             flag_CDA_AOS5=0
#             i_CDA_AOS5=-1
#             while (flag_CDA_AOS5==0):
#                 i_CDA_AOS5=i_CDA_AOS5+1
#                 if (i_CDA_AOS5_i_Datedate[i_CDA_AOS5]>CDA_AOS_Date[ii_AOS]):
#                     CDA_AOS5_Date.append(i_CDA_AOS5_i_Datedate[i_CDA_AOS5])
#                     flag_CDA_AOS5=1
#             flag_CDA_M=0
#             i_CDA_M=-1
#             while (flag_CDA_M==0):
#                 i_CDA_M=i_CDA_M+1
#                 if (i_CDA_M_i_Datedate[i_CDA_M]>CDA_AOS_Date[ii_AOS]):
#                     CDA_M_Date.append(i_CDA_M_i_Datedate[i_CDA_M])
#                     CDA_M_El.append(i_CDA_M_El[i_CDA_M])
#                     flag_CDA_M=1
#             flag_CDA_LOS5=0
#             i_CDA_LOS5=-1
#             while (flag_CDA_LOS5==0):
#                 i_CDA_LOS5=i_CDA_LOS5+1
#                 if (i_CDA_LOS5_i_Datedate[i_CDA_LOS5]>CDA_AOS_Date[ii_AOS]):
#                     CDA_LOS5_Date.append(i_CDA_LOS5_i_Datedate[i_CDA_LOS5])
#                     flag_CDA_LOS5=1
#             flag_CDA_LOSM=0
#             i_CDA_LOSM=-1
#             while (flag_CDA_LOSM==0):
#                 i_CDA_LOSM=i_CDA_LOSM+1
#                 if (i_CDA_LOSM_i_Datedate[i_CDA_LOSM]>CDA_AOS_Date[ii_AOS]):
#                     CDA_LOSM_Date.append(i_CDA_LOSM_i_Datedate[i_CDA_LOSM])
#                     flag_CDA_LOSM=1
#             flag_MCMURDO_Next_AOS=0
#             i_MCMURDO_Next_AOS=-1
#             while (flag_MCMURDO_Next_AOS==0):
#                 i_MCMURDO_Next_AOS=i_MCMURDO_Next_AOS+1
#                 if (i_MCMURDO_AOS_i_Datedate[i_MCMURDO_Next_AOS]>CDA_AOS_Date[ii_AOS]):
#                     MCMURDO_Next_AOS_Date.append(i_MCMURDO_AOS_i_Datedate[i_MCMURDO_Next_AOS])
#                     flag_MCMURDO_Next_AOS=1
#             flag_MCMURDO_AOS=0
#             i_MCMURDO_AOS=-1
#             while (flag_MCMURDO_AOS==0):
#                 i_MCMURDO_AOS=i_MCMURDO_AOS+1
#                 if (i_MCMURDO_AOS_i_Datedate[i_MCMURDO_AOS]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=60)):
#                     MCMURDO_AOS_Date.append(i_MCMURDO_AOS_i_Datedate[i_MCMURDO_AOS])
#                     MCMURDO_AOS_Azi.append(i_MCMURDO_AOS_Azi[i_MCMURDO_AOS])
#                     flag_MCMURDO_AOS=1
#             flag_MCMURDO_AOSM=0
#             i_MCMURDO_AOSM=-1
#             while (flag_MCMURDO_AOSM==0):
#                 i_MCMURDO_AOSM=i_MCMURDO_AOSM+1
#                 if (i_MCMURDO_AOSM_i_Datedate[i_MCMURDO_AOSM]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=60)):
#                     MCMURDO_AOSM_Date.append(i_MCMURDO_AOSM_i_Datedate[i_MCMURDO_AOSM])
#                     flag_MCMURDO_AOSM=1
#             flag_MCMURDO_AOS5=0
#             i_MCMURDO_AOS5=-1
#             while (flag_MCMURDO_AOS5==0):
#                 i_MCMURDO_AOS5=i_MCMURDO_AOS5+1
#                 if (i_MCMURDO_AOS5_i_Datedate[i_MCMURDO_AOS5]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=60)):
#                     MCMURDO_AOS5_Date.append(i_MCMURDO_AOS5_i_Datedate[i_MCMURDO_AOS5])
#                     flag_MCMURDO_AOS5=1
#             flag_MCMURDO_M=0
#             i_MCMURDO_M=-1
#             while (flag_MCMURDO_M==0):
#                 i_MCMURDO_M=i_MCMURDO_M+1
#                 if (i_MCMURDO_M_i_Datedate[i_MCMURDO_M]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=60)):
#                     MCMURDO_M_Date.append(i_MCMURDO_M_i_Datedate[i_MCMURDO_M])
#                     flag_MCMURDO_M=1
#             flag_MCMURDO_LOS5=0
#             i_MCMURDO_LOS5=-1
#             while (flag_MCMURDO_LOS5==0):
#                 i_MCMURDO_LOS5=i_MCMURDO_LOS5+1
#                 if (i_MCMURDO_LOS5_i_Datedate[i_MCMURDO_LOS5]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=60)):
#                     MCMURDO_LOS5_Date.append(i_MCMURDO_LOS5_i_Datedate[i_MCMURDO_LOS5])
#                     flag_MCMURDO_LOS5=1
#             flag_MCMURDO_LOSM=0
#             i_MCMURDO_LOSM=-1
#             while (flag_MCMURDO_LOSM==0):
#                 i_MCMURDO_LOSM=i_MCMURDO_LOSM+1
#                 if (i_MCMURDO_LOSM_i_Datedate[i_MCMURDO_LOSM]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=60)):
#                     MCMURDO_LOSM_Date.append(i_MCMURDO_LOSM_i_Datedate[i_MCMURDO_LOSM])
#                     flag_MCMURDO_LOSM=1
#             flag_MCMURDO_LOS=0
#             i_MCMURDO_LOS=-1
#             while (flag_MCMURDO_LOS==0):
#                 i_MCMURDO_LOS=i_MCMURDO_LOS+1
#                 if (i_MCMURDO_LOS_i_Datedate[i_MCMURDO_LOS]>CDA_AOS_Date[ii_AOS]-datetime.timedelta(minutes=60)):
#                     MCMURDO_LOS_Date.append(i_MCMURDO_LOS_i_Datedate[i_MCMURDO_LOS])
#                     flag_MCMURDO_LOS=1
#             
#             
#             TC_len_s = (CDA_LOS5_Date[-1]-CDA_AOS5_Date[-1]).seconds
#             TC_len_ms = (CDA_LOS5_Date[-1]-CDA_AOS5_Date[-1]).microseconds
#             TC_len = TC_len_s + TC_len_ms*1e-6
#             C_O = 65
#             Window = TC_len-(2*C_O)
# # =============================================================================
# #             print([CDA_AOS5_Date[-1],(CDA_LOS5_Date[-1]-CDA_AOS5_Date[-1]).seconds,Window,3*C_O,1.5*C_O])
# # =============================================================================
#             
#             FIX = (TC_len/2-C_O)/3
#             OFFSET_1=FIX+C_O
#             OFFSET_2=TC_len/2
#             OFFSET_3=TC_len-C_O-FIX
#             if ( Window > 2*3*C_O ):
#                 nRNGDOP = 3
#                 i_CDA_nRNG = [CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_1),CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_2),CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_3)]
#                 i_CDA_nDOP = [CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_1+10),CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_2+10),CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_3+10)]
#             elif ( Window > 2*1.5*C_O):
#                 nRNGDOP = 2
#                 i_CDA_nRNG = [CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_1),CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_3)]
#                 i_CDA_nDOP = [CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_1+10),CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_3+10)]
#             else:
#                 nRNGDOP = 1
#                 i_CDA_nRNG = [CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_2)]
#                 i_CDA_nDOP = [CDA_AOS5_Date[-1]+datetime.timedelta(seconds=OFFSET_2+10)]
#                  
#             if (TC_len <= 397.5):
#                 nRNGDOP = 1
#             elif (TC_len <= 495):
#                 nRNGDOP = 2
#             else:
#                 nRNGDOP = 3
#             
#             
#             CDA_nRNG.append(i_CDA_nRNG)
#             CDA_nDOP.append(i_CDA_nDOP)
#             CDA_RNGDOP.append(nRNGDOP)
#                 
#     data = {'S/C': CDA_AOS_SC,
#             'NOAA_BOS': NOAA_BOS,
#             'GDS_GAC': GDS_GAC,
#             'M01': CDA_AOS_M01,
#             'CDAn': CDA_n,
#             'TM_Format': CDA_AOS_DEFPass,
#             'AOCS': CDA_AOS_AOCS,
#             'RNGDOP': CDA_RNGDOP,
#             'nRNG': CDA_nRNG,
#             'nDOP': CDA_nDOP,
#             'ANX': ANX,
#             'CDA_AOS': CDA_AOS_Date,
#             'CDA_nOrbit': CDA_AOS_nOrbit,
#             'CDA_AOS_Azi': CDA_AOS_Azi,
#             'CDA_AOSM': CDA_AOSM_Date,
#             'CDA_AOS5': CDA_AOS5_Date,
#             'CDA_Mid': CDA_M_Date,
#             'CDA_Mid_El': CDA_M_El,
#             'CDA_LOS5': CDA_LOS5_Date,
#             'CDA_LOSM': CDA_LOSM_Date,
#             'CDA_LOS': CDA_LOS_Date,
#             'ADA_AOS': MCMURDO_AOS_Date,
#             'ADA_AOS_Azi': MCMURDO_AOS_Azi,
#             'ADA_AOSM': MCMURDO_AOSM_Date,
#             'ADA_AOS5': MCMURDO_AOS5_Date,
#             'ADA_Mid': MCMURDO_M_Date,
#             'ADA_LOS5': MCMURDO_LOS5_Date,
#             'ADA_LOSM': MCMURDO_LOSM_Date,
#             'ADA_LOS': MCMURDO_LOS_Date,
#             'Next_ADA_AOS': MCMURDO_Next_AOS_Date
# #            'CDA_CONF_PI': CDA_CONF_PI,
# #            'CDA_CONF_S': CDA_CONF_S,
# #            'CDA_CONF_E': CDA_CONF_E,
# #            'CDA_PASS_S': CDA_AOS_Date,
# #            'CDA_PASS_E': CDA_LOS_Date,
# #            'CDA_STANDBY_S': CDA_STANDBY_S,
# #            'CDA_STANDBY_E': CDA_STANDBY_E
#             }
#     
# #    FDF_Pass = pd.DataFrame (data, columns = ['S/C','M01','ANX','CDA_AOS','CDA_nOrbit','CDA_AOS_Azi','CDA_AOSM','CDA_AOS5','CDA_Mid','CDA_LOS5','CDA_LOSM','CDA_LOS','ADA_AOS','ADA_AOS_Azi','ADA_AOSM','ADA_AOS5','ADA_Mid','ADA_LOS5','ADA_LOSM','ADA_LOS','CDA_CONF_PI','CDA_CONF_S','CDA_CONF_E','CDA_PASS_S','CDA_PASS_E','CDA_STANDBY_S','CDA_STANDBY_E'])
#     FDF_Pass = pd.DataFrame (data, columns = ['S/C','NOAA_BOS','GDS_GAC','M01','CDAn','TM_Format','AOCS','RNGDOP','nRNG','nDOP','ANX','CDA_AOS','CDA_nOrbit','CDA_AOS_Azi','CDA_AOSM','CDA_AOS5','CDA_Mid','CDA_Mid_El','CDA_LOS5','CDA_LOSM','CDA_LOS','ADA_AOS','ADA_AOS_Azi','ADA_AOSM','ADA_AOS5','ADA_Mid','ADA_LOS5','ADA_LOSM','ADA_LOS','Next_ADA_AOS'])
#     return FDF_Pass, error_line
# =============================================================================

def fcn_Wimpy_Maga(DS, DE, Wimpyfilepath, SC, CDAn ):
    
    now_custm16 =DS - datetime.timedelta(minutes=16)
    now_cust    =now_custm16 - datetime.timedelta(minutes=20) - datetime.timedelta(minutes=210/1)
    
    timestamp = datetime.datetime.timestamp(now_cust)
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    
    DEp16  = DE+datetime.timedelta(minutes=16)
    nowp36 = DE+datetime.timedelta(minutes=101+70) + datetime.timedelta(minutes=210/1)
    
    ErrorMsg = [0,0,0,0]
    flagErrorMsg = 0
    
    flag_nOrbit_DS = 1
    flag_nOrbit_DE = 0
    
    
    
    
    fp=open(Wimpyfilepath,'r')
    lines=fp.readlines()
    fp.close()
    
    
    
    metop=lines[17-1].strip()
    if ( metop[:5] == 'METOP' ):
        M01flag = int(metop[6:7])
        MN_SC = metop[:5]
    else:
        MN_SC = metop[:4]
        if ( metop[5:7] == 'NP' ):
            M01flag = int(19)
        else:
            M01flag = int(18)
           
    ii_RowNow=22
    flagline = 1
    flagDD1=1
    
    
    
    
    def Antenna_vet(CDAs, CDAs_LOS, i_chr_CDAs, flagCDAs_AOS, flagCDAs_AOSM, flagCDAs_ANX, idate, idate_OLD, nOrbit ):
        i_chr_CDAs_Azi = i_chr_CDAs[0:3]
        
        if (flagCDAs_ANX==1):
            flagCDAs_ANX = 0
            CDAs[0]=nOrbit
            CDAs[1]=idate
            
            
        if (i_chr_CDAs_Azi!='   ' and i_chr_CDAs_Azi!=''):
            i_CDAs_Azi=int(i_chr_CDAs[0:3])
            i_CDAs_El=int(i_chr_CDAs[4:6])
            i_chr_CDAs_M=i_chr_CDAs[7:8]
            if (i_CDAs_El==0 and flagCDAs_AOS==1):
                flagCDAs_AOS=0
                CDAs[2]=idate
                CDAs[3]=i_CDAs_Azi
                
            if (flagCDAs_AOSM==1 and i_chr_CDAs_M!='*'):
                flagCDAs_AOSM = 0
                CDAs[4]=idate
            if (i_chr_CDAs_M=='a'):
                #CDAs.append(idate)
                CDAs[4]=idate
            
            if (i_chr_CDAs_M=='A'):
                #CDAs.append(idate)
                CDAs[5]=idate
            if (i_chr_CDAs_M=='M'):
                #CDAs.append(idate)
                CDAs[6]=idate
                CDAs[7]=i_CDAs_Azi
                CDAs[8]=i_CDAs_El
            if (i_chr_CDAs_M=='L'):
                #CDAs.append(idate)
                CDAs[9]=idate
            
            if (i_chr_CDAs_M=='l'):
                #CDAs.append(idate)
                CDAs[10]=idate
            if (flagCDAs_AOSM==0 and CDAs[5]=='N/A' and i_chr_CDAs_M=='*'):
                CDAs[10]=idate_OLD
            
            if (i_CDAs_El==0 and flagCDAs_AOS==0):
                #CDAs_LOS.append(idate)
                CDAs[11]=idate
                CDAs[12]=i_CDAs_Azi
        return CDAs, flagCDAs_AOS, flagCDAs_AOSM, flagCDAs_ANX, CDAs_LOS
    
    
    
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
    nOrbit_cust = [0,0,0]
    
    while (flagline == 1):
        for i_RowNow in range(ii_RowNow,ii_RowNow+52):
            strPageDate=lines[i_RowNow-1].strip()
            
            
            i_nOrbit = int(strPageDate[21:26])
            Dhmss = strPageDate[0:26]
            
            DD_date=int(Dhmss[0:2])
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
                flagDD1 = 1
            else:
                Date_date=datetime.datetime(iDate_old.year, iDate_old.month, iDD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
                if (flagDD1 == 1):
                    iDate_old = Date_date
                    flagDD1 = 0
            
            if (flag_nOrbit_DS == 1 and Date_date >= now_cust):
                nOrbit_cust[0] = 1
                nOrbit_cust[1] = i_nOrbit-1
                flag_nOrbit_DS = 0
                flag_nOrbit_DE = 1
            
            if (flag_nOrbit_DE == 1 and Date_date >= nowp36):
                nOrbit_cust[2] = i_nOrbit+1
                flag_nOrbit_DS = 0
                flag_nOrbit_DE = 0
                flagline = 0
                
            DD_date_old = DD_date
            iDate_old = Date_date
        
        if ( i_RowNow >= len(lines) ):
            flagline = 0
        ii_RowNow = i_RowNow + 8
        
    
    
    
    
    
    # =============================================================================
    # nOrbit_cust[1] = 71516
    # nOrbit_cust[2] = 71517
    # =============================================================================
    
    i_nOrbit_valid_Old = nOrbit_cust[1]
    
    i_nOrbit_Valid = 0
    ii_RowNow=22
    flagline = 1
    flagDD1=1
    
    CDA      = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    MCMURDO  = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    WALLOPS  = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    FAIRBANK = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    KOUROU   = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    VILSP1   = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    MASPA    = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    
    CDA_LOS = []
    MCMURDO_LOS = []
    WALLOPS_LOS = []
    FAIRBANK_LOS = []
    KOUROU_LOS = []
    VILSP1_LOS = []
    MASPA_LOS = []
    
    
    ii_CDA = []
    ii_MCMURDO = []
    ii_WALLOPS = []
    ii_FAIRBANK = []
    ii_KOUROU = []
    ii_VILSP1 = []
    ii_MASPA = []
    
    flagCDA_ANX = 1
    flagMCMURDO_ANX = 1
    flagWALLOPS_ANX = 1
    flagFAIRBANK_ANX = 1
    flagKOUROU_ANX = 1
    flagVILSP1_ANX = 1
    flagMASPA_ANX = 1
    
    flagCDA_AOS = 1
    flagMCMURDO_AOS = 1
    flagWALLOPS_AOS = 1
    flagFAIRBANK_AOS = 1
    flagKOUROU_AOS = 1
    flagVILSP1_AOS = 1
    flagMASPA_AOS = 1
    
    flagCDA_AOSM = 1
    flagMCMURDO_AOSM = 1
    flagWALLOPS_AOSM = 1
    flagFAIRBANK_AOSM = 1
    flagKOUROU_AOSM = 1
    flagVILSP1_AOSM = 1
    flagMASPA_AOSM = 1
    
    flagCDA_LOS = 1
    flagMCMURDO_LOS = 1
    flagWALLOPS_LOS = 1
    flagFAIRBANK_LOS = 1
    flagKOUROU_LOS = 1
    flagVILSP1_LOS = 1
    flagMASPA_LOS = 1
    
    
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
    
    
    
    
    
    while (flagline == 1):
        for i_RowNow in range(ii_RowNow,ii_RowNow+52):
            strPageDate=lines[i_RowNow-1].strip()
            
            
            i_nOrbit = int(strPageDate[21:26])
            Dhmss = strPageDate[0:26]
            
            DD_date=int(Dhmss[0:2])
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
                flagDD1 = 1
            else:
                Date_date=datetime.datetime(iDate_old.year, iDate_old.month, iDD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
                if (flagDD1 == 1):
                    iDate_old = Date_date
                    flagDD1 = 0
            
            
            
            
            
            
            
            if (i_nOrbit >= nOrbit_cust[1] and i_nOrbit <= nOrbit_cust[2]):
                if (flagErrorMsg==0 and Date_date<iDate_old):
                    flagline = 0
                    Date_before = lines[i_RowNow-1-1].strip()[0:15]
                    Date_after = lines[i_RowNow-1].strip()[0:15]
                    ErrorMsg=[1,Wimpyfilepath,i_RowNow-1,i_RowNow,Date_before,Date_after]
                    #print(ErrorMsg)
                    flagErrorMsg = 1
                
                i_nOrbit_Valid = i_nOrbit
                if (i_nOrbit_Valid != i_nOrbit_valid_Old):
                    if (len(CDA_LOS)!=0):
                        CDA.append(max(CDA_LOS))
                    
                    if (len(WALLOPS_LOS)!=0):
                        WALLOPS.append(max(WALLOPS_LOS))
                    if (len(FAIRBANK_LOS)!=0):
                        FAIRBANK.append(max(FAIRBANK_LOS))
                    if ( MN_SC == 'METOP' ):
                        if (len(MCMURDO_LOS)!=0):
                            MCMURDO.append(max(MCMURDO_LOS))
                        if (len(KOUROU_LOS)!=0):
                            KOUROU.append(max(KOUROU_LOS))
                        if (len(VILSP1_LOS)!=0):
                            VILSP1.append(max(VILSP1_LOS))
                        if (len(MASPA_LOS)!=0):
                            MASPA.append(max(MASPA_LOS))
                    
                    ii_CDA.append(CDA)
                    ii_MCMURDO.append(MCMURDO)
                    ii_WALLOPS.append(WALLOPS)
                    ii_FAIRBANK.append(FAIRBANK)
                    ii_KOUROU.append(KOUROU)
                    ii_VILSP1.append(VILSP1)
                    ii_MASPA.append(MASPA)
                    
                    CDA      = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                    MCMURDO  = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                    WALLOPS  = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                    FAIRBANK = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                    KOUROU   = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                    VILSP1   = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                    MASPA    = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                    
                    CDA_LOS = []
                    MCMURDO_LOS = []
                    WALLOPS_LOS = []
                    FAIRBANK_LOS = []
                    KOUROU_LOS = []
                    VILSP1_LOS = []
                    MASPA_LOS = []
                    
                    flagCDA_ANX = 1
                    flagMCMURDO_ANX = 1
                    flagWALLOPS_ANX = 1
                    flagFAIRBANK_ANX = 1
                    flagKOUROU_ANX = 1
                    flagVILSP1_ANX = 1
                    flagMASPA_ANX = 1
                    
                    flagCDA_AOS = 1
                    flagMCMURDO_AOS = 1
                    flagWALLOPS_AOS = 1
                    flagFAIRBANK_AOS = 1
                    flagKOUROU_AOS = 1
                    flagVILSP1_AOS = 1
                    flagMASPA_AOS = 1
                    
                    flagCDA_AOSM = 1
                    flagMCMURDO_AOSM = 1
                    flagWALLOPS_AOSM = 1
                    flagFAIRBANK_AOSM = 1
                    flagKOUROU_AOSM = 1
                    flagVILSP1_AOSM = 1
                    flagMASPA_AOSM = 1
                    
                    flagCDA_LOS = 1
                    flagMCMURDO_LOS = 1
                    flagWALLOPS_LOS = 1
                    flagFAIRBANK_LOS = 1
                    flagKOUROU_LOS = 1
                    flagVILSP1_LOS = 1
                    flagMASPA_LOS = 1
                    
                    
                iCDA = 29
                i_chr_CDA = strPageDate[iCDA:(iCDA+9)]
                #print(i_chr_CDA)
                CDA, flagCDA_AOS, flagCDA_AOSM, flagCDA_ANX, CDA_LOS = Antenna_vet(CDA, CDA_LOS, i_chr_CDA, flagCDA_AOS, flagCDA_AOSM, flagCDA_ANX, Date_date, iDate_old, i_nOrbit_Valid )
                
                iCDA = 51
                if ( MN_SC != 'METOP'  ):
                    iCDA = 40
                i_chr_WALLOPS = strPageDate[iCDA:(iCDA+9)]
                WALLOPS, flagWALLOPS_AOS, flagWALLOPS_AOSM, flagWALLOPS_ANX, WALLOPS_LOS = Antenna_vet(WALLOPS, WALLOPS_LOS, i_chr_WALLOPS, flagWALLOPS_AOS, flagWALLOPS_AOSM, flagWALLOPS_ANX, Date_date, iDate_old, i_nOrbit_Valid )
                
                iCDA = 62
                if ( MN_SC != 'METOP' ):
                    iCDA = 51
                i_chr_FAIRBANK = strPageDate[iCDA:(iCDA+9)]
                FAIRBANK, flagFAIRBANK_AOS, flagFAIRBANK_AOSM, flagFAIRBANK_ANX, FAIRBANK_LOS = Antenna_vet(FAIRBANK, FAIRBANK_LOS, i_chr_FAIRBANK, flagFAIRBANK_AOS, flagFAIRBANK_AOSM, flagFAIRBANK_ANX, Date_date, iDate_old, i_nOrbit_Valid )
                
                if ( MN_SC == 'METOP'  ):
                    iCDA = 40
                    i_chr_MCMURDO = strPageDate[iCDA:(iCDA+9)]
                    MCMURDO, flagMCMURDO_AOS, flagMCMURDO_AOSM, flagMCMURDO_ANX, MCMURDO_LOS = Antenna_vet(MCMURDO, MCMURDO_LOS, i_chr_MCMURDO, flagMCMURDO_AOS, flagMCMURDO_AOSM, flagMCMURDO_ANX, Date_date, iDate_old, i_nOrbit_Valid )
                    
                    iCDA = 73
                    i_chr_KOUROU = strPageDate[iCDA:(iCDA+9)]
                    KOUROU, flagKOUROU_AOS, flagKOUROU_AOSM, flagKOUROU_ANX, KOUROU_LOS = Antenna_vet(KOUROU, KOUROU_LOS, i_chr_KOUROU, flagKOUROU_AOS, flagKOUROU_AOSM, flagKOUROU_ANX, Date_date, iDate_old, i_nOrbit_Valid )
                    
                    iCDA = 84
                    i_chr_VILSP1 = strPageDate[iCDA:(iCDA+9)]
                    VILSP1, flagVILSP1_AOS, flagVILSP1_AOSM, flagVILSP1_ANX, VILSP1_LOS = Antenna_vet(VILSP1, VILSP1_LOS, i_chr_VILSP1, flagVILSP1_AOS, flagVILSP1_AOSM, flagVILSP1_ANX, Date_date, iDate_old, i_nOrbit_Valid )
                    
                    iCDA = 95
                    i_chr_MASPA = strPageDate[iCDA:(iCDA+9)]
                    MASPA, flagMASPA_AOS, flagMASPA_AOSM, flagMASPA_ANX, MASPA_LOS = Antenna_vet(MASPA, MASPA_LOS, i_chr_MASPA, flagMASPA_AOS, flagMASPA_AOSM, flagMASPA_ANX, Date_date, iDate_old, i_nOrbit_Valid )
            
                i_nOrbit_valid_Old = i_nOrbit_Valid
            
            
            
            
            
            DD_date_old = DD_date
            iDate_old = Date_date
            
            if (i_nOrbit > nOrbit_cust[2]):
                flagline = 0
        
        if ( i_RowNow >= len(lines) ):
            flagline = 0
        ii_RowNow = i_RowNow + 8
    
    
    datacolumns = ['S/C','NOAA_BOS','GDS_GAC','M01','CDAn','TM_Format','AOCS','RNGDOP','nRNG','nDOP','CDA_nOrbit','ANX']
    datacolumns = datacolumns+['CDA_AOS','CDA_AOS_Azi','CDA_AOSM','CDA_AOS5','CDA_Mid','CDA_Mid_Azi','CDA_Mid_El','CDA_LOS5','CDA_LOSM','CDA_LOS','CDA_LOS_Azi']
    datacolumns = datacolumns+['ADA_AOS','ADA_AOS_Azi','ADA_AOSM','ADA_AOS5','ADA_Mid','ADA_Mid_Azi','ADA_Mid_El','ADA_LOS5','ADA_LOSM','ADA_LOS','ADA_LOS_Azi']
    datacolumns = datacolumns+['WAL_AOS','WAL_AOS_Azi','WAL_AOSM','WAL_AOS5','WAL_Mid','WAL_Mid_Azi','WAL_Mid_El','WAL_LOS5','WAL_LOSM','WAL_LOS','WAL_LOS_Azi']
    datacolumns = datacolumns+['FBK_AOS','FBK_AOS_Azi','FBK_AOSM','FBK_AOS5','FBK_Mid','FBK_Mid_Azi','FBK_Mid_El','FBK_LOS5','FBK_LOSM','FBK_LOS','FBK_LOS_Azi']
    datacolumns = datacolumns+['KOU_AOS','KOU_AOS_Azi','KOU_AOSM','KOU_AOS5','KOU_Mid','KOU_Mid_Azi','KOU_Mid_El','KOU_LOS5','KOU_LOSM','KOU_LOS','KOU_LOS_Azi']
    datacolumns = datacolumns+['VL1_AOS','VL1_AOS_Azi','VL1_AOSM','VL1_AOS5','VL1_Mid','VL1_Mid_Azi','VL1_Mid_El','VL1_LOS5','VL1_LOSM','VL1_LOS','VL1_LOS_Azi']
    datacolumns = datacolumns+['MAS_AOS','MAS_AOS_Azi','MAS_AOSM','MAS_AOS5','MAS_Mid','MAS_Mid_Azi','MAS_Mid_El','MAS_LOS5','MAS_LOSM','MAS_LOS','MAS_LOS_Azi']
    
    data=[]
    for i_Pass in range(0,len(ii_CDA)):
        CDA_AOS5_Date = ii_CDA[i_Pass][5]
        CDA_LOS5_Date = ii_CDA[i_Pass][9]
        
        TC_len_s = (CDA_LOS5_Date-CDA_AOS5_Date).seconds
        TC_len_ms = (CDA_LOS5_Date-CDA_AOS5_Date).microseconds
        TC_len = TC_len_s + TC_len_ms*1e-6
        C_O = 65
        Window = TC_len-(2*C_O)
        
        FIX = (TC_len/2-C_O)/3
        OFFSET_1=FIX+C_O
        OFFSET_2=TC_len/2
        OFFSET_3=TC_len-C_O-FIX
        if ( Window > 2*3*C_O ):
            nRNGDOP = 3
            i_CDA_nRNG = [CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_1),CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_2),CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_3)]
            i_CDA_nDOP = [CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_1+10),CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_2+10),CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_3+10)]
        elif ( Window > 2*1.5*C_O):
            nRNGDOP = 2
            i_CDA_nRNG = [CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_1),CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_3)]
            i_CDA_nDOP = [CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_1+10),CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_3+10)]
        else:
            nRNGDOP = 1
            i_CDA_nRNG = [CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_2)]
            i_CDA_nDOP = [CDA_AOS5_Date+datetime.timedelta(seconds=OFFSET_2+10)]
             
        if (TC_len <= 397.5):
            nRNGDOP = 1
        elif (TC_len <= 495):
            nRNGDOP = 2
        else:
            nRNGDOP = 3
        
        i_data = [SC,'N/A','N/A',M01flag,CDAn,'DEF_PLM','',nRNGDOP,i_CDA_nRNG,i_CDA_nDOP]+ii_CDA[i_Pass]
        #if ( SC != 'N19' or SC != 'N18' ):
        i_data = i_data + ii_MCMURDO[i_Pass][2:]
        i_data = i_data + ii_WALLOPS[i_Pass][2:]
        i_data = i_data + ii_FAIRBANK[i_Pass][2:]
        i_data = i_data + ii_KOUROU[i_Pass][2:]
        i_data = i_data + ii_VILSP1[i_Pass][2:]
        i_data = i_data + ii_MASPA[i_Pass][2:]
        data.append(i_data)
    
    FDF_Pass = DataFrame (data, columns = datacolumns)
    
    flagROUT = 1
    AOCSchk = 'CDA_LOS'
    for iPass in range(0,FDF_Pass.shape[0]-1):
        if  ( iPass > 1 ):
            Data_AOCS13 = datetime.datetime(FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].year, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].month, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].day, 13, 0, 0, 0*1000)
            Data_AOCS11 = datetime.datetime(FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].year, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].month, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].day, 11, 10, 0, 0*1000)
            Data_AOCS1 = datetime.datetime(FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].year, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].month, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].day, 1, 0, 0, 0*1000)
            Data_AOCS23 = datetime.datetime(FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].year, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].month, FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk].day, 23, 59, 0, 0*1000)
            
            
            if (FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk] >= Data_AOCS13 and FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk] <= Data_AOCS13 + datetime.timedelta(minutes=101) ):
                iPassAOCS13 = iPass-2
                if (FDF_Pass.loc[iPassAOCS13,['CDA_AOS']]['CDA_AOS'] < Data_AOCS11 ):
                    FDF_Pass.at[iPassAOCS13,'AOCS'] = 'AOCS'
            
            
            if (FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk] >= Data_AOCS1 and FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk] <= Data_AOCS1 + datetime.timedelta(minutes=101) ):
                iPassAOCS1 = iPass-2
                #print(FDF_Pass.loc[iPass,[AOCSchk]][AOCSchk], Data_AOCS1)
                if (FDF_Pass.loc[iPassAOCS1,['CDA_AOS']]['CDA_AOS'] < Data_AOCS23 ):
                    FDF_Pass.at[iPassAOCS1,'AOCS'] = 'AOCS'
        
        if  ( iPass > 2 ):
            Data_ROUT8 = datetime.datetime(FDF_Pass.loc[iPass,['CDA_AOS5']]['CDA_AOS5'].year, FDF_Pass.loc[iPass,['CDA_AOS5']]['CDA_AOS5'].month, FDF_Pass.loc[iPass,['CDA_AOS5']]['CDA_AOS5'].day, 7, 45, 0, 0*1000)
            Data_AOCS5 = datetime.datetime(FDF_Pass.loc[iPass,['CDA_AOS5']]['CDA_AOS5'].year, FDF_Pass.loc[iPass,['CDA_AOS5']]['CDA_AOS5'].month, FDF_Pass.loc[iPass,['CDA_AOS5']]['CDA_AOS5'].day, 4, 2, 0, 0*1000)
            if ( FDF_Pass.loc[iPass,['CDA_LOS5']]['CDA_LOS5'] >= Data_ROUT8 and FDF_Pass.loc[iPass,['CDA_LOS5']]['CDA_LOS5'] <= Data_ROUT8 + datetime.timedelta(minutes=99) ):
                iPassROUT = iPass-3
                if (FDF_Pass.loc[iPassROUT,['CDA_AOS']]['CDA_AOS'] < Data_AOCS5):
                    flagROUT = 0
                    FDF_Pass.at[iPassROUT,'TM_Format'] = 'DEF_ROUT'
                    
    return FDF_Pass, ErrorMsg




















def mergeWimpy(frames, delflag, DS, DE, MSW_info ):
    result = concat(frames)
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
                CDAn_MPF = FDF_Pass_M.loc[wrow,['CDAn']]['CDAn']
                CDAn_ = FDF_Pass_M.loc[wrow,['PGF_MPF_ACQ_SITE']]['PGF_MPF_ACQ_SITE']
                if (MSW_info[0]==1):
                    if (AOS>=MSW_info[1] and AOS<=MSW_info[2]):
                        if (CDAn_MPF=='AUTO'):
                            if (CDAn_=='CDA1'):
                                CDAn = 'CDA2'
                            else:
                                CDAn = 'CDA1'
                        elif (CDAn_MPF[0:3] == 'CDA'):
                            if (CDAn_MPF=='CDA1'):
                                CDAn = 'CDA2'
                            else:
                                CDAn = 'CDA1'
                        else:
                            CDAn = CDAn_MPF
                    else:
                        if (CDAn_MPF=='AUTO'):
                            CDAn = CDAn_
                        else:
                            CDAn = CDAn_MPF
                else:
                    CDAn = CDAn_MPF
                
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
    
        pd_next_Az_M = DataFrame(data, columns = ['Next_Az_MetOp'])
        
        FDF_Pass_M = concat([FDF_Pass_M, pd_next_Az_M.reindex(pd_next_Az_M.index)], axis=1)
    
    return FDF_Pass_M











def MPF_PGFDumpSynchSchedule(MPF_PGFfilepath):
    fp=open(MPF_PGFfilepath,'r')
    lines=fp.readlines()
    
    MPF_ACQ_SITE_vet = []
    _ACQ_START_vet = []
    _ACQ_STOP_vet = []
    _DATA_SOURCE_vet = []
    _LOC_ID_vet = []
    _ORBITSTART_vet = []
    _ORBITSTOP_vet = []
    _PROD_RULES_vet = []
    _SAT_ID_vet = []
    _SENSING_START_vet = []
    _SENSING_STOP_vet = []
    _VCIDFILTERING_vet = []
    
    def Date_Str2Datetime2(i_line):
        i_year=int(i_line[:4])
        i_DOY=int(i_line[5:8])
        d = datetime.date(i_year, 1, 1) + datetime.timedelta(i_DOY - 1)
        i_MM=d.month
        i_dd=d.day
        i_hh=int(i_line[9:11])
        i_mm=int(i_line[12:14])
        i_s=int(i_line[15:17])
        i_s2=int(i_line[18:22])
        i_Datedate=datetime.datetime(i_year, i_MM, i_dd, i_hh, i_mm, i_s, i_s2*1000)
        return i_Datedate
    
    for row in range(1,len(lines),12):
        MPF_ACQ_SITE_vet.append(lines[row][-5:-1])
        _ACQ_START_vet.append(Date_Str2Datetime2(lines[row+1][-22:-1]))
        _ACQ_STOP_vet.append(Date_Str2Datetime2(lines[row+2][-22:-1]))
        _DATA_SOURCE_vet.append(lines[row+3][-5:-1])
        _LOC_ID_vet.append(lines[row+4][-4:-1])
        falg_ORBITSTART = 1
        iter_ORBITSTART = 0
        while (falg_ORBITSTART == 1):
            iter_ORBITSTART = iter_ORBITSTART + 1
            checkstop = lines[row+5][-iter_ORBITSTART]
            if (checkstop == '\t'):
                falg_ORBITSTART = 0
        _ORBITSTART_vet.append(int(lines[row+5][-iter_ORBITSTART+1:-1]))
        falg_ORBITSTOP = 1
        iter_ORBITSTOP = 0
        while (falg_ORBITSTOP == 1):
            iter_ORBITSTOP = iter_ORBITSTOP + 1
            checkstop = lines[row+6][-iter_ORBITSTOP]
            if (checkstop == '\t'):
                falg_ORBITSTOP = 0
        _ORBITSTOP_vet.append(int(lines[row+6][-iter_ORBITSTOP+1:-1]))
        _PROD_RULES_vet.append(lines[row+7][-10:-1])
        _SAT_ID_vet.append(lines[row+8][-4:-1])
        _SENSING_START_vet.append(Date_Str2Datetime2(lines[row+9][-22:-1]))
        _SENSING_STOP_vet.append(Date_Str2Datetime2(lines[row+10][-22:-1]))
        _VCIDFILTERING_vet.append(lines[row+11][-2:-1])
        
    fp.close()
    
    col_name = ['MPF_ACQ_SITE', '_ACQ_START', '_ACQ_STOP', '_DATA_SOURCE', '_LOC_ID', '_ORBITSTART', '_ORBITSTOP', '_PROD_RULES', '_SAT_ID', '_SENSING_START', '_SENSING_STOP', '_VCIDFILTERING']
    data = {col_name[0]: MPF_ACQ_SITE_vet,
            col_name[1]: _ACQ_START_vet,
            col_name[2]: _ACQ_STOP_vet,
            col_name[3]: _DATA_SOURCE_vet,
            col_name[4]: _LOC_ID_vet,
            col_name[5]: _ORBITSTART_vet,
            col_name[6]: _ORBITSTOP_vet,
            col_name[7]: _PROD_RULES_vet,
            col_name[8]: _SAT_ID_vet,
            col_name[9]: _SENSING_START_vet,
            col_name[10]: _SENSING_STOP_vet,
            col_name[11]: _VCIDFILTERING_vet
        }
    PGFDumpSynchSchedule = DataFrame (data, columns = col_name )
    return PGFDumpSynchSchedule











def fcn_MPF_mang(FDF_Pass, PGFDSS):
    CDA_CONF_PI=[]
    CDA_CONF_S=[]
    CDA_CONF_E=[]
    CDA_AOS_Date = []
    CDA_LOS_Date = []
    CDA_STANDBY_S=[]
    CDA_STANDBY_E=[]
    CDA_FEP=[]
    CDA_PGF=[]
    
    if (PGFDSS[0] == 1):
        PGFDumpSynchSchedule = PGFDSS[1]
        
    MPF_ACQ_SITE_vet = []
    _ACQ_START_vet = []
    _ACQ_STOP_vet = []
    _DATA_SOURCE_vet = []
    _LOC_ID_vet = []
    _ORBITSTART_vet = []
    _ORBITSTOP_vet = []
    _PROD_RULES_vet = []
    _SAT_ID_vet = []
    _SENSING_START_vet = []
    _SENSING_STOP_vet = []
    _VCIDFILTERING_vet = []
    _Dump_Start_vet = []
    _Dump_End_vet = []
    
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
    
    i_Pass = 0
    if (PGFDSS[0] == 1):
        for i_PGF in range(0,PGFDumpSynchSchedule.shape[0]):    
            if (PGFDumpSynchSchedule.loc[i_PGF,['_ORBITSTOP']]['_ORBITSTOP']==FDF_Pass.loc[i_Pass,['CDA_nOrbit']]['CDA_nOrbit']):
                MPF_ACQ_SITE_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['MPF_ACQ_SITE']]['MPF_ACQ_SITE'])
                _ACQ_START_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_ACQ_START']]['_ACQ_START'])
                _ACQ_STOP_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_ACQ_STOP']]['_ACQ_STOP'])
                _DATA_SOURCE_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_DATA_SOURCE']]['_DATA_SOURCE'])
                _LOC_ID_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_LOC_ID']]['_LOC_ID'])
                _ORBITSTART_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_ORBITSTART']]['_ORBITSTART'])
                _ORBITSTOP_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_ORBITSTOP']]['_ORBITSTOP'])
                _PROD_RULES_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_PROD_RULES']]['_PROD_RULES'])
                _SAT_ID_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_SAT_ID']]['_SAT_ID'])
                _SENSING_START_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_SENSING_START']]['_SENSING_START'])
                _SENSING_STOP_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_SENSING_STOP']]['_SENSING_STOP'])
                _VCIDFILTERING_vet.append(PGFDumpSynchSchedule.loc[i_PGF,['_VCIDFILTERING']]['_VCIDFILTERING'])
                i_Pass = i_Pass + 1
    else:
        MPF_ACQ_SITE_vet=[0] * FDF_Pass.shape[0]
        _ACQ_START_vet=[0] * FDF_Pass.shape[0]
        _ACQ_STOP_vet=[0] * FDF_Pass.shape[0]
        _DATA_SOURCE_vet=[0] * FDF_Pass.shape[0]
        _LOC_ID_vet=[0] * FDF_Pass.shape[0]
        _ORBITSTART_vet=[0] * FDF_Pass.shape[0]
        _ORBITSTOP_vet=[0] * FDF_Pass.shape[0]
        _PROD_RULES_vet=[0] * FDF_Pass.shape[0]
        _SAT_ID_vet=[0] * FDF_Pass.shape[0]
        _SENSING_START_vet=[0] * FDF_Pass.shape[0]
        _SENSING_STOP_vet=[0] * FDF_Pass.shape[0]
        _VCIDFILTERING_vet=[0] * FDF_Pass.shape[0]
        _Dump_Start_vet=[0] * FDF_Pass.shape[0]
        _Dump_End_vet=[0] * FDF_Pass.shape[0]
        
    col_name = ['CDA_CONF_PI','CDA_CONF_S','CDA_CONF_E','CDA_PASS_S','CDA_PASS_E','CDA_STANDBY_S','CDA_STANDBY_E','PGF_MPF_ACQ_SITE', 'PGF_ACQ_START', 'PGF_ACQ_STOP', 'PGF_DATA_SOURCE', 'PGF_LOC_ID', 'PGF_ORBITSTART', 'PGF_ORBITSTOP', 'PGF_PROD_RULES', 'PGF_SAT_ID', 'PGF_SENSING_START', 'PGF_SENSING_STOP', 'PGF_VCIDFILTERING','Dump_Start','Dump_End']
    data = {
            col_name[0]: CDA_CONF_PI,
            col_name[1]: CDA_CONF_S,
            col_name[2]: CDA_CONF_E,
            col_name[3]: CDA_AOS_Date,
            col_name[4]: CDA_LOS_Date,
            col_name[5]: CDA_STANDBY_S,
            col_name[6]: CDA_STANDBY_E,
            col_name[7]: MPF_ACQ_SITE_vet,
            col_name[8]: _ACQ_START_vet,
            col_name[9]: _ACQ_STOP_vet,
            col_name[10]: _DATA_SOURCE_vet,
            col_name[11]: _LOC_ID_vet,
            col_name[12]: _ORBITSTART_vet,
            col_name[13]: _ORBITSTOP_vet,
            col_name[14]: _PROD_RULES_vet,
            col_name[15]: _SAT_ID_vet,
            col_name[16]: _SENSING_START_vet,
            col_name[17]: _SENSING_STOP_vet,
            col_name[18]: _VCIDFILTERING_vet,
            col_name[19]: _Dump_Start_vet,
            col_name[20]: _Dump_End_vet
            }
    
    MPF_Pass = DataFrame(data, columns = col_name )
    
    FDF_MPF_Pass = concat([FDF_Pass, MPF_Pass.reindex(MPF_Pass.index)], axis=1)
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
    Wrow_ADA_CDA_Start_TT=0
    flagTTLOS=0
    ADASflag=0
    flagTC_SSR=0
    flagTC_ADA_S=0
    flagTC_CDA_S = 0
    flagTC_ADA_CDA_S=0
    while (flagTC==0):
        TCrow =TCrow+1
        i_line=TClines[TCrow].strip()
        i_Datedate = TCDate_Str2Datetime2(i_line)
        
# =============================================================================
#         if (FDF_Pass.loc[Wrow_CDA_Start_TT,['M01']]['M01'] != 1):
#             if (flagTC_CDA_S == 0):
#                 print (1)
#                 if (i_Datedate > FDF_Pass.loc[Wrow_CDA_Start_TT,['CDA_AOS']]['CDA_AOS']):
#                     TC_CDAStart = i_line[91:97]
#                     if (TC_CDAStart == 'LOX003'):
#                         PGFAcquisitionStart.append(i_Datedate)
#                         PGFTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
#                         PGFTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(hours=3))
#                         
#                         FEPAcquisitionStart.append(i_Datedate)
#                         FEPTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
#                         PGFTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(seconds=1+60*60+38*60+30))
#                     if (TC_CDAStart == 'LOX004'):
#                         PGFAcquisitionStop.append(i_Datedate)
#                         FEPAcquisitionStop.append(i_Datedate)
#                         
#                         iPGFSensingStart = i_Datedate - datetime.timedelta(minutes=60+42)
#                         iPGFSensingStart_test = iPGFSensingStart.minute % 3
#                         iiPGFSensingStart = datetime.datetime(iPGFSensingStart.year, iPGFSensingStart.mouth, iPGFSensingStart.day, iPGFSensingStart.hour, iPGFSensingStart.minute, 0, 0*1000)
#                         if (iPGFSensingStart_test != 0):
#                             PGFSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
#                             FEPSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
#                         else:
#                             PGFSensingStart.append(iiPGFSensingStart)
#                             FEPSensingStart.append(iiPGFSensingStart)
#                         
#                         iPGFSensingStop = i_Datedate
#                         iPGFSensingStop_test = iPGFSensingStop.minute % 3
#                         iiPGFSensingStop = datetime.datetime(iPGFSensingStop.year, iPGFSensingStop.month, iPGFSensingStop.day, iPGFSensingStop.hour, iPGFSensingStop.minute, 0, 0*1000)
#                         if (iPGFSensingStop_test != 0):
#                             PGFSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
#                             FEPSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
#                         else:
#                             PGFSensingStop.append(iiPGFSensingStop)
#                             FEPSensingStop.append(iiPGFSensingStop)
#                         
#                         Wrow_CDA_Start_TT=Wrow_CDA_Start_TT+1   
# =============================================================================
        
        
        if (flagTC_CDA_S == 0):
            nMN_CDA = FDF_Pass.loc[Wrow_CDA_Start_TT,['M01']]['M01']
            if ( nMN_CDA == 1):
                if (i_Datedate > FDF_Pass.loc[Wrow_CDA_Start_TT,['CDA_AOS']]['CDA_AOS']):
                    TC_CDAStart = i_line[91:97]
                    
                    if (TC_CDAStart == 'LOX003'):
                        FEPAcquisitionStart.append(i_Datedate)
                        FEPTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
                        FEPTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(seconds=1+60*60+38*60+30))
                    if (TC_CDAStart == 'LOX004'):
                        PGFAcquisitionStop.append(i_Datedate)
                        FEPAcquisitionStop.append(i_Datedate)
                        
                        
                        iPGFSensingStart = i_Datedate - datetime.timedelta(minutes=60+42)
                        iiPGFSensingStart = datetime.datetime(i_Datedate.year, i_Datedate.month, i_Datedate.day, i_Datedate.hour, i_Datedate.minute, 0, 0*1000) - datetime.timedelta(minutes=60+42)
                        iPGFSensingStart_test = iiPGFSensingStart.minute % 3
                        if (iPGFSensingStart_test != 0):
                            PGFSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                            FEPSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                        else:
                            PGFSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3))
                            FEPSensingStart.append(iiPGFSensingStart + datetime.timedelta(minutes=3))
                        
                        #iPGFSensingStop = i_Datedate
                        iiPGFSensingStop = datetime.datetime(i_Datedate.year, i_Datedate.month, i_Datedate.day, i_Datedate.hour, i_Datedate.minute, 0, 0*1000)
                        iPGFSensingStop_test = iiPGFSensingStop.minute % 3
                        
                        if (iPGFSensingStop_test != 0):
                            PGFSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                            FEPSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3-iPGFSensingStart_test))
                        else:
                            PGFSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3))
                            FEPSensingStop.append(iiPGFSensingStop + datetime.timedelta(minutes=3))
                        
                        Wrow_CDA_Start_TT=Wrow_CDA_Start_TT+1
            else:
                PGFAcquisitionStop.append(0)
                PGFSensingStart.append(0)
                PGFSensingStop.append(0)
                FEPAcquisitionStart.append(0)
                FEPAcquisitionStop.append(0)
                FEPTime_Tag_Start.append(0)
                FEPTime_Tag_Stop.append(0)
                FEPSensingStart.append(0)
                FEPSensingStop.append(0)
                Wrow_CDA_Start_TT=Wrow_CDA_Start_TT+1
                
        if (flagTC_ADA_CDA_S == 0):
            nMN_ADA_CDA = FDF_Pass.loc[Wrow_ADA_CDA_Start_TT,['M01']]['M01']
            if (nMN_ADA_CDA == 1):
                if (i_Datedate > FDF_Pass.loc[Wrow_ADA_CDA_Start_TT,['ADA_AOS']]['ADA_AOS']):
                    TC_CDAStart = i_line[91:97]
                    if (TC_CDAStart == 'LOX003'):
                        PGFAcquisitionStart.append(i_Datedate)
                        PGFTime_Tag_Start.append(i_Datedate - datetime.timedelta(minutes=1))
                        PGFTime_Tag_Stop.append(i_Datedate - datetime.timedelta(minutes=1) + datetime.timedelta(minutes=3*60+30))
                        Wrow_ADA_CDA_Start_TT = Wrow_ADA_CDA_Start_TT + 1
            else:
                PGFAcquisitionStart.append(0)   
                PGFTime_Tag_Start.append(0)        
                PGFTime_Tag_Stop.append(0)
                Wrow_ADA_CDA_Start_TT=Wrow_ADA_CDA_Start_TT+1
        
        if (flagTC_ADA_S == 0):
            nMN_ADA = FDF_Pass.loc[Wrow_ADA_Start_TT,['M01']]['M01']
            if (nMN_ADA == 1):
                if (i_Datedate > FDF_Pass.loc[Wrow_ADA_Start_TT,['ADA_AOS']]['ADA_AOS']):
                    TC_ADAStart = i_line[91:101]
                    if (TC_ADAStart=='LOS121_E01'):
                        ADA_Start_TT.append(i_Datedate)
                        Wrow_ADA_Start_TT=Wrow_ADA_Start_TT+1
            else:
                ADA_Start_TT.append(0)
                Wrow_ADA_Start_TT=Wrow_ADA_Start_TT+1
                        
            
        if (flagTC_SSR==0):
            nMN_SSR = FDF_Pass.loc[Wrow_SSR_TT,['M01']]['M01']
            if (nMN_SSR == 1):
                if (i_Datedate>FDF_Pass.loc[Wrow_SSR_TT,['CDA_LOS']]['CDA_LOS']):
                    i_line_2=TClines[TCrow-1].strip()
                    
                    i_Datedate_2 = TCDate_Str2Datetime2(i_line_2)
                    
                    if (i_Datedate-i_Datedate_2>datetime.timedelta(seconds=4*60)):
                        
                        if (flagTTLOS==0):
                            ii_TT=FDF_Pass.loc[Wrow_SSR_TT,['CDA_LOS']]['CDA_LOS']
                        else:
                            ii_TT=i_Datedate_2
                        
                        i_TT=datetime.datetime(ii_TT.year, ii_TT.month, ii_TT.day, ii_TT.hour, ii_TT.minute, 0, 0)+datetime.timedelta(seconds=2*60)
                        
                        if (i_TT<i_Datedate-datetime.timedelta(seconds=60) and i_TT <FDF_Pass.loc[Wrow_SSR_TT,['CDA_LOS']]['CDA_LOS']+datetime.timedelta(minutes=30)):
                            SSR_TT.append(i_TT)
                            print(i_TT)
                            Wrow_SSR_TT=Wrow_SSR_TT+1
                        else:
                            flagTTLOS=1
            else:
                SSR_TT.append(0)
                Wrow_SSR_TT=Wrow_SSR_TT+1
        
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
        if (Wrow_ADA_CDA_Start_TT>=FDF_Pass.shape[0]):
            flagTC_ADA_CDA_S = 1
        if (flagTC_SSR==1 and flagTC_ADA_S==1 and flagTC_CDA_S==1 and flagTC_ADA_CDA_S==1):
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
    
    datacolum =  ['ADA_Start_TT','SSR_TT']
    datacolum = ['ADA_Start_TT','SSR_TT','EOA030','EOA031','PGF_Acquisition_Start','PGF_Acquisition_Stop','PGF_Time_Tag_Start','PGF_Time_Tag_Stop','PGF_Sensing_Start','PGF_Sensing_Stop','FEP_Acquisition_Start','FEP_Acquisition_Stop','FEP_Time_Tag_Start','FEP_Time_Tag_Stop','FEP_Sensing_Start','FEP_Sensing_Stop']
    
    
    #print(len(ADA_Start_TT),len(SSR_TT),len(TC_EOA030_Pass),len(TC_EOA031_Pass),len(PGFAcquisitionStart))
    
    
    data = {
        'ADA_Start_TT': ADA_Start_TT,
        'SSR_TT': SSR_TT,
        'EOA030': TC_EOA030_Pass,
        'EOA031': TC_EOA031_Pass,
        'PGF_Acquisition_Start': PGFAcquisitionStart,
        'PGF_Acquisition_Stop': PGFAcquisitionStop,
        'PGF_Time_Tag_Start': PGFTime_Tag_Start,
        'PGF_Time_Tag_Stop': PGFTime_Tag_Stop,
        'PGF_Sensing_Start': PGFSensingStart,
        'PGF_Sensing_Stop': PGFSensingStop,
        'FEP_Acquisition_Start': FEPAcquisitionStart,
        'FEP_Acquisition_Stop': FEPAcquisitionStop,
        'FEP_Time_Tag_Start': FEPTime_Tag_Start,
        'FEP_Time_Tag_Stop': FEPTime_Tag_Stop,
        'FEP_Sensing_Start': FEPSensingStart,
        'FEP_Sensing_Stop': FEPSensingStop
        
        }
    
    TC_Pass = DataFrame(data, columns = datacolum)
    
    FDF_TC_Pass = concat([FDF_Pass, TC_Pass.reindex(FDF_Pass.index)], axis=1)
    
    fp.close()
    return FDF_TC_Pass, TC_Pass