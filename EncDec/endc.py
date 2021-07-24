def enc():
	mess=input('Enter text to be encrypted:\n')
	code = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
	key=7
	en = ''
	res=''
	for i in mess:
		pos = code.find(i)
		newpos = (pos+key)%52
		res += code[newpos]
	print('\nEncrypted code:',res)


def dec():
	mess=input('Enter text to be decrypted:\n')
	code = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
	key=7
	en = ''
	res=''
	for i in mess:
		pos = code.find(i)
		newpos = (pos-key)%52
		res += code[newpos]
	print('\nDecrypted code:',res)




	
if __name__ == '__main__':
	
		s = int(input('Enter mode: \n1. Encrypt \n2. Decrypt\n'))
		if s==1:
			enc()
		elif s==2:
			dec()
		else:
			print(' Invalid input')

