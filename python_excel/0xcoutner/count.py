from collections import Counter
import openpyxl

favorites = []
work_book = openpyxl.load_workbook('../excels/젤루조아/favorites.xlsx')
sheet = work_book.active

for row in sheet['A2:E6']:
    for cell in row:
        if cell.value:
            favorites.append(cell.value)


counter = Counter(favorites)
print(counter.most_common(1))







