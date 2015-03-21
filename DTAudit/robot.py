from pipe import JSONPipe


class robot(JSONPipe):
    '''A robot that crawls the website given a set of seed URLs.
    '''

    def __init__(self):
        pass


    def process(self, incomings):
        '''Crawl the website with given seed URLs in `incomings[0]`

        `incomings[0]` is a list of URLs

        return : a list of endpoints, each endpoint should have the following format
            {
                'url'    : 'http://url.to.a.page',
                'points' : [
                    {
                        'type' : 'GET',
                        'param' : 'bar'
                    },
                    {
                        'type' : 'Header',
                        'param' : 'X-Requested-By'
                    }
                ],
                'extras' : [
                    'auth' : {
                        'url' : 'http://login.page.url',
                        'method' : 'POST',
                        'action' : 'http://action.page.url',
                        'formField1' : 'value1',
                        'formField2' : 'value2'
                    },
                    'headers' : {
                        'X-Foo' : 'foo',
                        'X-Bar' : 'bar'
                    }
                ]
            }
        '''
        return incomings[0]
