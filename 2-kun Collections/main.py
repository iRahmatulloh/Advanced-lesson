from collections import Counter, deque, ChainMap, namedtuple, defaultdictfrom os import systemsystem('cls')x = {'uz' : 'salom'}y = {'en': 'hi'}combined = ChainMap(x, y)# print(combined['uz'])ls = [1,2,3,2]res = dict()for i in ls:    if i in res:        res[i] += 1    else:        res[i] = 1# print(res)## count ning boshqacha uslubi# print(dict(Counter(ls)))ls = deque([1,2,8,9], maxlen=6)ls.append(3)ls.append(4)ls.append(5)# print(list(ls))    #   namedtuple()Student = namedtuple('Student', [    'name',    'age',    'school'])rahmatjon = Student('Rahmatjon', 17, 'TUM')john = Student('John', 21, 'Cambridge University')# print(rahmatjon)    # defaultdictmavjudlar = defaultdict(lambda : 0)mavjudlar['otabek'] = 1mavjudlar['john'] = 2# print(mavjudlar[23])fruits = ['olma', 'banan', 'olma', 'olma']sanoq = defaultdict(int)for i in fruits:    sanoq[i] += 1print(dict(sanoq))