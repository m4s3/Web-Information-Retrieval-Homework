import sys
import csv
import tspr



input_graph_weighted_adjacency_list_file_name = sys.argv[1]
input_movie_rating=open(sys.argv[2],'r')
csv_reader_user_movie=csv.reader(input_movie_rating,delimiter='\t', quotechar='"',quoting=csv.QUOTE_NONE)

if(len(sys.argv) == 4):
	
	#print("this is an user's topic") 
	user_id=int(sys.argv[3])
	user_topic={}
	tot=0.0
	
	for elem in csv_reader_user_movie:
		user_id_tmp=int(elem[0])
		
		if(user_id_tmp == user_id):
			rate=float(elem[2])
			tot+=rate
			user_topic[int(elem[1])]=rate
			
		elif(user_id_tmp > user_id):
			break
			
	input_movie_rating.close()
			
	if(user_topic != {}):
		
		for key in user_topic.keys():
			user_topic[key]/=tot
			
		pr=tspr.start(input_graph_weighted_adjacency_list_file_name,user_topic)
		items=[[b,a] for a,b in pr.items()]
		items.sort(reverse=True)
		
		for elem in items:
			if(elem[1] not in user_topic):
				print(str(elem[1])+","+str(elem[0]))


	else:
		print("this user didn't rate any movies")
		
else: 
	#print("this is a simple topic")
	topic={}
	tot=0.
	
	for elem in csv_reader_user_movie:
		rate=float(elem[1])
		topic[int(elem[0])]=rate
		tot+=rate
		
	input_movie_rating.close()
	
	for key in topic.keys():
		topic[key]/=tot
		
	pr=tspr.start(input_graph_weighted_adjacency_list_file_name,topic)
	items=[[b,a] for a,b in pr.items()]
	items.sort(reverse=True)
	
	for elem in items:
		if (elem[1] not in topic):
			print(str(elem[1])+","+str(elem[0]))


	
	
	


		
		


