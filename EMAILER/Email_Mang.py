# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:33:52 2020

@author: matte
"""

import win32com.client as win32
import os


def Emailer(text, subject, From, recipient, CC):
    outlook = win32.Dispatch('outlook.application')
    
    emialfrom = outlook.Session.Accounts[From]
    
    mail = outlook.CreateItem(0)
    mail.To = recipient
    if ( len(CC) != 0 ):
        mail.CC = CC
    mail.Subject = subject
    #mail.HtmlBody = text
    message = text
    mail.GetInspector 

    index = mail.HTMLbody.find('>', mail.HTMLbody.find('<body'))
    mail.HTMLbody = mail.HTMLbody[:index + 1] + message + mail.HTMLbody[index + 1:]
    ###

# =============================================================================
#     attachment1 = os.getcwd() +"\\file.ini"
#     mail.Attachments.Add(attachment1)
# =============================================================================

    ###
    mail._oleobj_.Invoke(*(64209, 0, 8, 0, emialfrom))
    mail.Display()
#end def



MailSubject= "Auto test mail"

html_SE = '<p>'
html_SE = ''
heading = 'Dear all,<br><br>Today, DOY 000, we received the following alarm:'
MailInput=html_SE + heading + html_SE

MailFrom   = "matteo.nicoli@outlook.com"
MailAdress = "matteo.nicoli.17@gmail.com;matteo.nicoli.17@gmail.com"
#MailAdress = "matteo.nicoli.17@gmail.com"
MailCC     = MailAdress

Emailer(MailInput, MailSubject, MailFrom, MailAdress, MailCC) #that open a new outlook mail even outlook closed.

