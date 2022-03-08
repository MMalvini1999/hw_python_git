def sort_list():
	Mylist=[8, 4, 7, 16]
	n=4
	i=0
	while (i<n-1):	
		q=i+1
		while (q<n-1):
			temp=0
			if Mylist[i]>Mylist[q]:
				temp=Mylist[i]
				Mylist[i]=Mylist[q]
				Mylist[q]=temp
			q=q+1
		i=i+1 
	print(Mylist)
sort_list()
