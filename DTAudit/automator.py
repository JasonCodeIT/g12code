from pipe import JSONPipe


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
        return ['data/scripts/exploit-1', 'data/scripts/exploit-2']

