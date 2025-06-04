#!/usr/bin/env python
import os

def main():
    print("""
Welcome to the puzzle!
The entire puzzle is solvable by commands / code you can write in this shell!
You'll quickly identify some shortcomings of the shell (that you can work around) but
one thing we'll call out from the start is that when you run 'python' it's actually running 'micropython'
which is a smaller implementation of python that doesn't have some of the libraries you're used to.
Additionally, mark down any clues you find as your progress won't be saved if you refresh the page.
Good luck!
=====================================

STEP ONE:
Decode the following payload by implementing puzzle/decode.py
    """)

    encoded_str = """
    ABCDICoiICIgIiAiICQoJiUmLCYsJi8iISIgJScmJSYsJiMmLyYtJiUiICckJi8iICckJigmJSIgJyAnJScqJyomLCYlIiAiKCYpIiAmJyclJiUnIycjIiwiICcgJyUnKicqJiwmJSIgJyAmISciJyQiICMiIiAmISckIiAnJCYoJ
    """
    print(encoded_str)

    # Attempt to decode it using decode.py
    try:
        import decode  # This should contain a 'decode_payload' function
        decoded_text = decode.decode_payload(encoded_str)
        print("Decoded payload:\n")
        print(decoded_text)
    except (ImportError, AttributeError, Exception) as e:
        print("It looks like puzzle/decode.py is missing or broken!")
        print("Error details:", e)
        print("Please fix puzzle/decode.py so we can decode the message.")


if __name__ == '__main__':
    main()