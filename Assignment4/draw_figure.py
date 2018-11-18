import matplotlib.pyplot as plt
import numpy as np


def main():
	problemSet = ["steps", "rewards", "times"]
	titles = ["Hard Grid World # of Steps", "Hard Grid World Rewards", "Hard Grid World Time Cost"]
	names = ["Value Iteration,", "Policy Iteration", "Q Learning"]
	y_list = []
	for i,problem in enumerate(problemSet):
		y_list = []
		with open("{}.txt".format(problem)) as f:
			iterations = [int(x) for x in f.readline().split(',')]
			y_list.append([float(x) for x in f.readline().split(',')])
			y_list.append([float(x) for x in f.readline().split(',')])
			y_list.append([float(x) for x in f.readline().split(',')])
		draw(iterations, y_list, "Iterations", problem, titles[i])


def draw(x_list, y_list, x_label, y_label, title):
	plt.figure()
	plt.title(title)

	plt.xlabel(x_label)
	plt.ylabel(y_label)

	plt.yscale('log')
	plt.plot(x_list, y_list[0], color='g', label="Value Iteration")
	plt.plot(x_list, y_list[1], color='r', label="Policy Iteration")
	plt.plot(x_list, y_list[2], color='y', label="Q Learning")

	plt.legend(loc='best')
	plt.show()

if __name__=="__main__":
	main()