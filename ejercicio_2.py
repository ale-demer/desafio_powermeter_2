import json

repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

duplicados_1 = [x for x in repetidos if repetidos.count(x) > 1]
for num in duplicados_1:
    repetidos.remove(num)

print(repetidos)

duplicados_2 = [x for x in repetidos if x in r]

print(duplicados_2)

result_3 = json.loads(d_str)

print(result_3)
print(type(result_3))


