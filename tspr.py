import csv
import pprint as pp
import networkx as nx


alpha = .15
epsilon = 10**-6



def create_initial_pagerank_vector(graph):
	page_rank_vector = {}
	num_nodes = graph.number_of_nodes()
	default_pageRank_value = 1./num_nodes
	
	for node_id in range(1, num_nodes+1):
		page_rank_vector[node_id] = default_pageRank_value
		
	return page_rank_vector





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
		
		






def get_distance(vector_1, vector_2):
	distance = 0.
	
	for node_id in vector_1.keys():
		distance += abs(vector_1[node_id] - vector_2[node_id])
	return distance





def start(input_graph_weighted_adjacency_list_file_name,topic):
	g = nx.Graph()
	input_file = open(input_graph_weighted_adjacency_list_file_name, 'r')
	input_file_csv_reader = csv.reader(input_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
	
	for elem in input_file_csv_reader:
		g.add_edge(int(elem[0]),int(elem[1]),weight = float(elem[2]))
	input_file.close()

	previous_page_rank_vector = create_initial_pagerank_vector(g)
	page_rank_vector = {}
	num_iterations = 0
	while True:
	
	#pp.pprint(previous_page_rank_vector)
		page_rank_vector = single_iteration_page_rank(g, previous_page_rank_vector, alpha,topic)
		num_iterations += 1
		#print(num_iterations)
		distance = get_distance(previous_page_rank_vector, page_rank_vector)
	
	#print(" iteration number " + str(num_iterations))
	#print(" distance= " + str(distance))
	# check convergency
		if distance <= epsilon:
			#print(" Convergence!")
			return page_rank_vector
		#print(distance)
	
		previous_page_rank_vector = page_rank_vector
	
	#pp.pprint(page_rank_vector)
	
	
	### Useful code for debugging ;)
	'''
	print("")
	print( "start PR")
	damping_factor = 1. - alpha
	pr = nx.pagerank(g, alpha=alpha, tol=epsilon)
	print ("end PR")
	pp.pprint(pr)
	print("")
	distance = get_distance(page_rank_vector, pr)
	print (" distance(just_implemented_pr, NetworkX_pr)= " + str(distance))
	print("")
	
	
	
	'''
	'''
	from networkx import nx 
	>>> DG = nx.DiGraph()
	>>> DG.add_weighted_edges_from([("A", "B", 50),("B", "A",1)])25
	>>> pr = nx.pagerank(DG)
	>>> pr
	{'A': 0.5, 'B': 0.5}
	
	'''
























