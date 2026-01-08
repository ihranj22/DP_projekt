# Generated from gramatika_recepti.g4 by ANTLR 4.13.1
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
        4,1,22,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,
        0,30,8,0,1,1,1,1,3,1,34,8,1,1,2,1,2,3,2,38,8,2,1,2,1,2,3,2,42,8,
        2,1,3,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,4,1,4,3,4,54,8,4,1,4,
        1,4,3,4,58,8,4,1,4,3,4,61,8,4,1,4,3,4,64,8,4,1,4,1,4,1,4,1,4,3,4,
        70,8,4,1,4,3,4,73,8,4,1,4,3,4,76,8,4,3,4,78,8,4,1,5,1,5,3,5,82,8,
        5,1,6,1,6,3,6,86,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,6,1,0,2,3,1,0,15,
        16,1,0,5,6,1,0,13,14,1,0,11,12,1,0,20,21,98,0,29,1,0,0,0,2,31,1,
        0,0,0,4,35,1,0,0,0,6,43,1,0,0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,83,
        1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,30,1,0,0,0,17,18,3,4,2,0,
        18,19,5,0,0,1,19,30,1,0,0,0,20,21,3,8,4,0,21,22,5,0,0,1,22,30,1,
        0,0,0,23,24,3,10,5,0,24,25,5,0,0,1,25,30,1,0,0,0,26,27,3,12,6,0,
        27,28,5,0,0,1,28,30,1,0,0,0,29,14,1,0,0,0,29,17,1,0,0,0,29,20,1,
        0,0,0,29,23,1,0,0,0,29,26,1,0,0,0,30,1,1,0,0,0,31,33,5,1,0,0,32,
        34,5,18,0,0,33,32,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,37,7,0,0,
        0,36,38,5,17,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,41,
        3,6,3,0,40,42,5,18,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,
        43,48,5,19,0,0,44,45,7,1,0,0,45,47,5,19,0,0,46,44,1,0,0,0,47,50,
        1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,7,1,0,0,0,50,48,1,0,0,0,51,
        53,7,2,0,0,52,54,5,7,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,
        0,55,57,5,8,0,0,56,58,7,3,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,60,
        1,0,0,0,59,61,3,6,3,0,60,59,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,
        62,64,5,18,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,78,1,0,0,0,65,66,5,
        9,0,0,66,67,5,10,0,0,67,69,7,4,0,0,68,70,7,3,0,0,69,68,1,0,0,0,69,
        70,1,0,0,0,70,72,1,0,0,0,71,73,3,6,3,0,72,71,1,0,0,0,72,73,1,0,0,
        0,73,75,1,0,0,0,74,76,5,18,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,
        1,0,0,0,77,51,1,0,0,0,77,65,1,0,0,0,78,9,1,0,0,0,79,81,5,4,0,0,80,
        82,5,18,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,83,85,7,5,
        0,0,84,86,5,18,0,0,85,84,1,0,0,0,85,86,1,0,0,0,86,13,1,0,0,0,15,
        29,33,37,41,48,53,57,60,63,69,72,75,77,81,85
    ]

class gramatika_receptiParser ( Parser ):

    grammarFileName = "gramatika_recepti.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'imam'", "'sastojci'", "'pomoc'", 
                     "'daj'", "'predlozi'", "'mi'", "'recept'", "'sto'", 
                     "'mogu'", "'kuhati'", "'skuhati'", "'s'", "'od'", "'i'", 
                     "','", "':'", "<INVALID>", "<INVALID>", "'izlaz'", 
                     "'dovidenja'" ]

    symbolicNames = [ "<INVALID>", "POZDRAV", "IMAM", "SASTOJCI", "POMOC", 
                      "DAJ", "PREDLOZI", "MI", "RECEPT", "STO", "MOGU", 
                      "KUHATI", "SKUHATI", "S", "OD", "I", "ZAREZ", "DVOTOCKA", 
                      "INTERPUNKCIJA", "SASTOJAK", "IZLAZ", "DOVIDJENJA", 
                      "WS" ]

    RULE_ulaz = 0
    RULE_pozdrav = 1
    RULE_sastojciInput = 2
    RULE_listaSastojaka = 3
    RULE_zahtjevRecept = 4
    RULE_pomoc = 5
    RULE_izlaz = 6

    ruleNames =  [ "ulaz", "pozdrav", "sastojciInput", "listaSastojaka", 
                   "zahtjevRecept", "pomoc", "izlaz" ]

    EOF = Token.EOF
    POZDRAV=1
    IMAM=2
    SASTOJCI=3
    POMOC=4
    DAJ=5
    PREDLOZI=6
    MI=7
    RECEPT=8
    STO=9
    MOGU=10
    KUHATI=11
    SKUHATI=12
    S=13
    OD=14
    I=15
    ZAREZ=16
    DVOTOCKA=17
    INTERPUNKCIJA=18
    SASTOJAK=19
    IZLAZ=20
    DOVIDJENJA=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class UlazContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pozdrav(self):
            return self.getTypedRuleContext(gramatika_receptiParser.PozdravContext,0)


        def EOF(self):
            return self.getToken(gramatika_receptiParser.EOF, 0)

        def sastojciInput(self):
            return self.getTypedRuleContext(gramatika_receptiParser.SastojciInputContext,0)


        def zahtjevRecept(self):
            return self.getTypedRuleContext(gramatika_receptiParser.ZahtjevReceptContext,0)


        def pomoc(self):
            return self.getTypedRuleContext(gramatika_receptiParser.PomocContext,0)


        def izlaz(self):
            return self.getTypedRuleContext(gramatika_receptiParser.IzlazContext,0)


        def getRuleIndex(self):
            return gramatika_receptiParser.RULE_ulaz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUlaz" ):
                listener.enterUlaz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUlaz" ):
                listener.exitUlaz(self)




    def ulaz(self):

        localctx = gramatika_receptiParser.UlazContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ulaz)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.pozdrav()
                self.state = 15
                self.match(gramatika_receptiParser.EOF)
                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.sastojciInput()
                self.state = 18
                self.match(gramatika_receptiParser.EOF)
                pass
            elif token in [5, 6, 9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.zahtjevRecept()
                self.state = 21
                self.match(gramatika_receptiParser.EOF)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.pomoc()
                self.state = 24
                self.match(gramatika_receptiParser.EOF)
                pass
            elif token in [20, 21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.izlaz()
                self.state = 27
                self.match(gramatika_receptiParser.EOF)
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


    class PozdravContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POZDRAV(self):
            return self.getToken(gramatika_receptiParser.POZDRAV, 0)

        def INTERPUNKCIJA(self):
            return self.getToken(gramatika_receptiParser.INTERPUNKCIJA, 0)

        def getRuleIndex(self):
            return gramatika_receptiParser.RULE_pozdrav

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPozdrav" ):
                listener.enterPozdrav(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPozdrav" ):
                listener.exitPozdrav(self)




    def pozdrav(self):

        localctx = gramatika_receptiParser.PozdravContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pozdrav)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(gramatika_receptiParser.POZDRAV)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 32
                self.match(gramatika_receptiParser.INTERPUNKCIJA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SastojciInputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaSastojaka(self):
            return self.getTypedRuleContext(gramatika_receptiParser.ListaSastojakaContext,0)


        def IMAM(self):
            return self.getToken(gramatika_receptiParser.IMAM, 0)

        def SASTOJCI(self):
            return self.getToken(gramatika_receptiParser.SASTOJCI, 0)

        def DVOTOCKA(self):
            return self.getToken(gramatika_receptiParser.DVOTOCKA, 0)

        def INTERPUNKCIJA(self):
            return self.getToken(gramatika_receptiParser.INTERPUNKCIJA, 0)

        def getRuleIndex(self):
            return gramatika_receptiParser.RULE_sastojciInput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSastojciInput" ):
                listener.enterSastojciInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSastojciInput" ):
                listener.exitSastojciInput(self)




    def sastojciInput(self):

        localctx = gramatika_receptiParser.SastojciInputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sastojciInput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 36
                self.match(gramatika_receptiParser.DVOTOCKA)


            self.state = 39
            self.listaSastojaka()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 40
                self.match(gramatika_receptiParser.INTERPUNKCIJA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaSastojakaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SASTOJAK(self, i:int=None):
            if i is None:
                return self.getTokens(gramatika_receptiParser.SASTOJAK)
            else:
                return self.getToken(gramatika_receptiParser.SASTOJAK, i)

        def I(self, i:int=None):
            if i is None:
                return self.getTokens(gramatika_receptiParser.I)
            else:
                return self.getToken(gramatika_receptiParser.I, i)

        def ZAREZ(self, i:int=None):
            if i is None:
                return self.getTokens(gramatika_receptiParser.ZAREZ)
            else:
                return self.getToken(gramatika_receptiParser.ZAREZ, i)

        def getRuleIndex(self):
            return gramatika_receptiParser.RULE_listaSastojaka

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaSastojaka" ):
                listener.enterListaSastojaka(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaSastojaka" ):
                listener.exitListaSastojaka(self)




    def listaSastojaka(self):

        localctx = gramatika_receptiParser.ListaSastojakaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listaSastojaka)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(gramatika_receptiParser.SASTOJAK)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                self.match(gramatika_receptiParser.SASTOJAK)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ZahtjevReceptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECEPT(self):
            return self.getToken(gramatika_receptiParser.RECEPT, 0)

        def DAJ(self):
            return self.getToken(gramatika_receptiParser.DAJ, 0)

        def PREDLOZI(self):
            return self.getToken(gramatika_receptiParser.PREDLOZI, 0)

        def MI(self):
            return self.getToken(gramatika_receptiParser.MI, 0)

        def listaSastojaka(self):
            return self.getTypedRuleContext(gramatika_receptiParser.ListaSastojakaContext,0)


        def INTERPUNKCIJA(self):
            return self.getToken(gramatika_receptiParser.INTERPUNKCIJA, 0)

        def S(self):
            return self.getToken(gramatika_receptiParser.S, 0)

        def OD(self):
            return self.getToken(gramatika_receptiParser.OD, 0)

        def STO(self):
            return self.getToken(gramatika_receptiParser.STO, 0)

        def MOGU(self):
            return self.getToken(gramatika_receptiParser.MOGU, 0)

        def KUHATI(self):
            return self.getToken(gramatika_receptiParser.KUHATI, 0)

        def SKUHATI(self):
            return self.getToken(gramatika_receptiParser.SKUHATI, 0)

        def getRuleIndex(self):
            return gramatika_receptiParser.RULE_zahtjevRecept

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZahtjevRecept" ):
                listener.enterZahtjevRecept(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZahtjevRecept" ):
                listener.exitZahtjevRecept(self)




    def zahtjevRecept(self):

        localctx = gramatika_receptiParser.ZahtjevReceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_zahtjevRecept)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 52
                    self.match(gramatika_receptiParser.MI)


                self.state = 55
                self.match(gramatika_receptiParser.RECEPT)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13 or _la==14:
                    self.state = 56
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 59
                    self.listaSastojaka()


                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 62
                    self.match(gramatika_receptiParser.INTERPUNKCIJA)


                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(gramatika_receptiParser.STO)
                self.state = 66
                self.match(gramatika_receptiParser.MOGU)
                self.state = 67
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13 or _la==14:
                    self.state = 68
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 71
                    self.listaSastojaka()


                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 74
                    self.match(gramatika_receptiParser.INTERPUNKCIJA)


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


    class PomocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POMOC(self):
            return self.getToken(gramatika_receptiParser.POMOC, 0)

        def INTERPUNKCIJA(self):
            return self.getToken(gramatika_receptiParser.INTERPUNKCIJA, 0)

        def getRuleIndex(self):
            return gramatika_receptiParser.RULE_pomoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPomoc" ):
                listener.enterPomoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPomoc" ):
                listener.exitPomoc(self)




    def pomoc(self):

        localctx = gramatika_receptiParser.PomocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pomoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(gramatika_receptiParser.POMOC)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 80
                self.match(gramatika_receptiParser.INTERPUNKCIJA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IzlazContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IZLAZ(self):
            return self.getToken(gramatika_receptiParser.IZLAZ, 0)

        def DOVIDJENJA(self):
            return self.getToken(gramatika_receptiParser.DOVIDJENJA, 0)

        def INTERPUNKCIJA(self):
            return self.getToken(gramatika_receptiParser.INTERPUNKCIJA, 0)

        def getRuleIndex(self):
            return gramatika_receptiParser.RULE_izlaz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIzlaz" ):
                listener.enterIzlaz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIzlaz" ):
                listener.exitIzlaz(self)




    def izlaz(self):

        localctx = gramatika_receptiParser.IzlazContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_izlaz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 84
                self.match(gramatika_receptiParser.INTERPUNKCIJA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





