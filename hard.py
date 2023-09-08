height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(height)
Left = [0]
Right = [0]
Min_L_and_R = []
Count = 0

#left list
for i in height:
    if Left[len(Left)-1] < i:
        Left.append(i)
    else:
        Left.append(Left[len(Left)-1])
Left.pop()
print(Left)

#Right list
for i in (height[::-1]):
    if Right[len(Right) - 1] < i:
        Right.append(i)
    else:
        Right.append(Right[len(Right) - 1])
Right.pop()
Right = Right[::-1]
print(Right)

for i in range(len(height)):
    y=(min(Left[i], Right[i]))
    Min_L_and_R.append(y)
print (Min_L_and_R)

for i in range(len(height)):
    if(Min_L_and_R[i] - height[i])<=0:
        None
    else:
        Count += Min_L_and_R[i] - height[i]

print(Count)