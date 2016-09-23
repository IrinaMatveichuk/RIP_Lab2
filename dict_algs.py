def childrenunder18(masdic):
    mas = []
    for dic in masdic:
        for child in dic['children']:
            if child['age'] > 18:
                mas.append(dic['name'])
                break
    return mas

ivan = {
    "name" : "ivan",
    "age" : 34,
    "children" : [{
        "name" : "vasja",
        "age" : 20,
    }, {
        "name" : "petja",
        "age" : 14,
    }],
}

darja = {
    "name": "darja",
    "age" : 41,
    "children" : [{
        "name" : "kirill",
        "age" : 21,
    }, {
        "name" : "pavel",
        "age" : 20,
    }],
}

emps = [ivan, darja]
print(childrenunder18(emps))