from pipe import JSONPipe

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class automator(JSONPipe):
    '''Generate selenium scripts that automatically validate given exploits.
    '''

    def __init__(self):
        pass


    def process(self, incomings):
        '''Generate the selenium script here.

        `incomings[0]` is a list of exploits to be validated.

        return : a list of paths to the generated selenium scripts
        '''

        for exploit in incomings[0]:

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


        return ['data/scripts/exploit-1', 'data/scripts/exploit-2']
