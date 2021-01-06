from d_12_parse import input_parse
import d_12_p1

class Waypoint(d_12_p1.Ship):
	def __init__(self, instructions):
		self.move_to((10, 1))
		self.instructions = instructions
		self.ship_coords = [0, 0]

	def turn_left(self, v):
		turn = (v / 90) % 4
		if turn == 1:
			self.move_to((-self.y, self.x))
		elif turn == 2:
			self.move_to((-self.x, -self.y))
		elif turn == 3:
			self.move_to((self.y, -self.x))
	def move_forwards(self, v):
		for i in (0, 1):
			self.ship_coords[i] += v * self.coords[i]

if __name__ == "__main__":
	w = Waypoint(input_parse())
	w.run()

	print(abs(w.ship_coords[0]) + abs(w.ship_coords[1]))
