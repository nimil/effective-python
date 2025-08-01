from urllib.parse import parse_qs


myvalue = parse_qs("https://en.wikipedia.org/wiki?action=query&repo=shhhsd")
print(myvalue)


# 复杂的表达式 ，尤其是那种需要重复使用的复杂表达式，应该写到辅助函数里

def getValueOrDefault(dictDef,key,defaultValue="bar"):
    if key in dictDef:
        return dictDef[key]
    else:
        return defaultValue

print(getValueOrDefault(myvalue,"foo"))
print(getValueOrDefault(myvalue,"repo"))