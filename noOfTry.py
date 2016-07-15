data_file=open('noOfTry.html','r')
data=data_file.read()
data_file.close()
data=data.split('\n')
total_number=[]
total_page=[]
for line in data:
	if '1-100' in line:
		line_data=line.split('>')
		total_number.append(line_data[1][9:18])
for item in total_number[0]:
	for letter in item:
		if letter!=',':
			total_page.append(letter)
print int(''.join(total_page))/100