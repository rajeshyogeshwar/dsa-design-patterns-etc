"""The Euclidean Algorithm is a technique for quickly finding the GCD of two integers.

Algorithm:

The Euclidean Algorithm for finding GCD(A,B) is as follows:
    If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.
    If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
    Write A in quotient remainder form (A = B⋅Q + R)
    Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
"""


def get_gcd(first_number: int, second_number: int):
    """Get gcd of the two numbers using Euclidean algorithm."""

    if first_number == 0:
        return second_number
    elif second_number == 0:
        return first_number

    remainder = first_number % second_number
    return get_gcd(second_number, remainder)


if __name__ == "__main__":
    first_number = 45
    second_number = 105
    gcd = get_gcd(first_number, second_number)
    print(f"GCD of {first_number} and {second_number} is {gcd}")