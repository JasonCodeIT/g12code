from pipe import JSONPipe


class factory(JSONPipe):
    '''Generate payload for injection to webpages under audit
    '''

    def __init__(self):
        pass


    def process(self, incomings):
        '''Just generate all possible payloads and return them in a list.
        Ignore the `incomings` parameter because there are no inputs.

        return : a list of payloads
        '''
        return ['../../../../../../etc/passwd']

