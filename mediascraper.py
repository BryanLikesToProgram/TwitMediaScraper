import requests
import os
import platform
import time
import csv

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
    def csvCol(self):
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
                print ("Directory Created: " + downloadDir)
        except OSError:
                print ('Error: Creating directory. ' + downloadDir)
        return

    def readCSV(self, downloadDir, fileName, csvCol):
        lineNum = 0
        nameList = [""]
        urlList = [""]
        with open('twitData.csv', newline='', encoding='utf8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                if lineNum > 0:
                    #            = Unique ID_TwitterHandle
                    nameList.append(row[csvCol[0]]+"_"+row[csvCol[1]]+".jpg")
                    urlList.append(row[csvCol[2]])
                else:
                    print("Reading from CSV: "+str(row[csvCol[0]])+" "+str(row[csvCol[1]])+" "+str(row[csvCol[2]]))
                lineNum = lineNum + 1
        return nameList, urlList

def downloadJPG(directory, nameList, urlList):
    index = 1;
    for name in nameList[index:]:
        r = requests.get( urlList[index])
        print(directory+name)
        open(directory+name, 'wb').write(r.content)
        print("Downloaded jpg:"+name)
        index = index + 1
    return

ospath  = os.path.expanduser('~')
directory =  ospath + '/Desktop/TwitMediaTest/'
userOS = platform.system()
userDistro = platform.version()

csvfile = 'twitData.csv'
columns = [0,10,20]
    #UniqueID  TwitterHandle ImageURL
csvnameList= [""]
csvurlList = [""]
fileObj = CSVhandle(userOS, userDistro, directory, csvfile, columns)
fileObj.createFolder(fileObj.downloadDir) 
csvnameList, csvurlList = fileObj.readCSV(fileObj.downloadDir, fileObj.fileName, fileObj.csvCol)

downloadJPG(directory, csvnameList, csvurlList)










