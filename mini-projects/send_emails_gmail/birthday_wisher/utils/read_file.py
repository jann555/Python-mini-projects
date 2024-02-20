import pandas as pd
from random import choice


class CustomFileReader:
    def __init__(self, file_path='', header=True):
        self.file_path: str = file_path
        self.data_frame: pd.DataFrame = pd.DataFrame()
        self.read_csv(header)

    def __str__(self):
        return self.data_frame.to_csv(index=False, header=False)

    def __repr__(self):
        return self.data_frame[0].to_string()

    def read_csv(self, header):
        if self.file_path == '':
            print('File path is empty!')
        try:
            if header:
                df = pd.read_csv(self.file_path)
            else:
                df = pd.read_csv(self.file_path, header=None)
        except FileNotFoundError:
            print(f'File path {self.file_path} could not be located')
        else:
            self.data_frame = df

    def get_all_lines(self):
        f"""
        A list of Quotes from file
        :returns
        :return:
        """
        content = self.data_frame
        return content["text"].to_list()

    def get_random_line(self):
        """
        Random Quote from list of quotes
        :return:
        """
        lines = self.get_all_lines()
        return choice(lines) if lines != "" else lines

    def load_birthday_dict(self):
        """
        Returns a Dictionary DataFrame in orient="records"
        :return:
        """
        return {
            (data_row["month"], data_row["day"]): data_row
            for (index, data_row)
            in self.data_frame.iterrows()
        }
