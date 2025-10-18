# score =[]
# for i in range(5):
#     score1 = int(input(f"Enter {i+1} number:  "))
#     score.append(score1)

# print(score)

# import statistics as st
# score = [2,3,4,5]
# df =st.median(score)
# print(df)

score = [1,2,7,4,5,7]
# sum = 15
# def mean():
#     return sum/len(score)
# print(mean())

def median(li):
    n = len(li)
    if(n % 2 == 0):
        t1 = li[int(n/2)]
        t2 = li[int((n/2)-1)]
        return (t1 + t2)/2
    else:
        return li[int(n/2)]        


print(median(score))
