import pandas as pd

class Reader:
    pass

class XLSLReader(Reader):

    @classmethod
    def read(cls, filepath):
        xl_file = pd.read_excel(filepath)
        return xl_file

class XLSLMCMReader(XLSLReader):
    pass


class CSVReader(Reader):
    @classmethod
    def read(cls, filepath):
        xl_file = pd.read_csv(filepath)
        return xl_file