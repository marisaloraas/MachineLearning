'''
for a given line
	positive side is correct, shade that side
	ax + by + c
	to fix:
		a-p b-q
	generate 10 points on each side of this line, 30 points total by the end
	use additive colors on shades for changing lines (yellow + blue = green)
	click next, pick the next point to update
	line should keep moving for each line reclassification
	make it 10 points
	plot vector a by c, b by c
		(0,0) to (a/c, b/c)
'''
# ask whether to take a new point as input or generate random one
import random
import matplotlib.pyplot as plt
import numpy as np

plt.ion()
# plt.figure(figsize=(5,5))
fig, (ax, ax1) = plt.subplots(2)


#number of points in the data set
n = 10

def abc_gen():
	'''generate a, b, and c constants for 0 = ax + by + c'''
	a = random.randint(-5, 5)
	b = random.randint(-9, 9)
	c = random.randint(-9, 9)
	return a, b, c

a, b, c = abc_gen()

#m = -A/B       (intercept) c = -C/B
m = (-float(a))/float(b)
intercept = (-float(c))/float(b)

def f(x, m, c):
	'''return y for a point x'''
	return m * x + c

#Generates original random line to separate the points by + and -

def line_equation(m, intercept, ax):
	'''Converts to slope intercept'''
	x_vals = np.array(ax.get_xlim())
	y_vals = intercept + (m * x_vals)
	return x_vals, y_vals

points = np.random.randint(1, 10, size=(n, 3), dtype=np.uint8)

def points_gen():
	'''classify points as positive or negative points'''
	points[:,2] = 0
	for i in points:
		if i[1] >= f(i[0], m, intercept):
			i[2] = 1

def gen_line(m, intercept):
	'''generate a line for consistently beautiful demos'''
	points_gen()
	while points[:,2].sum() < 3 or points[:,2].sum() > 7:
		a, b, c = abc_gen()
		#m = -A/B       (intercept) c = -C/B
		m = (-float(a))/float(b)
		intercept = (-float(c))/float(b)

		points[:,2] = 0
		for i in points:
			if i[1] >= f(i[0], m, intercept):
				i[2] = 1

	return m, intercept

a1, b1, c1 = abc_gen()

m1 = (-float(a1))/float(b1)
intercept1 = (-float(c1))/float(b1)

eqn1 = {
	'a1': a1,
	'b1': b1,
	'c1': c1,
	'm1': m1,
	'intercept1': intercept1,
	'count': 0,
	'a2': a1,
	'b2': b1
}

def onclick(event):
	if event.button == 1:
		print(eqn1)
		if eqn1['count'] > 9:
			eqn1['count'] = 0

		if(points[eqn1['count']][2] == 0 and points[eqn1['count']][1] <= f(points[eqn1['count']][0], eqn1['m1'], eqn1['intercept1'])):
			eqn1['count'] += 1

		elif(points[eqn1['count']][2] == 1 and points[eqn1['count']][1] >= f(points[eqn1['count']][0], eqn1['m1'], eqn1['intercept1'])):
			eqn1['count'] += 1

		elif(points[eqn1['count']][2] == 0 and points[eqn1['count']][1]  > f(points[eqn1['count']][0], eqn1['m1'], eqn1['intercept1'])):
			eqn1['a2'] = eqn1['a1']
			eqn1['b2'] = eqn1['b1']

			eqn1['a1'] = eqn1['a1'] - points[eqn1['count']][0]
			eqn1['b1'] = eqn1['b1'] - points[eqn1['count']][1]
			eqn1['m1'] = (float(eqn1['a1']))/float(eqn1['b1'])
			eqn1['intercept1'] = (-float(eqn1['c1']))/float(eqn1['b1'])
			x_line1, y_line1 = line_equation(eqn1['m1'], eqn1['intercept1'], ax)
			# fig.clf()
			# plt.cla()
			ax.clear()
			ax.set_xlim([0, 10])
			ax.set_ylim([0, 10])
			ax1.set_xlim([-10, 10])
			ax1.set_ylim([-10, 10])
			# fig.canvas.flush_events()
			ax.scatter(
				points[points[:,2] == 0][:,0],
				points[points[:,2] == 0][:,1],
				marker="_")
			ax.scatter(
				points[points[:,2] == 1][:,0],
				points[points[:,2] == 1][:,1],
				marker="+")
			ax.plot(
				x_line,
				y_line,
				c="blue")
			ax.plot(
				x_line1,
				y_line1,
				c="red")
			ax.set_ylabel("y")
			ax.set_xlabel("x")
			ax.set_title("Cateogized Dataset Example")
			ax.fill_between(x_line, y_line, 10, alpha=0.3, facecolor="blue")
			ax.fill_between(x_line1, y_line1, 10, alpha=0.3)
			ax.figure.canvas.draw() #redraw
			eqn1['count'] += 1

			ax1.plot(
				[0, eqn1['a2']/eqn1['c1'] * 10],
				[0, eqn1['b2']/eqn1['c1'] * 10],
				c="black")
			ax1.figure.canvas.draw()

		else:
			eqn1['a2'] = eqn1['a1']
			eqn1['b2'] = eqn1['b1']

			eqn1['a1'] = eqn1['a1'] + points[eqn1['count']][0]
			eqn1['b1'] = eqn1['b1'] + points[eqn1['count']][1]
			eqn1['m1'] = (-float(eqn1['a1']))/float(eqn1['b1'])
			eqn1['intercept1'] = (-float(eqn1['c1']))/float(eqn1['b1'])
			x_line1, y_line1 = line_equation(eqn1['m1'], eqn1['intercept1'], ax)
			# fig.clf()
			# plt.cla()
			ax.clear()
			ax.set_xlim([0, 10])
			ax.set_ylim([0, 10])
			ax1.set_xlim([-10, 10])
			ax1.set_ylim([-10, 10])
			# fig.canvas.flush_events()
			ax.scatter(
				points[points[:,2] == 0][:,0],
				points[points[:,2] == 0][:,1],
				marker="_")

			ax.scatter(
				points[points[:,2] == 1][:,0],
				points[points[:,2] == 1][:,1],
				marker="+")
			ax.plot(
				x_line,
				y_line,
				c="blue")
			ax.plot(
				x_line1,
				y_line1,
				c="red")
			ax.set_ylabel("y")
			ax.set_xlabel("x")
			ax.set_title("Cateogized Dataset Example")
			ax.fill_between(x_line, y_line, 10, alpha=0.3, facecolor="blue")
			ax.fill_between(x_line1, y_line1, 10, alpha=0.3)
			ax.figure.canvas.draw() #redraw
			eqn1['count'] += 1

			ax1.plot(
				[0, eqn1['a2']/eqn1['c1'] * 10],
				[0, eqn1['b2']/eqn1['c1'] * 10],
				c="black")
			ax1.figure.canvas.draw()

		ax1.plot(
			[0, eqn1['a1']/eqn1['c1'] * 10],
			[0, eqn1['b1']/eqn1['c1'] * 10],
			c="red")

		print(eqn1)
		print()

m, intercept = gen_line(m, intercept)

line = [0, n];
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax1.set_xlim([-10, 10])
ax1.set_ylim([-10, 10])

ax.scatter(
	points[points[:,2] == 0][:,0],
	points[points[:,2] == 0][:,1],
	marker="_")

ax.scatter(
	points[points[:,2] == 1][:,0],
	points[points[:,2] == 1][:,1],
	marker="+")

x_line, y_line = line_equation(m, intercept, ax)


ax.plot(
	x_line,
	y_line,
	c="blue")

ax1.plot(
	[0, a/c * 10],
	[0, b/c * 10],
	c="blue")

ax1.plot(
	[0, eqn1['a1']/eqn1['c1'] * 10],
	[0, eqn1['b1']/eqn1['c1'] * 10],
	c="red")

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.set_title("Cateogized Dataset Example")

# plt.draw()bb

x_line1, y_line1 = line_equation(m1, intercept1, ax)

ax.plot(
	x_line1,
	y_line1,
	c="red")
ax.fill_between(x_line, y_line, 20, alpha=0.3, facecolor="blue")
ax.fill_between(x_line1, y_line1, 20, alpha=0.3)
# plt.draw()
# plt.pause(15)
# plt.pause(0.001)
fig.canvas.draw()
fig.canvas.mpl_connect('button_press_event',onclick)
while plt.get_fignums():
	plt.pause(0.001)
