# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 01:30:43 2020

@author: Nicoli
"""

import datetime
from datetime import timezone

import pandas as pd

def fcn_XTTC_FBK(Wimpyfilepath, nOrbit_cust):
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
    
    def Antenna_vet(CDAs, CDAs_LOS, i_chr_CDAs, flagCDAs_AOS, idate ):
        i_chr_CDAs_Azi = i_chr_CDAs[0:3]
        
        if (i_chr_CDAs_Azi!='   ' and i_chr_CDAs_Azi!=''):
            i_CDAs_Azi=int(i_chr_CDAs[0:3])
            i_CDAs_El=int(i_chr_CDAs[4:6])
            i_chr_CDAs_M=i_chr_CDAs[7:8]
            if (i_CDAs_El==0 and flagCDAs_AOS==1):
                flagCDAs_AOS=0
                CDAs[0]=idate
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
            if (i_CDAs_El==0 and flagCDAs_AOS==0):
                #CDAs_LOS.append(idate)
                CDAs[6]=idate
        return CDAs, flagCDAs_AOS, CDAs_LOS
    
    
    
    
    while (flagline == 1):
        YYMM = lines[ii_RowNow-7-1].strip()
        YYYYPageDate = int(YYMM[20:24])
        MMPageDate = int(YYMM[25:27])
        
        for i_RowNow in range(ii_RowNow,ii_RowNow+52):
            strPageDate=lines[i_RowNow-1].strip()
            
            
            i_nOrbit = int(strPageDate[21:26])
            if (i_nOrbit == nOrbit_cust):
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
                    Date_date=datetime.datetime(YYYYPageDate, MMPageDate, iDD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)+datetime.timedelta(days=1)
                else:
                    Date_date=datetime.datetime(YYYYPageDate, MMPageDate, iDD_date, hh_date, mm_date, s1ss_date, s2ss_date*1000)
                    if (flagDD1 == 1):
                        iDate_old = Date_date
                        flagDD1 = 0
                
                
                iCDA = 29
                i_chr_CDA = strPageDate[iCDA:(iCDA+8)]
                CDA, flagCDA_AOS, CDA_LOS = Antenna_vet(CDA, CDA_LOS, i_chr_CDA, flagCDA_AOS, Date_date )
                
                iCDA = 40
                i_chr_MCMURDO = strPageDate[iCDA:(iCDA+9)]
                
                MCMURDO, flagMCMURDO_AOS, MCMURDO_LOS = Antenna_vet(MCMURDO, MCMURDO_LOS, i_chr_MCMURDO, flagMCMURDO_AOS, Date_date )
                
                iCDA = 51
                i_chr_WALLOPS = strPageDate[iCDA:(iCDA+9)]
                WALLOPS, flagWALLOPS_AOS, WALLOPS_LOS = Antenna_vet(WALLOPS, WALLOPS_LOS, i_chr_WALLOPS, flagWALLOPS_AOS, Date_date )
                
                iCDA = 62
                i_chr_FAIRBANK = strPageDate[iCDA:(iCDA+9)]
                FAIRBANK, flagFAIRBANK_AOS, FAIRBANK_LOS = Antenna_vet(FAIRBANK, FAIRBANK_LOS, i_chr_FAIRBANK, flagFAIRBANK_AOS, Date_date )
                
                iCDA = 73
                i_chr_KOUROU = strPageDate[iCDA:(iCDA+9)]
                KOUROU, flagKOUROU_AOS, KOUROU_LOS = Antenna_vet(KOUROU, KOUROU_LOS, i_chr_KOUROU, flagKOUROU_AOS, Date_date )
                
                iCDA = 84
                i_chr_VILSP1 = strPageDate[iCDA:(iCDA+9)]
                VILSP1, flagVILSP1_AOS, VILSP1_LOS = Antenna_vet(VILSP1, VILSP1_LOS, i_chr_VILSP1, flagVILSP1_AOS, Date_date )
                
                iCDA = 95
                i_chr_MASPA = strPageDate[iCDA:(iCDA+9)]
                MASPA, flagMASPA_AOS, MASPA_LOS = Antenna_vet(MASPA, MASPA_LOS, i_chr_MASPA, flagMASPA_AOS, Date_date )
                
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
    
    XTTC_FBK = pd.DataFrame (data, index=dataindex, columns = datacolumns)
    
    return XTTC_FBK