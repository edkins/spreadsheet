# Generated from Formula.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,3,0,18,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,4,1,31,8,1,11,1,12,1,32,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,8,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,55,8,1,10,1,12,
        1,58,9,1,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,77,8,3,1,4,1,4,1,4,5,4,82,8,4,10,4,12,4,
        85,9,4,1,5,1,5,1,5,3,5,90,8,5,1,5,0,1,2,6,0,2,4,6,8,10,0,2,1,0,11,
        12,1,0,13,14,103,0,17,1,0,0,0,2,41,1,0,0,0,4,59,1,0,0,0,6,76,1,0,
        0,0,8,78,1,0,0,0,10,89,1,0,0,0,12,13,5,1,0,0,13,18,5,17,0,0,14,15,
        3,2,1,0,15,16,5,0,0,1,16,18,1,0,0,0,17,12,1,0,0,0,17,14,1,0,0,0,
        18,1,1,0,0,0,19,20,6,1,-1,0,20,21,5,2,0,0,21,22,3,4,2,0,22,23,5,
        3,0,0,23,24,5,4,0,0,24,25,3,2,1,7,25,42,1,0,0,0,26,42,5,15,0,0,27,
        42,5,16,0,0,28,29,5,17,0,0,29,31,5,5,0,0,30,28,1,0,0,0,31,32,1,0,
        0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,42,5,17,0,0,35,
        42,5,17,0,0,36,42,5,18,0,0,37,38,5,6,0,0,38,39,3,2,1,0,39,40,5,7,
        0,0,40,42,1,0,0,0,41,19,1,0,0,0,41,26,1,0,0,0,41,27,1,0,0,0,41,30,
        1,0,0,0,41,35,1,0,0,0,41,36,1,0,0,0,41,37,1,0,0,0,42,56,1,0,0,0,
        43,44,10,9,0,0,44,45,7,0,0,0,45,55,3,2,1,10,46,47,10,8,0,0,47,48,
        7,1,0,0,48,55,3,2,1,9,49,50,10,10,0,0,50,51,5,2,0,0,51,52,3,8,4,
        0,52,53,5,3,0,0,53,55,1,0,0,0,54,43,1,0,0,0,54,46,1,0,0,0,54,49,
        1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,3,1,0,0,0,58,
        56,1,0,0,0,59,64,3,6,3,0,60,61,5,8,0,0,61,63,3,6,3,0,62,60,1,0,0,
        0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,5,1,0,0,0,66,64,1,
        0,0,0,67,68,5,9,0,0,68,69,5,17,0,0,69,70,5,10,0,0,70,77,5,15,0,0,
        71,72,5,17,0,0,72,73,5,10,0,0,73,77,5,15,0,0,74,77,5,10,0,0,75,77,
        5,17,0,0,76,67,1,0,0,0,76,71,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,
        77,7,1,0,0,0,78,83,3,10,5,0,79,80,5,8,0,0,80,82,3,10,5,0,81,79,1,
        0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,9,1,0,0,0,85,
        83,1,0,0,0,86,90,5,15,0,0,87,90,5,17,0,0,88,90,5,10,0,0,89,86,1,
        0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,11,1,0,0,0,9,17,32,41,54,56,
        64,76,83,89
    ]

class FormulaParser ( Parser ):

    grammarFileName = "Formula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'['", "']'", "'->'", "'::'", 
                     "'('", "')'", "','", "'#'", "':'", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "UINT", "UFLOAT", "NAME", "QUOTED", 
                      "WS" ]

    RULE_formula = 0
    RULE_expr = 1
    RULE_args = 2
    RULE_arg = 3
    RULE_indexes = 4
    RULE_index = 5

    ruleNames =  [ "formula", "expr", "args", "arg", "indexes", "index" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    UINT=15
    UFLOAT=16
    NAME=17
    QUOTED=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormulaParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ImportContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(FormulaParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport" ):
                listener.enterImport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport" ):
                listener.exitImport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport" ):
                return visitor.visitImport(self)
            else:
                return visitor.visitChildren(self)


    class BareExprContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FormulaParser.ExprContext,0)

        def EOF(self):
            return self.getToken(FormulaParser.EOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBareExpr" ):
                listener.enterBareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBareExpr" ):
                listener.exitBareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBareExpr" ):
                return visitor.visitBareExpr(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = FormulaParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = FormulaParser.ImportContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(FormulaParser.T__0)
                self.state = 13
                self.match(FormulaParser.NAME)
                pass
            elif token in [2, 6, 15, 16, 17, 18]:
                localctx = FormulaParser.BareExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(FormulaParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormulaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NamespacedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(FormulaParser.NAME)
            else:
                return self.getToken(FormulaParser.NAME, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaced" ):
                listener.enterNamespaced(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaced" ):
                listener.exitNamespaced(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespaced" ):
                return visitor.visitNamespaced(self)
            else:
                return visitor.visitChildren(self)


    class GetItemContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FormulaParser.ExprContext,0)

        def indexes(self):
            return self.getTypedRuleContext(FormulaParser.IndexesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetItem" ):
                listener.enterGetItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetItem" ):
                listener.exitGetItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetItem" ):
                return visitor.visitGetItem(self)
            else:
                return visitor.visitChildren(self)


    class UintContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UINT(self):
            return self.getToken(FormulaParser.UINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUint" ):
                listener.enterUint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUint" ):
                listener.exitUint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUint" ):
                return visitor.visitUint(self)
            else:
                return visitor.visitChildren(self)


    class QuotedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUOTED(self):
            return self.getToken(FormulaParser.QUOTED, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.ExprContext)
            else:
                return self.getTypedRuleContext(FormulaParser.ExprContext,i)

        def MUL(self):
            return self.getToken(FormulaParser.MUL, 0)
        def DIV(self):
            return self.getToken(FormulaParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.ExprContext)
            else:
                return self.getTypedRuleContext(FormulaParser.ExprContext,i)

        def ADD(self):
            return self.getToken(FormulaParser.ADD, 0)
        def SUB(self):
            return self.getToken(FormulaParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FormulaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class UfloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UFLOAT(self):
            return self.getToken(FormulaParser.UFLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUfloat" ):
                listener.enterUfloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUfloat" ):
                listener.exitUfloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUfloat" ):
                return visitor.visitUfloat(self)
            else:
                return visitor.visitChildren(self)


    class LambdaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def args(self):
            return self.getTypedRuleContext(FormulaParser.ArgsContext,0)

        def expr(self):
            return self.getTypedRuleContext(FormulaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda" ):
                listener.enterLambda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda" ):
                listener.exitLambda(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambda" ):
                return visitor.visitLambda(self)
            else:
                return visitor.visitChildren(self)


    class NameContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(FormulaParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FormulaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = FormulaParser.LambdaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(FormulaParser.T__1)
                self.state = 21
                self.args()
                self.state = 22
                self.match(FormulaParser.T__2)
                self.state = 23
                self.match(FormulaParser.T__3)
                self.state = 24
                self.expr(7)
                pass

            elif la_ == 2:
                localctx = FormulaParser.UintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(FormulaParser.UINT)
                pass

            elif la_ == 3:
                localctx = FormulaParser.UfloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(FormulaParser.UFLOAT)
                pass

            elif la_ == 4:
                localctx = FormulaParser.NamespacedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 28
                        self.match(FormulaParser.NAME)
                        self.state = 29
                        self.match(FormulaParser.T__4)

                    else:
                        raise NoViableAltException(self)
                    self.state = 32 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 34
                self.match(FormulaParser.NAME)
                pass

            elif la_ == 5:
                localctx = FormulaParser.NameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(FormulaParser.NAME)
                pass

            elif la_ == 6:
                localctx = FormulaParser.QuotedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(FormulaParser.QUOTED)
                pass

            elif la_ == 7:
                localctx = FormulaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(FormulaParser.T__5)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.match(FormulaParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = FormulaParser.MulDivContext(self, FormulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 44
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = FormulaParser.AddSubContext(self, FormulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 47
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = FormulaParser.GetItemContext(self, FormulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 50
                        self.match(FormulaParser.T__1)
                        self.state = 51
                        self.indexes()
                        self.state = 52
                        self.match(FormulaParser.T__2)
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.ArgContext)
            else:
                return self.getTypedRuleContext(FormulaParser.ArgContext,i)


        def getRuleIndex(self):
            return FormulaParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = FormulaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.arg()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 60
                self.match(FormulaParser.T__7)
                self.state = 61
                self.arg()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormulaParser.RULE_arg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArgWithoutNameContext(ArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ArgContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgWithoutName" ):
                listener.enterArgWithoutName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgWithoutName" ):
                listener.exitArgWithoutName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgWithoutName" ):
                return visitor.visitArgWithoutName(self)
            else:
                return visitor.visitChildren(self)


    class SubcellArgWithSizeContext(ArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ArgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(FormulaParser.NAME, 0)
        def UINT(self):
            return self.getToken(FormulaParser.UINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubcellArgWithSize" ):
                listener.enterSubcellArgWithSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubcellArgWithSize" ):
                listener.exitSubcellArgWithSize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubcellArgWithSize" ):
                return visitor.visitSubcellArgWithSize(self)
            else:
                return visitor.visitChildren(self)


    class ArgWithoutSizeContext(ArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ArgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(FormulaParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgWithoutSize" ):
                listener.enterArgWithoutSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgWithoutSize" ):
                listener.exitArgWithoutSize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgWithoutSize" ):
                return visitor.visitArgWithoutSize(self)
            else:
                return visitor.visitChildren(self)


    class ArgWithSizeContext(ArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ArgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(FormulaParser.NAME, 0)
        def UINT(self):
            return self.getToken(FormulaParser.UINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgWithSize" ):
                listener.enterArgWithSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgWithSize" ):
                listener.exitArgWithSize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgWithSize" ):
                return visitor.visitArgWithSize(self)
            else:
                return visitor.visitChildren(self)



    def arg(self):

        localctx = FormulaParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arg)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = FormulaParser.SubcellArgWithSizeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(FormulaParser.T__8)
                self.state = 68
                self.match(FormulaParser.NAME)
                self.state = 69
                self.match(FormulaParser.T__9)
                self.state = 70
                self.match(FormulaParser.UINT)
                pass

            elif la_ == 2:
                localctx = FormulaParser.ArgWithSizeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(FormulaParser.NAME)
                self.state = 72
                self.match(FormulaParser.T__9)
                self.state = 73
                self.match(FormulaParser.UINT)
                pass

            elif la_ == 3:
                localctx = FormulaParser.ArgWithoutNameContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(FormulaParser.T__9)
                pass

            elif la_ == 4:
                localctx = FormulaParser.ArgWithoutSizeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(FormulaParser.NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.IndexContext)
            else:
                return self.getTypedRuleContext(FormulaParser.IndexContext,i)


        def getRuleIndex(self):
            return FormulaParser.RULE_indexes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexes" ):
                listener.enterIndexes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexes" ):
                listener.exitIndexes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexes" ):
                return visitor.visitIndexes(self)
            else:
                return visitor.visitChildren(self)




    def indexes(self):

        localctx = FormulaParser.IndexesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_indexes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.index()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 79
                self.match(FormulaParser.T__7)
                self.state = 80
                self.index()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormulaParser.RULE_index

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AllIndexContext(IndexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.IndexContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllIndex" ):
                listener.enterAllIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllIndex" ):
                listener.exitAllIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllIndex" ):
                return visitor.visitAllIndex(self)
            else:
                return visitor.visitChildren(self)


    class NameIndexContext(IndexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.IndexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(FormulaParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameIndex" ):
                listener.enterNameIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameIndex" ):
                listener.exitNameIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameIndex" ):
                return visitor.visitNameIndex(self)
            else:
                return visitor.visitChildren(self)


    class UintIndexContext(IndexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.IndexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UINT(self):
            return self.getToken(FormulaParser.UINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUintIndex" ):
                listener.enterUintIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUintIndex" ):
                listener.exitUintIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUintIndex" ):
                return visitor.visitUintIndex(self)
            else:
                return visitor.visitChildren(self)



    def index(self):

        localctx = FormulaParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_index)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = FormulaParser.UintIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(FormulaParser.UINT)
                pass
            elif token in [17]:
                localctx = FormulaParser.NameIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(FormulaParser.NAME)
                pass
            elif token in [10]:
                localctx = FormulaParser.AllIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(FormulaParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         




