import os
import csv




def Search(alist, item):
	if item not in alist:
		#print(item)
		#print("Non e presente")
		return 1
	else:
		return 0
		
	
	

def check_start(file1,file2 ):
	fin1=open(file1, 'r')
	fin2=open(file2,'r')
	
	
	print("check query_id between " +fin1.name +" and " + fin2.name + "\n\n" )
	q1=[]
	q2=[]
	count=0
	for line in fin1:
		raw=line.split(",")
		raw[0]=int(raw[0])
		raw[1]=round(float(raw[1]),4)
		q1.append(raw)
	fin1.close()
	
	for line in fin2:
		raw=line.split(",")
		raw[0]=int(raw[0])
		raw[1]=round(float(raw[1]),4)
		q2.append(raw)
	fin2.close()
	
	lenq1=len(q1)
	lenq2=len(q2)
	
	listshorter=[]
	listlonger=[]
	print(q1==q2)
	
	if(lenq1 > lenq2):
		print("il secondo file è più piccolo")
		listshorter=q2
		listlonger=q1
		
		
	elif(lenq1 < lenq2):
		print("il primo file è più piccolo")
		listshorter=q1
		listlonger=q2
	else:
		print("sono uguali inizio dal primo al secondo...")
		listshorter=q1
		listlonger=q2
		
		
	
	
	
	
	print("dal file piu piccolo al piu grande")
	count=0
	for elem in listshorter:
		count+=Search(listlonger,elem)
	print(count)
	count=0
	print("dal file piu grande al piu piccolo")
	for elem in listlonger:
		count+=Search(listshorter,elem)
	print(count)
		
		
	
			
			
		
	
	
check_start("/home/daemonn/Desktop/Uni/WIR/hw2/fin_out.txt","/home/daemonn/Desktop/Uni/WIR/hw2/parte3.txt")
			
			
		
	
