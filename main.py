import lib.des.des as desImport
from lib.hill_cipher import HillCipher as hc
import lib.const.const as const

# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
#
#
# @app.route("/hill/encryption", methods=['POST'])
# def encryption():
#     try:
#         plainText = request.form["plainText"]
#         plainText = hc.HillCipher.encryption(plainText.upper())
#         return plainText
#     except:
#         return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}
#
#
# @app.route("/hill/decryption", methods=['POST'])
# def decryption():
#     try:
#         cipherText = request.form["cipherText"]
#         cipherText = hc.HillCipher.decryption(cipherText.upper())
#         return cipherText
#     except:
#         return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}
#
#
# @app.route("/des/encryption", methods=['POST'])
# def encryptionDes():
#     try:
#         dsiObj = Des()
#         plainText = request.form["plainText"]
#         print(plainText)
#         plainText = dsiObj.encrypt(const.KEY_DES, plainText, 0)
#         return plainText
#     except:
#         return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}
#
#
# @app.route("/des/decryption", methods=['POST'])
# def decryptionDes():
#     try:
#         dsiObj = Des()
#         cipherText = request.form["cipherText"]
#         print(cipherText == "ÿ< yÎT)\\x9eÿ< yÎT)\\x9e")
#         print("ÿ< yÎT)\x9eÿ< yÎT)\x9e")
#         cipherText = dsiObj.decrypt(const.KEY_DES, f'{cipherText}', 1)
#         return cipherText
#     except:
#         return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}


if __name__ == '__main__':
    plainText = "ABDALFTA"
    x = desImport.des(const.KEY_DES)
    c = x.encrypt(plainText)
    print(c)
    e = x.decrypt(c)
    print(e)

    print(x.encrypt(e))

    print("\n\n*****************************\n\n")
