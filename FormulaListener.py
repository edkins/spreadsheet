# Generated from Formula.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete listener for a parse tree produced by FormulaParser.
class FormulaListener(ParseTreeListener):

    # Enter a parse tree produced by FormulaParser#formula.
    def enterFormula(self, ctx:FormulaParser.FormulaContext):
        pass

    # Exit a parse tree produced by FormulaParser#formula.
    def exitFormula(self, ctx:FormulaParser.FormulaContext):
        pass


    # Enter a parse tree produced by FormulaParser#ufloat.
    def enterUfloat(self, ctx:FormulaParser.UfloatContext):
        pass

    # Exit a parse tree produced by FormulaParser#ufloat.
    def exitUfloat(self, ctx:FormulaParser.UfloatContext):
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


    # Enter a parse tree produced by FormulaParser#uint.
    def enterUint(self, ctx:FormulaParser.UintContext):
        pass

    # Exit a parse tree produced by FormulaParser#uint.
    def exitUint(self, ctx:FormulaParser.UintContext):
        pass


    # Enter a parse tree produced by FormulaParser#Lambda.
    def enterLambda(self, ctx:FormulaParser.LambdaContext):
        pass

    # Exit a parse tree produced by FormulaParser#Lambda.
    def exitLambda(self, ctx:FormulaParser.LambdaContext):
        pass


    # Enter a parse tree produced by FormulaParser#args.
    def enterArgs(self, ctx:FormulaParser.ArgsContext):
        pass

    # Exit a parse tree produced by FormulaParser#args.
    def exitArgs(self, ctx:FormulaParser.ArgsContext):
        pass


    # Enter a parse tree produced by FormulaParser#ArgWithSize.
    def enterArgWithSize(self, ctx:FormulaParser.ArgWithSizeContext):
        pass

    # Exit a parse tree produced by FormulaParser#ArgWithSize.
    def exitArgWithSize(self, ctx:FormulaParser.ArgWithSizeContext):
        pass


    # Enter a parse tree produced by FormulaParser#ArgWithoutName.
    def enterArgWithoutName(self, ctx:FormulaParser.ArgWithoutNameContext):
        pass

    # Exit a parse tree produced by FormulaParser#ArgWithoutName.
    def exitArgWithoutName(self, ctx:FormulaParser.ArgWithoutNameContext):
        pass


    # Enter a parse tree produced by FormulaParser#ArgWithoutSize.
    def enterArgWithoutSize(self, ctx:FormulaParser.ArgWithoutSizeContext):
        pass

    # Exit a parse tree produced by FormulaParser#ArgWithoutSize.
    def exitArgWithoutSize(self, ctx:FormulaParser.ArgWithoutSizeContext):
        pass



del FormulaParser