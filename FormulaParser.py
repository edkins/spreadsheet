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
        4,1,15,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,30,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,43,8,1,
        10,1,12,1,46,9,1,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,3,1,3,
        1,3,1,3,1,3,3,3,61,8,3,1,4,1,4,1,4,5,4,66,8,4,10,4,12,4,69,9,4,1,
        5,1,5,1,5,3,5,74,8,5,1,5,0,1,2,6,0,2,4,6,8,10,0,2,1,0,8,9,1,0,10,
        11,82,0,12,1,0,0,0,2,29,1,0,0,0,4,47,1,0,0,0,6,60,1,0,0,0,8,62,1,
        0,0,0,10,73,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,
        16,6,1,-1,0,16,17,5,1,0,0,17,18,3,4,2,0,18,19,5,2,0,0,19,20,5,3,
        0,0,20,21,3,2,1,5,21,30,1,0,0,0,22,30,5,12,0,0,23,30,5,13,0,0,24,
        30,5,14,0,0,25,26,5,4,0,0,26,27,3,2,1,0,27,28,5,5,0,0,28,30,1,0,
        0,0,29,15,1,0,0,0,29,22,1,0,0,0,29,23,1,0,0,0,29,24,1,0,0,0,29,25,
        1,0,0,0,30,44,1,0,0,0,31,32,10,7,0,0,32,33,7,0,0,0,33,43,3,2,1,8,
        34,35,10,6,0,0,35,36,7,1,0,0,36,43,3,2,1,7,37,38,10,8,0,0,38,39,
        5,1,0,0,39,40,3,8,4,0,40,41,5,2,0,0,41,43,1,0,0,0,42,31,1,0,0,0,
        42,34,1,0,0,0,42,37,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,
        0,0,0,45,3,1,0,0,0,46,44,1,0,0,0,47,52,3,6,3,0,48,49,5,6,0,0,49,
        51,3,6,3,0,50,48,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,
        0,53,5,1,0,0,0,54,52,1,0,0,0,55,56,5,14,0,0,56,57,5,7,0,0,57,61,
        5,12,0,0,58,61,5,7,0,0,59,61,5,14,0,0,60,55,1,0,0,0,60,58,1,0,0,
        0,60,59,1,0,0,0,61,7,1,0,0,0,62,67,3,10,5,0,63,64,5,6,0,0,64,66,
        3,10,5,0,65,63,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,
        68,9,1,0,0,0,69,67,1,0,0,0,70,74,5,12,0,0,71,74,5,14,0,0,72,74,5,
        7,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,11,1,0,0,0,7,
        29,42,44,52,60,67,73
    ]

class FormulaParser ( Parser ):

    grammarFileName = "Formula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'->'", "'('", "')'", "','", 
                     "':'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "ADD", "SUB", "UINT", "UFLOAT", "NAME", 
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
    MUL=8
    DIV=9
    ADD=10
    SUB=11
    UINT=12
    UFLOAT=13
    NAME=14
    WS=15

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

        def expr(self):
            return self.getTypedRuleContext(FormulaParser.ExprContext,0)


        def EOF(self):
            return self.getToken(FormulaParser.EOF, 0)

        def getRuleIndex(self):
            return FormulaParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula" ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)




    def formula(self):

        localctx = FormulaParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expr(0)
            self.state = 13
            self.match(FormulaParser.EOF)
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
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = FormulaParser.LambdaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 16
                self.match(FormulaParser.T__0)
                self.state = 17
                self.args()
                self.state = 18
                self.match(FormulaParser.T__1)
                self.state = 19
                self.match(FormulaParser.T__2)
                self.state = 20
                self.expr(5)
                pass
            elif token in [12]:
                localctx = FormulaParser.UintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(FormulaParser.UINT)
                pass
            elif token in [13]:
                localctx = FormulaParser.UfloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(FormulaParser.UFLOAT)
                pass
            elif token in [14]:
                localctx = FormulaParser.NameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(FormulaParser.NAME)
                pass
            elif token in [4]:
                localctx = FormulaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(FormulaParser.T__3)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(FormulaParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = FormulaParser.MulDivContext(self, FormulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 32
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = FormulaParser.AddSubContext(self, FormulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 35
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = FormulaParser.GetItemContext(self, FormulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 38
                        self.match(FormulaParser.T__0)
                        self.state = 39
                        self.indexes()
                        self.state = 40
                        self.match(FormulaParser.T__1)
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            self.state = 47
            self.arg()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 48
                self.match(FormulaParser.T__5)
                self.state = 49
                self.arg()
                self.state = 54
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
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = FormulaParser.ArgWithSizeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(FormulaParser.NAME)
                self.state = 56
                self.match(FormulaParser.T__6)
                self.state = 57
                self.match(FormulaParser.UINT)
                pass

            elif la_ == 2:
                localctx = FormulaParser.ArgWithoutNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(FormulaParser.T__6)
                pass

            elif la_ == 3:
                localctx = FormulaParser.ArgWithoutSizeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
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
            self.state = 62
            self.index()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 63
                self.match(FormulaParser.T__5)
                self.state = 64
                self.index()
                self.state = 69
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
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = FormulaParser.UintIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(FormulaParser.UINT)
                pass
            elif token in [14]:
                localctx = FormulaParser.NameIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(FormulaParser.NAME)
                pass
            elif token in [7]:
                localctx = FormulaParser.AllIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(FormulaParser.T__6)
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




