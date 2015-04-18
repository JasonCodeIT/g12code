import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open json file

inputFileName = "exploitData.json"

with open(inputFileName) as inputFile:
	inputData = json.load(inputFile)

#extract data from json file
exploits = inputData['exploits']
for exploit in exploits:

    url = exploit["url"]
    loginCredentials = exploit["loginCredentials"]
    credentialsFields = exploit["credentialFields"]
    exploitUrl =exploit["exploiturl"]


    for cred in loginCredentials:
        username = cred['username']
        password = cred['password']

    for field in credentialsFields:
        usernameBox = field['usernameBox']
        passwordBox = field['passwordBox']

    print("url: "+url)
    print("exploitUrl: "+exploitUrl)
    print("username: "+username)
    print("usernameBox: "+usernameBox)
    print("password:" +password)
    print("passwordBox:"+passwordBox)


    #opening web browser using selenium
    driver = webdriver.Firefox()
    driver.get(url)

    #login into webpage if needed
    #temporary assuming that we find element by name
    if username != "":
        usernameField = driver.find_element_by_name(usernameBox)
        passwordField = driver.find_element_by_name(passwordBox)
        usernameField.send_keys(username)
        passwordField.send_keys(password)
        usernameField.send_keys(Keys.RETURN)



    ##################################################
    ########### ensure that we are login #############
    ##################################################

    #input attack data
    driver.get(exploitUrl)

    ####################################################
    ######## verify if attack is successful ############
    ####################################################

