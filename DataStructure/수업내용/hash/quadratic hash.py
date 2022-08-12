class Dictionary:
    def __init__(self, size):
        self.M = size
        self.keyList = [None] * size
        self.valueList = [None] * size
        self.N = 0

    def hashFunc(self, key):
        return key % self.M
    
    def put(self, key, value):
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0

        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return

            if self.keyList[i] == key:
                self.valueList[i] = value
                return
            
            j +=1
            i = (initialPos + j*j) % self.M

            if self.N > self.M:
                return

    def get(self, key):
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0

        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]

            j +=1
            i = (initialPos + j*j) % self.M
        return None

d=Dictionary(10)
d.put(1,'가')
d.put(2,'나')
d.put(3,'다')
d.put(1,'라')
d.put(1,'마')
out1=d.get(1)
out2=d.get(1)
print(out1)
print(out2)