# Generated from Formula.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete generic visitor for a parse tree produced by FormulaParser.

class FormulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormulaParser#Import.
    def visitImport(self, ctx:FormulaParser.ImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#BareExpr.
    def visitBareExpr(self, ctx:FormulaParser.BareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Namespaced.
    def visitNamespaced(self, ctx:FormulaParser.NamespacedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#GetItem.
    def visitGetItem(self, ctx:FormulaParser.GetItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Uint.
    def visitUint(self, ctx:FormulaParser.UintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#MulDiv.
    def visitMulDiv(self, ctx:FormulaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#AddSub.
    def visitAddSub(self, ctx:FormulaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Parens.
    def visitParens(self, ctx:FormulaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Ufloat.
    def visitUfloat(self, ctx:FormulaParser.UfloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Lambda.
    def visitLambda(self, ctx:FormulaParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Name.
    def visitName(self, ctx:FormulaParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#args.
    def visitArgs(self, ctx:FormulaParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#ArgWithSize.
    def visitArgWithSize(self, ctx:FormulaParser.ArgWithSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#ArgWithoutName.
    def visitArgWithoutName(self, ctx:FormulaParser.ArgWithoutNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#ArgWithoutSize.
    def visitArgWithoutSize(self, ctx:FormulaParser.ArgWithoutSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#indexes.
    def visitIndexes(self, ctx:FormulaParser.IndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#UintIndex.
    def visitUintIndex(self, ctx:FormulaParser.UintIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#NameIndex.
    def visitNameIndex(self, ctx:FormulaParser.NameIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#AllIndex.
    def visitAllIndex(self, ctx:FormulaParser.AllIndexContext):
        return self.visitChildren(ctx)



del FormulaParser