#-*-coding:utf-8-*-


def quick(array):
	if len(array)<2:
		return array
	else:
		pivot=array[0]
		less=[i for i in  array[1:] if i <= pivot]
		greater =[i for i in array[1:] if i> pivot]
		return quick(less) +[pivot] +quick(greater)
print quick([7,5,12,15,2,20,6])


def quicksort(arr,strat,end):
	if (len(arr)<2):
		print arr
	else:
		i=strat
		j=end
		key=arr[i]
		while(i<j):
			while (i<j) and (key<=arr[j]):
				j-=1
			if (key>arr[j]):
				arr[i]=arr[j]
				arr[j]=key
			while(i<j) and (key>=arr[i]):
				i+=1
			if (key<arr[i]):
				arr[j]=arr[i]
				arr[i]=key
		if(i>strat):
			quicksort(arr,strat,i-1)
		if(end>j):
			quicksort(arr,j+1,end)
	return arr

arr=[7,5,12,15,2,20,6]
strat=0
end= len(arr) - 1
print quicksort(arr,strat,end)