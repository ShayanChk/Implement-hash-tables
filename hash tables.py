class ChainingHash:


	class Record:
		def __init__(self, key = None, value=None):
			self.key = key
			self.value = value


	def __init__(self, cap=32):
		self.map = [[] for i in range(cap)]
		self.cap = cap

	def insert(self,key, value):
		
		if (self.search(key)!=None):
			return False

		if(len(self) == self.cap):
			new_map = [[] for i in range(self.cap*2)]
			for i in range(self.cap):
				new_map[i]=self.map[i]
			self.map = new_map
			self.cap *= 2

		x = hash(key)   
		idx = x % self.cap 
		self.map[idx].append(self.Record(key,value))
		return True

	def modify(self, key, value):

		x = hash(key)   
		idx = x % self.cap   
		i=0
		while i < len(self.map[idx]):
			if self.map[idx][i].key == key:
				self.map[idx][i].value = value
				return True
			i+=1

		return False

	def remove(self, key):
		if (self.search(key)==None):
			return False

		c = self.cap  
		
		while c > 0 :
			x = hash(key)   
			idx = x % c  
			i=0
			while i < len(self.map[idx]):
				if self.map[idx][i].key == key:
					del self.map[idx][i]
					return True
				i+=1
			c = c//2

		return False

	def search(self, key):
		c = self.cap  
		while c > 0 :
			x = hash(key)   
			idx = x % c   
			for i in self.map[idx]:
				if i.key == key:
					return i.value
			c = c//2

		return None


	def capacity(self):
		return self.cap

	def __len__(self):
		i =0
		count = 0
		while(i < len(self.map)):
			if(self.map[i]!=[]):
				count+= len(self.map[i])
			i+=1
		return count


class LinearProbingHash:
	class Record:
		def __init__(self, key, value):
			self.key = key
			self.value = value


	def __init__(self, cap=32):
		self.map = [None for i in range(cap)]
		self.cap = cap


	def insert(self, key, value):
		if (self.search(key)!=None):
			return False

		x = hash(key)   
		i = x % self.cap 
		while i < self.cap*2:
			if self.map[i%self.cap ] == None:
				self.map[i%self.cap ] = self.Record(key,value)
				break
			i+=1
					


		if(len(self) >= self.cap*0.7):
			new_map = [None for i in range(self.cap*2)]
			for i in range(self.cap):
				new_map[i]=self.map[i]
			self.map = new_map
			self.cap *= 2

		return True

	def modify(self, key, value):
		x = hash(key)   
		i = x % self.cap 

		while i < self.cap*2:
			if self.map[i%self.cap] != None and self.map[i%self.cap].key == key:
				self.map[i%self.cap].value = value
				return True
			i+=1
		return False


	def remove(self, key):
		x = hash(key)   
		i = x % self.cap 

		while i < self.cap*2:
			if self.map[i%self.cap] != None and self.map[i%self.cap].key == key:
				self.map[i%self.cap] = None
				return True
			i+=1

		return False

	def search(self, key):
		x = hash(key)   
		i = x % self.cap 

		while i < self.cap*2:
			if self.map[i%self.cap] != None and self.map[i%self.cap].key == key:
				return self.map[i%self.cap].value
			i+=1

		return None

	def capacity(self):
		return self.cap

	def __len__(self):
		i =0
		count = 0
		while(i < len(self.map)):
			if(self.map[i]!=None):
				count+=1
			i+=1
		return count


