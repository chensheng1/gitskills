#-*-coding:utf-8-*-

def findsmallet(arr):
	smallet=arr[0]
	smallet_index=0
	for i in range(1,len(arr)):
		if smallet>arr[i]:
			smallet=arr[i]
			smallet_index=i
	return smallet_index
		
def find(arr):
	newarr=[]
	for i in range(len(arr)):
		small=findsmallet(arr)
		newarr.append(arr.pop(small))
	return newarr
	
print find([1,7,5,9])