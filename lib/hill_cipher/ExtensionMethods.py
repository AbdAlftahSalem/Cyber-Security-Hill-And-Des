import math
import string

import numpy as np
from sympy import Matrix


class ExtensionMethods:
    @staticmethod
    def getAlphabet():
        alphabet = {}
        for character in string.ascii_uppercase:
            alphabet[character] = string.ascii_uppercase.index(character)

        reverse_alphabet = {}
        for key, value in alphabet.items():
            reverse_alphabet[value] = key

        alphabet.update({" ": 26})
        reverse_alphabet.update({26: " "})
        return alphabet, reverse_alphabet

    @staticmethod
    def getText(key, alphabet):
        while True:
            text = key.upper()
            if all(keys in alphabet for keys in text):
                return text
            else:
                print("TEXT NOT FOUND")

    @staticmethod
    def isSquareMatrix(key):
        key_length = len(key)
        if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
            return True
        else:
            return False

    @staticmethod
    def getKeyMatrix(key, alphabet):
        k = list(key)
        m = int(math.sqrt(len(k)))
        for (i, character) in enumerate(k):
            k[i] = alphabet[character]

        return np.reshape(k, (m, m))

    @staticmethod
    def getTextMatrix(text, m, alphabet):
        matrix = list(text)
        remainder = len(text) % m
        for (i, character) in enumerate(matrix):
            matrix[i] = alphabet[character]
        if remainder != 0:
            for i in range(m - remainder):
                matrix.append(25)

        return np.reshape(matrix, (int(len(matrix) / m), m)).transpose()

    @staticmethod
    def encrypt(key, plaintext, alphabet):
        m = key.shape[0]
        m_grams = plaintext.shape[1]
        ciphertext = np.zeros((m, m_grams)).astype(int)
        for i in range(m_grams):
            ciphertext[:, i] = np.reshape(np.dot(key, plaintext[:, i]) % len(alphabet), m)
        return ciphertext

    @staticmethod
    def matrixToText(matrix, order, alphabet):
        if order == 't':
            textArray = np.ravel(matrix, order='F')
        else:
            textArray = np.ravel(matrix)
        text = ""
        for i in range(len(textArray)):
            text = text + alphabet[textArray[i]]
        return text

    @staticmethod
    def getInverse(matrix, alphabet):
        alphabet_len = len(alphabet)
        if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
            matrix = Matrix(matrix)
            return np.matrix(matrix.inv_mod(alphabet_len))
        else:
            return None

    @staticmethod
    def decrypt(k_inverse, c, alphabet):
        return ExtensionMethods.encrypt(k_inverse, c, alphabet)
