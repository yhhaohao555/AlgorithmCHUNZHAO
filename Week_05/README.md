学习笔记

x & 1 得到最低位
x & 1 == 1 (x % 2 == 1)
x >> 1 (x // 2)
x = x & x - 1 清零最低位的1
x & -x 得到最低位的1
x & ~x = 0

双向BFS
beginset = set([beginNode])
endset = set([endNode])
visited = set([beginNode, endNode])
while beginset：
	swap（beginset, endset） 优化算法，缩短时间
	for x in beginset:
		if x in endset:
			return
		if x not in visited:
			nextset.add(x)
			visited.add(x)
	beginset = nextset
	step += 1
