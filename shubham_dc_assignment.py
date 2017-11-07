import matplotlib.pyplot as plt
print('----LINE CODING----')
print("")
print('1.NRZ-UNIPOLAR')
print('2.NRZ-L')
print('3.NRZ-I')
print('4.MANCHESTER')
print('5.DIFFERENTIAL-MANCHESTER')
print('6.AMI')
print('')
choice=int(input('Enter your choice:'))


x = list()
y = list()
str = input("Enter Bits:")
num = len(str)

for i in range(num):
    y.append(int(str[i]))


if choice==1:
    ### NRZ,Unipolar
    for j in range(num):
        x.append(int(j))

    x = x*2
    x.sort()
    x.remove(x[0])
    x.append(num)
    m = []
    for k in y:
        m.extend([k, k])
    y = m
    zeros = list()
    for i in range(2 * num):
        zeros.append(int(0))

    l = list()
    for i in range(1, num + 1):
        l.append(int(i))

    print(zeros)
    print(x)
    print(y)

    plt.plot(x, y, linewidth=5.0)
    plt.plot(x, zeros, linewidth=1.0)
    plt.grid()
    plt.plot([0, 0], [0, 1.5])
    plt.title("NRZ-UNIPOLAR")
    plt.show()
    ############
if choice==2:
    ### NRZL,Polar

    for j in range(num):
        x.append(int(j))

    for i in range(num):
        if y[i] == 0:
            y[i] = 1
        else:
            y[i] = -1

    x=x*2
    x.sort()
    x.remove(x[0])
    x.append(num)
    m = []
    for k in y:
        m.extend([k, k])
    y = m

    print(x)
    print(y)

    zeros = list()
    for i in range(2 * num):
        zeros.append(int(0))

    print(zeros)

    plt.plot(x, y, linewidth=5.0)
    plt.plot(x, zeros, linewidth=1.0)
    plt.plot([0, 0, 0], [0, 1.5, -1.5])
    plt.grid()
    plt.title("NRZ-L")
    plt.show()
    ##########
if choice==3:
    ### NRZ-I
    for j in range(num):
        x.append(int(j))


    for i in range(num - 1):
        if i == 0:
            y[i] = 1
        if y[i + 1] == 1:
            if y[i] == 1:
                y[i + 1] = -1
            elif y[i] == -1:
                y[i + 1] = 1
        elif y[i + 1] == 0:
            if y[i] == 1:
                y[i + 1] = 1
            elif y[i] == -1:
                y[i + 1] = -1

    print(y)
    print(x)
    x = x*2
    x.sort()
    x.remove(x[0])
    x.append(num)
    m = []
    for k in y:
        m.extend([k, k])
    y = m
    zeros = list()
    for i in range(2 * num):
        zeros.append(int(0))

    plt.plot(x, y, linewidth=5.0)
    plt.plot(x, zeros, linewidth=1.0)
    plt.plot([0, 0, 0], [0, 1.5, -1.5])
    plt.grid()
    plt.title("NRZ-I:-POLAR")
    plt.show()
    ##############
if choice==4:
    ##Manchester

    yaxis = list()
    for i in range(0, num):
        if y[i] == 1:
            yaxis.append(-1)
            yaxis.append(1)
        if y[i] == 0:
            yaxis.append(1)
            yaxis.append(-1)
    print(yaxis)

    x = []
    for i in range(2 * num):
        x.append(i)
    x = x * 2
    x.sort()
    x.remove(x[0])
    x.append(2 * num)

    m = []
    for i in yaxis:
        m.extend([i, i])
    yaxis = m
    print(yaxis)
    print(x)

    zeros = list()
    for i in range(0, 4 * num):
        zeros.append(int(0))

    print(zeros)

    plt.plot(x, yaxis, linewidth=5.0)
    plt.plot(x, zeros, linewidth=1.0)
    plt.plot([0, 0, 0], [0, 1.5, -1.5])
    plt.grid()
    plt.title("MANCHESTER")
    plt.show()
    #######
if choice==5:
    ##D Manchester

    print(y)
    yaxis = list()
    for i in range(num - 1):
        if i == 0:
            if y[i] == 1:
                yaxis.append(1)
                yaxis.append(-1)
            elif y[i] == 0:
                yaxis.append(-1)
                yaxis.append(1)
        if y[i + 1] == 0:
            if yaxis[-1] == -1:
                yaxis.append(1)
                yaxis.append(-1)
            elif yaxis[-1] == 1:
                yaxis.append(-1)
                yaxis.append(1)
        if y[i + 1] == 1:
            if yaxis[-1] == -1:
                yaxis.append(-1)
                yaxis.append(1)
            elif yaxis[-1] == 1:
                yaxis.append(1)
                yaxis.append(-1)

    print(yaxis)
    m = []
    for i in yaxis:
        m.extend([i, i])
    yaxis = m
    for i in range(2 * num):
        x.append(i)
    x = x * 2
    x.sort()
    x.remove(x[0])
    x.append(2 * num)
    print(x)
    print(yaxis)

    zeros = list()
    for i in range(0, 4 * num):
        zeros.append(int(0))

    plt.plot(x, yaxis, linewidth=5.0)
    plt.plot(x, zeros, linewidth=1.0)
    plt.plot([0, 0, 0], [0, 1.5, -1.5])
    plt.grid()
    plt.title("DIFFERENTIAL-MANCHESTER")
    plt.show()
    #######
if choice==6:
    ##AMI
    for j in range(num):
        x.append(int(j))
    print(y)

    for i in range(len(y)):
        if y[i] == 1:
            for j in range(i - 1, -1, -1):
                if y[j] == 1:
                    y[i] = -1
                    break
                elif y[j] == -1:
                    y[i] = 1
                    break
    print(y)
    x1=list()
    y1=list()
    y1=y
    x1=x
    x=x*2
    x.sort()
    x.remove(x[0])
    x.append(num)
    m = []
    for k in y:
        m.extend([k, k])
    y = m

    zeros = list()
    for i in range(2 * num):
        zeros.append(int(0))

    ###AMI
    plt.plot(x, y, linewidth=5.0)
    plt.plot(x, zeros, linewidth=1.0)
    plt.plot([0, 0, 0], [0, 1.5, -1.5])
    plt.grid()
    plt.title("AMI")
    plt.show()
    ###########SCRAMBLING#############
    scr=input('Do you want to scramble this signal:[y/n]')
    if scr=='y':
        print('1.B8ZS')
        print('2.HDB3')
        ch=int(input('Enter scrambling scheme:'))
        if ch==1:
            ###
            l = str.find('00000000')
            for i in range(l):
                if y1[i] == 1:
                    for j in range(i - 1, -1, -1):
                        if y1[j] == 1:
                            y1[i] = -1
                            break
                        elif y1[j] == -1:
                            y1[i] = 1
                            break

            if (l != -1):
                for i in range(l, -1, -1):
                    if y1[i] == 1:
                        y1[l + 3] = 1
                        y1[l + 4] = -1
                        y1[l + 5] = 0
                        y1[l + 6] = -1
                        y1[l + 7] = 1
                        break
                    if y1[i] == -1:
                        y1[l + 3] = -1
                        y1[l + 4] = 1
                        y1[l + 5] = 0
                        y1[l + 6] = 1
                        y1[l + 7] = -1
                        break
            else:
                print('Not applicable!!')

            for i in range(l, len(str)):
                if y1[i] == 1:
                    for j in range(i - 1, l + 7, -1):
                        if y1[j] == 1:
                            y1[i] = -1
                            break
                        elif y1[j] == -1:
                            y1[i] = 1
                            break

            print(y1)
            m = []
            for i in y1:
                m.extend([i, i])
            y1 = m

            x1 = x1 * 2
            x1.sort()
            x1.remove(x1[0])
            x1.append(len(str))
            print(x1)
            print(y1)
            print(l)

            zeros = list()
            for i in range(2 * len(str)):
                zeros.append(0)

            ###B8ZS
            plt.plot(x1, y1, linewidth=5.0)
            plt.plot(x1, zeros, linewidth=1.0)
            plt.plot([0, 0, 0], [0, 1.5, -1.5])
            plt.grid()
            plt.title("B8ZS")
            plt.show()
            #########
        if ch==2:
            ####
            l = str.find('0000')
            ones = str.count('1',0,l)
            for i in range(l):
                if y1[i] == 1:
                    for j in range(i - 1, -1, -1):
                        if y1[j] == 1:
                            y1[i] = -1
                            break
                        elif y1[j] == -1:
                            y1[i] = 1
                            break

            if (l != -1):
                if ones % 2 == 0:
                    y1[l] = 1
                    y1[l+1] = 0
                    y1[l+2] = 0
                    y1[l+3] = 1
                elif ones % 2 != 0:
                    y1[l] = 0
                    y1[l+1] = 0
                    y1[l+2] = 0
                    y1[l+3] = -1
            else:
                print('Not applicable!!')
                exit()

            print(y1)
            m = []
            for i in y1:
                m.extend([i, i])
            y1 = m

            x1 = x1 * 2
            x1.sort()
            x1.remove(x[0])
            x1.append(len(str))
            print(x1)
            print(y1)
            print(l)

            zeros = list()
            for i in range(2 * len(str)):
                zeros.append(int(0))

            ###HDB3
            plt.plot(x1, y1, linewidth=5.0)
            plt.plot(x1, zeros, linewidth=1.0)
            plt.plot([0, 0, 0], [0, 1.5, -1.5])
            plt.grid()
            plt.title("HDB3")
            plt.show()

    if scr=='n':
        exit()



