_author__ = "Chinmay Kumar Singh"
# Application of Max flow and bipartite graph algorithm. to find maximum pairs of black and white on a chessboard

def checkingBipartiteness(cboard_dict,nwhites,nblacks):
    '''
    This method checks for maximum pair obtained from bipartite graph- cboard_dict
    :param cboard_dict: python dictionary conataing structure of chessboard
    :param nwhites: number of whites in the chessboard
    :param nblacks: number of blacks in the chessboard
    :return:None
    '''
    visited=[]
    paired =0
    for key,value in cboard_dict.items():
        # Pairing whites and blacks one to one.
        while len(value) >0:
            x = value.pop(0)
            if x in visited:
                continue
            else:
                visited.append(x)
                paired +=1
                break

    if paired == nwhites:
        fl="YES"
        # Checking if any blakes are left un paired in the graph
        for k,v in cboard_dict.items():
            for val in v:
                if val in visited:
                    flag = "Yes"
                    continue
                else:
                    fl = "NO"
                    #print("NO")
                    break
        if flag == "Yes" and fl != "NO":
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

def main():
    '''
        This method takes input from console. Creates a dictionary containing the graph structure.
        Creates neighbors of the all the nodes.

    :return: None
    '''
    totalElement = input().split(" ")
    nrows = int(totalElement[0])
    ncols = int(totalElement[1])

    cboard = []
    for _ in range(nrows):
        row = input().split(" ")
        # Converting to int from strings
        for b,c in enumerate(row):
            row[b] = int(c)
        cboard.append(row)

    cboard_dict = {}
    oddEven = 0
    EvenOdd = 1
    nblacks, nwhites = 0,0
    # creating a bipartite graph using dictionary.
    for idx, i in enumerate(cboard):
        #EvenOdd += 1
        #if EvenOdd %2 == 0:
            #oddEven =0
        #else:
            #oddEven =1
        for index,j in enumerate(i):
            # Assuming board starts from white
            if oddEven % 2 == 0:
                # Ignoring already filled spaces
                if j == 1:
                    oddEven += 1
                else:
                    if idx == 0:
                        # Top left element of matrix
                        if index == 0:
                            li = []
                            if cboard[idx][index+1] == 0:
                                li.append(idx*ncols + (index+1))
                                #print(li)
                            if cboard[idx + 1][index] == 0:
                                li.append((idx+1)*ncols + index)
                            cboard_dict[idx*ncols + index] = li
                        # Top right element of matrix
                        elif index == ncols-1 :
                            li = []
                            if cboard[idx][index-1] == 0:
                                li.append(idx * ncols + (index - 1))
                            if cboard[idx+1][index] == 0:
                                li.append((idx + 1) * ncols + index)
                            cboard_dict[idx * ncols + index] = li
                        # Elements in matrix in between corner nodes
                        else:
                            li = []
                            if cboard[idx][index + 1] == 0:
                                li.append(idx * ncols + (index + 1))
                            if cboard[idx][index - 1] == 0:
                                li.append(idx * ncols + (index - 1))
                            if cboard[idx + 1][index] == 0:
                                li.append((idx + 1) * ncols + index)
                            cboard_dict[idx * ncols + index] = li
                    # Bottom left element of matrix
                    elif idx == nrows-1:
                        if index == 0:
                            li = []
                            if cboard[idx][index + 1] == 0:
                                li.append(idx * ncols + (index + 1))
                                #print(li)
                            if cboard[idx - 1][index] == 0:
                                li.append((idx - 1) * ncols + index)
                            cboard_dict[idx * ncols + index] = li
                        # Bottom right element of matrix.
                        elif index == ncols -1 :
                            li = []
                            if cboard[idx][index - 1] == 0:
                                li.append(idx * ncols + (index - 1))
                            if cboard[idx - 1][index] == 0:
                                li.append((idx - 1) * ncols + idx)
                            cboard_dict[idx * ncols + index] = li
                        # Elements in matrix between the corners
                        else:
                            li = []
                            if cboard[idx][index - 1] == 0:
                                li.append(idx * ncols + (index - 1))
                            if cboard[idx - 1][index] == 0:
                                li.append((idx - 1) * ncols + index)
                            if cboard[idx][index + 1] == 0:
                                li.append(idx * ncols + (index + 1))
                            cboard_dict[idx * ncols + index] = li
                    # All elements except top and bottom row
                    else:
                        # Elements at first row
                        if index == 0:
                            li = []
                            if cboard[idx - 1][index] == 0:
                                li.append((idx - 1) * ncols + index)
                            if cboard[idx][index + 1] == 0:
                                li.append(idx * ncols + (index + 1))
                            if cboard[idx + 1][index] == 0:
                                li.append((idx + 1) * ncols + index)

                            cboard_dict[idx * ncols + index] = li
                        # Elements at right most corners
                        elif index == ncols - 1 :
                            li = []
                            if cboard[idx - 1][index] == 0:
                                li.append((idx - 1) * ncols + index)
                            if cboard[idx][index - 1] == 0:
                                li.append(idx * ncols + (index - 1))

                            if cboard[idx + 1][index] == 0:
                                li.append((idx + 1) * ncols + index)

                            cboard_dict[idx * ncols + index] = li
                        # Elements in centre
                        else:
                            li = []
                            if cboard[idx - 1][index] == 0:
                                li.append((idx - 1) * ncols + index)
                            if cboard[idx][index - 1] == 0:
                                li.append(idx * ncols + (index - 1))
                            if cboard[idx][index + 1] == 0:
                                li.append(idx * ncols + (index + 1))
                            if cboard[idx + 1][index] == 0:
                                li.append((idx + 1) * ncols + index)

                            cboard_dict[idx * ncols + index] = li
                    nwhites += 1
                    oddEven += 1
            # Incrementing the count of Blake
            else:
                if j == 1:
                    oddEven += 1
                else:
                    nblacks += 1
                    oddEven += 1


    #print(cboard_dict)
    #print(nwhites,nblacks)
    checkingBipartiteness(cboard_dict,nwhites,nblacks)



if __name__ == '__main__':
    main()