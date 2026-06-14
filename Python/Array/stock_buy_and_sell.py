arr = [1,5,3,1,2,8]

profit = 0
buy = arr[0]

for i in range(1,len(arr),1):
    if arr[i-1] > arr[i]:
        profit += arr[i-1] -buy
        buy = arr[i]
    
    # print("current stock price",arr[i-1])
    # print("current profit", profit)
    # print("current buy price",buy)
profit += (arr[i] -buy)

print("max profit",profit)