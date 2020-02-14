
def segitigakata(y):
    z = ''
    x = 0
    kata = y.replace(' ', '')
    # Pola Segitiga
    pola = list(map(lambda row: row * (row + 1)/2, range(len(kata))))
    pola = list(map(int, pola))

    # Bentuk segitiga kata
    if len(kata) not in pola:
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
    else:
        for i in range(pola.index(len(kata))):
            for j in range(pola[i], pola[i + 1]):
                z += f"{kata[j]} "
                x += 1
            z += '\n'
        # print(z)

    return z

print(segitigakata('Purwadhika'))
print(segitigakata('Purwadhika Startup and Coding School @BSD'))
print(segitigakata('kode'))
print(segitigakata('kode python'))
print(segitigakata('Lintang'))

#import xlrd
#import xlsxwriter
#book = xlsxwriter.Workbook('Ujian_SegitigaExcel.xlsx')
#sheet = book._add_sheet('python to excel')


