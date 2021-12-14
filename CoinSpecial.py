import time
import math
from itertools import combinations, count

def addOne(arr, length, base):
    currentIdx = length-1
    arr[currentIdx] += 1
    while arr[currentIdx] >= base:
        arr[currentIdx] %= base
        currentIdx -= 1
        arr[currentIdx] += 1
    

print("Coin flip")
flips = 400 # diubah sesuai jumlah flips

cases = 2
caseEffect = [-10, 20]
#caseEffect = [-850, -700, -550, -400, -250, -100, 50, 200, 350, 500, 650, 800, 950, 1100, 1250, 1400, 1550, 1700, 1850, 2000, 2000, 2000, 2000, 2000, 2000]
totalCases = cases**flips
countRugi = 0
countUntung = 0



a = [0 for i in range(flips)]


start_time = time.time()
"""
for x in range(totalCases):
    Money = 0
    for y in range(flips):
        Money += caseEffect[a[y]]
    if (Money < 0):
        countRugi += 1
    elif (Money > 0):
        countUntung += 1
    addOne(a, flips, cases)
"""
# kasus untung jika (banyak 1 * keuntungan) > (banyak 0 * kerugian)
untungPerRugi = caseEffect[1] / abs(caseEffect[0])
ratioSama = 1 - untungPerRugi/(untungPerRugi+1)
sama1s = ratioSama*flips



# untung -> jumlah 1 > sama1s
# sama -> jumlah 1 = sama1s
# rugi -> jumlah 1 < sama1s
countUntung = 0
countRugi = 0
if math.floor(sama1s) == math.ceil(sama1s):
    sama1s = math.floor(sama1s)
    countSama = math.perm(flips, flips)/(math.factorial(sama1s)*math.factorial(flips-sama1s))
    batasBawahUntung = sama1s + 1
    batasAtasRugi = sama1s
else:
    countSama = 0
    batasBawahUntung = math.ceil(sama1s)
    batasAtasRugi = math.floor(sama1s) + 1
if ratioSama < 0.5:
    for i in range(0, batasAtasRugi):
        countRugi += math.perm(flips, flips)/(math.factorial(i)*math.factorial(flips-i))
    countUntung = totalCases - countSama - countRugi
else:
    for i in range(batasBawahUntung, flips+1):
        countUntung += math.perm(flips, flips)/(math.factorial(i)*math.factorial(flips-i))
    countRugi = totalCases - countSama - countUntung

pUntung = round(((countUntung*100)/totalCases), 10)
pRugi = round(((countRugi*100)/totalCases), 10)
pSama = round(((countSama*100)/totalCases), 10)

print("Runtime = ", round((time.time()-start_time), 1))
print("Total kasus = " + "{:.3e}".format(totalCases))
print("Kasus untung = " + "{:.3e}".format(countUntung) + " (" + str(pUntung) + "%)")
print("Kasus rugi = " + "{:.3e}".format(countRugi) + " (" + str(pRugi) + "%)")
print("Kasus sama = " + "{:.3e}".format(countSama) + " (" + str(pSama) + "%)")



