class DFA:
    alphabets = {
        "#": set("123456789"),
        "A": set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"),

    }

    def __init__(self, **kwargs) -> None:
        # if set("transition_table", "valid_states", "name") != set(kwargs.keys):
        #     raise("Missing arguments")

        self.transition_table = kwargs["transition_table"]
        self.valid_states = kwargs["valid_states"]
        self.name = kwargs["name"]
        pass

    def process_token(self, token: str) -> bool:
        # Replace all chars of an ALPHABET with an identifier

        newToken = ""
        for i in range(len(token)):
            if token[i] in self.alphabets["#"]:
                newToken += "#"
            elif token[i] in self.alphabets["A"] and token[i] not in self.transition_table:
                newToken += "A"
            else:
                newToken += token[i]

        token = newToken
        # ( X = 0 )
        # Token characters are processed, and can be interpreted by a default transition table
        state = 0
        for char in token:

            if char not in self.transition_table:
                return False
            state = self.transition_table[char][state]
        return state in self.valid_states

    pass


class oneCharDFA(DFA):

    def __init__(self, symbol, **kwargs):
        if len(symbol) > 1:
            raise("DFA must be a single character")
        self.symbol = symbol
        self.name = kwargs["name"]

    def process_token(self, token: str) -> bool:
        return token == self.symbol
# arr  = ["=" , "-", "+" , "*", "(", ")", "^"]
# for char in arr:
#     s = s.replace(char,f" {char} ")


class commentDFA():

    def __init__(self):
        self.name = "Comentario"

    def process_token(self, token):
        return len(token) > 1 and token[0:2] == "//"
