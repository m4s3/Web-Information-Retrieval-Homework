import sys
import csv
import pprint as pp
import networkx as nx


alpha = .15
epsilon = 10**-6


########################################################################

def create_initial_pagerank_vector(graph,topic,len_topic):
	page_rank_vector = {}
	default_pageRank_value = 1./len_topic
	num_nodes=graph.number_of_nodes()
	
	for node_id in range(1, num_nodes+1):
		#page_rank_vector[node_id] = 1/num_nodes this line was used for the implementation without topic
		if(node_id in topic):
			page_rank_vector[node_id] = default_pageRank_value
		else:
			page_rank_vector[node_id] = 0.
		
	return page_rank_vector
########################################################################



########################################################################

def single_iteration_page_rank(graph, page_rank_vector, alpha,topic):
	next_page_rank_vector = {}
	sum_of_all_partial_pr_values = 0.
	
	for node_j in graph.nodes():
		next_page_rank_vector[node_j] = 0.
		
	for node_j in graph.nodes():
		tot_weight_j=0.
		
		for node_i in graph.neighbors(node_j):
			tot_weight_j+=graph[node_j][node_i]['weight']
			
		for node_i in graph.neighbors(node_j):
			next_page_rank_vector[node_i] += (1. - alpha) * graph[node_j][node_i]['weight'] * page_rank_vector[node_j] /  tot_weight_j
	
	sum_of_all_partial_pr_values=sum(next_page_rank_vector.values())

	leaked_pr = 1. - sum_of_all_partial_pr_values
	
	if(topic == {}):
		num_nodes = graph.number_of_nodes()
		fraction_of_leaked_pr_to_give_to_each_node = leaked_pr / num_nodes
		
		for node_j in next_page_rank_vector:
			next_page_rank_vector[node_j] = next_page_rank_vector[node_j] + fraction_of_leaked_pr_to_give_to_each_node
	else:
		for node_j in topic:
			next_page_rank_vector[node_j]+= leaked_pr * topic[node_j]

	return next_page_rank_vector
		
########################################################################		





########################################################################

def get_distance(vector_1, vector_2):
	distance = 0.
	
	for node_id in vector_1.keys():
		distance += abs(vector_1[node_id] - vector_2[node_id])
	return distance
	
########################################################################



########################################################################

def tspr(input_graph_weighted_adjacency_list_file_name,topic):
	g = nx.Graph()
	input_file = open(input_graph_weighted_adjacency_list_file_name, 'r')
	input_file_csv_reader = csv.reader(input_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
	
	for elem in input_file_csv_reader:
		g.add_edge(int(elem[0]),int(elem[1]),weight = float(elem[2]))
	input_file.close()
	card_topic=len(topic.keys())
	previous_page_rank_vector = create_initial_pagerank_vector(g,topic,card_topic)
	page_rank_vector = {}
	num_iterations = 0
	while True:
		page_rank_vector = single_iteration_page_rank(g, previous_page_rank_vector, alpha,topic)
		num_iterations += 1
		distance = get_distance(previous_page_rank_vector, page_rank_vector)
	
		if distance <= epsilon:
			return page_rank_vector
		
	
		previous_page_rank_vector = page_rank_vector
		
########################################################################
	
	
########################################################################
	
if(len(sys.argv)==4):

	input_graph_weighted_adjacency_list_file_name = sys.argv[1]
	input_movie_rating=open(sys.argv[2],'r')
	csv_reader_user_movie=csv.reader(input_movie_rating,delimiter='\t', quotechar='"',quoting=csv.QUOTE_NONE)
	 
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
	for key in user_topic.keys():
		user_topic[key]/=tot
			
	pr=tspr(input_graph_weighted_adjacency_list_file_name,user_topic)
	items=[[b,a] for a,b in pr.items()]
	items.sort(reverse=True)
			
	for elem in items:
		if(elem[1] not in user_topic):
			print(str(elem[1])+","+str(elem[0]))

########################################################################
