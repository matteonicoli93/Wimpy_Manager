# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:47:19 2020

@author: Nicoli
"""
import datetime

#==============================================================================
def acq_GEMS_Info(GEMS_URL):
    def GEMS_value(str_text, indx_i):
        
        GEMS_F = GEMS_URL.find(indx_i)
        i_GEMS_F = GEMS_F
        flag_GEMS_F = 1
        while (flag_GEMS_F == 1 ):
            if ( GEMS_URL[ i_GEMS_F:i_GEMS_F+1] == '&' ):
                flag_GEMS_F = 0
                str_F = GEMS_URL[GEMS_F+len(indx_i):i_GEMS_F]        
            i_GEMS_F = i_GEMS_F + 1
        return str_F
    
    def GEMS_str2date(str_Date):
        Datestr_YYYY = 2000+int(str_Date[0:2])
        DOY = int(str_Date[3:6])
        mmDD = datetime.datetime(Datestr_YYYY, 1, 1) + datetime.timedelta(DOY - 1)
        Datestr_mm = mmDD.month
        Datestr_DD = mmDD.day
        Datestr_HH = int(str_Date[7:9])
        Datestr_MM = int(str_Date[10:12])
        Datestr_SS = int(str_Date[13:15])
        date = datetime.datetime(Datestr_YYYY, Datestr_mm, Datestr_DD, Datestr_HH, Datestr_MM, Datestr_SS, 0*1000)
        return date
    
    indx_ST = 'startTime='
    str_ST = GEMS_value(GEMS_URL, indx_ST)
    date_ST = GEMS_str2date(str_ST)
    
    indx_ET = 'endTime='
    str_ET = GEMS_value(GEMS_URL, indx_ET)
    date_ET = GEMS_str2date(str_ET)
    
    indx_F = 'facility='
    str_F = GEMS_value(GEMS_URL, indx_F)
    
    GEMS_info_list = [True,GEMS_URL,str_F,Sev,date_ST,date_ET,'']
    
    return GEMS_info_list
#end def
    
