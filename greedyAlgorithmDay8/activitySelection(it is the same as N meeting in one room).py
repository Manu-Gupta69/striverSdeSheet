def maximumMeetings(self,n,start,end):
    ds = []
    for i in range(n):
        ds.append([end[i],start[i]])
    ds.sort(key = lambda i:i[0])
    e = ds[0][0]
    count = 1
    for i in range(1,n):
        if ds[i][1] > e:
            count += 1
            e = ds[i][0]
    return count
