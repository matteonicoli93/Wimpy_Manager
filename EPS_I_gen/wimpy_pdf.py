# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:25:49 2020

@author: matte
"""


import datetime

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter

from reportlab.platypus import Table
from reportlab.lib.units import cm

# add style
from reportlab.platypus import TableStyle
from reportlab.lib import colors











def Set_SimpleDocTemplate(fileName):
    pdf = SimpleDocTemplate(
        fileName,
        pagesize=letter,
#        rightMargin=72,leftMargin=72,
        topMargin=5,bottomMargin=5
    )
    return pdf











def Set_GFeatures():
    sFT=10
    sLB = 1
    sBP = 1
    return sFT, sLB, sBP











def Set_TableStyle(data_Int):
    nCol = len(data_Int[0])-1
    sFT, sLB, sBP = Set_GFeatures()
    ts_Int = TableStyle(
        [
        ('FONTSIZE', (0,0), (nCol,0), sFT),
        ('LINEBELOW',(0,0),(nCol,0),sLB,colors.black),
        ('BOTTOMPADDING',(0,0),(nCol,0),sBP)
        ]
    )
    return ts_Int, nCol











def date2str(dataAOS):
    midrosecond=int(dataAOS.strftime('%f'))
    if (midrosecond>500000):
        dataAOS1=dataAOS+datetime.timedelta(seconds=1)
    else:
        dataAOS1=dataAOS
    DOY=dataAOS1.strftime('%j')
    if (dataAOS1.hour<10):
        HH = '0'+str(dataAOS1.hour)
    else:
        HH = str(dataAOS1.hour)
    if (dataAOS1.minute<10):
        MM = '0'+str(dataAOS1.minute)
    else:
        MM = str(dataAOS1.minute)
    if (dataAOS1.second<10):
        SS = '0'+str(dataAOS1.second)
    else:
        SS = str(dataAOS1.second)
    strDOYhms=DOY+'-'+HH+':'+MM+':'+SS
    return strDOYhms





    
    
    
    
    
    
def DataMag_iPass_SpaGrndCon(PassM0136h,i_Pass,SpaGrndCon):
    SC=PassM0136h.loc[i_Pass,['S/C']]['S/C']
    M01=PassM0136h.loc[i_Pass,['M01']]['M01']
    NOAA_BOS = PassM0136h.loc[i_Pass,['NOAA_BOS']]['NOAA_BOS']
    
    CDAn=PassM0136h.loc[i_Pass,['CDAn']]['CDAn']
    nOrbit=PassM0136h.loc[i_Pass,['CDA_nOrbit']]['CDA_nOrbit']
    DEF_Pss=PassM0136h.loc[i_Pass,['TM_Format']]['TM_Format']
    
    AOCS_TMF = ''
    if (DEF_Pss=='DEF_ROUT'):
        AOCS_TMF = DEF_Pss
    
    AOS=PassM0136h.loc[i_Pass,['CDA_AOS']]['CDA_AOS']
    LOS=PassM0136h.loc[i_Pass,['CDA_LOS']]['CDA_LOS']
    AOS_Az=PassM0136h.loc[i_Pass,['CDA_AOS_Azi']]['CDA_AOS_Azi']
    
    CDA_CONF_PI=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_CONF_S=PassM0136h.loc[i_Pass,['CDA_CONF_S']]['CDA_CONF_S']
    CDA_CONF_E=PassM0136h.loc[i_Pass,['CDA_CONF_E']]['CDA_CONF_E']
    CDA_PASS_S=PassM0136h.loc[i_Pass,['CDA_PASS_S']]['CDA_PASS_S']
    CDA_PASS_E=PassM0136h.loc[i_Pass,['CDA_PASS_E']]['CDA_PASS_E']
    CDA_STANDBY_S=PassM0136h.loc[i_Pass,['CDA_STANDBY_S']]['CDA_STANDBY_S']
    CDA_STANDBY_E=PassM0136h.loc[i_Pass,['CDA_STANDBY_E']]['CDA_STANDBY_E']
    
    FEP_ACQ_START=PassM0136h.loc[i_Pass,['FEP_Acquisition_Start']]['FEP_Acquisition_Start']
    FEP_ACQ_STOP=PassM0136h.loc[i_Pass,['FEP_Acquisition_Stop']]['FEP_Acquisition_Stop']
    FEP_TT_START=PassM0136h.loc[i_Pass,['FEP_Time_Tag_Start']]['FEP_Time_Tag_Start']
    FEP_TT_STOP=PassM0136h.loc[i_Pass,['FEP_Time_Tag_Stop']]['FEP_Time_Tag_Stop']
    FEP_SEN_START=PassM0136h.loc[i_Pass,['FEP_Sensing_Start']]['FEP_Sensing_Start']
    FEP_SEN_STOP=PassM0136h.loc[i_Pass,['FEP_Sensing_Stop']]['FEP_Sensing_Stop']
    
    PGF_ACQ_START=PassM0136h.loc[i_Pass,['PGF_Acquisition_Start']]['PGF_Acquisition_Start']
    PGF_ACQ_STOP=PassM0136h.loc[i_Pass,['PGF_Acquisition_Stop']]['PGF_Acquisition_Stop']
    PGF_TT_START=PassM0136h.loc[i_Pass,['PGF_Time_Tag_Start']]['PGF_Time_Tag_Start']
    PGF_TT_STOP=PassM0136h.loc[i_Pass,['PGF_Time_Tag_Stop']]['PGF_Time_Tag_Stop']
    PGF_SEN_START=PassM0136h.loc[i_Pass,['PGF_Sensing_Start']]['PGF_Sensing_Start']
    PGF_SEN_STOP=PassM0136h.loc[i_Pass,['PGF_Sensing_Stop']]['PGF_Sensing_Stop']
    
    EOA030=PassM0136h.loc[i_Pass,['EOA030']]['EOA030']
    EOA031=PassM0136h.loc[i_Pass,['EOA031']]['EOA031']
    
    AOSstr=date2str(AOS)
    LOSstr=date2str(LOS)
    CDA_CONF_PIsrt=date2str(CDA_CONF_PI)
    CDA_CONF_Ssrt=date2str(CDA_CONF_S)
    CDA_CONF_Esrt=date2str(CDA_CONF_E)
    CDA_PASS_Ssrt=date2str(CDA_PASS_S)
    CDA_PASS_Esrt=date2str(CDA_PASS_E)
    CDA_STANDBY_Ssrt=date2str(CDA_STANDBY_S)
    CDA_STANDBY_Esrt=date2str(CDA_STANDBY_E)
    
    FEP_ACQ_STARTsrt=date2str(FEP_ACQ_START)
    FEP_ACQ_STOPsrt=date2str(FEP_ACQ_STOP)
    FEP_TT_STARTsrt=date2str(FEP_TT_START)
    FEP_TT_STOPsrt=date2str(FEP_TT_STOP)
    FEP_SEN_STARTsrt=date2str(FEP_SEN_START)
    FEP_SEN_STOPsrt=date2str(FEP_SEN_STOP)
    
    PGF_ACQ_STARTsrt=date2str(PGF_ACQ_START)
    PGF_ACQ_STOPsrt=date2str(PGF_ACQ_STOP)
    PGF_TT_STARTsrt=date2str(PGF_TT_START)
    PGF_TT_STOPsrt=date2str(PGF_TT_STOP)
    PGF_SEN_STARTsrt=date2str(PGF_SEN_START)
    PGF_SEN_STOPsrt=date2str(PGF_SEN_STOP)
    
    if (EOA030!=0):
        EOA030str=date2str(EOA030)
    else:
        EOA030str=''
    if (EOA031!=0):
        EOA031str=date2str(EOA031)
    else:
        EOA031str=''
    
    if (SpaGrndCon==1 or SpaGrndCon==2):
        ADA_Mid=PassM0136h.loc[i_Pass,['ADA_Start_TT']]['ADA_Start_TT']
        SSR_TT=PassM0136h.loc[i_Pass,['SSR_TT']]['SSR_TT']
        ADA_Midsrt=date2str(ADA_Mid)
        SSR_TTsrt=date2str(SSR_TT)
    
    if (SpaGrndCon==1):
        if (M01==1):
            data_iPass = [
                ['S/C: '+SC                 , 'PI Activ: '+CDA_CONF_PIsrt               , 'PI Activ: '                  , 'PI Activ: '                  ,''],
                ['Orbit: '+str(nOrbit)      , 'CONF: '+CDA_CONF_Ssrt                    , 'ACQ S: '+FEP_ACQ_STARTsrt    , 'ACQ S: '+PGF_ACQ_STARTsrt    ,''],
                [ CDAn+' Az: '+str(AOS_Az)  , '            '+CDA_CONF_Esrt              , 'ACQ E: '+FEP_ACQ_STOPsrt     , 'ACQ E: '+PGF_ACQ_STOPsrt     ,''],
                ['SVL AOS: '+AOSstr         , 'PASS: '+CDA_PASS_Ssrt                    , 'TT S: '+FEP_TT_STARTsrt      , 'TT S: '+PGF_TT_STARTsrt      ,'ADA Start: '+ADA_Midsrt],
                ['SVL LOS: '+LOSstr         , '            '+CDA_PASS_Esrt              , 'TT E: '+FEP_TT_STOPsrt       , 'TT E: '+PGF_TT_STOPsrt       ,'SSR GAP: '+SSR_TTsrt],
                [AOCS_TMF                   , 'STANDBY: '+CDA_STANDBY_Ssrt              , 'ORBIT S: '+str(nOrbit-1)     , 'ORBIT S: '+str(nOrbit-1)     ,''],
                [''                         , '                   '+CDA_STANDBY_Esrt    , 'ORBIT E: '+str(nOrbit)       , 'ORBIT E: '+str(nOrbit)       ,''],
                [''                         , ''                                        , 'SENS S: '+FEP_SEN_STARTsrt   , 'SENS S: '+PGF_SEN_STARTsrt   ,''],
                [''                         , ''                                        , 'SENS E: '+FEP_SEN_STARTsrt   , 'SENS E: '+PGF_SEN_STOPsrt    ,''],
            ]
        elif (M01==2 or M01==3):
            data_iPass = [
                ['S/C: '+SC                 , 'PI Activ: '+CDA_CONF_PIsrt               , 'PI Activ: '                   , 'PI Activ: '                 ,''],
                ['Orbit: '+str(nOrbit)      , 'CONF: '+CDA_CONF_Ssrt                    , 'ACQ S: '+FEP_ACQ_STARTsrt     , 'ACQ S: '+PGF_ACQ_STARTsrt   ,''],
                [ CDAn+' Az: '+str(AOS_Az)  , '            '+CDA_CONF_Esrt              , 'ACQ E: '+FEP_ACQ_STOPsrt      , 'ACQ S: '+PGF_ACQ_STOPsrt    ,''],
                ['SVL AOS: '+AOSstr         , 'PASS: '+CDA_PASS_Ssrt                    , 'TT S: '+FEP_TT_STARTsrt       , 'TT S: '+PGF_TT_STARTsrt     ,''],
                ['SVL LOS: '+LOSstr         , '            '+CDA_PASS_Esrt              , 'TT E: '+FEP_TT_STOPsrt        , 'TT E: '+PGF_TT_STOPsrt      ,''],
                [AOCS_TMF                   , 'STANDBY: '+CDA_STANDBY_Ssrt              , 'ORBIT S: '+str(nOrbit-1)      , 'ORBIT S: '+str(nOrbit-1)    ,''],
                [''                         , '                   '+CDA_STANDBY_Esrt    , 'ORBIT E: '+str(nOrbit)        , 'ORBIT E: '+str(nOrbit)      ,''],
                [''                         , ''                                        , 'SENS S: '+FEP_SEN_STARTsrt    , 'SENS S: '+PGF_SEN_STARTsrt  ,''],
                [''                         , ''                                        , 'SENS E: '+FEP_SEN_STARTsrt    , 'SENS E: '+PGF_SEN_STOPsrt   ,''],
            ]
        elif (NOAA_BOS != 'N/A'):
            data_iPass = [
                ['S/C: '+SC                 , 'PI Activ: '+CDA_CONF_PIsrt               , 'PI Activ: '                   , 'PI Activ: '                 ,''],
                ['Orbit: '+str(nOrbit)      , 'CONF: '+CDA_CONF_Ssrt                    , 'ACQ S: '+FEP_ACQ_STARTsrt     , 'ACQ S: '+PGF_ACQ_STARTsrt   ,''],
                [ CDAn+' Az: '+str(AOS_Az)  , '            '+CDA_CONF_Esrt              , 'ACQ E: '+FEP_ACQ_STOPsrt      , 'ACQ S: '+PGF_ACQ_STOPsrt    ,''],
                ['SVL AOS: '+AOSstr         , 'PASS: '+CDA_PASS_Ssrt                    , 'TT S: '+FEP_TT_STARTsrt       , 'TT S: '+PGF_TT_STARTsrt     ,''],
                ['SVL LOS: '+LOSstr         , '            '+CDA_PASS_Esrt              , 'TT E: '+FEP_TT_STOPsrt        , 'TT E: '+PGF_TT_STOPsrt      ,''],
                [''                         , 'STANDBY: '+CDA_STANDBY_Ssrt              , 'ORBIT S: '+str(nOrbit-1)      , 'ORBIT S: '+str(nOrbit-1)    ,''],
                [''                         , '                   '+CDA_STANDBY_Esrt    , 'ORBIT E: '+str(nOrbit)        , 'ORBIT E: '+str(nOrbit)      ,''],
                [''                         , ''                                        , 'SENS S: '+FEP_SEN_STARTsrt    , 'SENS S: '+PGF_SEN_STARTsrt  ,''],
                [''                         , ''                                        , 'SENS E: '+FEP_SEN_STARTsrt    , 'SENS E: '+PGF_SEN_STOPsrt   ,''],
            ]
    elif  (SpaGrndCon==2):
        if (M01==1):
            data_iPass = [
                ['S/C: '+SC              , 'EOA030: '+EOA030str , ''                       , '' ],
                ['Orbit: '+str(nOrbit)   , 'EOA031: '+EOA031str , 'ADA Start: '+ADA_Midsrt , '' ],
                ['SVL AOS: '+AOSstr      , 'TT IASI: '          , 'SSR GAP: '+SSR_TTsrt    , '' ],
                ['SVL LOS:  '+LOSstr     , ''                   , ''                       , '' ],
                [ AOCS_TMF               , ''                   , ''                       , '' ]
            ]
        elif (M01==2 or M01==3):
            data_iPass = [
                ['S/C: '+SC              , 'EOA030: '+EOA030str , '', '' ],
                ['Orbit: '+str(nOrbit)   , 'EOA031: '+EOA031str , '', '' ],
                ['SVL AOS: '+AOSstr      , 'TT IASI: '          , '', '' ],
                ['SVL LOS:  '+LOSstr     , ''                   , '', '' ],
                [ AOCS_TMF               , ''                   , '', '' ]
            ]
    elif  (SpaGrndCon==3):
        if (M01==1 or M01==2 or M01==3):
            data_iPass = [
                ['S/C: '+SC                 , 'PI Activ: '+CDA_CONF_PIsrt               , 'PI Activ: '                   , 'PI Activ: '                 ],
                ['Orbit: '+str(nOrbit)      , 'CONF: '+CDA_CONF_Ssrt                    , 'ACQ S: '+FEP_ACQ_STARTsrt     , 'ACQ S: '+PGF_ACQ_STARTsrt   ],
                [ CDAn+' Az: '+str(AOS_Az)  , '            '+CDA_CONF_Esrt              , 'ACQ E: '+FEP_ACQ_STOPsrt      , 'ACQ S: '+PGF_ACQ_STOPsrt    ],
                ['SVL AOS: '+AOSstr         , 'PASS: '+CDA_PASS_Ssrt                    , 'TT S: '+FEP_TT_STARTsrt       , 'TT S: '+PGF_TT_STARTsrt     ],
                ['SVL LOS: '+LOSstr         , '            '+CDA_PASS_Esrt              , 'TT E: '+FEP_TT_STOPsrt        , 'TT E: '+PGF_TT_STOPsrt      ],
                [''                         , 'STANDBY: '+CDA_STANDBY_Ssrt              , 'ORBIT S: '+str(nOrbit-1)      , 'ORBIT S: '+str(nOrbit-1)    ],
                [''                         , '                   '+CDA_STANDBY_Esrt    , 'ORBIT E: '+str(nOrbit)        , 'ORBIT E: '+str(nOrbit)      ],
                [''                         , ''                                        , 'SENS S: '+FEP_SEN_STARTsrt    , 'SENS S: '+PGF_SEN_STARTsrt  ],
                [''                         , ''                                        , 'SENS E: '+FEP_SEN_STARTsrt    , 'SENS E: '+PGF_SEN_STOPsrt   ],
            ]
        elif (NOAA_BOS != 'N/A' ):
            data_iPass = [
                ['S/C: '+SC                 , 'PI Activ: '+CDA_CONF_PIsrt               , 'PI Activ: '                   , 'PI Activ: '                 ],
                ['Orbit: '+str(nOrbit)      , 'CONF: '+CDA_CONF_Ssrt                    , 'ACQ S: '+FEP_ACQ_STARTsrt     , 'ACQ S: '+PGF_ACQ_STARTsrt   ],
                [ CDAn+' Az: '+str(AOS_Az)  , '            '+CDA_CONF_Esrt              , 'ACQ E: '+FEP_ACQ_STOPsrt      , 'ACQ S: '+PGF_ACQ_STOPsrt    ],
                ['SVL AOS: '+AOSstr         , 'PASS: '+CDA_PASS_Ssrt                    , 'TT S: '+FEP_TT_STARTsrt       , 'TT S: '+PGF_TT_STARTsrt     ],
                ['SVL LOS: '+LOSstr         , '            '+CDA_PASS_Esrt              , 'TT E: '+FEP_TT_STOPsrt        , 'TT E: '+PGF_TT_STOPsrt      ],
                [''                         , 'STANDBY: '+CDA_STANDBY_Ssrt              , 'ORBIT S: '+str(nOrbit-1)      , 'ORBIT S: '+str(nOrbit-1)    ],
                [''                         , '                   '+CDA_STANDBY_Esrt    , 'ORBIT E: '+str(nOrbit)        , 'ORBIT E: '+str(nOrbit)      ],
                [''                         , ''                                        , 'SENS S: '+FEP_SEN_STARTsrt    , 'SENS S: '+PGF_SEN_STARTsrt  ],
                [''                         , ''                                        , 'SENS E: '+FEP_SEN_STARTsrt    , 'SENS E: '+PGF_SEN_STOPsrt   ],
            ]
    return data_iPass











def fcn_WimpySpaGrndConpdf(fileName,PassM0136h, SpaGrndCon):
    pdf = Set_SimpleDocTemplate(fileName)
    sFT, sLB, sBP = Set_GFeatures()
    
    
    
    # List of Lists
    if (SpaGrndCon==1):
        nrow = 9-1
        data_SpaCon_Int = [
            ['Pass'          , 'PMON', 'FEP', 'PGF', 'SSR Anomaly' ]
        ]
        colWidths_cm = 4.2
        rowHeights_vet = (0.5*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.25*cm)
    elif (SpaGrndCon==2):
        nrow = 5-1
        data_SpaCon_Int = [
            ['Pass'          , 'ENA0011', 'SSR Anomaly', '' ]
        ]
        colWidths_cm = 5
        rowHeights_vet = (0.5*cm,0.375*cm,0.375*cm,0.375*cm,0.25*cm)
    elif (SpaGrndCon==3):
        nrow = 9-1
        data_SpaCon_Int = [
            ['Pass'          , 'PMON', 'FEP', 'PGF' ]
        ]
        colWidths_cm = 5
        rowHeights_vet = (0.5*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.25*cm)
    
    # 3) Add borders
    ts_Int, nCol = Set_TableStyle(data_SpaCon_Int)
    ts_iPass = TableStyle(
        [
        #('LINEBEFORE',(2,1),(2,-1),2,colors.black),
        ('FONTSIZE', (0,0), (nCol,nrow), sFT),
        ('LINEABOVE',(0,0),(nCol,0),sLB,colors.black),
        ('LINEBELOW',(0,nrow),(nCol,nrow),sLB,colors.black),
        ('BOTTOMPADDING',(0,nrow),(nCol,nrow),sBP)
        ]
    )
    
    table_SpaCon_Int = Table(data_SpaCon_Int, colWidths=[colWidths_cm*cm] * len(data_SpaCon_Int[0]))
    table_SpaCon_Int.setStyle(ts_Int)
    
    elems = []
    elems.append(table_SpaCon_Int)
    
    for i_Pass in range(0,PassM0136h.shape[0]):
        data_iPass = DataMag_iPass_SpaGrndCon(PassM0136h,i_Pass,SpaGrndCon)
        
        table_iPass = Table(data_iPass, colWidths=[colWidths_cm*cm] * len(data_iPass[0]),rowHeights=rowHeights_vet)
        table_iPass.setStyle(ts_iPass)
        elems.append(table_iPass)
    
    pdf.build(elems)