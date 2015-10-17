
# #check if snap is working fine on the machine
# status = False
# try:
# 	import snap
# 	version = snap.Version
# 	i = snap.TInt(5)
# 	if i == 5:
# 		status = True
# except:
# 	pass

# if status:
# 	print "snap is working properly on this computer"
# else:
# 	print "Unfortunately the snap is not working properly on this computer"

from snap import *

def intro():

	#create a graph PNGraph
	G1 = TNGraph.New()
	G1.AddNode(1)
	G1.AddNode(5)
	G1.AddNode(32)
	G1.AddEdge(1,5)
	G1.AddEdge(5,1)
	G1.AddEdge(5,32)

	print "G1 Nodes: %d ,Edges : %d" %(G1.GetNodes(),G1.GetEdges())

	#created a random directed graph on 100 nodes and 1000 edges
	G2 = GenRndGnm(PNGraph,100,1000)
	print "G2 Nodes: %d ,Edges : %d" %(G2.GetNodes(),G2.GetEdges())	


if __name__ == '__main__':
	intro()


