import sys
from collections import OrderedDict


user_vector=sys.argv[1].split("_")
user_vector=list(map(int, user_vector))
tot_pref=sum(user_vector)
prs={}
for index in range(len(user_vector)):
	fin=open("./datasets/out_categ_"+str(index+1)+".txt",'r')
	user_preference=user_vector[index]
	prs[index+1]={}
	for line in fin:          #{1:{2:3},2:{3:2}}
		row=line.split(",")
		prs[index+1][int(row[0])]=user_preference/tot_pref*float(row[1])
final_pr={}
for movie_id  in prs[1]:
	movie_id=int(movie_id)
	final_pr[movie_id]=0
	for category in prs:
		final_pr[movie_id]+=prs[category][movie_id]
	items=[[b,a] for a,b in final_pr.items()]
	items.sort(reverse=True)
for elem in items:
	print(str(elem[1])+","+str(elem[0]))
	
	
		
