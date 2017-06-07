_author__ = "Chinmay Kumar Singh"
# Tis program finds number of right triangles, given a set of points in a 2d space. Time Complexity- O(n^2logn)


import math

def findRightTriangle(totalPoints):
    '''

    :param totalPoints:
    :return:
    '''
    counter=0
    for x,i in enumerate(totalPoints):
        for j in range(x+1,len(totalPoints)):
            for k in range(j+1,len(totalPoints)):
                l = math.sqrt(math.pow((totalPoints[j][1] - i[1]), 2) + math.pow((totalPoints[j][0] - i[0]), 2))
                w = math.sqrt(math.pow((totalPoints[k][1] - i[1]), 2) + math.pow((totalPoints[k][0] - i[0]), 2))
                h = math.sqrt(math.pow((totalPoints[k][1] - totalPoints[j][1]), 2) + math.pow((totalPoints[k][0] - totalPoints[j][0]), 2))
                if l>w and l>h:
                    hyp = round(math.pow(l,2))
                    base = round(math.pow(w,2))
                    height= round(math.pow(h,2))
                    if hyp == base + height:
                        counter+=1

                elif w>l and w>h:
                    hyp = round(math.pow(w, 2))
                    base = round(math.pow(l, 2))
                    height = round(math.pow(h, 2))
                    if hyp == base + height:
                        counter += 1
                else:
                    hyp = round(math.pow(h, 2))
                    base = round(math.pow(w, 2))
                    height = round(math.pow(l, 2))
                    if hyp == base + height:
                        counter += 1
    print(counter)

def findSlopeProductInBS(slopes, xaxis, yaxis):
    '''
    This method checks which particular slopes product= -1 and verifies if points are common then it comes
    to a decision which all points can form a right triangle.
    if product of two line's slope is -1 then they are perpendicular to each other and if they have a
    common point then they form a right angled triangle.
    :param slopes: list of slopes between two points
    :return: None
    '''
    count=0

    for i,x in enumerate(slopes):
        try:
            item= -1/x[0]
            first = i
            last = len(slopes)
            itemFound= True
            # Using binary search to find item
            while first <= last and itemFound :
                mid = (first + last)//2
                if slopes[mid][0] == item and (x[2] in slopes[mid] or x[1] in slopes[mid]) :
                    count += 1
                    w = mid - 1
                    y = mid + 1
                    # checking if multiple item is in list less than location of item
                    while slopes[w ][0] == item  :
                        if (x[2] in slopes[w] or x[1] in slopes[w]):
                            count += 1
                            w = w-1
                        else:
                            w = w-1
                    # checking if multiple item is in list greater than location of item
                    while slopes[y ][0] == item :
                        if (x[2] in slopes[y] or x[1] in slopes[y]):
                            count += 1
                            y = y + 1
                        else:
                            y = y+1
                    itemFound= False

                else:
                    if item < slopes[mid][0]:
                        last = mid - 1
                    else:
                        first = mid + 1
        except:
            pass

    # Handling exceptional cases when slope is either 0 or Not defined
    for z in xaxis:
        for w in yaxis:
            if z == w:
                count +=1


    print(count)



def findSlope(points):
    '''
        This method calculates slopes between two points selected and stores it in a list
        corresponding co ordinates are also stores so as to verify while counting triangles.
    :param points: list of points
    :return: Slopes,xaxis, yaxis: All are list containing slopes and its corresponding points.
                xaxis is list of points whose slope is not defined
                yaxis is list of points whose slope is 0.
    '''
    slopes=[]
    xaxis=[]
    yaxis=[]
    for i,x in enumerate(points):
        for j,y in enumerate(points[i+1:]):
            num=y[1] - x[1]
            den=y[0] - x[0]
            try:
                slope=num/den
                if slope == 0:
                    yaxis.append(x)
                    yaxis.append(y)
                else:
                    temp=[]
                    temp.append(slope)
                    temp.append(x)
                    temp.append(y)
                    slopes.append(temp)
            except:
                xaxis.append(x)
                xaxis.append(y)
                pass

    return slopes, xaxis, yaxis

def main():
    '''
    This method takes input from user and stores it in a list of points.
    :return: None
    '''

    noOfPoints=int(input())
    totalPoints=[]
    for i in range(noOfPoints):
        points=[int(n) for n in input().strip().split()]
        totalPoints.append(points)

    totalPoints.sort()
    slopes, xaxis, yaxis = findSlope(totalPoints)
    slopes.sort()
    findSlopeProductInBS(slopes, xaxis, yaxis)




if __name__ == '__main__':
    main()