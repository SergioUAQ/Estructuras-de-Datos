from collections import deque

class Cola:
	def __init__(self):
		self._datos = deque()

	def enqueue(self, valor):
		self._datos.append(valor)
	
	def dequeue(self):
		if self.esta_vacia():
			raise IndexError("No se puede hacer dequeue de una cola vacia")
		return self._datos.popleft()

	def frente(self):
		if self.esta_vacia():
			raise IndexError("Cola vacia")
		return self._datos[0]

	def esta_vacia(self):
		return len(self._datos) == 0

c = Cola()
c.enqueue("A")
c.enqueue("B")
c.enqueue("C")
print(c.dequeue())
print(c.frente())

