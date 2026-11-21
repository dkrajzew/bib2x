#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bib2x - a bibtex clone"""
# ===========================================================================
# - https://github.com/dkrajzew/bib2x
# - http://www.krajzewicz.de/docs/bib2x/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import bib2x.texfile as texfile
import bib2x.texhandler.memory as memoryhandler

class BSTParser:
    def __init__(self):
        self._intvars = {}
        self._strvars = {}
        self._fields = []
        self._functions = {}
        self._macros = {}
        self._entries = None
        self._stack = []
        self._name2brackets = {
            "entry": 3,
            "function": 2,
            "execute": 1,
            "integers": 1,
            "strings": 1,
            "macro": 2,
            "read": 0,
            "sort": 0,
            "iterate": 1,
            "reverse": 1,
        }
        self._internal_functions = {
            "+": self._add,
            "-": self._sub,
            ">": self._gt,
            "<": self._lt,
            "=": self._eq,
            "*": self._concat,
            ":=": self._assign,
            "add.period$": self._add_period,
            "call.type$": self._call_type,
            "change.case$": self._change_case,
            "chr.to.int$": self._chr_to_int,
            "cite$": self._cite,
            "duplicate$": self._duplicate,
            "empty$": self._empty,
            "format.name$": self._format_name,
            "global.max$": self._global_max,
            "if$": self._if,
            "int.to.chr$": self._int_to_chr,
            "int.to.str$": self._int_to_str,
            "missing$": self._missing,
            "newline$": self._newline,
            "num.names$": self._num_names,
            "pop$": self._pop,
            "preamble$": self._preamble,
            "purify$": self._purify,
            "quote$": self._quote,
            "skip$": self._skip,
            "sort.key$": self._sort_key,
            "stack$": self._stack,
            "substring$": self._substring,
            "swap$": self._swap,
            "text.length$": self._text_length,
            "text.prefix$": self._text_prefix,
            "top$": self._top,
            "type$": self._type,
            "warning$": self._warning,
            "while$": self._while,
            "width$": self._width,
            "write$": self._write
        }

    def report(self, msg):
        print ("REPORT: %s" % msg)


    def _add(self, entry=None):
        v2 = self.stack_pop()
        v1 = self.stack_pop()
        return v1+v2

    def _sub(self, entry=None):
        v2 = self.stack_pop()
        v1 = self.stack_pop()
        return v1-v2

    def _gt(self, entry=None):
        v2 = self.stack_pop()
        v1 = self.stack_pop()
        return 1 if v1>v2 else 0

    def _lt(self, entry=None):
        v2 = self.stack_pop()
        v1 = self.stack_pop()
        return 1 if v1<v2 else 0

    def _eq(self, entry=None):
        v2 = self.stack_pop()
        v1 = self.stack_pop()
        return 1 if v1==v2 else 0

    def _concat(self, entry=None):
        v2 = self.stack_pop()
        v1 = self.stack_pop()
        return v1+v2

    def _assign(self, entry=None):
        var = self.stack_pop()
        v = self.stack_pop()
        if var in strvars: # !!! type check v
            strvars[var] = v
        if var in intvars: # !!! type check v
            intvars[var] = v
        return None

    def _add_period(self, entry=None):
        v = self.stack_pop()
        if v[-1]=='.' or v[-1]=='!' or v[-1]=='?':
            return v
        return v + "."

    def _call_type(self, entry=None):
        raise "_call_type"

    def _change_case(self, entry=None):
        t = self.stack_pop()
        v = self.stack_pop()
        if t=="t":
            vt = v.lower()
            return v[0] + vt[1:]
        if t=="l":
            return v.lower()
        if t=="u":
            return v.upper()
        raise ValueError(f"_change_case got an unknown command '{t}'")

    def _cite(self, entry=None):
        return entry

    def _duplicate(self, entry=None):
        v = self.stack_pop()
        self._stack.append(v)
        return v

    def _empty(self, entry=None): # !!! recheck
        v = self.stack_pop() # !!!
        return 1 if v=="" else 0 # !!!
        #return 1 if len(self._stack)==0 else 0


    def _format_name(self, entry=None):
        s2 = self.stack_pop()
        i = int(self.stack_pop())
        s1 = self.stack_pop()
        names = s1.split(" and ")
        namevals = self._split_name(names[i-1])
        #print (namevals)
        # parse parts (!!! improve)
        parts = []
        b = 0
        e = 0
        depth = 0
        while e<len(s2):
            if s2[e]=='{':
                depth += 1
                e += 1
                continue
            if s2[e]=='}':
                if depth==0:
                    raise ValueError("no")
                depth -= 1
                if depth==0:
                    p = s2[b:e+1]
                    parts.append(p)
                    b = e + 1
                    e = b
                    continue
            e += 1
        if b!=e:
            p = s2[b:]
            parts.append(p)
        # format
        ret = ""
        for p in parts:
            while len(p)>0 and p[0]=='{' and p[-1]=='}':
                p = p[1:-1]
            if p.find("ff")>=0:
                p = p.replace("ff", namevals[0]) if len(namevals[0])!=0 else ""
            elif p.find("f")>=0:
                p = p.replace("f", str(namevals[0][0])) + '.' if len(namevals[0])!=0 else ""
            elif p.find("vv")>=0:
                p = p.replace("vv", namevals[1]) if len(namevals[1])!=0 else ""
            elif p.find("v")>=0:
                p = p.replace("v", str(namevals[1][0])) + '.' if len(namevals[1])!=0 else ""
            elif p.find("ll")>=0:
                p = p.replace("ll", namevals[2]) if len(namevals[2])!=0 else ""
            elif p.find("l")>=0:
                p = p.replace("l", str(namevals[2][0])) + '.' if len(namevals[2])!=0 else ""
            if p.find("jj")>=0:
                p = p.replace("jj", namevals[3]) if len(namevals[3])!=0 else ""
            elif p.find("j")>=0:
                p = p.replace("j", str(namevals[3][0])) + '.' if len(namevals[3])!=0 else ""
            p = p.replace("{", "").replace("}", "") # !!! {} als leerer String
            ret = ret + p

        return ret

    def _global_max(self, entry=None):
        return 10000


    def _if(self, entry=None):
        f2 = self.stack_pop()
        f1 = self.stack_pop()
        i = self.stack_pop()
        return f1(entry) if i>0 else f2(entry)

    def _chr_to_int(self, entry=None):
        return ord(self.stack_pop()[0])

    def _int_to_chr(self, entry=None):
        return chr(self.stack_pop())

    def _int_to_str(self, entry=None):
        return chr(self.stack_pop())

    def _missing(self, entry=None):
        c = self.stack_pop()
        return 1 if self.has_attribute(entry, c) else 0

    def _newline(self, entry=None):
        report("\n")
        return None

    def _num_names(self, entry=None):
        s = self.stack_pop()
        return s.count(" and ") + 1

    def _pop(self, entry=None):
        self.stack_pop()
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

    def _swap(self, entry=None):
        e2 = self.stack_pop()
        e1 = self.stack_pop()
        self._stack.append(e2)
        return e1

    def _text_length(self, entry=None):
        s = self.stack_pop()
        return len(s)

    def _text_prefix(self, entry=None):
        i = self.stack_pop()
        s = self.stack_pop()
        return s[:i]

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


    # ------- name processing

    def parse_name_no_comma(self, name):
        parts = name.split(" ")
        types = [-1]*len(parts)
        i = 0
        while i<len(parts):
            pi = 0
            #while pi<len(parts[i]) and (parts[i][pi]=='{' or parts[i][pi]=='/'):
            #    pi += 1
            if pi<len(parts[i]) and parts[i][pi].islower():
                types[i] = 1
            i += 1
        types[-1] = 2
        for i in range(0, len(parts)):
            if types[i]!=-1:
                continue
            if i>0 and i<len(parts)-2 and types[i-i]==1 and types[i+1]==1:
                types[i] = 1
            elif i==0 or types[i-1]==0:
                types[i] = 0
            else:
                types[i] = 2
        ret = [ "", "", "", "" ]
        for it,t in enumerate(parts):
            parts[it] = parts[it].replace("{", "").replace("}", "")
        for it,t in enumerate(types):
            if len(ret[t])!=0:
                ret[t] = ret[t] + " "
            ret[t] = ret[t] + parts[it]
        return ret


    def parse_name_one_comma(self, name):
        parts1 = name.split(",")
        first = parts1[1].split(" ")
        parts = parts1[0].split(" ")
        types = [-1]*len(parts)
        i = 0
        while i<len(parts):
            pi = 0
            if pi<len(parts[i]) and parts[i][pi].islower():
                types[i] = 1
            i += 1
        types[-1] = 2
        for i in range(0, len(parts)):
            if types[i]!=-1:
                continue
            if i>0 and i<len(parts)-2 and types[i-i]==1 and types[i+i]==1:
                types[i] = 1
            elif i<len(parts)-2 and types[i+1]==1:
                types[i] = 1
            else:
                types[i] = 2
        ret = [ "", "", "", "" ]
        for it,t in enumerate(first):
            p = first[it].replace("{", "").replace("}", "")
            if len(ret[0])!=0:
                ret[0] = ret[0] + " "
            ret[0] = ret[0] + p
        for it,t in enumerate(parts):
            parts[it] = parts[it].replace("{", "").replace("}", "")
        for it,t in enumerate(types):
            if len(ret[t])!=0:
                ret[t] = ret[t] + " "
            ret[t] = ret[t] + parts[it]
        return ret



    def parse_name_two_comma(self, name):
        parts = name.split(",")
        ret = one_comma(", ".join(list(parts[0], parts[2])))
        jrs = parts[1].strip().split(" ")
        for jr in jrs:
            p = jr.replace("{", "").replace("}", "")
            if len(ret[3]) != 0:
                ret[3] = ret[3] + " "
            ret[3] = ret[3] + p
        return ret

    def _split_name(self, name):
        nc = name.count(",")
        ret = []
        if nc==0:
            return self.parse_name_no_comma(name)
        elif nc == 1:
            return self.parse_name_one_comma(name)
        elif nc == 2:
            return self.parse_name_two_comma(name)
        else:
            raise ValueException("no")

    # !!! make following internal as well (add _ prefix)


    def stack_pop(self):
        l = self._stack[-1]
        self._stack = self._stack[:-1]
        return l


    def get_name(self, src, pos):
        b = pos
        while pos<len(src) and src[pos]!=' ' and src[pos]!='\n' and src[pos]!='{':
            pos += 1
        return src[b:pos]


    def get_end(self, src, pos):
        n = 0
        quoting = False
        while True:
            if src[pos]=='"':
                quoting = not quoting
            if not quoting:
                if src[pos]=='{':
                    n += 1
                elif src[pos]=='}':
                    n -= 1
                    if n==0:
                        return pos
            pos += 1

    def get_params(self, src, name, pos):
        ret = []
        n_params = self._name2brackets[name]
        for i in range(0, n_params):
            e = self.get_end(src, pos)
            b1 = src.find("{", pos)
            par = src[b1+1:e]
            par = " ".join(par.split())
            ret.append(par.strip())
            pos = e+1
        return pos, ret


    def get_end2(self, src, pos):
        n = 0
        quoting = False
        while pos<len(src):
            if src[pos]=='"':
                if quoting:
                    return pos+1
                quoting = not quoting
            if not quoting:
                if src[pos]=='{':
                    n += 1
                elif src[pos]=='}':
                    n -= 1
                    if n==0:
                        return pos
                elif src[pos] == ' ':
                    return pos+1
            pos += 1
        return len(src)

    def get_params2(self, src):
        ret = []
        pos = 0
        while pos<len(src):
            e = self.get_end2(src, pos)
            par = src[pos:e]
            if par[0]=='"':
                assert par[-1]=='"'
                par = par[1:-1]
            if len(par.strip())!=0:
                ret.append(par.strip())
                pos = e
            else:
                pos = pos + 1
        return pos, ret

    def execute_function(self, name):
        if name=="format.name$":
            bla = 0
        if name in self._internal_functions:
            v = self._internal_functions[name]()
            if v is not None:
                self._stack.append(v)
            return
        f = self._functions[name]
        pos, params = self.get_params2(f)
        for v in params:
            #print (f"> {self._stack}")
            if v in self._functions or v in self._internal_functions:
                v = self.execute_function(v)
                if v is not None:
                    self._stack.append(v)
            elif v.startswith("#"):
                self._stack.append(int(v[1:]))
            elif v.startswith("'"):
                if v[1:] in self._strvars:
                    self._stack.append(strvars[v[1:]])
                else:
                    self._stack.append(intvars[v[1:]])
            else:
                self._stack.append(v)


    def sort_entries(self):
        pass

    def execute_entry_function(self, name, entry):
        pass


    def read_bibtex(self, filename):
        texF = texfile.TeXfile()
        content = texF.read2string(filename)
        handler = memoryhandler.StoringTeXhandler()
        texF.parse(content, handler)
        self._entries = handler


    def process_file(self, filename):
        fd = open(filename)
        lines = fd.readlines()
        fd.close()
        nlines = []
        for l in lines:
            if l.startswith("%"):
                continue
            if l.find("%")>0:
                l = l[:l.find("%")]
            nlines.append(l)
        bst = "".join(nlines)
        #
        b = 0
        e = 0
        while b<len(bst):
            while b<len(bst) and (bst[b]==' ' or bst[b]=='\n'):
                b += 1
                continue
            if b>=len(bst):
                break
            # get name
            name = self.get_name(bst, b)
            b = b + len(name)
            name = name.strip().lower()
            # get params
            e, params = self.get_params(bst, name, b)
            b = e
            #
            if name=="entry":
                self._fields = params[0].split(" ")
                names = params[1].split(" ")
                for n in names:
                    self._intvars[n] = 0
                names = params[2].split(" ")
                for n in names:
                    self._strvars[n] = ""
            elif name=="function":
                self._functions[params[0]] = params[1]
            elif name=="execute":
                self.execute_function(params[0])
            elif name=="integers":
                names = params[0].split(" ")
                for n in names:
                    self._intvars[n] = 0
            elif name=="strings":
                names = params[0].split(" ")
                for n in names:
                    self._strvars[n] = ""
            elif name=="macro":
                self._macros[params[0]] = params[1]
            elif name=="read":
                self.read_bibtex(filename)
            elif name=="sort":
                sort_entries()
            elif name=="iterate":
                for e in self._entries._entryIDs:
                    self.execute_entry_function(params[0], e)
            elif name=="reverse":
                rentries = self._entries._entryIDs
                rentries.reverse()
                for e in rentries:
                    self.execute_entry_function(params[0], e)
