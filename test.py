#1부터 50의 자연수 중 짝수를 구하는 함수가 있는 파일을 생성한다.배열로

def even():
    list=[]
    for i in range(1,51):
        if i % 2 == 0 :
            list.append(i)
        else:
            continue
    return list

print(even())
