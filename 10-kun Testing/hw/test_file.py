from random import choice, randint, shufflefrom re import subfrom string import punctuationfrom main import ContextManagertxt = '''hello_world!how_are_youh?'''class FileManager:    def __init__(self, filename):        self.file = None        self.filename = filename    def __enter__(self):        self.file = open(self.filename, 'r')        return self    def __exit__(self, exc_type, exc_value, exc_traceback):        self.file.close()    def text_edit1(self, find, change):        result = sub(find, change, self.file.read())        self.file = open(self.filename, 'w')        self.file.write(result)        return resultdef testTextEdit():    for _ in range(100):        punc = choice("¬!£$%^&*()_-?><@;:]#[{}~|=")        # print(punc)        with FileManager('matn.txt') as matn:            result1 = matn.text_edit1('_', punc)        with ContextManager('matn.txt') as matn2:            res2 = matn2.text_edit('_', punc)        assert result1 == res2        with open('matn.txt', 'r+') as file:            file.read()            f