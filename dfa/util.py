from array import array
from .dfas import DFA, oneCharDFA


def readFile(source):
    file = open(source)
    return file.read().splitlines()


def identifyToken(token: str, dfas: list[DFA] | list[oneCharDFA]):
    for dfa in dfas:
        if dfa.process_token(token):
            return dfa.name
    return "Error"


def separateTokens(lines):
    tokens = []
    for line in lines:
        comment = None
        if "//" in line:
            index = line.find("//")
            comment = line[index::]
            s = line[:index]

        else:
            s = line
        s = s.replace("*", f" * ")
        s = s.replace("(", f" ( ")
        s = s.replace(")", f" ) ")
        s = s.replace("^", f" ^ ")
        s = s.replace("=", f" = ")
        s = s.split(" ")
        for el in s:
            if len(el) > 0:
                tokens += [el]
        if comment:
            tokens += [comment]
    return tokens


def getTokens(source):
    lines = readFile(source)
    tokens = separateTokens(lines)
    return tokens
    # Lista que almacena tokens separados
