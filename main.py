import datetime

from flask import Flask, request

from lib.const import const
from lib.des.des import Des
from lib.hill_cipher import HillCipher as hc

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/hill/encryption", methods=['POST'])
def encryption():
    try:
        plainText = request.form["plainText"]
        plainText = hc.HillCipher.encryption(plainText.upper())
        return plainText
    except:
        return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}


@app.route("/hill/decryption", methods=['POST'])
def decryption():
    try:
        cipherText = request.form["cipherText"]
        cipherText = hc.HillCipher.decryption(cipherText.upper())
        return cipherText
    except:
        return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}


@app.route("/des/encryption", methods=['POST'])
def encryptionDes():
    try:
        dsiObj = Des()
        plainText = request.form["plainText"]
        print(plainText)
        plainText = dsiObj.encrypt(const.KEY_DES, plainText, 0)
        return plainText
    except:
        return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}


@app.route("/des/decryption", methods=['POST'])
def decryptionDes():
    try:
        dsiObj = Des()
        cipherText = request.form["cipherText"]
        print(cipherText == "ÿ< yÎT)\\x9eÿ< yÎT)\\x9e")
        print("ÿ< yÎT)\x9eÿ< yÎT)\x9e")
        cipherText = dsiObj.decrypt(const.KEY_DES, f'{cipherText}', 1)
        return cipherText
    except:
        return {"status": False, "message": "The request failed", "datetime": datetime.datetime.now()}



if __name__ == '__main__':
    plainText = "ABDALFTAABDALFTA"
    dsiObj = Des()
    print("DES : ")
    cipherRes = dsiObj.encrypt(const.KEY_DES, plainText, 0)
    plainRes = dsiObj.decrypt(const.KEY_DES, cipherRes["cipherText"], 1)
    print(f'ENC : {cipherRes["plainText"]}')
    print(f'DEC : {plainRes["cipherText"]} \n\n')

    print("Hill : ")
    cipherText = hc.HillCipher.encryption("Adel jarour")["ciphertext"]
    print(f'ENC  : {cipherText}')
    print(f'DEC  : {hc.HillCipher.decryption(cipherText)["plaintext"]}')
