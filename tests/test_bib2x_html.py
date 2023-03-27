from __future__ import print_function
# ===================================================================
# test_bib2x.py
#
# Tests module for bib2x
#
# (c) Daniel Krajzewicz 2020-2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/morphoxes
# - http://www.krajzewicz.de/blog/morphoxes.php
#
# Available under the BSD license.
# ===================================================================
import sys
import os
import shutil
from testfixtures import TempDirectory
from bib2x import bib2x
from bib2x import texhandler
from bib2x.texhandler import html


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "bib2x").replace("pytest.py", "bib2x").replace("__main__.py", "bib2x")

def bread(path):
    with open(path, "rb") as fd:
        return fd.read()



# --- test functions ------------------------------------------------
def test_main_turing2json(capsys):
    """Test behaviour when help is wished"""
    dir = os.path.split(__file__)[:-1]
    test_dir = os.path.join(*dir)
    d = TempDirectory()
    ipath = os.path.join(d.as_path(), "turing.bib")
    shutil.copy(os.path.join(test_dir, "turing.bib"), ipath)
    opath = os.path.join(d.as_path(), "turing.html")
    bib2x.main(["-i", ipath, "-o", opath, "-f", "html"])
    captured = capsys.readouterr()
    assert patchName(captured.out) == "Turing:1935:ELR 7\nTuring:1936:CNA 7\nTuring:1937:CD 7\nTuring:1937:CNA 7\nTuring:1937:FC 7\nTuring:1938:EG 7\nTuring:1938:FAL 7\nTuring:1938:SLB 9\nTuring:1939:SLB 7\nTuring:1940:TE 10\nNewman:1942:FTC 7\nTuring:1942:UDB 7\nTuring:1943:MCZ 7\nTuring:1945:PDM 10\nTuring:1946:PEC 10\nHartree:1947:MTL 4\nTuring:1947:LMF 4\nTuring:1948:IM 10\nTuring:1948:PFT 7\nTuring:1948:REM 7\nBodewig:1949:RRE 7\nTuring:1949:CLR 13\nMissing required attribute 'booktitle' in Turing:1949:CLR\nTuring:1950:CMI 7\nTuring:1950:WPS 7\nTuring:1951:LPM 13\nMissing required attribute 'booktitle' in Turing:1951:LPM\nLighthill:1951:MCM 10\nTuring:1951:PHM 6\nTuring:1952:CBM 7\nTuring:1953:DCA 13\nMissing required attribute 'booktitle' in Turing:1953:DCA\nTuring:1953:SCR 7\nTuring:1954:SUP 7\nTuring:1959:AMT 4\nTuring:1960:KMD 4\nTuring:1960:MLM 4\nAnderson:1964:MM 4\nCurtis:1965:TMS 7\nTuring:1965:SLB 12\nMissing required attribute 'booktitle' in Turing:1965:SLB\nMeltzer:1969:MI 4\nTuring:1969:IM 7\nLehman:1970:DZR 7\nWilkinson:1971:SCN 7\nRandell:1972:ATOa 10\nRandell:1972:ATOb 13\nMissing required attribute 'booktitle' in Randell:1972:ATOb\nTuring:1972:MTO 10\nTuring:1974:PPM 4\nAlton:1977:RPA 10\nCarpenter:1977:OTM 7\nLewin:1978:UGW 4\nBianco:1979:IFM 4\nAspray:1980:MCC 9\nMichie:1980:TOC 7\nWilkinson:1980:TWN 12\nEvans:1981:MMH 4\nCordy:1983:TAN 13\nMissing required attribute 'booktitle' in Cordy:1983:TAN\nCordy:1983:TNG 13\nMissing required attribute 'booktitle' in Cordy:1983:TNG\nHodges:1983:ATEa 4\nHodges:1983:ATEb 4\nAnderson:1984:CSM 4\nBolter:1984:TMW 4\nHolt:1984:ICS 4\nMorris:1984:EPP 7\nUnknown:1984:ATE 7\nAlton:1985:SCP 10\nHodges:1985:ATE 4\nHull:1985:NT 7\nTuring:1985:MM 4\nCarpenter:1986:MTA 4\nHolt:1986:DGT 10\nTuring:1986:LLM 7\nTuring:1986:MTA 4\nCordy:1987:DIE 7\nHochhuth:1987:ATE 4\nHolt:1987:TPL 10\nTherkildsen:1987:GAA 10\nTuring:1987:ISS 4\nWhitemore:1987:BCa 4\nWhitemore:1987:BCb 4\nWhitemore:1987:BCS 4\nLevy:1988:CCC 4\nHerken:1988:UTM 4\nHodges:1988:ATO 4\nHolt:1988:CPO 10\nHolt:1988:CPU 10\nHolt:1988:TPLa 7\nHolt:1988:TPLb 4\nPerelgut:1988:TPC 7\nTomayko:1988:AAT 7\nWeiss:1988:BOP 7\nWhitemore:1988:BC 4\nWhitemore:1988:BCP 4\nDewdney:1989:TOE 4\nHochhuth:1989:AT 4\nHodges:1989:ATEb 4\nHodges:1989:ATEa 4\nWilliams:1989:EBC 4\nDeavours:1990:TBW 7\nHolt:1990:ICS 4\nHume:1990:ICS 4\nMangel:1990:CTB 4\nStewart:1990:DTM 10\nEndresen:1991:TTA 10\nHuskey:1991:MED 7\nRigamonti:1991:TGS 4\nGood:1992:IRA 12\nMissing required attribute 'booktitle' in Good:1992:IRA\nHarrison:1992:TON 4\nHodges:1992:ATE 4\nPool:1992:DTD 7\nTuring:1992:M 4\nTuring:1992:MI 4\nDewdney:1993:NTO 4\nHill:1993:ATM 7\nHinsley:1993:CIS 4\nMurray:1993:MB 4\nSaunders:1993:ATB 7\nTropp:1993:CQD 7\nCrockett:1994:TTF 4\nHodges:1994:ATE 4\nSchonhage:1994:FAM 4\nStewart:1994:SNT 7\nSzepietowski:1994:TMS 4\nTuring:1994:IM 4\nGoranzon:1995:JAG 4\nHerken:1995:UTM 4\nTropp:1995:CQD 7\nTuring:1995:MT 4\nZabell:1995:ATC 7\nAnonymous:1996:QIO 4\nClark:1996:LAT 4\nGottfried:1996:ATA 4\nKidwell:1996:CWM 7\nLaplante:1996:GPC 4\nMillican:1996:LAT 4\nTuring:1996:IMH 7\nBenda:1997:TLI 7\nHodges:1997:ATHa 4\nHodges:1997:ATHb 4\nHodges:1997:TNP 4\nJastrow:1997:GGE 4\nLindsay:1997:BC 4\nRobinson:1997:GIP 4\nBarnette:1998:AT 4\nBloor:1998:GMA 4\nDeavours:1998:SCH 4\nLassegue:1998:T 4\nCopeland:1999:ATF 7\nGoutefangea:1999:ATP 9\nHodges:1999:T 4\nKnauff:1999:CCM 4\nStrathern:1999:TCB 4\nTuring:1999:MLM 4\nTuring:1999:TTE 10\nAnonymous:2000:AMT 4\nCopeland:2000:WTD 7\nDavis:2000:UCR 4\nHodges:2000:ATA 4\nHodges:2000:ATE 4\nRaphael:2000:GP 4\nRandell:2000:TML 7\nAgar:2001:TUM 4\nCastelfranchi:2001:AAA 7\nCopeland:2001:ANT 4\nDonofrio:2001:BIT 4\nDonofrio:2001:FM 7\nGladwin:2001:ATV 7\nHodges:2001:ATO 4\nPrager:2001:T 4\nTuring:2001:CWM 4\nTuring:2001:ML 4\nTuring:2001:VNC 7\nFlynn:2002:CS 4\nHarman:2002:CSM 4\nHodges:2002:EZS 4\nScheutz:2002:CND 4\nWelland:2002:TLS 4\nBooss:2003:MW 4\nGladwin:2003:AMT 7\nHodges:2003:SEV 4\nKovac:2003:TLC 4\nMoor:2003:TTE 4\nNewton:2003:ATS 4\nPapadimitriou:2003:TNA 4\nPazSoldan:2003:DT 4\nTofts:2003:PCI 4\nTuring:2003:CRS 7\nDeBrosse:2004:SBU 4\nCopeland:2004:ETS 4\nLemire:2004:ATH 4\nPiper:2004:TLC 4\nShieber:2004:TTV 4\nTeuscher:2004:ATL 4\nBrooks:2005:TLC 4\nCappuccio:2005:ATU 4\nCopeland:2005:IGA 4\nDeAngelis:2005:CPD 4\nHawking:2005:GCI 4\nLeavitt:2005:MWK 4\nLombardi:2005:LML 4\nNumerico:2005:ATI 4\nPiper:2005:CSG 7\nSmith:2005:TMS 7\nTuring:2005:NM 12\nMissing required attribute 'booktitle' in Turing:2005:NM\nTuring:2005:PEC 12\nMissing required attribute 'booktitle' in Turing:2005:PEC\nTuring:2005:TWL 12\nMissing required attribute 'booktitle' in Turing:2005:TWL\nBooker:2006:TRH 7\nCasselman:2006:BTM 7\nCasselman:2006:MTE 7\nCooper:2006:MWK 7\nDavis:2006:WIR 7\nFeferman:2006:TT 7\nHodges:2006:ETB 7\nJames:2006:ASH 4\nMairs:2006:TLL 4\nLevin:2006:MDT 4\nPazSoldan:2006:TD 4\nBecher:2007:TUA 7\nCorrigan:2007:AT 4\nEpstein:2007:PTT 4\nPatera:2007:MAH 4\nPetzold:2008:ATG 4\nBrown:2009:TAT 4\nMishra:2009:TPW 7\nMahon:2010:NEH 4\nSmiley:2010:MWI 4\nAnonymous:2011:TPS 7\nCook:2011:PPT 7\nCopeland:2011:MCRa 7\nCopeland:2011:MCRb 7\nMcGrayne:2011:TWH 4\nTrudgian:2011:ITM 7\nCooper:2012:TTM 7\nTuring:19xx:NNN 11\nAnonymous:1949:RCH 11\nAnonymous:1951:MUC 11\nBowden:1953:FTT 11\nFeldman:1963:CTC 4\nDavis:1965:UBP 4\nEvans:1968:CKP 4\nMichie:1969:MI 4\nMeltzer:1972:MI 11\nSTUG:1983:PUA 11\nUSENIX:1983:UCPb 11\nTuring:1992:PM 4\nRaphael:2000:GPS 4\nRaphael:2001:GPS 4\nCopeland:2005:ATA 4\n"
    #assert patchName(captured.err) == "Nooooooo! May be the same turing file!!!"
    assert bread(os.path.join(d.as_path(), "turing.html")) == bread(os.path.join(test_dir, "turing.html"))
    d.cleanup()