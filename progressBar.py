#progress bar:
import sys
def initBar():
    sys.stdout.write("[%-20s] %d%%" % ('='*0, 5*0))
    sys.stdout.flush()
    return 1, 1


def updateBar(i, j, length):
    if i > length/20 or (j==20 and i>=int(length/20)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*j, 5*j))
        sys.stdout.flush()
        i = 1
        j = j+1
    return i, j
