import datetime

from lib.const import const
from lib.hill_cipher import ExtensionMethods


class HillCipher:

    @staticmethod
    def encryption(plaintext):
        alphabet, reverse_alphabet = ExtensionMethods.ExtensionMethods.getAlphabet()
        key = ExtensionMethods.ExtensionMethods.getText(const.KEY_HILL, alphabet)
        if ExtensionMethods.ExtensionMethods.isSquareMatrix(key):
            key = ExtensionMethods.ExtensionMethods.getKeyMatrix(key, alphabet)
            plainText = ExtensionMethods.ExtensionMethods.getTextMatrix(plaintext.upper(), key.shape[0], alphabet)
            cipherText = ExtensionMethods.ExtensionMethods.encrypt(key, plainText, alphabet)
            ciphertext = ExtensionMethods.ExtensionMethods.matrixToText(cipherText, "t", reverse_alphabet)
            return {"status": True, "message": "The request send successfully", "datetime": datetime.datetime.now(),
                    "ciphertext": ciphertext}
        else:
            return {"status": False, "message": "The key is not invertible", "datetime": datetime.datetime.now()}

    @staticmethod
    def decryption(ciphertext):
        alphabet, reverse_alphabet = ExtensionMethods.ExtensionMethods.getAlphabet()
        key = ExtensionMethods.ExtensionMethods.getText(const.KEY_HILL, alphabet)
        if ExtensionMethods.ExtensionMethods.isSquareMatrix(key):
            key = ExtensionMethods.ExtensionMethods.getKeyMatrix(key, alphabet)
            k_inverse = ExtensionMethods.ExtensionMethods.getInverse(key, alphabet)
            if k_inverse is not None:
                cipherCode = ExtensionMethods.ExtensionMethods.getTextMatrix(ciphertext, k_inverse.shape[0],
                                                                             alphabet)
                palinCode = ExtensionMethods.ExtensionMethods.decrypt(k_inverse, cipherCode, alphabet)
                plaintext = ExtensionMethods.ExtensionMethods.matrixToText(palinCode, "t", reverse_alphabet)
                if len(ciphertext) <= 2:
                    return {"status": True,
                            "message": "The request send successfully", "datetime": datetime.datetime.now(),
                            "plaintext": plaintext}

                elif len(plaintext) % 2 == 0:
                    return {"status": True,
                            "message": "The request send successfully", "datetime": datetime.datetime.now(),
                            "plaintext": plaintext[: -1]}

                else:
                    return {"status": True,
                            "message": "The request send successfully", "datetime": datetime.datetime.now(),
                            "plaintext": plaintext}
            else:
                return {"status": False,
                        "message": "The key is not invertible", "datetime": datetime.datetime.now(),
                        "plaintext": ""}
        else:
            return {"status": False,
                    "message": "The key is not square", "datetime": datetime.datetime.now(),
                    "plaintext": ""}
