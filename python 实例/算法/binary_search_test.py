def binary_search(list,number):
	low =0
	high=len(list)-1
	result=[]
	while low<=high:
		mid=(low+high)/2
		result.append(list[mid])
		if(number<list[mid]):
			high=mid-1
		elif(number==list[mid]):
			return result
		else:
			low=mid+1
	return result
	
my_list=[1,3,5,7,9]
print binary_search(my_list,3)
