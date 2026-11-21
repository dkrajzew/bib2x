#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - Tests bstparser builtin functions"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.4.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Development"
# ===========================================================================
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import bib2x.bstparser as bstparser


# --- test classes ------------------------------------------------------------
class TestBSTParser_Builtin(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._parser = bstparser.BSTParser()


    def test__bst_parse__add1(self):
        self._parser._stack.append(1)
        self._parser._stack.append(1)
        assert(self._parser._add()==2)
        assert(self._parser._stack==[])
    

    def test__bst_parse__sub1(self):
        self._parser._stack.append(1)
        self._parser._stack.append(1)
        assert(self._parser._sub()==0)
        assert(self._parser._stack==[])
    

    def test__bst_parse__gt1(self):
        self._parser._stack.append(1)
        self._parser._stack.append(1)
        assert(self._parser._gt()==0)
        assert(self._parser._stack==[])
    
    def test__bst_parse__gt2(self):
        self._parser._stack.append(2)
        self._parser._stack.append(1)
        assert(self._parser._gt()==1)
        assert(self._parser._stack==[])
    
    def test__bst_parse__gt3(self):
        self._parser._stack.append(1)
        self._parser._stack.append(2)
        assert(self._parser._gt()==0)
        assert(self._parser._stack==[])
    

    def test__bst_parse__lt1(self):
        self._parser._stack.append(1)
        self._parser._stack.append(1)
        assert(self._parser._lt()==0)
        assert(self._parser._stack==[])
    
    def test__bst_parse__lt2(self):
        self._parser._stack.append(1)
        self._parser._stack.append(2)
        assert(self._parser._lt()==1)
        assert(self._parser._stack==[])

    def test__bst_parse__lt3(self):
        self._parser._stack.append(2)
        self._parser._stack.append(1)
        assert(self._parser._lt()==0)
        assert(self._parser._stack==[])
    

    def test__bst_parse__eq1(self):
        self._parser._stack.append(1)
        self._parser._stack.append(1)
        assert(self._parser._eq()==1)
        assert(self._parser._stack==[])
    
    def test__bst_parse__eq2(self):
        self._parser._stack.append(1)
        self._parser._stack.append(2)
        assert(self._parser._eq()==0)
        assert(self._parser._stack==[])


    def test__bst_parse__concat1(self):
        self._parser._stack.append("Hello")
        self._parser._stack.append("World")
        assert(self._parser._concat()=="HelloWorld")
        assert(self._parser._stack==[])


    def test__bst_parse__add_period1(self):
        self._parser._stack.append("Hello")
        assert(self._parser._add_period()=="Hello.")
        assert(self._parser._stack==[])

    def test__bst_parse__add_period2(self):
        self._parser._stack.append("Hello.")
        assert(self._parser._add_period()=="Hello.")
        assert(self._parser._stack==[])


    def test__bst_parse__change_case1(self):
        self._parser._stack.append("Hello")
        self._parser._stack.append("l")
        assert(self._parser._change_case()=="hello")
        assert(self._parser._stack==[])

    def test__bst_parse__change_case2(self):
        self._parser._stack.append("Hello")
        self._parser._stack.append("u")
        assert(self._parser._change_case()=="HELLO")
        assert(self._parser._stack==[])

    def test__bst_parse__change_case3(self):
        self._parser._stack.append("HEllo")
        self._parser._stack.append("t")
        assert(self._parser._change_case()=="Hello")
        assert(self._parser._stack==[])


    def test__bst_parse__duplicate1(self):
        self._parser._stack.append("Hello")
        assert(self._parser._duplicate()=="Hello")
        assert(self._parser._stack==["Hello"])
        
    def test__bst_parse__duplicate2(self):
        self._parser._stack.append(1)
        assert(self._parser._duplicate()==1)
        assert(self._parser._stack==[1])
        

    def test__bst_parse__empty1(self):
        self._parser._stack.append("Hello")
        assert(self._parser._empty()==0)
        assert(self._parser._stack==[])
        
    def test__bst_parse__empty2(self):
        self._parser._stack.append("")
        assert(self._parser._empty()==1)
        assert(self._parser._stack==[])
        
        
    def test__bst_parse__change_case__t1(self):
        self._parser._stack.append("lower")
        self._parser._stack.append("t")
        assert(self._parser._change_case()=="lower")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__t2(self):
        self._parser._stack.append("Lower")
        self._parser._stack.append("t")
        assert(self._parser._change_case()=="Lower")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__t3(self):
        self._parser._stack.append("LOWER")
        self._parser._stack.append("t")
        assert(self._parser._change_case()=="Lower")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__l1(self):
        self._parser._stack.append("lower")
        self._parser._stack.append("l")
        assert(self._parser._change_case()=="lower")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__l2(self):
        self._parser._stack.append("Lower")
        self._parser._stack.append("l")
        assert(self._parser._change_case()=="lower")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__l3(self):
        self._parser._stack.append("LOWER")
        self._parser._stack.append("l")
        assert(self._parser._change_case()=="lower")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__u1(self):
        self._parser._stack.append("lower")
        self._parser._stack.append("u")
        assert(self._parser._change_case()=="LOWER")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__u2(self):
        self._parser._stack.append("Lower")
        self._parser._stack.append("u")
        assert(self._parser._change_case()=="LOWER")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__u3(self):
        self._parser._stack.append("LOWER")
        self._parser._stack.append("u")
        assert(self._parser._change_case()=="LOWER")
        assert(self._parser._stack==[])
        
    def test__bst_parse__change_case__unknown1(self):
        self._parser._stack.append("LOWER")
        self._parser._stack.append("x")
        try:
            self._parser._change_case()
            assert(False) # pragma: no cover
        except ValueError as e:
            assert(str(e)=="_change_case got an unknown command 'x'")
        # !!! tests for missing values at stack
                  
        
    def test__bst_parse__chr_to_int1(self):
        self._parser._stack.append("a")
        assert(self._parser._chr_to_int()==97)
        assert(self._parser._stack==[])
        
    def test__bst_parse__chr_to_int2(self):
        self._parser._stack.append("b")
        assert(self._parser._chr_to_int()==98)
        assert(self._parser._stack==[])
      
        
    def test__bst_parse__int_to_chr1(self):
        self._parser._stack.append(97)
        assert(self._parser._int_to_chr()=="a")
        assert(self._parser._stack==[])
        
    def test__bst_parse__int_to_chr2(self):
        self._parser._stack.append(98)
        assert(self._parser._int_to_chr()=="b")
        assert(self._parser._stack==[])
      
        
    def test__bst_parse__int_to_str1(self):
        self._parser._stack.append(97)
        assert(self._parser._int_to_str()=="a")
        assert(self._parser._stack==[])
        
    def test__bst_parse__int_to_str2(self):
        self._parser._stack.append(98)
        assert(self._parser._int_to_str()=="b")
        assert(self._parser._stack==[])
      
        
    def test__bst_parse__num_names1(self):
        self._parser._stack.append("Daniel Krajzewicz")
        assert(self._parser._num_names()==1)
        assert(self._parser._stack==[])
        
    def test__bst_parse__num_names2(self):
        self._parser._stack.append("Daniel Krajzewicz and Daniel Krajzewicz")
        assert(self._parser._num_names()==2)
        assert(self._parser._stack==[])
      
        
    def test__bst_parse__pop1(self):
        self._parser._stack.append("a")
        assert(self._parser._pop()==None)
        assert(self._parser._stack==[])
        
    def test__bst_parse__pop2(self):
        self._parser._stack.append("a")
        self._parser._stack.append("b")
        assert(self._parser._pop()==None)
        assert(self._parser._stack==["a"])
      
        
    def test__bst_parse__quote1(self):
        self._parser._stack.append("foo")
        assert(self._parser._pop()==None)
        assert(self._parser._stack==[])
      

    def test__bst_parse__swap1(self):
        self._parser._stack.append("foo")
        self._parser._stack.append("bar")
        assert(self._parser._swap()=="foo")
        assert(self._parser._stack==["bar"])
      
        
    def test__bst_parse__text_length1(self):
        self._parser._stack.append("foo")
        assert(self._parser._text_length()==3)
        assert(self._parser._stack==[])
        

    def test__bst_parse__text_prefix1(self):
        self._parser._stack.append("foo")
        self._parser._stack.append(1)
        assert(self._parser._text_prefix()=="f")
        assert(self._parser._stack==[])
        
    def test__bst_parse__text_prefix2(self):
        self._parser._stack.append("foo")
        self._parser._stack.append(2)
        assert(self._parser._text_prefix()=="fo")
        assert(self._parser._stack==[])
        
        
        
"""
    def _assign(self, entry=None):
        var = self.stack_pop()
        v = self.stack_pop()
        if var in strvars: # !!! type check v
            strvars[var] = v
        if var in intvars: # !!! type check v
            intvars[var] = v
        return None

    def _call_type(self, entry=None):
        raise "_call_type"



    def _global_max(self, entry=None):
        return 10000
        

    def _if(self, entry=None):
        f2 = self.stack_pop()
        f1 = self.stack_pop()
        i = self.stack_pop()
        return f1(entry) if i>0 else f2(entry)
        

    def _missing(self, entry=None):
        c = self.stack_pop()
        return 1 if self.has_attribute(entry, c) else 0
        
    def _newline(self, entry=None):
        report("\n")
        return None


    def _preamble(self, entry=None):
        return "" # !!!

    def _purify(self, entry=None):
        raise "purify"

    def _quote(self, entry=None):
        return '"'

    def _skip(self, entry=None):
        return None

    def _sort_key(self, entry=None):
        raise "sort_key"

    def _stack(self, entry=None):
        print (self._stack)
        self._stack = []
        return None

    def _substring(self, entry=None):
        i2 = self.stack_pop()
        i1 = self.stack_pop()
        s = self.stack_pop()
        return s[i1+1:i1+i2+1]


    def _top(self, entry=None):
        print (self.stack_pop())
        return None

    def _type(self, entry=None):
        raise "type"

    def _warning(self, entry=None):
        print ("Warning: " + stack_pop())
        return None

    def _while(self, entry=None):
        f2 = self.stack_pop()
        f1 = self.stack_pop()
        while f2(entry):
            f1(entry)
        return None

    def _width(self, entry=None):
        raise "width"

    def _write(self, entry=None):
        s = self.stack_pop()
        report(s)
        return None
"""        
        