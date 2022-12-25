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
#     plainText = "ABDALFTA"
#     desObj = desImport.des(const.KEY_DES)
#     cipherText = desObj.encrypt(plainText)
#     plainRes = desObj.decrypt(cipherText)
#     print(cipherText)
#     print(plainRes)
#
#     print("\n\n*****************************\n\n")
import flet as ft

from lib.hill_cipher.HillCipher import HillCipher as hc


def main(page: ft.Page):
    page.title = "Flet counter example"
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
            t.value = "Dess"
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
        if typeAlgo == "enc":
            cipherText.value = hc.encryption(inputText)["ciphertext"]
        else:
            plainText.value = hc.decryption(inputText)["plaintext"]

        page.update()

    plainText = ft.TextField(value="", hint_text="Plain Text", text_align=ft.TextAlign.LEFT, width=700,
                             on_change=palinTextOnChange)
    cipherText = ft.TextField(value="", hint_text="Cipher Text", text_align=ft.TextAlign.LEFT, width=700,
                              on_change=cipherTextOnChange)
    t = ft.Text(value=algoNameUsed, color="white")

    algoName = ft.TextButton(text="Change Algo", on_click=changeAlgo)

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
