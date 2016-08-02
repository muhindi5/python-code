#!/usr/bin/python3
#simulation of the hot potato game usin a queue

import Queue

def sim_hp(name_list,num):
	sim_que = Queue()
	for n in name_list:
		sim_que.enqueue(n)
	while sim_que.size() > 1:
		for i in range(num):
			sim_que.enqueue(sim_que.dequeue())
		sim_que.dequeue()
	return sim_que.dequeue()
print(sim_hp(['Allex','Jack','Jane','Ben','Greg','Alan','Fred','Peter'],7))
