import bisect

def solution(info, query):
    l11 = ['-','cpp','java','python'] #언어 종류
    l12 = ['-', 'backend', 'frontend'] #직무
    l13 = ['-', 'junior', 'senior'] #경력
    l14 = ['-', 'chicken', 'pizza'] #음식
    L = [[] for i in range(108)]
    
    for s in info:
        z = s.split(' ')
        v1, v2, v3, v4 = l11.index(z[0]), l12.index(z[1]), l13.index([2]), l14.index([3])
        v5 = int(z[4])
        for c1 in [0, v1]:
            for c2 in [0, v2]:
                for c3 in [0, v3]:
                    for c4 in [0, v4]:
                        idx = c1*27  + c2*9 + c3*3 + c4
                        L[idx].append(v5)

    for i in range(108): #전처리 과정에 대한 정렬
        L[i].sort()
    
    #쿼리
    ret = []
    for q in query:
        z = q.split(' ')
        v1 , v2 = l11.index(z[0]), l12.index(z[2])
        v3, v4 = l13.index(z[4]), l12.index(z[6])
        target = int(z[7])
        idx = v1 * 27 + v2*9 + v3*3 + v4
        ret.append(len(L[idx]) - bisect.bisect_left(L[idx], target))
    return ret