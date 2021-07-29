import math
def binarySearch(arr, val):
    left_ptr = 0 #L
    right_ptr = len(arr) - 1 #R
    mid_ptr = math.floor((left_ptr+right_ptr) / 2) #M
    #print(left_ptr, mid_ptr, right_ptr)

    while not(arr[mid_ptr] == val) and left_ptr <= right_ptr:
        #if mid_ptr > val
        if val < arr[mid_ptr]:
            right_ptr = mid_ptr -1
        #if mid_ptr < val
        else:
            left_ptr = mid_ptr + 1

        #update mid_ptr everytime
        mid_ptr = math.floor((left_ptr+right_ptr) / 2)

        #print(left_ptr, mid_ptr, right_ptr)
    
    if arr[mid_ptr] == val:
        return mid_ptr
    else:
        return -1

    
custom_arr = [8,9,12,15,17,19,20,21,28]
print(binarySearch(custom_arr,15))
print(binarySearch(custom_arr,1))


'''
Dry run demo - 
[8,9,12,15,17,19,20,21,28]
 L         M           R   
 val to be found = 15, 15< M OR 15<17
 So, place R at left of M -> R = M-1
[8,9,12, 15, 17 , 19,20,21,28]
 L       R   M   (discarded part)  
 update middle ptr 
 [8, 9, 12, 15, 17 , 19,20,21,28]
  L  M      R   (discarded part) 
 val to be found = 15, 15 > M OR 15 > 9
  [8, 9,  12,   15,    17 , 19,20,21,28]
      M  L(2)   R(3)   (discarded part)   
update mid ptr = 2+3 / 2 = 2 (floor), so M -> 2
  [8, 9,  12,    15,    17 , 19,20,21,28]
         LM(2)   R(3)   (discarded part)
val to be found = 15, 15> M OR 15<12
 So, place L at right of M -> L = M+1
 [8, 9,  12,    15,    17 , 19,20,21,28]
         M(2)   LR(3)   (discarded part)
update mid ptr = 3+3 / 2 = 2 (floor), so M -> 3
[8, 9,  12,    15,    17 , 19,20,21,28]
              MLR(3)   (discarded part)
So, M= 15 -> value found. 
STOP
'''
