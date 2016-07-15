from os import listdir
from os.path import isfile, join
working_dir='D://auto//dodge//company'
onlyfiles=[f for f in listdir(working_dir) if isfile(join(working_dir,f))]
files_to_join=[]

for file in onlyfiles:
	if 'Companies' in file:
		files_to_join.append(file)
final_file=open(working_dir+'//Companies_final.csv','w')
print files_to_join[:3]
#heading of the excel file
data_file=open(working_dir+'//'+files_to_join[0],'r')
data=data_file.read()
data_file.close()
data=data.split('\n')
final_file.write(data[0]+'\n')
#print len(files_to_join)
for file in files_to_join:
	data_file=open(working_dir+'//'+file,'r')
	data=data_file.read()
	data_file.close()
	data=data.split('\n')
	#print data[-3:]
	for items in data[1:-2]:
		final_file.write(items+'\n')
final_file.close()