# Generated from Formula.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete listener for a parse tree produced by FormulaParser.
class FormulaListener(ParseTreeListener):

    # Enter a parse tree produced by FormulaParser#number.
    def enterNumber(self, ctx:FormulaParser.NumberContext):
        pass

    # Exit a parse tree produced by FormulaParser#number.
    def exitNumber(self, ctx:FormulaParser.NumberContext):
        pass


    # Enter a parse tree produced by FormulaParser#parens.
    def enterParens(self, ctx:FormulaParser.ParensContext):
        pass

    # Exit a parse tree produced by FormulaParser#parens.
    def exitParens(self, ctx:FormulaParser.ParensContext):
        pass


    # Enter a parse tree produced by FormulaParser#MulDiv.
    def enterMulDiv(self, ctx:FormulaParser.MulDivContext):
        pass

    # Exit a parse tree produced by FormulaParser#MulDiv.
    def exitMulDiv(self, ctx:FormulaParser.MulDivContext):
        pass


    # Enter a parse tree produced by FormulaParser#AddSub.
    def enterAddSub(self, ctx:FormulaParser.AddSubContext):
        pass

    # Exit a parse tree produced by FormulaParser#AddSub.
    def exitAddSub(self, ctx:FormulaParser.AddSubContext):
        pass


    # Enter a parse tree produced by FormulaParser#name.
    def enterName(self, ctx:FormulaParser.NameContext):
        pass

    # Exit a parse tree produced by FormulaParser#name.
    def exitName(self, ctx:FormulaParser.NameContext):
        pass



del FormulaParser