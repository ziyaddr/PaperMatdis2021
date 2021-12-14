import time

def addOne(arr, length, base):
    currentIdx = length-1
    arr[currentIdx] += 1
    while arr[currentIdx] >= base:
        arr[currentIdx] %= base
        currentIdx -= 1
        arr[currentIdx] += 1
    

print("Coin Toss")
# konfigurasi
cases = 2 # jumlah kemungkinan yang terjadi dalam satu proses
caseEffect = [-10, 20]
# efek yang didapat caseEffect[0] = kasus-0 (kalah), caseEffect[0] = kasus-1 (menang)
flips = 20 # jumlah flips
totalCases = cases**flips
countRugi = 0
countUntung = 0
a = [0 for i in range(flips)] # inisialisasi kasus pertama ([0, ..., 0])

start_time = time.time()
# proses iterasi
for x in range(totalCases):
    Money = 0
    for y in range(flips):
        Money += caseEffect[a[y]]
    if (Money < 0):
        countRugi += 1
    elif (Money > 0):
        countUntung += 1
    addOne(a, flips, cases) # next case

countSama = totalCases - countUntung - countRugi # jumlah kasus sama
pUntung = round(((countUntung*100)/totalCases), 2) # persen kasus untung
pRugi = round(((countRugi*100)/totalCases), 2) # presen kasus rugi
pSama = round(((countSama*100)/totalCases), 2) # persen kasus sama

# print hasil
print("Runtime = ", round((time.time()-start_time), 1))
print("Total kasus = " + str(totalCases))
print("Kasus untung = " + str(countUntung) + " (" + str(pUntung) + "%)")
print("Kasus rugi = " + str(countRugi) + " (" + str(pRugi) + "%)")
print("Kasus sama = " + str(countSama) + " (" + str(pSama) + "%)")



