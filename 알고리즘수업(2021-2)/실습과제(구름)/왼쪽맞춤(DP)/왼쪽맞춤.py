#여백만을 penalty라고 인식
def LeftSet(W, words):
    D = [0]*len(words)
    min_penalty =0
    curr_penalty =0
    index=0

    for i in range(1, len(words)):
        curr_width = 0
        min_penalty
        j=i

        while j >=0:
            curr_width += len(words[j])+1 #앞의 단어와 띄어쓰기 1칸
            print(f'word={words[j]}')
            print(f'curr_width={curr_width}')
            curr_penalty = D[j-1] + (W - curr_width +1)**3
            print(f'curr_penalt={curr_penalty}')

            if curr_width+len(words[j-1])>W:
                break
            j = j-1
            index+=1

        if i==len(words)-1:
            min_penalty = min(min_penalty, curr_penalty )

        elif min_penalty!=0:
            min_penalty += min(curr_penalty, min_penalty)
        else:
            min_penalty += curr_penalty

        D[i] = min_penalty
        print(D[i])

    return D[len(words)-1]

W = int(input())
words = input().split()
print(words)

print(LeftSet(W,words))
# code below