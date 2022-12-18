import datetime

from const import const


def converterToListOfBit(inputText):
    array = []
    for i in inputText:
        binaryValue = binValue(i, 8)
        array.extend([int(j) for j in list(binaryValue)])
    return array


def converterToString(inputArray):
    response = ''.join(
        [chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in spiltList(inputArray, 8)]])
    return response


def binValue(value, bitSize):
    binVal = bin(value)[2:] if isinstance(value, int) else bin(ord(value))[2:]
    if len(binVal) > bitSize:
        print("binary value larger than the expected size")
    while len(binVal) < bitSize:
        binVal = "0" + binVal
    return binVal


def spiltList(inputList, numberSize):
    return [inputList[k:k + numberSize] for k in range(0, len(inputList), numberSize)]


ENCRYPT = 1
DECRYPT = 0


class Des:

    def __init__(self):
        self.keys = None

    def run(self, key, text, status, action=ENCRYPT):
        if len(text) % 8 != 0:
            return {"message": "Data size should be multiple of 8", "plainText": "", "cipherText": "", "status": False}

        self.generateKeys()
        text_blocks = spiltList(text, 8)
        result = list()
        for block in text_blocks:
            block = converterToListOfBit(block)
            block = self.permitMethod(block, const.PI)
            firstList, secList = spiltList(block, 32)
            for i in range(16):
                expandTxtResult = self.expandPalinText(secList, const.E)
                if action == ENCRYPT:
                    xorResult = self.xorMethod(self.keys[i], expandTxtResult)
                else:
                    xorResult = self.xorMethod(self.keys[15 - i], expandTxtResult)
                xorResult = self.substitute(xorResult)
                xorResult = self.permitMethod(xorResult, const.P)
                xorResult = self.xorMethod(firstList, xorResult)
                firstList = secList
                secList = xorResult
            result += self.permitMethod(secList + firstList, const.PI_1)
        final_res = converterToString(result)

        if status == 0:
            return {"plainText": text, "cipherText": final_res, "key": key, "data": datetime.datetime.now(),
                    "algo": "des", "status": True}
        else:
            return {"plainText": final_res, "cipherText": text, "key": key, "data": datetime.datetime.now(),
                    "algo": "des", "status": True}

    def substitute(self, inputTxt):
        subBlocks = spiltList(inputTxt, 6)
        result = []
        for i in range(len(subBlocks)):
            block = subBlocks[i]
            row = int(str(block[0]) + str(block[5]), 2)
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)
            S_BOXValue = const.S_BOX[i][row][column]
            binaryValue = binValue(S_BOXValue, 4)
            result += [int(binV) for binV in binaryValue]
        return result

    def permitMethod(self, block, table):
        return [block[x - 1] for x in table]

    def expandPalinText(self, block, table):
        return [block[x - 1] for x in table]

    def xorMethod(self, firstText, secText):
        return [x ^ y for x, y in zip(firstText, secText)]

    def generateKeys(self):
        self.keys = []
        key = converterToListOfBit(const.KEY_DES)
        key = self.permitMethod(key, const.CP_1)
        firstList, secList = spiltList(key, 28)
        for i in range(16):
            firstList, secList = self.shift(firstList, secList, const.SHIFT[i])
            tmp = firstList + secList
            self.keys.append(self.permitMethod(tmp, const.CP_2))

    def shift(self, g, d, n):
        return g[n:] + g[:n], d[n:] + d[:n]

    def encrypt(self, key, text, status):
        return self.run(key, text, status, ENCRYPT)

    def decrypt(self, key, text, status):
        return self.run(key, text, status, DECRYPT)
