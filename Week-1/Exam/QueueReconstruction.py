def queueReconstruction(people_list):
    people_list=sorted(people_list)
    people_list.reverse()
    for i in range(len(people_list)-1):
        if(people_list[i][0]==people_list[i+1][0]):
            if(people_list[i][1]>people_list[i+1][1]):
                people_list[i],people_list[i+1]=people_list[i+1],people_list[i]
                i=0
    # print (people_list)
    result = []
    for people in people_list:
        result.insert(people[1], people)
        # print(result)
    return result
    pass

print (queueReconstruction([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
print(queueReconstruction([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]))
print(queueReconstruction([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]))