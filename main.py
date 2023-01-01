import flet as ft

import lib.des.des as des
from lib.const import const
# from lib.des.des import des
from lib.hill_cipher.HillCipher import HillCipher as hc


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
# if __name__ == '__main__':
# plainText = "ABDALFTA"
# cipherText = desObj.encrypt(plainText)
# plainRes = desObj.decrypt(cipherText)
# print(cipherText)
# print(plainRes)
#
#     print("\n\n*****************************\n\n")


def main(page: ft.Page):
    page.title = "Algorithm project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    algoNameUsed = "Hill"

    def palinTextOnChange(e):
        plainText.value = plainText.value
        cipherText.value = ""

        if t.value == "Hill":
            hillAlgo(plainText.value, "enc")
        else:
            desAlgo(plainText.value, "enc")

        page.update()

    def cipherTextOnChange(e):
        plainText.value = ""
        if t.value == "Hill":
            hillAlgo(cipherText.value, "dec")

        page.update()

    def changeAlgo(e):
        plainText.value = ""
        cipherText.value = ""
        if t.value == "Hill":
            t.value = "Dess [ Text should be multiple of 8 ]"
        else:
            t.value = "Hill"
        page.update()

    def hillAlgo(inputText, typeAlgo):
        if typeAlgo == "enc":
            cipherText.value = hc.encryption(inputText)["ciphertext"]
        else:
            plainText.value = hc.decryption(inputText.upper())["plaintext"]

        page.update()

    def desAlgo(inputText, typeAlgo):

        if len(inputText) % 8 == 0:
            x = des.des(const.KEY_DES)

            if typeAlgo == "enc":
                cipherText.value = x.encrypt("ADBODADD")
                print(cipherText.value)
            else:
                plainText.value = x.encrypt(inputText)
                print(plainText.value)
        page.update()

    plainText = ft.TextField(value="", hint_text="Plain Text", text_align=ft.TextAlign.LEFT, width=700,
                             on_change=palinTextOnChange)
    cipherText = ft.TextField(value="", hint_text="Cipher Text", text_align=ft.TextAlign.LEFT, width=700,
                              on_change=cipherTextOnChange)
    t = ft.Text(value=algoNameUsed, color="white")

    algoName = ft.TextButton(text="Change Algorithm", on_click=changeAlgo)

    page.add(
        ft.Column(
            [
                t,
                plainText,
                cipherText,
                algoName,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
