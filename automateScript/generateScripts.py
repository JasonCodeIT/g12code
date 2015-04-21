import json
import time
import os
import random

#open json file

inputFileName = "../output/exploits/own-exploits.json"
scriptFolder = "scripts"+str(int(time.time()))
if not os.path.exists(scriptFolder):
    os.makedirs(scriptFolder)
scriptFileName = "scriptNames.txt"
scriptFile = open(os.path.join(scriptFolder,scriptFileName),'a')


with open(inputFileName) as inputFile:
	inputData = json.load(inputFile)

#extract data from json file
for exploit in inputData:
    scriptName = exploit["name"]
    if not scriptName:
        scriptName = str(int(time.time()+random.randrange(0,int(time.time()))))
    scriptName+=".py"
    scriptPath = os.path.join(scriptFolder,scriptName)
    script = open(scriptPath,"w+")

    script.write("from selenium import webdriver\n")
    script.write("from selenium.webdriver.common.keys import Keys\n\n")
    script.write("driver = webdriver.Firefox()\n\n")

    exploitSteps = exploit["exploit"]
    firstLink = True
    for step in exploitSteps:
        url = step["url"]
        formFields = step["formFields"]
        script.write("driver.get('"+url+"')\n\n")
        cookies = step["cookies"]
        if cookies:
            for key, value in cookies.items():
                cookieName = key
                cookieValue = cookies.get(key)
                script.write("driver.add_cookie({'name:':'"+cookieName+"','value':'"+cookieValue+"'})\n")
            script.write("driver.get('"+url+"')\n\n")
        if formFields:
            fieldName = ""
            fieldValue =""
            for key, value in formFields.items():
                fieldName = key
                fieldValue = formFields.get(key)
                script.write("driver.find_element_by_name('"+fieldName+"').send_keys('"+fieldValue+"')\n")
            script.write("driver.find_element_by_name('"+fieldName+"').send_keys(Keys.RETURN)\n\n")
        if (firstLink):
            scriptFile.write("url:"+url+" =>"+scriptName+"\n")
            firstLink = False
        fileFields = step["fileFields"]
        if fileFields:
            fileFieldName = ""
            filePath = ""
            for key, value in fileFields.items():
                fileFieldName = key
                filePath = fileFields.get(key)
                script.write("driver.find_element_by_name('"+fileFieldName+"').send_keys('"+filePath+"')\n")
            #under the assumption that we can only upload a single file before the page is forced to reload
            script.write("driver.find_element_by_name('"+fileFieldName+"').send_keys(Keys.RETURN)\n\n")

    script.close()

scriptFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
scriptFile.close()
