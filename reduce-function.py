from functools import reduce

ls=[4,2,5,8,6,9,27]
ans=reduce(lambda x,y : x+y ,ls)
print(ans)
