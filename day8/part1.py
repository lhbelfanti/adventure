from operator import attrgetter


def create_layers(pixels, wide, tall):
	image_size = wide * tall
	layers = []
	length = len(pixels) + 1
	nums = []
	current = None
	for i in range(0, length):
		if i % image_size == 0:
			if len(nums) > 0:
				current.add_data(nums)
				layers.append(current)
			nums = []
			current = Layer(wide, tall)

		if i != length - 1:
			nums.append(pixels[i])

	return layers


class Layer:
	def __init__(self, wide, tall):
		self.wide = wide
		self.tall = tall
		self.zeros = 0
		self.ones = 0
		self.twos = 0
		self.matrix = [0] * self.tall
		for i in range(0, len(self.matrix)):
			self.matrix[i] = [0] * self.wide

	def add_data(self, nums):
		c = 0
		for i in range(0, self.tall):
			for j in range(0, self.wide):
				n = nums[c]
				self.zeros += 1 if n == 0 else 0
				self.ones += 1 if n == 1 else 0
				self.twos += 1 if n == 2 else 0
				self.matrix[i][j] = n
				c += 1

	def multiply(self):
		return self.ones * self.twos


def main():
	f = open("input.txt", "r")

	wide = 25
	tall = 6

	pixels = []
	line = ""
	for line in f:
		line = line.rstrip()

	for p in line:
		pixels.append(int(p))

	layers = create_layers(pixels, wide, tall)
	min_zeros = min(layers, key=attrgetter('zeros'))
	print("The number of 1 digits multiplied by the number of 2 digits is: " + str(min_zeros.multiply()))


main()

# wrong
# 1792
# 1834
# 3420
