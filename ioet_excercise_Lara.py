from datetime import datetime, time
from collections import namedtuple
from itertools import combinations

def set_range_schedules(data_dic):	
    for key in data_dic.keys():
        aux_dict = {}
        for i in data_dic[key]:
            start = datetime.strptime(i[2:].split(sep="-")[0], "%H:%M").time()
            end = datetime.strptime(i[2:].split(sep="-")[1], "%H:%M").time()
            aux_dict[i[:2]] = start, end
            data_dic[key] = aux_dict
    return data_dic

def open_txt_file(file_name):
    try:
        file = open(file_name,"r").read().splitlines()
    except FileNotFoundError:
        print("Wrong file or file path")        
    data_dic = {line.split(sep="=")[0] : line.split(sep="=")[1].split(sep=",") for line in file}
    return set_range_schedules(data_dic)

def is_overleap(data_dic):
    output = ""
    for (name_0, days_work_0), (name_1, days_work_1) in combinations(data_dic.items(),r=2):
        common = days_work_0.keys() & days_work_1.keys()
        cont=0
        for key in common:
            Range = namedtuple('Range',['start', 'end'])
            r1 = Range(start = data_dic[name_0][key][0], end = data_dic[name_0][key][1])
            r2 = Range(start = data_dic[name_1][key][0], end = data_dic[name_1][key][1])
            if (r1.start < r2.end ) and (r1.end > r2.start):
                cont += 1
        output += f'{name_0}-{name_1}: {cont}\n'
    return output


'''Change file name for another test'''
file = "input_data_ACME_3.txt"
data = open_txt_file(file)
result =is_overleap(data)
print(result)