
#It is a comparison-based algorithm in which each pair of adjacent elements is compared
# and the elements are swapped if they are not in order.

u_list=[2,1,5,4,3]


for u in u_list:
	for o in u_list:

		if u_list[o]>u_list[o+1]:
			temp=u_list[o]
			u_list[o]=u_list[o+1]
			u_list[o]=temp

print(u_list)

