class Jar:
    def __init__(self, capacity=12, cookies=0):
        if capacity > 12:
            raise ValueError("Over Capacity")
        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        i = self.cookies * "🍪"
        return f"This is a cookie jar with {i} cookies!!!"

    def deposit(self, n):
        self.cookies = self.cookies + n

    def withdraw(self, n):
        self.cookies = self.cookies - n

    #getter
    @property
    def capacity(self):
        return self._capacity
    
    #setter
    @capacity.setter
    def capacity(self, capacity):
        #capacity error checking
        self._capacity = capacity

    @property
    def cookies(self):
        return self._cookies
    
    @cookies.setter
    def cookies(self,cookies):
        #cookies error checking
        self._cookies = cookies
    
    
def main():
    jar = make_jar() #initialize with 2 cookies
    Jar.deposit(jar, 2) #deposit two additional cookies
    Jar.withdraw(jar, 1) #withdraw one cookie
    print(jar)
    
def make_jar():
    capacity = 10
    cookies = 2
    return Jar(capacity, cookies)
    
if __name__ == "__main__":
    main()