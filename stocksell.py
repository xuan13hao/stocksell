# find MaxSubArray of subArray where mid element sits in
def findMaxCrossingSubArray(A, low, mid, high):
    maxLeft = 0
    leftSum = float('-inf')
    sum = 0
    for i in range(mid, -1, -1):
        sum = sum + A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    maxRight = 0
    rightSum = float('-inf')
    sum = 0
    for i in range(mid+1, high + 1, 1):
        sum = sum + A[i]
        if sum > rightSum:
            rightSum = sum
            maxRight = i

    return (maxLeft, maxRight, leftSum + rightSum)


# recursive method to find maxSubArray
def findMaxSubArray(A, low, high):
    print("low: ", low, "high: ", high)
    # recursive stop contidion
    if low == high:
        return(low, high, A[low])
    else:
        mid = (low + high)//2
        # subArray sits in left subarray
        # or right subarray
        # or cross them
        # find maxium of them as the final result
        leftLow, leftHigh, leftSum = findMaxSubArray(A, low, mid)
        righLow, righHigh, rightSum = findMaxSubArray(A, mid + 1, high)
        crossLow, crossHigh, crossSum = findMaxCrossingSubArray(
            A, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return(leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >= crossSum:
            return(righLow, righHigh, rightSum)
        else:
            return(crossLow, crossHigh, crossSum)


if __name__ == '__main__':
    #data from Introduction to algorithms-3rd page 68
    A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    #Subtract two adjacent values in the original array to get a difference array B
    B = []
    for n in range(1, len(A)):
       B.append(A[n] - A[n-1])
    print(B)
    maxSubArray = findMaxSubArray(B, 0, len(B) - 1)
    print("LeftIndex: ", maxSubArray[0])
    print("RightIndex: ", maxSubArray[1])
    print("maxSubArraySum: ", maxSubArray[2])