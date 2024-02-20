import pandas as pd
from random import choice


class CustomFileReader:
    def __init__(self, file_path=''):
        self.file_path: str = file_path
        self.data_frame = {}

    def read_csv(self):
        if self.file_path == '':
            return ""
        try:
            df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f'File path {self.file_path} could not be located')
        else:
            self.data_frame = df

    def get_all_quotes(self):
        f"""
        A list of Quotes from file
        :returns
        :return:
        """
        self.read_csv()
        content = self.data_frame
        return content["quotes"].to_list()

    def get_random_quote(self):
        """
        Random Quote from list of quotes
        :return:
        """
        quotes = self.get_all_quotes()
        return choice(quotes) if quotes != "" else quotes
