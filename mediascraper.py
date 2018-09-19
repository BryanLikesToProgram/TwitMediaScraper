from selenium import webdriver
import time
import math
import os
import platform
from math import ceil

class Webscraper:

    def __init__(self, siteAddress):
        self._siteAddress = siteAddress
    return

    #Getters & Setters
    #siteAddress [Get, Set]
    @property
    def siteAddress(self):
        return self._siteAddress
    @siteAddress.setter
    def setSiteAddress(self, site):
        self._siteAddress = site
   
    def loadPage():
    return
def scrapeCSV():
return
def downloadJPG():
return

class Filehandle:
    def __init__(self, userOS, userDistro, desktopDir):
        self._userOS = userOS
        self._userDistro = userDistro
        self._siteAddress = siteAddress
    return

    #Getters & Setters
    #userOS [Get]
    @property
    def userOs(self):
        return self._userOS
    #userDistro [Get]
    @property
    def userDistro(self):
        return self._userDistro
    #desktopDir [Get]
    @property
    def desktopDir(self):
        return self._desktopDir

    def createFolder(self, directory):
        #credit: keithwaver github
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                #mkdir = single cell dir, makedirs = mutiple level 
        except OSERROR:
                print ('Error: Creating directory. ' + directory)
        return

driver = webdriver.Safari()
ospath  = os.path.expanduser('~')
directory =  ospath + '/Desktop/TwitMediaTest/'

Page  = Webscraper('https://ukjobs.uky.edu/hr/login')
Page.loadPage()
File = Filehandle(directory, None, None)
