def add(x: int,y: int) -> int:
     return x + y
 
def sub(x: int,y: int) -> int:
     return x - y
 
def prod(x: int,y: int) -> int:
    return x * y
 
def div(x: int,y: int) -> int:
    return x // y
print(f"I am in calculator {__name__}")
if __name__ == "__main__":
    
    a = 500
    b = 1000
    
    result = prod(a, b)
    print(result)

print(__name__)