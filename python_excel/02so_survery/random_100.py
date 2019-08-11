# 스택 오버플로우 설문 조사에서 랜덤한 100개의 결과만 뽑아봅시다.
# 뽑아낸 정보는 random_100.xlsx 에 저장해 봐요.
import openpyxl
import random

work_book = openpyxl.load_workbook('../excels/so_2019/survey_results_schema.xlsx')
sheet = work_book.active

length = len(sheet['A']) # 설문의 개수를 구합니다.

for _ in range(3):
    chosen = random.choice(range(2, length))
    for cell in sheet[chosen]:
        print(cell.value)







