# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:17:10 2020

@author: Nicoli
"""


import datetime
from datetime import timezone

import pandas as pd

def fcn_wimpy_mag(Wimpyfilepath, DS, DE, SC, CDAn ):
    
    now_custm16 =DS - datetime.timedelta(minutes=16)
    now_cust    =now_custm16 - datetime.timedelta(minutes=20)
    
    timestamp = datetime.datetime.timestamp(now_cust)
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    
    DEp16  = DE+datetime.timedelta(minutes=16)
    nowp36 = DE+datetime.timedelta(minutes=101+70)
    
    ErrorMsg = [0,0,0]
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
                if (flagErrorMsg==0  and Date_date<iDate_old):
                    flagline = 0
                    ErrorMsg=[1,Wimpyfilepath,i_RowNow-1,i_RowNow]
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
        
        i_data = [SC,'N/A','N/A',M01flag,CDAn,'DEF_PLM','AOCS',nRNGDOP,i_CDA_nRNG,i_CDA_nDOP]+ii_CDA[i_Pass]
        #if ( SC != 'N19' or SC != 'N18' ):
        i_data = i_data + ii_MCMURDO[i_Pass][2:]
        i_data = i_data + ii_WALLOPS[i_Pass][2:]
        i_data = i_data + ii_FAIRBANK[i_Pass][2:]
        i_data = i_data + ii_KOUROU[i_Pass][2:]
        i_data = i_data + ii_VILSP1[i_Pass][2:]
        i_data = i_data + ii_MASPA[i_Pass][2:]
        data.append(i_data)
    
    FDF_Pass = pd.DataFrame (data, columns = datacolumns)
    
    return FDF_Pass, ErrorMsg