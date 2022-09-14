import numpy as np
import matplotlib.pyplot as plt
import json
  
# Opening JSON file
f = open('8B6T.json')
dic8B6T = json.load(f)

positive2BQ1 = {
  "00": 1,
  "01": 3,
  "10": -1,
  "11": -3
}

negative2BQ1 = {
  "00": -1,
  "01": -3,
  "10": 1,
  "11": 3
}

dic4DPAM5 = {
  "00": -2,
  "01": 1,
  "10": -1,
  "11": 2
}

def plotSignal(arrayAmplitude,period,name,startTime=0):
    xAxle = []
    yAxle = []
    time = startTime
    for amplitude in arrayAmplitude:
        xAxle.append(amplitude)
        yAxle.append(time)
        time +=period
        xAxle.append(amplitude)
        yAxle.append(time)
    plt.plot(yAxle,xAxle)
    plt.plot([0,0],[10,-10])
    plt.grid()
    plt.title(name)
    plt.show()

def generate2B1Q(binarySequence):
    arrayAmplitude = [1]
    if len(binarySequence) % 2==1:
        binarySequence = '0'+binarySequence
    loops = int(len(binarySequence)/2)
    for i in range(loops):
        if(arrayAmplitude[-1]>0):
            # print(positive2BQ1[binarySequence[0:2]] , binarySequence[0:2])
            arrayAmplitude.append(positive2BQ1[binarySequence[0:2]])
            
        else:
            # print(negative2BQ1[binarySequence[0:2]] , binarySequence[0:2])
            arrayAmplitude.append(negative2BQ1[binarySequence[0:2]])
        binarySequence = binarySequence[2:]
    return (arrayAmplitude)

def generate8B6T(hexSequence):
    arrayAmplitude = []
    lastSum=0
    loops = int(len(hexSequence)/2)
    for i in range(loops):
        if(sum(dic8B6T[hexSequence[0:2]])==1 and lastSum==1):
            arrayAmplitude += [item * -1 for item in dic8B6T[hexSequence[0:2]]]
        else :
            arrayAmplitude += dic8B6T[hexSequence[0:2]]
        lastSum = sum(dic8B6T[hexSequence[0:2]])
        hexSequence = hexSequence[2:]
    return (arrayAmplitude)

def generate4DPAM5(binarySequence):
    arrayAmplitude = []
    if len(binarySequence) % 2==1:
        binarySequence = '0'+binarySequence
    loops = int(len(binarySequence)/2)
    for i in range(loops):
        arrayAmplitude.append(dic4DPAM5[binarySequence[0:2]])
        # print(binarySequence[0:2], dic4DPAM5[binarySequence[0:2]])
        binarySequence = binarySequence[2:]
    return (arrayAmplitude)

def generateMLT3(binarySequence):
    arrayAmplitude = [0]
    lastNonZero = -1
    for binary in (binarySequence):
        # print(binary +' ', end='')
        if(binary=='0'):
            # print("binario = 0")
            arrayAmplitude.append(arrayAmplitude[-1])
        elif(arrayAmplitude[-1]!=0):
            # print("anterior diferente de 0")
            arrayAmplitude.append(0)
        else:
            if(lastNonZero>0):
                # print("anterior nao zero positivo")
                arrayAmplitude.append(-1)
                lastNonZero = -1
            else:
                # print("anterior nao zero negativo")
                arrayAmplitude.append(1)
                lastNonZero = 1
    return (arrayAmplitude)
    
def generateBinarySequence(string):
    binarySequence = ''
    for char in string:
        binarySequence+= str(bin(ord(char)))[2:]
    return binarySequence

def generateHexadecimalSequence(string):
    hexSequence = ''
    for char in string:
        hexSequence+= str(hex(ord(char)))[2:]
    return hexSequence

string = str(input("enter your ascii string: "))
binarySequence = generateBinarySequence(string)
hexSequence = generateHexadecimalSequence(string)

plotSignal(generate2B1Q(binarySequence),1,"2B1Q",-1)
plotSignal(generate8B6T(hexSequence),1,"8B6T")
plotSignal(generate4DPAM5(binarySequence),1,"4DPAM5")
plotSignal(generateMLT3(binarySequence),1,"MLT3",-1)