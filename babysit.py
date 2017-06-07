_author__ = "Chinmay Kumar Singh"
# Application of Weighted Interval Scheduling- Babysitting problem

from operator import itemgetter
totalProfit =[]

def findMaxEarning(noOfJobs,inp):
    '''
    This method calculates the maximum possible earning that both brother and sister can earn on a
    particular day. It uses concept of DP. 2d array depicts possible job which each can take.
    :param noOfJobs: count of number of jobs that are between 600 hours to 2300 hours
    :param inp: input list consisting of day, start time, end time, no of children and hourly wages
    :return: None
    '''
    jobs = []
    backup =[]
    # Sort the list by end time
    inp.sort(key=itemgetter(2))
    zeroJob = [[0, 0, 0, 0, 0]]
    inp[:0] = zeroJob


    V=[]
    P = []
    #V.append(0)
    # wage/ value list V(j)
    for o in inp:
        V.append(((o[2] - o[1])/100)*o[4])

    # filling up scheduling list P(j)
    for _ in range(len(inp)):
        P.append(0)

    # calculating P table which depicts maximum ith job which ends before job i.
    for i in range(len(inp) -1,-1,-1):
        for j in range(i - 1,-1,-1):
             if inp[i][1] >= inp[j][2]:
                P[i] = j
                break

    #print(P)


    # innitializing a 2d array
    S=[[0 for _ in range(len(inp)  )] for _ in range(len(inp) )]

    for j in range(0, len(inp) ):
        for k in range(0, len(inp) ):
            if k == 0 and j == 0 :
                continue
            # jobs on the diagnol can be taken by both if saisfying the condition
            if j == k :
                if inp[j][3] >= 4:
                    S[j][k] = max(V[j] + S[P[j]][P[j]], S[j-1][j-1])
                else:
                    S[j][k] = max(V[j] + S[P[j]][k - 1], S[j-1][k-1])
            # j element will pick this job and k will traverse back to a previous job
            elif j > k:
                if inp[j][3] < 4:
                    S[j][k] = max(V[j] + S[P[j]][k], S[j-1][k])
                elif inp[j][3] >= 4:
                    S[j][k] = S[j-1][k]
            # k element will pick this job and j will traverse back to a previous job
            elif j < k:
                if inp[k][3] < 4:
                    S[j][k] = max(V[k] + S[j][P[k]], S[j][k-1])
                elif inp[k][3] >= 4:
                    S[j][k] = S[j][k-1]
    # maximum possible earning on a particular day
    maxi = S[len(inp) -1][len(inp)- 1]


    global totalProfit
    totalProfit.append(maxi)






def main():
    '''

    :return:
    '''
    noOfJobs = int(input())
    inp = []
    # Storing input
    for i in range(noOfJobs):
        t=[]
        temp=[]
        t=input().strip().split()
        for i in t:
            temp.append(int(i))
        if temp[1] >=600 and temp[2] <= 2300:
            inp.append(temp)
        else:
            pass

    # Sort the list by day
    #noOfJobs = noOfJobs - len(inp)
    inp.sort()
    #print(inp)
    x=0
    # Breaking input list by day wise
    for i in range(len(inp) - 1):
        if inp[i][0] <inp[i + 1][0]:
            li = inp[x:i+1]
            if len(li) <2:
                global totalProfit
                ma = ((li[2] - li[1]) / 100) * li[4]
                totalProfit.append(ma)
            else:
                findMaxEarning(noOfJobs, li)
            x = i

    if i == len(inp) - 2:
        findMaxEarning(noOfJobs, inp)

    sum =0
    # Sum will store maximum earnings that can be earned on a given dates.
    global totalProfit
    for i in totalProfit:
        sum += i

    print(int(sum))


if __name__ == '__main__':
    main()
