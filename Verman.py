pt = input("PLAINTEXT:\t")
otp = input("key:\t")
ptList = list()
otpList = list()
uPt = pt.upper()
updatedOtp = otp.upper()

for character1 in uPt:
    temp1 = ord(character1) - 65
    ptList.append(temp1)

for character2 in updatedOtp:
    temp1 = ord(character2) - 65
    otpList.append(temp1)

for number in ptList:
    if (number < 0):
        ptList.remove(number)

for number in otpList:
    if (number < 0):
        otpList.remove(number)


tempList = [i + j for i, j in zip(ptList, otpList)]

ctList = []
for item in tempList:
    if (item > 25):
        item -= 26
        ctList.append(item)
    else:
        ctList.append(item)

sadiq = ""
for number in ctList:
    number += 65
    temp = chr(number)
    tempstr = str(temp)
    sadiq = sadiq + tempstr

print("CIPHERTEXT:\t", sadiq.lower())
