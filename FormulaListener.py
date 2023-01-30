# Generated from Formula.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete listener for a parse tree produced by FormulaParser.
class FormulaListener(ParseTreeListener):

    # Enter a parse tree produced by FormulaParser#Import.
    def enterImport(self, ctx:FormulaParser.ImportContext):
        pass

    # Exit a parse tree produced by FormulaParser#Import.
    def exitImport(self, ctx:FormulaParser.ImportContext):
        pass


    # Enter a parse tree produced by FormulaParser#BareExpr.
    def enterBareExpr(self, ctx:FormulaParser.BareExprContext):
        pass

    # Exit a parse tree produced by FormulaParser#BareExpr.
    def exitBareExpr(self, ctx:FormulaParser.BareExprContext):
        pass


    # Enter a parse tree produced by FormulaParser#Namespaced.
    def enterNamespaced(self, ctx:FormulaParser.NamespacedContext):
        pass

    # Exit a parse tree produced by FormulaParser#Namespaced.
    def exitNamespaced(self, ctx:FormulaParser.NamespacedContext):
        pass


    # Enter a parse tree produced by FormulaParser#GetItem.
    def enterGetItem(self, ctx:FormulaParser.GetItemContext):
        pass

    # Exit a parse tree produced by FormulaParser#GetItem.
    def exitGetItem(self, ctx:FormulaParser.GetItemContext):
        pass


    # Enter a parse tree produced by FormulaParser#Uint.
    def enterUint(self, ctx:FormulaParser.UintContext):
        pass

    # Exit a parse tree produced by FormulaParser#Uint.
    def exitUint(self, ctx:FormulaParser.UintContext):
        pass


    # Enter a parse tree produced by FormulaParser#Quoted.
    def enterQuoted(self, ctx:FormulaParser.QuotedContext):
        pass

    # Exit a parse tree produced by FormulaParser#Quoted.
    def exitQuoted(self, ctx:FormulaParser.QuotedContext):
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


    # Enter a parse tree produced by FormulaParser#Parens.
    def enterParens(self, ctx:FormulaParser.ParensContext):
        pass

    # Exit a parse tree produced by FormulaParser#Parens.
    def exitParens(self, ctx:FormulaParser.ParensContext):
        pass


    # Enter a parse tree produced by FormulaParser#Ufloat.
    def enterUfloat(self, ctx:FormulaParser.UfloatContext):
        pass

    # Exit a parse tree produced by FormulaParser#Ufloat.
    def exitUfloat(self, ctx:FormulaParser.UfloatContext):
        pass


    # Enter a parse tree produced by FormulaParser#Lambda.
    def enterLambda(self, ctx:FormulaParser.LambdaContext):
        pass

    # Exit a parse tree produced by FormulaParser#Lambda.
    def exitLambda(self, ctx:FormulaParser.LambdaContext):
        pass


    # Enter a parse tree produced by FormulaParser#Name.
    def enterName(self, ctx:FormulaParser.NameContext):
        pass

    # Exit a parse tree produced by FormulaParser#Name.
    def exitName(self, ctx:FormulaParser.NameContext):
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


    # Enter a parse tree produced by FormulaParser#indexes.
    def enterIndexes(self, ctx:FormulaParser.IndexesContext):
        pass

    # Exit a parse tree produced by FormulaParser#indexes.
    def exitIndexes(self, ctx:FormulaParser.IndexesContext):
        pass


    # Enter a parse tree produced by FormulaParser#UintIndex.
    def enterUintIndex(self, ctx:FormulaParser.UintIndexContext):
        pass

    # Exit a parse tree produced by FormulaParser#UintIndex.
    def exitUintIndex(self, ctx:FormulaParser.UintIndexContext):
        pass


    # Enter a parse tree produced by FormulaParser#NameIndex.
    def enterNameIndex(self, ctx:FormulaParser.NameIndexContext):
        pass

    # Exit a parse tree produced by FormulaParser#NameIndex.
    def exitNameIndex(self, ctx:FormulaParser.NameIndexContext):
        pass


    # Enter a parse tree produced by FormulaParser#AllIndex.
    def enterAllIndex(self, ctx:FormulaParser.AllIndexContext):
        pass

    # Exit a parse tree produced by FormulaParser#AllIndex.
    def exitAllIndex(self, ctx:FormulaParser.AllIndexContext):
        pass



del FormulaParser