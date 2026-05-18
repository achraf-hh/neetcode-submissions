class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        self.cars = []
        self.times = []
        self.nbFleet = []
        n = len(position)
        for i in range(n):
            self.cars.append([position[i], speed[i]])
        self.carsSorted = sorted(self.cars)

        for L in self.carsSorted : 
            self.times.append((target - L[0])/L[1])

        self.nbFleet.append(self.times[-1])
        self.times.pop()
        for t in reversed(self.times):
            if t > self.nbFleet[-1]:
                self.nbFleet.append(t)




        return len(self.nbFleet)

