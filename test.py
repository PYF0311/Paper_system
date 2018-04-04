import forms

def operation(result):
	editor=''
	for i in range(1,3):
		if result[i] is not None:
			editor=editor+" "+str(result[i])
	papername=result[4]
	pubname=result[5]
	year=result[6].year
	issue=result[7]
	page=result[8]
	printstr=editor+"."+papername+"[J]"+"."+pubname+","+str(year)+",("+issue+"):"+page
	return (printstr)

if __name__ == '__main__':
	result=forms.all_paper_from_db()
	for i in range (len(result)):
		result1=operation(result[i])
		with open('testapp.txt', 'a+') as f:
			f.write(result1+"\n")


