'''
1)computare il  topic specific page rank per ogni categoria che viene rappresentata dalla riga del file di input 5 righe 5 categorie
1.1)ogni movie di una categoria ha peso 1 riusare il topic fatto nel 2
2)salvarli su un file per la parte online


'''
import sys
import csv
from WebIR_HW_2_part_2 import tspr
from collections import OrderedDict


if(len(sys.argv) == 3):
	input_categ_movies=open(sys.argv[2],'r')
	csv_reader_categ_movie=csv.reader(input_categ_movies,delimiter='\t', quotechar='"',quoting=csv.QUOTE_NONE)
	
	#we now create a dictionary with keys as category_id and as values a movie_ids' list
	diz={}
	count=1
	for row in csv_reader_categ_movie:
		diz[count]=[]
		for index in range(len(row)):
			diz[count].append(int(row[index]))
		count+=1
	input_categ_movies.close()
		
	
	#for each category we have to compute the tspr then we have to store output into the directory datasets
	count=1
	rate=1 #we assume that for each category the movie rate is unitary
	for categories in diz:
		movies_id=diz[categories]
		topic={}
		tot=len(movies_id)
		
		for movie_id in movies_id:
			topic[movie_id]=rate/tot
		pr=tspr(sys.argv[1],topic)
		#before to store this page rank we have to sort its for movie_id in order to simplify the next step
		OrderedDict(sorted(pr.items(), key=lambda t: t[0]))
		fout=open("./datasets/out_categ_"+str(count)+".txt",'w')
		for elem in pr:
			fout.write(str(elem)+","+str(pr[elem])+"\n")
		fout.close()
		count+=1
else:
	print("usage: prog movie-graph.txt category_movies.txt");
	
	
		
		
	
	
	
		
	
	
