import csv
from django.conf import settings
from datetime import datetime
import os


# Функция для записи в csv файл
class WriteToCsv:
    # file_name, title, data_list[]
    def __init__(self, file_name, title, data):
        self.file_name = file_name
        self.title = title
        self.data = data
    
    def write(self):
        path = f"media/reports/{str(datetime.today().date())}"
        os.mkdir(f'{path}')
        with open(f'{path}/{self.file_name}', 'w') as file:
            report = csv.writer(file)
            report.writerow(self.title)
            for item in self.data:
                report.writerow(item)
а