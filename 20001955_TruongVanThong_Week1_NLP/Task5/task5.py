class Stack:
    def __init__(self):
        self.st = []

    def push(self, el):
        self.st.append(el)

    def pop(self):
        return self.st.pop()

    def isEmpty(self):
        return len(self.st) == 0

    def size(self):
        return len(self.st)

    def top(self):
        return self.st[-1]

if __name__ == "__main__":
    st = Stack()
    st.push(5)
    st.push(7)  
    st.push(9)  
    print(st.pop())
    print(st.top())  
    
    # Sử dụng Stack để nhập vào 1 số ở dạng thập phân, in ra số đó ở hệ nhị phân tương ứng
    number = int(input("Enter a decimal number: "))
    stack = Stack()

    while number > 0:
        remainder = number % 2
        stack.push(remainder)
        number //= 2

    binary_number = ""

    while not stack.isEmpty():
        binary_number += str(stack.pop())

    print("The binary number is: " + binary_number)
