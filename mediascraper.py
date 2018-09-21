import requests
import os
import platform


class CSVhandle:
    def __init__(self, userOS, userDistro, downloadDir, fileName, csvCol):
        self._userOS = userOS
        self._userDistro = userDistro
        self._downloadDir = downloadDir
        self._fileName = fileName
        self._csvCol = csvCol
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
    #downloadDir [Get]
    @property
    def downloadDir(self):
        return self._downloadDir
    #fileName [Get, Set]
    @property
    def fileName(self):
        return self._fileName
    @fileName.setter
    def setFileName(self, name):
        self._fileName = name
    #csvCol [Get, Set]
    @property
    def csvColName(self):
        return self._csvCol
    @csvCol.setter
    def setCSVCol(self, columns):
        self._csvCol = columns

    #Create a foler to store images in 
    def createFolder(self, downloadDir):
        #credit: keithwaver github
        try:
            if not os.path.exists(downloadDir):
                os.makedirs(downloadDir)
                #mkdir = single cell dir, makedirs = mutiple level 
        except OSERROR:
                print ('Error: Creating directory. ' + downloadDir)
        return

    def readCSV(self, downloadDir, fileName, csvCol):



ospath  = os.path.expanduser('~')
directory =  ospath + '/Desktop/TwitMediaTest/'
userOS = platform.system()
userDistro = platform.version()

csvfile = 'twitData.csv'
columns = [0,10,20]
    #UniqueID  
File = CSVhandle(userOS, userDistro, directory, csvfile)
