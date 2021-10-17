#!/usr/bin/env python3

"""
A Polybius Square is a table that allows someone to translate letters into numbers.

https://www.braingle.com/brainteasers/codes/polybius.php
"""

import numpy as np


class PolybiusCipher:
    def __init__(self) -> None:
        SQUARE = [
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "k"],
            ["l", "m", "n", "o", "p"],
            ["q", "r", "s", "t", "u"],
            ["v", "w", "x", "y", "z"],
        ]
        self.SQUARE = np.array(SQUARE)

    def letter_to_numbers(self, letter: str) -> np.ndarray:
        """
        Return the pair of numbers that represents the given letter in the
        polybius square
        >>> PolybiusCipher().letter_to_numbers('a')
        [1, 1]

        >>> PolybiusCipher().letter_to_numbers('u')
        [4, 5]
        """
        index1, index2 = np.where(self.SQUARE == letter)
        indexes = np.concatenate([index1 + 1, index2 + 1])
        return indexes

    def numbers_to_letter(self, index1: int, index2: int) -> str:
        """
        Return the letter corresponding to the position [index1, index2] in
        the polybius square

        >>> PolybiusCipher()..numbers_to_letters(4, 5)
        "u"

        >>> PolybiusCipher()..numbers_to_letters(1, 1)
        "a"
        """
        letter = self.SQUARE[index1 - 1, index2 - 1]
        return letter

    def encode(self, message: str) -> str:
        """
        Return the encoded version of message according to the polybius cipher

        >>> PolybiusCipher().encode("test message")
        "44154344 32154343112215"

        >>> PolybiusCipher().encode("Test Message")
        44154344 32154343112215"
        """
        message = message.lower()
        message = message.replace("j", "i")

        encoded_message = ""
        for letter_index in range(len(message)):
            if message[letter_index] != " ":
                numbers = self.letter_to_numbers(message[letter_index])
                encoded_message = encoded_message + str(numbers[0]) + str(numbers[1])
            elif message[letter_index] == " ":
                encoded_message = encoded_message + " "

        return encoded_message

    def decode(self, message: str) -> str:
        """
        Return the decoded version of message according to the polybius cipher

        >>> PolybiusCipher().decode("44154344 32154343112215")
        "test message"

        >>> PolybiusCipher().decode("4415434432154343112215")
        testmessage"
        """
        message = message.replace(" ", "  ")
        decoded_message = ""
        for numbers_index in range(int(len(message) / 2)):
            if message[numbers_index * 2] != " ":
                index1 = message[numbers_index * 2]
                index2 = message[numbers_index * 2 + 1]

                letter = self.numbers_to_letter(int(index1), int(index2))
                decoded_message = decoded_message + letter
            elif message[numbers_index * 2] == " ":
                decoded_message = decoded_message + " "

        return decoded_message
