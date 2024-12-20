def separate_even_odd_squares(start, end):
    """
    Calculates the squares of numbers within a specified range, separates them into even and odd lists.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.

    Returns:
        tuple: A tuple containing two lists: the first list contains even squares, the second contains odd squares.
    """

    squares = [num**2 for num in range(start, end + 1)]
    even_squares = [square for square in squares if square % 2 == 0]
    odd_squares = [square for square in squares if square % 2 != 0]

    return even_squares, odd_squares

if __name__ == "__main__":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    even_squares, odd_squares = separate_even_odd_squares(start, end)

    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)



    