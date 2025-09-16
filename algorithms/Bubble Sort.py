arr=[1,6,8,9,12,5,8,9,7,55,6,45,3,0] 
def Bubble_Sort(arr) :
    swaped=False
    n= len(arr)
    for i in range(n):
        swaped=True
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaped=True
                if swaped == False:
                    break
    for k in range(len(arr)):
        print(arr[k] ,end=" ")
Bubble_Sort(arr)