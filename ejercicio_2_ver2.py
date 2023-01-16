import json

repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

rep_set = set(repetidos)
print(list(rep_set))

inter_set = rep_set.intersection(set(r))
print(list(inter_set))

result_3 = json.loads(d_str)
print(result_3)
print(type(result_3))


