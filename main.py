from dfa import DFA, oneCharDFA, commentDFA
import sys
from dfa.util import getTokens, identifyToken


def main(path):

    tokens = getTokens(path)

    # Definición de autómatas

    reales_dfa = DFA(
        transition_table={
            "0": [1, 1, 1, 4, 4, 7, 6, 7, 7, 9],
            "#": [1, 1, 1, 4, 4, 6, 6, 6, 6, 9],
            "-": [2, 9, 9, 9, 9, 8, 9, 9, 9, 9],
            "+": [2, 9, 9, 9, 9, 8, 9, 9, 9, 9],
            ".": [3, 3, 3, 9, 9, 9, 9, 9, 9, 9],
            "E": [9, 9, 9, 9, 5, 9, 9, 9, 9, 9],
            "e": [9, 9, 9, 9, 5, 9, 9, 9, 9, 9],
        },
        valid_states=[3, 4, 6],
        name="Real"
    )

    int_dfa = DFA(
        transition_table={
            "0": [3, 3, 4, 3, 4],
            "#": [3, 3, 3, 3, 4],
            "-": [2, 4, 4, 4, 4],
            "+": [1, 4, 4, 4, 4],
        },
        valid_states=[3],
        name="Entero"
    )

    var_dfa = DFA(
        transition_table={
            "A": [1, 1, 2],
            "_": [2, 1, 2],
            "#": [2, 1, 2]
        },
        valid_states=[1],
        name="Variable"
    )
    comment_dfa = DFA(
        transition_table={
            "/": [1, 2, 2, 3],
            "A": [3, 3, 2, 3],
            "#": [3, 3, 2, 3],
            ".": [3, 3, 2, 3],
            "(": [3, 3, 2, 3],
            ")": [3, 3, 2, 3],
            "+": [3, 3, 2, 3],
            "-": [3, 3, 2, 3],
            "^": [3, 3, 2, 3],
            "*": [3, 3, 2, 3],
            "_": [3, 3, 2, 3],
            "0": [3, 3, 2, 3],
            " ": [3, 3, 2, 3],
            "=": [3, 3, 2, 3],
        },
        valid_states=[2],
        name="Comentario"
    )
    open_parentheses = oneCharDFA("(", name="Paréntesis que cierra")
    closing_parentheses = oneCharDFA(")", name="Paréntesis que abre")
    mult_dfa = oneCharDFA("*", name="Multiplicación")
    subst_dfa = oneCharDFA("-", name="Resta")
    power_dfa = oneCharDFA("^", name="Potencia")
    division_dfa = oneCharDFA("/", name="División")
    suma_dfa = oneCharDFA("+", name="Asignación")
    asignacion_dfa = oneCharDFA("=", name="Asignación")

    # Autómatas listados en el orden en el que se ejecutaran

    automatas = [
        comment_dfa,
        int_dfa,
        reales_dfa,
        var_dfa,
        open_parentheses,
        closing_parentheses,
        mult_dfa,
        subst_dfa,
        power_dfa,
        division_dfa,
        suma_dfa,
        asignacion_dfa
    ]
    # Inicializar tabla para output estilizado
    for token in tokens:
        token_type = identifyToken(token, automatas)
        print(f"{token} ----> {token_type}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise "Expected an argument in command line"
    main(sys.argv[1])
