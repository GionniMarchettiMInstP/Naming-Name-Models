import numpy as np
import random
import time

# This script simulates the naming game dynamics of N interacting agents
# who can learn two names only, namely A and B.

def main():
    with open("input.txt", "r") as ins:
        inputs = []
        for line in ins:
            inputs.append(line)

    noAgents = int(inputs[0])
    nA = int(inputs[1])
    nB = int(inputs[2])
    noSteps = int(inputs[3])
    initSeed = int(inputs[4])

    print('number of Agents', noAgents)
    print('number of Simulation Steps', noSteps)
    print('initial seed', initSeed)


    xA = float(nA) / float(noAgents)
    xB = 1.0 - xA
    print('populations initial fractions nA, nB', xA, xB)

    n_up = nA + nB
    if n_up != noAgents:
        print('Error population fraction number!!')
        sys.exit('Terminate')

    print('nA, nB, n_up', nA, nB, n_up)

    def checkEqual(lst):
        return lst[1:] == lst[:-1]


    random.seed(initSeed)


    invList = [[] for a in range(0, noAgents)]
    binaryList = [0, 1]

    successRateList = [0] * noSteps
    totalWordList = [0] * noSteps


    counterA1 = 0
    counterB1 = 0
    nPart = 0

    while nPart < noAgents:
        nPart = counterA1 + counterB1
        integerR = random.sample(binaryList, 1)
        if integerR[0] == 0:
            if counterA1 < nA:
                invList[nPart].append(integerR[0])
                counterA1 = counterA1 + 1
        else:
            if counterB1 < nB:
                invList[nPart].append(integerR[0])
                counterB1 = counterB1 + 1

    print('random initialisation done')
    print(invList)



    tconv = 0

    for tsteps in range(0, noSteps):
        templist = random.sample(range(0, noAgents), 2)
        partialSum = 0

        for item in invList:
            l = len(item)
            partialSum = partialSum + l

        totalWordList[tsteps] = partialSum


        s = templist[0]
        h = templist[1]

        item = random.choice(invList[s])

        if item in invList[h]:
            del invList[s][:]
            del invList[h][:]
            invList[s].append(item)
            invList[h].append(item)
            successRateList[tsteps] = 1
        else:
            invList[h].append(item)
            successRateList[tsteps] = 0

        boolean = checkEqual(invList)
        ll = len(invList[-1])

        if boolean == True and ll == 1:
            tconv = tsteps + 1
            print('Consensus Achieved at time-step', tconv)
            print(invList)
            file_name = 'Flag' + '.txt'
            g = open(file_name, 'w')
            print(tconv, file=g)
            break




    if tconv == 0:
        print('Consensus Not Achieved')


    totalWordArray = np.array(totalWordList)
    maxTotWord = np.amax(totalWordArray)
    print('maximum of  total number of words', maxTotWord)
    successRateArray = np.array(successRateList)


    for j in range(tconv, noSteps):
        totalWordArray[j] = noAgents
        successRateArray[j] = 1

    np.save('successRate.dat', successRateArray)
    np.save('totalWord.dat', totalWordArray)


    filename = 'results' + '.txt'
    f = open(filename, 'w')
    print('0-nA, 1-nB, winning', 0, nA, 1, nB, invList[0], file=f)
    print('Overall Simulation time', noSteps, file=f)
    print('Convergence time', tconv, file=f)
    print('Max Total Number Words', maxTotWord, file=f)
    print('Seed', initSeed, file=f)
    print('Current Date and Time ' + time.strftime("%c"), file=f)


if __name__ == '__main__':
    start = time.time()
    main()
    print('total time %s sec' % (round(time.time() - start, 1)))
