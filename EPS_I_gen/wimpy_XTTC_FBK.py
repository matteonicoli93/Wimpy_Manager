# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 01:30:43 2020

@author: Nicoli
"""

import datetime
#from datetime import timezone

#import pandas as pd
from pandas import DataFrame

def fcn_XTTC_FBK(Wimpyfilepath, nOrbit_cust):
    ErrorMsg = [0,0,0,0]
    flagErrorMsg = 0
    
    fp=open(Wimpyfilepath,'r')
    lines=fp.readlines()
    
    metop=lines[17-1].strip()
    M01flag = int(metop[6:7])
    
    ii_RowNow=22
    flagline = 1
    flagDD1=1
    
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
    
    CDA = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    MCMURDO = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    WALLOPS = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    FAIRBANK = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    KOUROU = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    VILSP1 = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    MASPA = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']
    
    CDA_LOS = []
    MCMURDO_LOS = []
    WALLOPS_LOS = []
    FAIRBANK_LOS = []
    KOUROU_LOS = []
    VILSP1_LOS = []
    MASPA_LOS = []
    
    def Antenna_vet(CDAs, CDAs_LOS, i_chr_CDAs, flagCDAs_AOS, flagCDAs_AOSM, idate, idate_OLD ):
        i_chr_CDAs_Azi = i_chr_CDAs[0:3]
        
        if (i_chr_CDAs_Azi!='   ' and i_chr_CDAs_Azi!=''):
            i_CDAs_Azi=int(i_chr_CDAs[0:3])
            i_CDAs_El=int(i_chr_CDAs[4:6])
            i_chr_CDAs_M=i_chr_CDAs[7:8]
            if (i_CDAs_El==0 and flagCDAs_AOS==1):
                flagCDAs_AOS=0
                CDAs[0]=idate
            if (flagCDAs_AOSM==1 and i_chr_CDAs_M!='*'):
                flagCDAs_AOSM = 0
                CDAs[1]=idate
            if (i_chr_CDAs_M=='a'):
                #CDAs.append(idate)
                CDAs[1]=idate
            if (i_chr_CDAs_M=='A'):
                #CDAs.append(idate)
                CDAs[2]=idate
            if (i_chr_CDAs_M=='M'):
                #CDAs.append(idate)
                CDAs[3]=idate
            if (i_chr_CDAs_M=='L'):
                #CDAs.append(idate)
                CDAs[4]=idate
            if (i_chr_CDAs_M=='l'):
                #CDAs.append(idate)
                CDAs[5]=idate
            if (flagCDAs_AOSM==0 and CDAs[5]=='N/A' and i_chr_CDAs_M=='*'):
                CDAs[5]=idate_OLD
            if (i_CDAs_El==0 and flagCDAs_AOS==0):
                #CDAs_LOS.append(idate)
                CDAs[6]=idate
        return CDAs, flagCDAs_AOS, flagCDAs_AOSM, CDAs_LOS
    
    
    
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
# =============================================================================
#         YYMM = lines[ii_RowNow-7-1].strip()
#         YYYYPageDate = int(YYMM[20:24])
#         MMPageDate = int(YYMM[25:27])
# =============================================================================
        
        for i_RowNow in range(ii_RowNow,ii_RowNow+52):
            if (i_RowNow<= len(lines)):
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
                
                if (i_nOrbit == nOrbit_cust):
                    if (flagErrorMsg==0  and Date_date<iDate_old):
                        flagline = 0
                        Date_before = lines[i_RowNow-1-1].strip()[0:15]
                        Date_after = lines[i_RowNow-1].strip()[0:15]
                        ErrorMsg=[1,Wimpyfilepath,i_RowNow-1,i_RowNow,Date_before,Date_after]
                        #ErrorMsg=[1,i_RowNow-1,i_RowNow]
                        flagErrorMsg = 1
                    
                    
                    iCDA = 29
                    i_chr_CDA = strPageDate[iCDA:(iCDA+8)]
                    CDA, flagCDA_AOS, flagCDA_AOSM, CDA_LOS = Antenna_vet(CDA, CDA_LOS, i_chr_CDA, flagCDA_AOS, flagCDA_AOSM, Date_date, iDate_old )
                    
                    iCDA = 40
                    i_chr_MCMURDO = strPageDate[iCDA:(iCDA+9)]
                    
                    MCMURDO, flagMCMURDO_AOS, flagMCMURDO_AOSM, MCMURDO_LOS = Antenna_vet(MCMURDO, MCMURDO_LOS, i_chr_MCMURDO, flagMCMURDO_AOS, flagMCMURDO_AOSM, Date_date, iDate_old )
                    
                    iCDA = 51
                    i_chr_WALLOPS = strPageDate[iCDA:(iCDA+9)]
                    WALLOPS, flagWALLOPS_AOS, flagWALLOPS_AOSM, WALLOPS_LOS = Antenna_vet(WALLOPS, WALLOPS_LOS, i_chr_WALLOPS, flagWALLOPS_AOS, flagWALLOPS_AOSM, Date_date, iDate_old )
                    
                    iCDA = 62
                    i_chr_FAIRBANK = strPageDate[iCDA:(iCDA+9)]
                    FAIRBANK, flagFAIRBANK_AOS, flagFAIRBANK_AOSM, FAIRBANK_LOS = Antenna_vet(FAIRBANK, FAIRBANK_LOS, i_chr_FAIRBANK, flagFAIRBANK_AOS, flagFAIRBANK_AOSM, Date_date, iDate_old )
                    
                    iCDA = 73
                    i_chr_KOUROU = strPageDate[iCDA:(iCDA+9)]
                    KOUROU, flagKOUROU_AOS, flagKOUROU_AOSM, KOUROU_LOS = Antenna_vet(KOUROU, KOUROU_LOS, i_chr_KOUROU, flagKOUROU_AOS, flagKOUROU_AOSM, Date_date, iDate_old )
                    
                    iCDA = 84
                    i_chr_VILSP1 = strPageDate[iCDA:(iCDA+9)]
                    VILSP1, flagVILSP1_AOS, flagVILSP1_AOSM, VILSP1_LOS = Antenna_vet(VILSP1, VILSP1_LOS, i_chr_VILSP1, flagVILSP1_AOS, flagVILSP1_AOSM, Date_date, iDate_old )
                    
                    iCDA = 95
                    i_chr_MASPA = strPageDate[iCDA:(iCDA+9)]
                    MASPA, flagMASPA_AOS, flagMASPA_AOSM, MASPA_LOS = Antenna_vet(MASPA, MASPA_LOS, i_chr_MASPA, flagMASPA_AOS, flagMASPA_AOSM, Date_date, iDate_old )
                    
                DD_date_old = DD_date
                iDate_old = Date_date
        
        if (i_nOrbit > nOrbit_cust):
            flagline = 0
        if ( i_RowNow >= len(lines) ):
            flagline = 0
        ii_RowNow = i_RowNow + 8
    
    if (len(CDA_LOS)!=0):
        CDA.append(max(CDA_LOS))
    if (len(MCMURDO_LOS)!=0):
        MCMURDO.append(max(MCMURDO_LOS))
    if (len(WALLOPS_LOS)!=0):
        WALLOPS.append(max(WALLOPS_LOS))
    if (len(FAIRBANK_LOS)!=0):
        FAIRBANK.append(max(FAIRBANK_LOS))
    if (len(KOUROU_LOS)!=0):
        KOUROU.append(max(KOUROU_LOS))
    if (len(VILSP1_LOS)!=0):
        VILSP1.append(max(VILSP1_LOS))
    if (len(MASPA_LOS)!=0):
        MASPA.append(max(MASPA_LOS))
    
    
# =============================================================================
#     print(VILSP1)
#     nCDA = 7
#     nnCDA=[]
#     for i in range(0,nCDA):
#         nnCDA.append('N/A')
#     
#     if (len(CDA)!=nCDA):
#         CDA = nnCDA
#     if (len(MCMURDO)!=nCDA):
#         MCMURDO = nnCDA
#     if (len(WALLOPS)!=nCDA):
#         WALLOPS = nnCDA
#     if (len(FAIRBANK)!=nCDA):
#         FAIRBANK = nnCDA
#     if (len(KOUROU)!=nCDA):
#         KOUROU = nnCDA
#     if (len(VILSP1)!=nCDA):
#         VILSP1 = nnCDA
#         print('cios')
#     if (len(MASPA)!=nCDA):
#         MASPA = nnCDA
# =============================================================================
    fp.close()
    
    dataindex = ['AOS','AOSM','AOS5','Mid','LOS5','LOSM', 'LOS']
    datacolumns = ['CDA','MCMURDO','WAL','FBK','KOU','VL1','MAS']
    
    data = {datacolumns[0]: CDA,
            datacolumns[1]: MCMURDO,
            datacolumns[2]: WALLOPS,
            datacolumns[3]: FAIRBANK,
            datacolumns[4]: KOUROU,
            datacolumns[5]: VILSP1,
            datacolumns[6]: MASPA
            }
    
    XTTC_FBK = DataFrame (data, index=dataindex, columns = datacolumns)
    
    return XTTC_FBK, ErrorMsg












def fcn_Manoeuvre(DTBurn, Wimpyfilepath):
    
    ErrorMsg = [0,0,0,0]
    flagErrorMsg = 0
    
    fp=open(Wimpyfilepath,'r')
    lines=fp.readlines()
    fp.close()
    
    
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
    
    nOrbit_icust = []
    
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
            
            if (Date_date >= DTBurn ):
                flagline = 0
            
            if ( flagline == 1 ):
                nOrbit_icust.append(i_nOrbit)
            
            DD_date_old = DD_date
            iDate_old = Date_date
        
        if ( i_RowNow >= len(lines) ):
            flagline = 0
        ii_RowNow = i_RowNow + 8
    
    
    
    
    
    
    
    
    
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
    
    
    if (len(nOrbit_icust)>=5):
        nOrbit_cust[0] = 1
        nOrbit_cust[1] = nOrbit_icust[-5]
        nOrbit_cust[2] = nOrbit_icust[-1]
        
        i_nOrbit_valid_Old = nOrbit_cust[1]
        i_nOrbit_Valid = 0
        ii_RowNow=22
        flagline = 1
        flagDD1=1
        
        CDA      = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
        
        CDA_LOS = []
        
        ii_CDA = []
        
        flagCDA_ANX = 1
        
        flagCDA_AOS = 1
        
        flagCDA_AOSM = 1
        
        flagCDA_LOS = 1
        
        
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
                        #ErrorMsg=[1,Wimpyfilepath,i_RowNow-1,i_RowNow]
                        flagErrorMsg = 1
                    
                    i_nOrbit_Valid = i_nOrbit
                    if (i_nOrbit_Valid != i_nOrbit_valid_Old):
                        if (len(CDA_LOS)!=0):
                            CDA.append(max(CDA_LOS))
                        
                        
                        ii_CDA.append(CDA)
                        
                        CDA      = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                        
                        CDA_LOS = []
                        
                        flagCDA_ANX = 1
                        
                        flagCDA_AOS = 1
                        
                        flagCDA_AOSM = 1
                        
                        flagCDA_LOS = 1
                        
                        
                    iCDA = 29
                    i_chr_CDA = strPageDate[iCDA:(iCDA+9)]
                    #print(i_chr_CDA)
                    CDA, flagCDA_AOS, flagCDA_AOSM, flagCDA_ANX, CDA_LOS = Antenna_vet(CDA, CDA_LOS, i_chr_CDA, flagCDA_AOS, flagCDA_AOSM, flagCDA_ANX, Date_date, iDate_old, i_nOrbit_Valid )
                    
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
            data.append(i_data)
        
        FDF_Pass = DataFrame (data, columns = datacolumns)
        
        if (FDF_Pass.loc[FDF_Pass.shape[0],['CDA_AOS']]['CDA_AOS']>DTBurn):
            FDF_Pass = FDF_Pass.drop([FDF_Pass.shape[0]])
        else:
            FDF_Pass = FDF_Pass.drop([0])
            
        
        Man_info = [1,FDF_Pass, ErrorMsg]
    else:
        Man_info = [0,0,0]
    
    return Man_info