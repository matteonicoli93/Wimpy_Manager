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











def DataMag_iPass_SpaCon(PassM0136h,i_Pass):
    SC=PassM0136h.loc[i_Pass,['S/C']]['S/C']
    M01=PassM0136h.loc[i_Pass,['M01']]['M01']
    nOrbit=PassM0136h.loc[i_Pass,['CDA_nOrbit']]['CDA_nOrbit']
    DEF_Pss=PassM0136h.loc[i_Pass,['TM_Format']]['TM_Format']
    AOS=PassM0136h.loc[i_Pass,['CDA_AOSM']]['CDA_AOSM']
    LOS=PassM0136h.loc[i_Pass,['CDA_LOSM']]['CDA_LOSM']
    EOA030=PassM0136h.loc[i_Pass,['EOA030']]['EOA030']
    EOA031=PassM0136h.loc[i_Pass,['EOA031']]['EOA031']
    
    AOSstr=date2str(AOS)
    LOSstr=date2str(LOS)
    if (EOA030!=0):
        EOA030str=date2str(EOA030)
    else:
        EOA030str=''
    if (EOA031!=0):
        EOA031str=date2str(EOA031)
    else:
        EOA031str=''
    
    if (M01==1):
        ADA_Mid=PassM0136h.loc[i_Pass,['ADA_Start_TT']]['ADA_Start_TT']
        SSR_TT=PassM0136h.loc[i_Pass,['SSR_TT']]['SSR_TT']
        ADA_Midsrt=date2str(ADA_Mid)
        SSR_TTsrt=date2str(SSR_TT)
        data_iPass = [
            ['SC: '+SC               , 'EOA030: '+EOA030str , ''                       , '' ],
            ['Orbit: '+str(nOrbit)   , 'EOA031: '+EOA031str , 'ADA Start: '+ADA_Midsrt , '' ],
            ['SVL AOSM: '+AOSstr     , 'TT IASI: '          , 'SSR GAP: '+SSR_TTsrt    , '' ],
            ['SVL LOSM: '+LOSstr     , ''                   , ''                       , '' ],
            [ DEF_Pss                , ''                   , ''                       , '' ]
        ]
    else:
        data_iPass = [
            ['SC: '+SC               , 'EOA030: '+EOA030str , '', '' ],
            ['Orbit: '+str(nOrbit)   , 'EOA031: '+EOA031str , '', '' ],
            ['SVL AOSM: '+AOSstr     , 'TT IASI: '          , '', '' ],
            ['SVL LOSM: '+LOSstr     , ''                   , '', '' ],
            [ DEF_Pss                , ''                   , '', '' ]
        ]
    return data_iPass











def fcn_WimpySpaConpdf(fileName,PassM0136h):
    pdf = Set_SimpleDocTemplate(fileName)
    sFT, sLB, sBP = Set_GFeatures()
    
    # List of Lists
    data_SpaCon_Int = [
        ['Pass'          , 'ENA0011', 'SSR Anomaly', '' ]
    ]
    
    # 3) Add borders
    ts_Int, nCol = Set_TableStyle(data_SpaCon_Int)
    ts_iPass = TableStyle(
        [
        #('LINEBEFORE',(2,1),(2,-1),2,colors.black),
        ('FONTSIZE', (0,0), (nCol,0), sFT),
        ('LINEABOVE',(0,0),(nCol,0),sLB,colors.black),
        ('LINEBELOW',(0,4),(nCol,4),sLB,colors.black),
        ('BOTTOMPADDING',(0,4),(nCol,4),sBP)
        ]
    )
    
    table_SpaCon_Int = Table(data_SpaCon_Int, colWidths=[5*cm] * len(data_SpaCon_Int[0]))
    table_SpaCon_Int.setStyle(ts_Int)
    
    elems = []
    elems.append(table_SpaCon_Int)
    
    for i_Pass in range(0,PassM0136h.shape[0]):
        data_iPass = DataMag_iPass_SpaCon(PassM0136h,i_Pass)
        
        table_iPass = Table(data_iPass, colWidths=[5*cm] * len(data_iPass[0]), rowHeights=(0.5*cm,0.375*cm,0.375*cm,0.375*cm,0.25*cm))
        table_iPass.setStyle(ts_iPass)
        elems.append(table_iPass)
    
    pdf.build(elems)











def DataMag_iPass_GrndCon(PassM0136h,i_Pass):
    SC=PassM0136h.loc[i_Pass,['S/C']]['S/C']
    M01=PassM0136h.loc[i_Pass,['M01']]['M01']
    CDAn=PassM0136h.loc[i_Pass,['CDAn']]['CDAn']
    nOrbit=PassM0136h.loc[i_Pass,['CDA_nOrbit']]['CDA_nOrbit']
    AOS=PassM0136h.loc[i_Pass,['CDA_AOSM']]['CDA_AOSM']
    LOS=PassM0136h.loc[i_Pass,['CDA_LOSM']]['CDA_LOSM']
    AOS_Az=PassM0136h.loc[i_Pass,['CDA_AOS_Azi']]['CDA_AOS_Azi']
    CDA_CONF_PI=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_CONF_S=PassM0136h.loc[i_Pass,['CDA_CONF_S']]['CDA_CONF_S']
    CDA_CONF_E=PassM0136h.loc[i_Pass,['CDA_CONF_E']]['CDA_CONF_E']
    CDA_PASS_S=PassM0136h.loc[i_Pass,['CDA_PASS_S']]['CDA_PASS_S']
    CDA_PASS_E=PassM0136h.loc[i_Pass,['CDA_PASS_E']]['CDA_PASS_E']
    CDA_STANDBY_S=PassM0136h.loc[i_Pass,['CDA_STANDBY_S']]['CDA_STANDBY_S']
    CDA_STANDBY_E=PassM0136h.loc[i_Pass,['CDA_STANDBY_E']]['CDA_STANDBY_E']
    CDA_FEP_A=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_FEP_E=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_PGF_A=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_PGF_A=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    
    AOSstr=date2str(AOS)
    LOSstr=date2str(LOS)
    CDA_CONF_PIsrt=date2str(CDA_CONF_PI)
    CDA_CONF_Ssrt=date2str(CDA_CONF_S)
    CDA_CONF_Esrt=date2str(CDA_CONF_E)
    CDA_PASS_Ssrt=date2str(CDA_PASS_S)
    CDA_PASS_Esrt=date2str(CDA_PASS_E)
    CDA_STANDBY_Ssrt=date2str(CDA_STANDBY_S)
    CDA_STANDBY_Esrt=date2str(CDA_STANDBY_E)
    CDA_FEP_Asrt=date2str(CDA_FEP_A)
    CDA_FEP_Esrt=date2str(CDA_FEP_E)
    CDA_PGF_Asrt=date2str(CDA_PGF_A)
    CDA_PGF_Esrt=date2str(CDA_PGF_A)
    
    
    data_iPass = [
        ['SC: '+SC                  , 'PI Activ: '+CDA_CONF_PIsrt               , 'PI Activ: '      , 'Activ: ' ],
        ['Orbit: '+str(nOrbit)      , 'CONF: '+CDA_CONF_Ssrt                    , 'ACQ_START:'      , 'ACQ_START: ' ],
        [ CDAn+' Az: '+str(AOS_Az)  , '            '+CDA_CONF_Esrt              , 'ACQ_STOP:'       , 'ACQ_STOP: ' ],
        ['SVL AOSM: '+AOSstr        , 'PASS: '+CDA_PASS_Ssrt                    , 'TT Start: '      , 'TT Start: ' ],
        ['SVL LOSM: '+LOSstr        , '            '+CDA_PASS_Esrt              , 'TT Stop: '       , 'TT Stop: ' ],
        [''                         , 'STANDBY: '+CDA_STANDBY_Ssrt              , 'ORBITSTART: '+str(nOrbit-1)    , 'ORBITSTART: '+str(nOrbit-1) ],
        [''                         , '                   '+CDA_STANDBY_Esrt    , 'ORBITSTOP: '+str(nOrbit)     , 'ORBITSTOP: '+str(nOrbit) ],
        [''                         , ''                                        , 'SENSING_START: ' , 'SENSING_START: ' ],
        [''                         , ''                                        , 'SENSING_STOP: '  , 'SENSING_STOP: ' ],
    ]
    return data_iPass











def fcn_WimpyGrndConpdf(fileName,PassM0136h):
    pdf = Set_SimpleDocTemplate(fileName)
    sFT, sLB, sBP = Set_GFeatures()
    nrow = 9-1
    # List of Lists
    data_SpaCon_Int = [
        ['Pass'          , 'PMON', 'FEP', 'PGF' ]
    ]
    
    # 3) Add borders
    ts_Int, nCol = Set_TableStyle(data_SpaCon_Int)
    ts_iPass = TableStyle(
        [
        #('LINEBEFORE',(2,1),(2,-1),2,colors.black),
        ('FONTSIZE', (0,0), (nCol,0), sFT),
        ('LINEABOVE',(0,0),(nCol,0),sLB,colors.black),
        ('LINEBELOW',(0,nrow),(nCol,nrow),sLB,colors.black),
        ('BOTTOMPADDING',(0,nrow),(nCol,nrow),sBP)
        ]
    )
    
    table_SpaCon_Int = Table(data_SpaCon_Int, colWidths=[5*cm] * len(data_SpaCon_Int[0]))
    table_SpaCon_Int.setStyle(ts_Int)
    
    elems = []
    elems.append(table_SpaCon_Int)
    
    for i_Pass in range(0,PassM0136h.shape[0]):
        data_iPass = DataMag_iPass_GrndCon(PassM0136h,i_Pass)
        
        table_iPass = Table(data_iPass, colWidths=[5*cm] * len(data_iPass[0]),rowHeights=(0.5*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.25*cm))
        table_iPass.setStyle(ts_iPass)
        elems.append(table_iPass)
    
    pdf.build(elems)
    
    
    
    
    
    
    
    
    
    
    
    
    
def DataMag_iPass_SpaGrndCon(PassM0136h,i_Pass):
    SC=PassM0136h.loc[i_Pass,['S/C']]['S/C']
    M01=PassM0136h.loc[i_Pass,['M01']]['M01']
    CDAn=PassM0136h.loc[i_Pass,['CDAn']]['CDAn']
    nOrbit=PassM0136h.loc[i_Pass,['CDA_nOrbit']]['CDA_nOrbit']
    DEF_Pss=PassM0136h.loc[i_Pass,['TM_Format']]['TM_Format']
    AOS=PassM0136h.loc[i_Pass,['CDA_AOSM']]['CDA_AOSM']
    LOS=PassM0136h.loc[i_Pass,['CDA_LOSM']]['CDA_LOSM']
    AOS_Az=PassM0136h.loc[i_Pass,['CDA_AOS_Azi']]['CDA_AOS_Azi']
    CDA_CONF_PI=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_CONF_S=PassM0136h.loc[i_Pass,['CDA_CONF_S']]['CDA_CONF_S']
    CDA_CONF_E=PassM0136h.loc[i_Pass,['CDA_CONF_E']]['CDA_CONF_E']
    CDA_PASS_S=PassM0136h.loc[i_Pass,['CDA_PASS_S']]['CDA_PASS_S']
    CDA_PASS_E=PassM0136h.loc[i_Pass,['CDA_PASS_E']]['CDA_PASS_E']
    CDA_STANDBY_S=PassM0136h.loc[i_Pass,['CDA_STANDBY_S']]['CDA_STANDBY_S']
    CDA_STANDBY_E=PassM0136h.loc[i_Pass,['CDA_STANDBY_E']]['CDA_STANDBY_E']
    CDA_FEP_A=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_FEP_E=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_PGF_A=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
    CDA_PGF_E=PassM0136h.loc[i_Pass,['CDA_CONF_PI']]['CDA_CONF_PI']
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
    CDA_FEP_Asrt=date2str(CDA_FEP_A)
    CDA_FEP_Esrt=date2str(CDA_FEP_E)
    CDA_PGF_Asrt=date2str(CDA_PGF_A)
    CDA_PGF_Esrt=date2str(CDA_PGF_E)
    
    if (EOA030!=0):
        EOA030str=date2str(EOA030)
    else:
        EOA030str=''
    if (EOA031!=0):
        EOA031str=date2str(EOA031)
    else:
        EOA031str=''
    
    if (M01==1):
        ADA_Mid=PassM0136h.loc[i_Pass,['ADA_Start_TT']]['ADA_Start_TT']
        SSR_TT=PassM0136h.loc[i_Pass,['SSR_TT']]['SSR_TT']
        ADA_Midsrt=date2str(ADA_Mid)
        SSR_TTsrt=date2str(SSR_TT)
        data_iPass = [
            ['SC: '+SC                   , 'PI Activ: '+CDA_CONF_PIsrt               , ''                        , ''                        ,'' ],
            ['Orbit: '+str(nOrbit)       , 'CONF: '+CDA_CONF_Ssrt                    , ''                        , ''                        ,'' ],
            [CDAn+' Az: '+str(AOS_Az)    , '            '+CDA_CONF_Esrt              , 'PI Activ: '+CDA_FEP_Asrt , 'PI Activ: '+CDA_PGF_Asrt ,'ADA Start: '+ADA_Midsrt ],
            ['SVL AOSM: '+AOSstr         , 'PASS: '+CDA_PASS_Ssrt                    , 'Exec:     '+CDA_FEP_Esrt , 'Exec:     '+CDA_PGF_Esrt ,'SSR GAP: '+SSR_TTsrt ],
            ['SVL LOSM: '+LOSstr         , '            '+CDA_PASS_Esrt              , ''                        , ''                        ,'' ],
            [ DEF_Pss                    , 'STANDBY: '+CDA_STANDBY_Ssrt              , ''                        , ''                        ,'' ],
            [''                          , '                   '+CDA_STANDBY_Esrt    , ''                        , ''                        ,'' ]
        ]
    else:
        data_iPass = [
            ['SC: '+SC                   , 'PI Activ: '+CDA_CONF_PIsrt               , ''                        , ''                        ,'' ],
            ['Orbit: '+str(nOrbit)       , 'CONF: '+CDA_CONF_Ssrt                    , ''                        , ''                        ,'' ],
            [CDAn+' Az: '+str(AOS_Az)    , '            '+CDA_CONF_Esrt              , 'PI Activ: '+CDA_FEP_Asrt , 'PI Activ: '+CDA_PGF_Asrt ,'' ],
            ['SVL AOSM: '+AOSstr         , 'PASS: '+CDA_PASS_Ssrt                    , 'Exec:     '+CDA_FEP_Esrt , 'Exec:     '+CDA_PGF_Esrt ,'' ],
            ['SVL LOSM: '+LOSstr         , '            '+CDA_PASS_Esrt              , ''                        , ''                        ,'' ],
            [ DEF_Pss                    , 'STANDBY: '+CDA_STANDBY_Ssrt              , ''                        , ''                        ,'' ],
            [''                          , '                   '+CDA_STANDBY_Esrt    , ''                        , ''                        ,'' ]
        ]
    
    return data_iPass











def fcn_WimpySpaGrndConpdf(fileName,PassM0136h):
    pdf = Set_SimpleDocTemplate(fileName)
    sFT, sLB, sBP = Set_GFeatures()
    
    # List of Lists
    data_SpaCon_Int = [
        ['Pass'          , 'PMON', 'FEP', 'PGF', 'SSR Anomaly' ]
    ]
    
    # 3) Add borders
    ts_Int, nCol = Set_TableStyle(data_SpaCon_Int)
    ts_iPass = TableStyle(
        [
        #('LINEBEFORE',(2,1),(2,-1),2,colors.black),
        ('FONTSIZE', (0,0), (nCol,6), sFT),
        ('LINEABOVE',(0,0),(nCol,0),sLB,colors.black),
        ('LINEBELOW',(0,6),(nCol,6),sLB,colors.black),
        ('BOTTOMPADDING',(0,6),(nCol,6),sBP)
        ]
    )
    
    table_SpaCon_Int = Table(data_SpaCon_Int, colWidths=[4.2*cm] * len(data_SpaCon_Int[0]))
    table_SpaCon_Int.setStyle(ts_Int)
    
    elems = []
    elems.append(table_SpaCon_Int)
    
    for i_Pass in range(0,PassM0136h.shape[0]):
        data_iPass = DataMag_iPass_SpaGrndCon(PassM0136h,i_Pass)
        
        table_iPass = Table(data_iPass, colWidths=[4.2*cm] * len(data_iPass[0]),rowHeights=(0.5*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.375*cm,0.25*cm))
        table_iPass.setStyle(ts_iPass)
        elems.append(table_iPass)
    
    pdf.build(elems)