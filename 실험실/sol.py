# from typing import TextIO
#
# def filter_by_text(text) :
#     f: TextIO=open("txt", mode='r')
#
#     corpus=[]
#
#     corpus=list(f.split('/')) #이건 참고만해! 구글링으로 txt문자 입력 받기 하면 금방 나옴
#     # 저 방법 아니면, for문으로 f안의 모든 문자 받기
#     # for문으로 문자열 끝날 때까지 받아서 split('/')으로 /나눈 거 대로 받게 하면 될거야
#
#     result=[]
#
#     #빈도수 담을 리스트 선언
#     result2=[]
#     #text단어 추리기 & 단어와 빈도수 나눠서 result에 넣기
#     for i in range(len(corpus)):
#         if corpus[i] 가 text를 가지고 있는 지 and i<len(corpus):
#             result.append(corpus[i])
#             result2.append(corpus[i+1])
#
#     #통합정보담을 딕셔너리
#     dict={}
#     #딕셔너리로 각 정보 통합
#     for i in range(len(result)):
#         dict[f'{[result[i]]}']=result2[i]
#
#     #딕셔너리 숫자 기준으로 오름차순정렬
#     sorted_dict= sorted(dict.keys()) #빈도는 버리고, key값(텍스트)만 가져오기
#
#
#     answer=[]
#     #20번째까지만 answer에 저장
#     for i in range(0,20):
#         answer.append(sorted_dict[i])
#
# return answer
#
