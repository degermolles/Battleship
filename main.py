

class Grid():
	def __init__(self, size):
		self.size = size
		self.plateau = self.make_grid()

	def make_grid(self):
		plateau = []
		for i in range(self.size):
			plateau.append([False]*self.size)
		return plateau
		
	def show(case):
		"""
		
			param:
				case string
			return Boolean
			
		"""
		# case e.g.: 'A2'
		
		xLetter = case
		y = case
		
		x = xLetter
		
		return self.palteau[x][y-1]
		
	



def greetings():
	print('hello world!')

def bye():
	print('bye!')
	


if __name__ == '__main__':
	greetings()
	# faire le plateau
	g = Grid(5)
	print(g.plateau)
	bye()
	
	