# NOTE: do not modify the contents of this file
import pytest

from array_stack import ArrayStack, Empty
from calculator import Calculator, check_operator_on_stack_precedence, PostfixEvaluationError


# NOTE: order is actual/received student value, expected/solution
def test_standard_stack_ops():
    s = ArrayStack()
    assert s.is_empty() is True

    with pytest.raises(Empty):
        s.peek()
    with pytest.raises(Empty):
        s.pop()

    s.push("hello")
    assert s.is_empty() is False
    assert s.peek() == "hello"

    s.push("goodbye")
    assert s.is_empty() is False
    assert s.peek() == "goodbye"

    value = s.pop()
    assert value == "goodbye"
    assert s.is_empty() is False
    assert s.peek() == "hello"

    value = s.pop()
    assert value == "hello"
    assert s.is_empty() is True

    with pytest.raises(Empty):
        s.peek()
    with pytest.raises(Empty):
        s.pop()

    size = 10_000
    for i in range(size):
        s.push(str(i))

    assert s.is_empty() is False
    assert s.peek() == str(size - 1)

    if s.peek() == str(size - 1):
        # to prevent alot of output on failure
        for i in range(size - 1, -1, -1):
            assert s.pop() == str(i)

    assert s.is_empty() is True
    with pytest.raises(Empty):
        s.peek()
    with pytest.raises(Empty):
        s.pop()

def test_check_operator_on_stack_precedence():
    # operator on stack: "("
    assert check_operator_on_stack_precedence("(", "(") is False
    assert check_operator_on_stack_precedence("(", "^") is False
    assert check_operator_on_stack_precedence("(", "*") is False
    assert check_operator_on_stack_precedence("(", "/") is False
    assert check_operator_on_stack_precedence("(", "%") is False
    assert check_operator_on_stack_precedence("(", "+") is False
    assert check_operator_on_stack_precedence("(", "-") is False

    # ")" right paren is never on the stack

    assert check_operator_on_stack_precedence("^", "(") is False
    assert check_operator_on_stack_precedence("^", ")") is True
    assert check_operator_on_stack_precedence("^", "^") is False
    assert check_operator_on_stack_precedence("^", "*") is True
    assert check_operator_on_stack_precedence("^", "/") is True
    assert check_operator_on_stack_precedence("^", "%") is True
    assert check_operator_on_stack_precedence("^", "+") is True
    assert check_operator_on_stack_precedence("^", "-") is True

    mult_ops = ["*", "/", "%"]
    for op in mult_ops:
        assert check_operator_on_stack_precedence(op, "(") is False
        assert check_operator_on_stack_precedence(op, ")") is True
        assert check_operator_on_stack_precedence(op, "^") is False
        assert check_operator_on_stack_precedence(op, "*") is True
        assert check_operator_on_stack_precedence(op, "/") is True
        assert check_operator_on_stack_precedence(op, "%") is True
        assert check_operator_on_stack_precedence(op, "+") is True
        assert check_operator_on_stack_precedence(op, "-") is True

    add_ops = ["+", "-"]
    for op in add_ops:
        assert check_operator_on_stack_precedence(op, "(") is False
        assert check_operator_on_stack_precedence(op, ")") is True
        assert check_operator_on_stack_precedence(op, "^") is False
        assert check_operator_on_stack_precedence(op, "*") is False
        assert check_operator_on_stack_precedence(op, "/") is False
        assert check_operator_on_stack_precedence(op, "%") is False
        assert check_operator_on_stack_precedence(op, "+") is True
        assert check_operator_on_stack_precedence(op, "-") is True

def test_convert_infix_to_postfix():
    calc = Calculator()
    symbol_table = {}

    # incomplete symbol table
    symbol_table["A"] = "77"
    symbol_table["B"] = "55"
    symbol_table["C"] = "40"
    symbol_table["D"] = "15"
    symbol_table["E"] = "7"
    symbol_table["F"] = "1"
    symbol_table["G"] = "5"
    symbol_table["H"] = "-10"
    symbol_table["I"] = "-69"
    symbol_table["J"] = "33"
    symbol_table["K"] = "125"
    symbol_table["M"] = "9"
    symbol_table["N"] = "222"
    symbol_table["P"] = "33"
    symbol_table["Q"] = "2"
    symbol_table["R"] = "-1"
    symbol_table["X"] = "2"
    symbol_table["W"] = "20"
    symbol_table["Z"] = "500"

    calc.set_symbol_table(symbol_table)

    assert calc.convert_infix_to_postfix("A-B") == "AB-"
    assert calc.convert_infix_to_postfix("A+B") == "AB+"
    assert calc.convert_infix_to_postfix("A-(B+C)") == "ABC+-"
    assert calc.convert_infix_to_postfix("R*(P-H)") == "RPH-*"
    assert calc.convert_infix_to_postfix("D-(((C+D-G)-H)+F)") == "DCD+G-H-F+-"
    assert calc.convert_infix_to_postfix("(J-K)*(X-I^G+F)/Z") == "JK-XIG^-F+*Z/"
    assert calc.convert_infix_to_postfix("(((X+Z-H-I)*X)+W/(Z+X)/(Z^X))") == "XZ+H-I-X*WZX+/ZX^/+"

    # extras beyond original input file
    assert calc.convert_infix_to_postfix("Q*X") == "QX*"
    assert calc.convert_infix_to_postfix("X+B*C/G-X*X/Z") == "XBC*G/+XX*Z/-"
    assert calc.convert_infix_to_postfix("(X)+Q-R+(X-Z)") == "XQ+R-XZ-+"
    assert calc.convert_infix_to_postfix("(X+B*C/G-X*Z)^(X+Q)-R+(X-Z)") == "XBC*G/+XZ*-XQ+^R-XZ-+"

    # new almost full symbol table
    symbol_table["A"] = "-8"
    symbol_table["B"] = "14"
    symbol_table["C"] = "10"
    symbol_table["D"] = "5"
    symbol_table["E"] = "-7"
    symbol_table["F"] = "66"
    symbol_table["G"] = "0"
    symbol_table["H"] = "-11"
    symbol_table["I"] = "5"
    symbol_table["J"] = "32"
    symbol_table["K"] = "10"
    symbol_table["L"] = "-98"
    symbol_table["M"] = "6"
    symbol_table["N"] = "9"
    symbol_table["O"] = "778"
    symbol_table["P"] = "65"
    symbol_table["Q"] = "32"
    symbol_table["R"] = "-3"
    symbol_table["S"] = "0"
    symbol_table["T"] = "-7"
    # missing U in symbol table on purpose
    symbol_table["V"] = "-32"
    symbol_table["W"] = "3"
    symbol_table["X"] = "41"
    symbol_table["Y"] = "1"
    symbol_table["Z"] = "-1"

    calc.set_symbol_table(symbol_table)

    assert calc.convert_infix_to_postfix("(A+C)*D") == "AC+D*"
    assert calc.convert_infix_to_postfix("A+C*D") == "ACD*+"
    assert calc.convert_infix_to_postfix("(Y-Z)+(C^W)-W*Q/G") == "YZ-CW^+WQ*G/-"
    assert calc.convert_infix_to_postfix("H%N%M%D%H%I") == "HN%M%D%H%I%"
    assert calc.convert_infix_to_postfix("P/S/X/G/W/G") == "PS/X/G/W/G/"
    assert calc.convert_infix_to_postfix("N*T*L*L*L") == "NT*L*L*L*"
    assert calc.convert_infix_to_postfix("F+((H-M-L-J-C)/(F^B))") == "FHM-L-J-C-FB^/+"
    assert calc.convert_infix_to_postfix("H^Y-Y^H") == "HY^YH^-"
    assert calc.convert_infix_to_postfix("M^N-N^M") == "MN^NM^-"
    assert calc.convert_infix_to_postfix("(M^N)-(N^M)") == "MN^NM^-"
    assert calc.convert_infix_to_postfix("U-B") == "UB-"
    assert calc.convert_infix_to_postfix("A*B/C^D-G^G") == "AB*CD^/GG^-"
    assert calc.convert_infix_to_postfix("A") == "A"
    assert calc.convert_infix_to_postfix("(B)") == "B"
    assert calc.convert_infix_to_postfix("(((C)))") == "C"

def test_evaluate_postfix():
    calc = Calculator()
    symbol_table = {}
    # incomplete symbol table
    symbol_table["A"] = "77"
    symbol_table["B"] = "55"
    symbol_table["C"] = "40"
    symbol_table["D"] = "15"
    symbol_table["E"] = "7"
    symbol_table["F"] = "1"
    symbol_table["G"] = "5"
    symbol_table["H"] = "-10"
    symbol_table["I"] = "-69"
    symbol_table["J"] = "33"
    symbol_table["K"] = "125"
    symbol_table["M"] = "9"
    symbol_table["N"] = "222"
    symbol_table["P"] = "33"
    symbol_table["Q"] = "2"
    symbol_table["R"] = "-1"
    symbol_table["X"] = "2"
    symbol_table["W"] = "20"
    symbol_table["Z"] = "500"

    calc.set_symbol_table(symbol_table)

    assert calc.evaluate_postfix("AB-") == "22"
    assert calc.evaluate_postfix("AB+") == "132"
    assert calc.evaluate_postfix("ABC+-") == "-18"
    assert calc.evaluate_postfix("RPH-*") == "-43"
    assert calc.evaluate_postfix("DCD+G-H-F+-") == "-46"
    assert calc.evaluate_postfix("JK-XIG^-F+*Z/") == "-287781768"
    assert calc.evaluate_postfix("XZ+H-I-X*WZX+/ZX^/+") == "1162"

    # extras beyond original input file
    assert calc.evaluate_postfix("QX*") == "4"
    assert calc.evaluate_postfix("XBC*G/+XX*Z/-") == "442"
    assert calc.evaluate_postfix("XQ+R-XZ-+") == "-493"
    assert calc.evaluate_postfix("XBC*G/+XZ*-XQ+^R-XZ-+") == "96947539999"

    # new full symbol table
    symbol_table["A"] = "-8"
    symbol_table["B"] = "14"
    symbol_table["C"] = "10"
    symbol_table["D"] = "5"
    symbol_table["E"] = "-7"
    symbol_table["F"] = "66"
    symbol_table["G"] = "0"
    symbol_table["H"] = "-11"
    symbol_table["I"] = "5"
    symbol_table["J"] = "32"
    symbol_table["K"] = "10"
    symbol_table["L"] = "-98"
    symbol_table["M"] = "6"
    symbol_table["N"] = "9"
    symbol_table["O"] = "778"
    symbol_table["P"] = "65"
    symbol_table["Q"] = "32"
    symbol_table["R"] = "-3"
    symbol_table["S"] = "0"
    symbol_table["T"] = "-7"
    symbol_table["U"] = "-32"
    symbol_table["V"] = "-32"
    symbol_table["W"] = "3"
    symbol_table["X"] = "41"
    symbol_table["Y"] = "1"
    symbol_table["Z"] = "-1"

    calc.set_symbol_table(symbol_table)

    assert calc.evaluate_postfix("AC+D*") == "10"
    assert calc.evaluate_postfix("ACD*+") == "42"
    assert calc.evaluate_postfix("NT*L*L*L*") == "59295096"
    assert calc.evaluate_postfix("FHM-L-J-C-FB^/+") == "66"
    assert calc.evaluate_postfix("MN^NM^-") == "9546255"
    assert calc.evaluate_postfix("AB*CD^/GG^-") == "-1"
    assert calc.evaluate_postfix("A") == "-8"
    assert calc.evaluate_postfix("B") == "14"
    assert calc.evaluate_postfix("C") == "10"

# BONUS: this last test is for the BONUS task
# which is error checking for operands
def test_bonus_evaluate_postfix_errors():
    calc = Calculator()
    symbol_table = {}

    # new almost full symbol table
    symbol_table["A"] = "-8"
    symbol_table["B"] = "14"
    symbol_table["C"] = "10"
    symbol_table["D"] = "5"
    symbol_table["E"] = "-7"
    symbol_table["F"] = "66"
    symbol_table["G"] = "0"
    symbol_table["H"] = "-11"
    symbol_table["I"] = "5"
    symbol_table["J"] = "32"
    symbol_table["K"] = "10"
    symbol_table["L"] = "-98"
    symbol_table["M"] = "6"
    symbol_table["N"] = "9"
    symbol_table["O"] = "778"
    symbol_table["P"] = "65"
    symbol_table["Q"] = "32"
    symbol_table["R"] = "-3"
    symbol_table["S"] = "0"
    symbol_table["T"] = "-7"
    # missing U in symbol table on purpose
    symbol_table["V"] = "-32"
    symbol_table["W"] = "3"
    symbol_table["X"] = "41"
    symbol_table["Y"] = "1"
    symbol_table["Z"] = "-1"

    calc.set_symbol_table(symbol_table)

    with pytest.raises(PostfixEvaluationError):
        calc.evaluate_postfix("YZ-CW^+WQ*G/-") # divide by zero
    with pytest.raises(PostfixEvaluationError):
        assert calc.evaluate_postfix("HN%M%D%H%I%") # negative mod
    with pytest.raises(PostfixEvaluationError):
        assert calc.evaluate_postfix("PS/X/G/W/G/") # divide by zero
    with pytest.raises(PostfixEvaluationError):
        assert calc.evaluate_postfix("HY^YH^-") # negative exponent
    with pytest.raises(PostfixEvaluationError):
        assert calc.evaluate_postfix("UB-") # missing value