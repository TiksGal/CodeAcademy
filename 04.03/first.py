class Factorial:
    @classmethod
    def calculate(cls , number: int) -> int:
        if number == 0 or number == 1:
            return 1
        else:
            return number * cls.calculate(number - 1)

number = 8
result = Factorial.calculate(number)
print(f"The factorial of {number} is {result}")

# Create a class method to return the reversed string of a given string.

class StringReverser:
    @classmethod
    def reverse(cls, input_string: str) -> str:
        return input_string[::-1]

input_string = input("Enter a string to reverse: ")
reversed_string = StringReverser.reverse(input_string)
print(f"The reversed string is: {reversed_string}")


# Create a class method to return the list of prime numbers up to a given number.

class PrimeNumbers:
    @classmethod
    def is_prime(cls, number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    @classmethod
    def generate_primes(cls, limit: int) -> list[int]:
        primes = []
        for number in range(2, limit + 1):
            if cls.is_prime(number):
                primes.append(number)
        return primes


limit = 30
primes = PrimeNumbers.generate_primes(limit)
print(f"Prime numbers up to {limit}: {primes}")


