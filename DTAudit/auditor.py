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
        return incomings[0]

