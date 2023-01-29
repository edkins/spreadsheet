# Generated from Formula.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete generic visitor for a parse tree produced by FormulaParser.

class FormulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormulaParser#number.
    def visitNumber(self, ctx:FormulaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#parens.
    def visitParens(self, ctx:FormulaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#MulDiv.
    def visitMulDiv(self, ctx:FormulaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#AddSub.
    def visitAddSub(self, ctx:FormulaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#name.
    def visitName(self, ctx:FormulaParser.NameContext):
        return self.visitChildren(ctx)



del FormulaParser