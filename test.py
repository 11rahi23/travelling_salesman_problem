world={ 1: ["left", "dirty", "dirty"],
		2: ["right", "dirty", "dirty"],
		3: ["left", "dirty", "clean"],
		4: ["right", "dirty", "clean"],
		5: ["left", "clean", "dirty"],
		6: ["right", "clean", "dirty"],
		7: ["left", "clean", "clean"],
		8: ["right", "clean", "clean"]
		}
path=[]
failure=0

def is_goal(state):
	goal1=world[7]
	goal2=world[8]

	if state==world[7] or state==world[8]:
		print("goal reached")
		return True
	else:
		print("goal not reached")
		return False

init=["right", "clean", "clean"]
is_goal(init)
