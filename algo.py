def closest_triplet(arr, target):
    arr.sort() 
    min_diff = float('inf')
    closest_sum = None

    for i in range(len(arr) - 2):  
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                sum = arr[i] + arr[j] + arr[k]
                diff = abs(target - sum)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = sum
        
            sum = arr[i] + arr[j] + arr[k]

            diff = abs(target - sum)

            if diff < min_diff:
                min_diff = diff
                closest_sum = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    return closest_sum

arr = [1, 4, 2, 5, 3, 7]
target = 10 
result = closest_triplet(arr, target)
print(result)  # 9
