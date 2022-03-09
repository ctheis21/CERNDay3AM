import pickle
import os.path
"""
Add to the Stack class:
    a readonly property associated with the current maxSize of a Stack
"""
# __init__(self,content=[],size=__maxsize)

class Stack: # class Stack(object)
    
    __MAX_SIZE=10000 # A class variable
    
    def __init__(self, *args):
        try:
            if len(args)==1:
                # Stack(12)
                if isinstance(args[0], int) and args[0] > 0 and args[0] < Stack.__MAX_SIZE:
                    self.__maxSize=args[0]
                    self.content=[]
                # Stack([2,3,4])
                elif len(args[0]) > 0 and len(args[0]) < Stack.__MAX_SIZE:
                        self.__maxSize=len(args[0])
                        self.content=list(args[0])
                else:
                    raise Exception("Problem using the Stack constructor")
            elif len(args)==2:
                if isinstance(args[0], int) and args[0] > 0 and args[0] < Stack.__MAX_SIZE:
                    self.__maxSize=args[0]
                    self.content=[e for e in args[1][:args[0]]]
                else:
                    raise Exception("Problem using the Stack constructor")
            else:
                raise Exception("Problem using the Stack constructor")
        except:
             raise Exception("Problem using the Stack constructor")
    @property
    def maxSize(self):
        return self.__maxSize
    
    def __repr__(self):
        return f"({len(self)}/{self.maxSize}) {self.content}"
    def __len__(self):
        return len(self.content)
    def __eq__(self, other):
        return self.maxSize == other.maxSize and self.content == other.content
    def __contains__(self, value): # in
        return value in self.content
    
    def __iter__(self): # invoked by iter()
        for ix in range(len(self)-1, -1, -1):
            yield self.content[ix]

    def push(self, value):
        if len(self) >= self.maxSize: #The stack is full
            raise Exception("Stack full!")
        else:
            self.content.append(value)
    def pop(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return self.content.pop()
    def peek(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return self.content[-1]
    def clear(self):
        self.content.clear()
    def isEmpty(self):
        return len(self)==0
    def extend(self, newSize):
        if isinstance(newSize, int) and newSize > self.maxSize and newSize <= Stack.__MAX_SIZE:
            self.__maxSize=newSize
        else:
            raise Exception("Wrong stack size given")
    def serialize(self,filename):
        with open(filename, "wb") as fic:
            pickle.dump(self,fic)
            
    @staticmethod 
    def deserialize(filename):
        if os.path.exists(filename):
            try:
                with open(filename, "rb") as fic:
                    temp=pickle.load(fic)
                    return temp
            except Exception:
                raise
        else:
            raise Exception(f"{filename} not found!")
            
    @staticmethod 
    def getMaxSize():
        return Stack.__MAX_SIZE   
       
if __name__ == "__main__":
    d=(2,3,4,5,10)
    s=Stack(3, d)
    print(s) # (3/3) [2,3,4]
    s=Stack(d)
    print(s) # (5/5) [2,3,4,5,10]
    s=Stack(10,d)
    print(s) # (5/10) [2,3,4,5,10]
   
    s1=Stack(10) # 10 is the maximum size of the Stack
    s1.push(24)
    s1.push(27)
    s1.push(29) # obj.method(arg1, arg2) -> method(obj, arg1, arg2)
    print("*"*50)
    # A Stack is an iterable object now, I can use a for loop
    print(s1)
    for e in s1:
        print(e)
        
    # A Stack is an iterable object now, I can use the map() function 
    l=list(map(lambda a: a**2, s1))
    print(l)
    
    print(f"Current maxSize of s1 is {s1.maxSize}")
    
    #s1.maxSize=23 # Exception raised here !!!
    
    s1.serialize("data.pick")
    s4=Stack.deserialize("data.pick")
    print(s4)
    print(len(s1)) # 3
    print(len(s1)) # 3
    print(s1) # (3/10) [24,27,29]
    if 56 in s1:
        print("56 is in the Stack")
    else:
        print("56 is not in the Stack")
    top=s1.pop()
    print(top) # 29
    print(s1) # (2/10) [24,27]
    print(len(s1)) # 2
    top=s1.pop()
    print(top) # 27
    print(s1) # (1/10) [24]
    top=s1.peek()
    print(top) # 24
    print(s1) # (1/10) [24]
    s2=Stack(20) # 20 is the maximum size of the Stack
    s2.push(24)
    print(s2)
    print(s1==s2)
    s2.extend(25)
    print(s2)
    s2.clear()
    print(s2)
    
