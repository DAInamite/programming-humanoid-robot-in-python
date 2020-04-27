#!/usr/bin/env python
##
##  sexpr.py - by Yusuke Shinyama
##
##  * public domain *
##
import future

##  AbstractFilter
##
class AbstractFilter:
    def __init__(self, next_filter):
        self.next_filter = next_filter
        return

    def process(self, s):
        raise NotImplementedError

    def feed(self, s):
        self.feed_next(self.process(s))
        return

    def feed_next(self, s):
        self.next_filter.feed(s)
        return

    def close(self):
        self.next_filter.close()
        return


##  AbstractConsumer
##
class AbstractConsumer:
    def feed(self, s):
        raise NotImplementedError

    def close(self):
        return


##  SExprReader
##
class SExprReader(AbstractFilter):
    """Usage:
    reader = SExprReader(consumer)
    reader.feed("(this is (sexpr))")
    reader.close()
    """

    COMMENT_BEGIN = ";"
    COMMENT_END = "\n"
    SEPARATOR = " \t\n"
    PAREN_BEGIN = "("
    PAREN_END = ")"
    QUOTE = '"'
    ESCAPE = "\\"

    def __init__(self, next_filter,
                 comment_begin=COMMENT_BEGIN,
                 comment_end=COMMENT_END,
                 separator=SEPARATOR,
                 paren_begin=PAREN_BEGIN,
                 paren_end=PAREN_END,
                 quote=QUOTE,
                 escape=ESCAPE):
        AbstractFilter.__init__(self, next_filter)
        self.comment_begin = comment_begin
        self.comment_end = comment_end
        self.separator = separator
        self.paren_begin = paren_begin
        self.paren_end = paren_end
        self.quote = quote
        self.escape = escape
        self.special = comment_begin + separator + paren_begin + paren_end + quote + escape
        self.reset()

    # SExprReader ignores any error and
    # try to continue as long as possible.
    # if you want to throw exception however,
    # please modify these methods.

    # called if redundant parantheses are found.
    def illegal_close_paren(self, i):
        print("Ignore a close parenthesis: %d" % i)

    # called if it reaches the end-of-file while the stack is not empty.
    def premature_eof(self, i, x):
        print("Premature end of file: %d parens left, partial=%s" % (i, x))

    # reset the internal states.
    def reset(self):
        self.incomment = False              # if within a comment.
        self.inquote = False                # if within a quote.
        self.inescape = False               # if within a escape.
        self.sym = ''                       # partially constructed symbol.
        # NOTICE: None != nil (an empty list)
        self.build = None                   # partially constructed list.
        self.build_stack = []     # to store a chain of partial lists.
        return self

    # analyze strings
    def feed(self, tokens):
        for (i, c) in enumerate(tokens):
            if self.incomment:
                # within a comment - skip
                self.incomment = (c not in self.comment_end)
            elif self.inescape or (c not in self.special):
                # add to the current working symbol
                self.sym += c
                self.inescape = False
            elif c in self.escape:
                # escape
                self.inescape = True
            elif self.inquote and (c not in self.quote):
                self.sym += c
            else:
                # special character (blanks, parentheses, or comment)
                if self.sym:
                    # close the current symbol
                    if self.build is None:
                        self.feed_next(self.sym)
                    else:
                        self.build.append(self.sym)
                    self.sym = ''
                if c in self.comment_begin:
                    # comment
                    self.incomment = True
                elif c in self.quote:
                    # quote
                    self.inquote = not self.inquote
                elif c in self.paren_begin:
                    # beginning a new list.
                    self.build_stack.append(self.build)
                    empty = []
                    if self.build is None:
                        # begin from a scratch.
                        self.build = empty
                    else:
                        # begin from the end of the current list.
                        self.build.append(empty)
                        self.build = empty
                elif c in self.paren_end:
                    # terminating the current list
                    if self.build is None:
                        # there must be a working list.
                        self.illegal_close_paren(i)
                    else:
                        if len(self.build_stack) == 1:
                            # current working list is the last one in the stack.
                            self.feed_next(self.build)
                        self.build = self.build_stack.pop()
        return self

    # terminate
    def terminate(self):
        # a working list should not exist.
        if self.build is not None:
            # error - still try to construct a partial structure.
            if self.sym:
                self.build.append(self.sym)
                self.sym = ''
            if len(self.build_stack) == 1:
                x = self.build
            else:
                x = self.build_stack[1]
            self.build = None
            self.build_stack = []
            self.premature_eof(len(self.build_stack), x)
        elif self.sym:
            # flush the current working symbol.
            self.feed_next(self.sym)
        self.sym = ''
        return self

    # closing.
    def close(self):
        AbstractFilter.close(self)
        self.terminate()


##  StrictSExprReader
##
class SExprIllegalClosingParenError(ValueError):
    """It throws an exception with an ill-structured input."""
    pass


class SExprPrematureEOFError(ValueError):
    pass


class StrictSExprReader(SExprReader):
    def illegal_close_paren(self, i):
        raise SExprIllegalClosingParenError(i)

    def premature_eof(self, i, x):
        raise SExprPrematureEOFError(i, x)


##  str2sexpr
##
class _SExprStrConverter(AbstractConsumer):
    results = []

    def feed(self, s):
        _SExprStrConverter.results.append(s)


_str_converter = SExprReader(_SExprStrConverter())
_str_converter_strict = StrictSExprReader(_SExprStrConverter())


def str2sexpr(s):
    """parse a string as a sexpr."""
    _SExprStrConverter.results = []
    _str_converter.reset().feed(s).terminate()
    return _SExprStrConverter.results


def str2sexpr_strict(s):
    """parse a string as a sexpr."""
    _SExprStrConverter.results = []
    _str_converter_strict.reset().feed(s).terminate()
    return _SExprStrConverter.results


##  sexpr2str
##
def sexpr2str(e):
    """convert a sexpr into Lisp-like representation."""
    if not isinstance(e, list):
        return e
    return "(" + " ".join(map(sexpr2str, e)) + ")"
