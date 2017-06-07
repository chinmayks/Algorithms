_author__ = "Chinmay Kumar Singh"
# Implementation of Kruskal's Algorithm using union find data structure method.

from operator import itemgetter


def setsUnion(u,v):
    '''
    A helper function of unionOfEdges.
    :param u: vertex 1
    :param v: vertex 2
    :return: a set after combining component1 and component2.
    '''

    if isinstance(u,int):
        if isinstance(v,int):
            temp = []
            temp.append(u)
            temp.append(v)
            #print(temp)
            return temp
        else:
            temp = []
            temp.append(u)
            temp.extend(v)
            #print(temp)
            return temp
    else:
        if isinstance(v,list):
            for vj in v:
                u.append(vj)
        else:
            u.append(v)
        #print(u)
        return u





def unionOfEdges(u,v,boss,size,set):
    '''
    This method combines vertices if they belong to different components.
    after union it increases size, and clubs them into a set.
    :param u: vertex1
    :param v: vertex 2
    :param boss: an array containing boss/parent of each vertices.
    :param size: an array with default size 1 for each node and increases gradually.
    :param set: set of vertices that have same boss/parent
    :return: boss, set, size arrays.
    '''
    if size[boss[u]] >= size[boss[v]]:

        #print(set[boss[u]], set[boss[v]])

        set[boss[u]] = setsUnion(set[boss[u]], set[boss[v]])
        size[boss[u]] += size[boss[v]]
        if size[boss[v]] >1:
            for z in set[boss[v]]:
                #print(set[boss[v]])
                boss[z] = boss[u]
        else:
            boss[v] = boss[u]

    else:
        set[boss[v]] = setsUnion(set[boss[v]], set[boss[u]])
        size[boss[v]] += size[boss[u]]
        if size[boss[u]] > 1:
            #print(set[boss[u]])
            for z in set[boss[u]]:
                #print(z)
                boss[z] = boss[v]
        else:
            boss[u] = boss[v]

    return boss , size, set

def find(u, boss):
    '''

    :param u:
    :return:
    '''
    return boss[u]


def minSpanningTree(graphObj, edges):
    '''
    This method is an implementation of finding min spanning tree by using Kruskal's Algorithm
    :param graphObj: List of list containing edges,weight and flag
    :return: Minimum weight to create s MST
    '''

    boss = [0 for _ in range(edges)]
    set =  [0 for _ in range(edges)]
    size = [0 for _ in range(edges)]
    T = []
    weight = 0
    for i in graphObj:
        boss[i[0]], boss[i[1]] = i[0], i[1]
        set[i[0]], set[i[1]] = i[0], i[1]
        size[i[0]], size[i[1]] = 1, 1
    #print(set[97])
    # To check for flag status 'F', if F then include that edge and check whether it creates a cycle or not.
    for x in graphObj:
        if x[3] == 1:
            if find(x[0], boss) != find(x[1], boss):
                t = []
                t.append(x[0])
                t.append(x[1])
                T.append(t)
                boss, size, set = unionOfEdges(x[0], x[1], boss, size, set)
                weight += x[2]
            else:
                return -1
    # It finds MST for all edges other that with flag status.
    for j in graphObj:
        if j[3] != 1:
            if find(j[0], boss) != find(j[1],boss):
                t=[]
                t.append(j[0])
                t.append(j[1])
                T.append(t)
                boss , size, set = unionOfEdges(j[0], j[1], boss, size, set)
                weight += j[2]

    # checking for connected components
    for ind in range(0, len(boss) -1):
        if boss[ind] != boss[ind + 1]:
            return -1


    return weight




def main():
    '''
    Implementation of Kruskal's Algorithm
    :return: None
    '''
    edges = []
    edges = input().split(" ")
    graphObj =[]



    for _ in range(int(edges[1])):
        gr = input().split(" ")
        for j,x in enumerate(gr):
            gr[j] = int(x)
        graphObj.append(gr)
    # Sorting graph list in order of weight
    graphObj.sort(key= itemgetter(2))

    wt = minSpanningTree(graphObj, int(edges[0]))
    print(wt)


if __name__ == '__main__':
    main()