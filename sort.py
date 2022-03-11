def sort_list(Mylist):
	n=len(Mylist)
	i=0
	while (i<n):
		q=i+1
		while (q<n):
			temp=0
			if Mylist[i]>Mylist[q]:
				temp=Mylist[i]
				Mylist[i]=Mylist[q]
				Mylist[q]=temp
			q=q+1
		i=i+1
	return Mylist
