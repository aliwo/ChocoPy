import openpyxl


class ExcelSheet:

    def __init__(self, file_path, start_pos):
        self.xlsx = openpyxl.Workbook(file_path)
        self.columns = self.set_columns()
        self.pos = start_pos

    def set_columns(self):
        pass

    def fill_row(self, collection):
        pass

    def write(self, collection):
        for obj in collection:
            self.fill_row(obj)
            self.pos += 1
        self.xlsx.close()
