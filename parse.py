from antlr4 import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.error.ErrorListener import ErrorListener
from FormulaLexer import FormulaLexer
from FormulaParser import FormulaParser
from FormulaVisitor import FormulaVisitor

class ParseError(Exception):
    pass

class Expr:
    pass

class ExceptionErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseError(msg)

class Apply(Expr):
    def __init__(self, func: str, *args: Expr):
        self.func = func
        self.args = args

    def __repr__(self):
        return f"{self.func}({', '.join(map(repr, self.args))})"

class Number(Expr):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Name(Expr):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

class FormulaVisitor(FormulaVisitor):
    def visitFormula(self, ctx: FormulaParser.FormulaContext):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx: FormulaParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == FormulaParser.MUL:
            return Apply("*", left, right)
        else:
            return Apply("/", left, right)

    def visitAddSub(self, ctx: FormulaParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == FormulaParser.ADD:
            return Apply("+", left, right)
        else:
            return Apply("-", left, right)

    def visitNumber(self, ctx: FormulaParser.NumberContext):
        return Number(float(ctx.NUMBER().getText()))

    def visitParens(self, ctx: FormulaParser.ParensContext):
        return self.visit(ctx.expr())

    def visitName(self, ctx: FormulaParser.NameContext):
        return Name(ctx.NAME().getText())

def parse(expr: str) -> Expr:
    lexer = FormulaLexer(InputStream(expr))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ExceptionErrorListener())
    stream = CommonTokenStream(lexer)
    parser = FormulaParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ExceptionErrorListener())
    tree = parser.formula()
    visitor = FormulaVisitor()
    result = visitor.visit(tree)
    if result == None:
        raise Exception("Result shouldn't be None")
    return result
