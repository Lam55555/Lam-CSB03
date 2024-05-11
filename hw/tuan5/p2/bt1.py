arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 90]
arradd = []
multi = []
shift = []
for i in range(len(arr)):
    arradd.append(arr[i]+2)
    multi.append(arr[i]*2)
    shift.append(arr[(i + 2) % len(arr)])
print('Original list :',arr)
print('Add 2: ',arradd)
print('Multiply by 2 :',multi)
print('Shift 2 ',shift)

