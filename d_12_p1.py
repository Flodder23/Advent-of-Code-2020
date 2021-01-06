from d_12_parse import input_parse

class Ship:
	def __init__(self, instructions):
		self.move_to((0, 0))
		self.facing = 0
		self.instructions = instructions
	
	def run(self):
		n = 0
		while n < len(self.instructions):
			self.execute_instruction(n)
			n += 1
	
	def execute_instruction(self, n):
		i, v = [self.instructions[n][key] for key in ("instruction", "value")]
		if i == "N":
			self.move_north(v)
		elif i == "S":
			self.move_south(v)
		elif i == "E":
			self.move_east(v)
		elif i == "W":
			self.move_west(v)
		elif i == "L":
			self.turn_left(v)
		elif i == "R":
			self.turn_right(v)
		elif i == "F":
			self.move_forwards(v)
		else:
			raise ValueError(f"{i} invalid instruction.")
	
	def move_to(self, coords):
		x, y = coords
		self.coords = [x, y]
		self.x = x
		self.y = y

	def move_north(self, v):
		self.move_to((self.x, self.y + v))
	def move_south(self, v):
		self.move_to((self.x, self.y - v))
	def move_east(self, v):
		self.move_to((self.x + v, self.y))
	def move_west(self, v):
		self.move_to((self.x - v, self.y))
	def turn_left(self, v):
		self.facing = (self.facing - v / 90) % 4
	def turn_right(self, v):
		self.turn_left(-v)
	def move_forwards(self, v):
		if self.facing == 0:
			self.move_east(v)
		elif self.facing == 1:
			self.move_south(v)
		elif self.facing == 2:
			self.move_west(v)
		elif self.facing == 3:
			self.move_north(v)

if __name__ == "__main__":
	ship = Ship(input_parse())
	ship.run()

	print(abs(ship.x) + abs(ship.y))
