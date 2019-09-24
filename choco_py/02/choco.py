from datetime import datetime, timedelta
import time

class Choco:

    def __init__(self, sweetness):
        self.sweetness = sweetness
        self.created_at = datetime.now() + timedelta(hours=9)

    def format_report(self):
        '''
        TODO : 초콜릿의 자기소개 만들기
        :return: str
        '''

        return ''
