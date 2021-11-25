#여백만을 penalty라고 인식
def LeftSet(W, words):
    D = [0]*len(words)
    min_penalty =0
    curr_penalty =0
    index=0

    for i in range(1, len(words)):
        curr_width = 0
        # min_penalty =
        j=i

        while j >=0:
            curr_width += len(words[j])+1 #앞의 단어와 띄어쓰기 1칸
            print(f'word={words[j]}')
            print(f'curr_width={curr_width}')
            curr_penalty = D[j-1] + (W - curr_width +1)**3
            print(f'curr_penalt={curr_penalty}')

            if curr_width+len(words[j-1])>W or index>len(words)-1:
                print(f'i번째:{i}')
                # min_penalty = min(D[i - 1] + (W - len(words[j]) ** 3), curr_penalty)

                if D[i-1] !=0: #D[1~n-1]과 비교하는 경우
                    min_penalty=min(D[i-1]+(W-len(words[j]))**3, curr_penalty)
                else: #D[0]과 비교하는 경우
                    min
                    _penalty=curr_penalty
                break
            j = j-1
            index = index + 2
            print(f'index={index}')

        D[i] = min_penalty
        print(D[i])

    return D[len(words)-1]

W = int(input())
words = input().split()
print(words)

print(LeftSet(W,words))
# code below