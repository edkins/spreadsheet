from antlr4 import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.error.ErrorListener import ErrorListener
from FormulaLexer import FormulaLexer
from FormulaParser import FormulaParser
from FormulaVisitor import FormulaVisitor
from typing import Optional

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

class Arg:
    def __init__(self, name: Optional[str], size: Optional[int]):
        self.name = name
        self.size = size

    def __repr__(self):
        if self.size == None:
            return self.name
        else:
            return f"{self.name}:{self.size}"

class Lambda(Expr):
    def __init__(self, args: tuple[str], expr: Expr):
        self.args = args
        self.expr = expr

    def __repr__(self):
        return f"{self.names} -> {self.expr}"

class FormulaVisitor(FormulaVisitor):
    def visitFormula(self, ctx: FormulaParser.FormulaContext):
        return self.visit(ctx.expr())

    def visitLambda(self, ctx: FormulaParser.LambdaContext):
        args = [self.visit(arg) for arg in ctx.args().arg()]
        expr = self.visit(ctx.expr())
        names = tuple(arg.name for arg in args if arg.name != None)
        if len(names) != len(set(names)):
            raise ParseError(f"Duplicate argument name in lambda: {names}")
        return Lambda(args, expr)

    def visitArgWithSize(self, ctx: FormulaParser.ArgWithSizeContext):
        return Arg(ctx.NAME().getText(), int(ctx.UINT().getText()))

    def visitArgWithoutSize(self, ctx: FormulaParser.ArgWithoutSizeContext):
        return Arg(ctx.NAME().getText(), None)

    def visitArgWithoutName(self, ctx: FormulaParser.ArgWithoutNameContext):
        return Arg(None, None)

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

    def visitUint(self, ctx: FormulaParser.UintContext):
        return Number(float(ctx.UINT().getText()))

    def visitUfloat(self, ctx: FormulaParser.UfloatContext):
        return Number(float(ctx.UFLOAT().getText()))

    def visitParens(self, ctx: FormulaParser.ParensContext):
        return self.visit(ctx.expr())

    def visitName(self, ctx: FormulaParser.NameContext):
        return Name(ctx.NAME().getText())

def parse(expr: str) -> Lambda:
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
