"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import unittest
import random

from collections import Counter

import thinkstats2

class Test(unittest.TestCase):

    def testOdds(self):
        p = 0.75
        o = thinkstats2.Odds(p)
        self.assertEquals(o, 3)

        p = thinkstats2.Probability(o)
        self.assertEquals(p, 0.75)
        
        p = thinkstats2.Probability2(3, 1)
        self.assertEquals(p, 0.75)
        
    def testMean(self):
        t = [1, 1, 1, 3, 3, 591]
        mean = thinkstats2.Mean(t)
        self.assertEquals(mean, 100)

    def testVar(self):
        t = [1, 1, 1, 3, 3, 591]
        mean = thinkstats2.Mean(t)
        var1 = thinkstats2.Var(t)
        var2 = thinkstats2.Var(t, mean)
        
        self.assertAlmostEquals(mean, 100.0)
        self.assertAlmostEquals(var1, 48217.0)
        self.assertAlmostEquals(var2, 48217.0)

    def testMeanVar(self):
        t = [1, 1, 1, 3, 3, 591]
        mean, var = thinkstats2.MeanVar(t)
        
        self.assertAlmostEquals(mean, 100.0)
        self.assertAlmostEquals(var, 48217.0)

    def testBinomialCoef(self):
        res = thinkstats2.BinomialCoef(10, 3)
        self.assertEquals(round(res), 120)

        res = thinkstats2.BinomialCoef(100, 4)
        self.assertEquals(round(res), 3921225)

    def testInterpolator(self):
        xs = [1, 2, 3]
        ys = [4, 5, 6]
        interp = thinkstats2.Interpolator(xs, ys)

        y = interp.Lookup(1)
        self.assertAlmostEquals(y, 4)

        y = interp.Lookup(2)
        self.assertAlmostEquals(y, 5)

        y = interp.Lookup(3)
        self.assertAlmostEquals(y, 6)

        y = interp.Lookup(1.5)
        self.assertAlmostEquals(y, 4.5)

        y = interp.Lookup(2.75)
        self.assertAlmostEquals(y, 5.75)

        x = interp.Reverse(4)
        self.assertAlmostEquals(x, 1)

        x = interp.Reverse(6)
        self.assertAlmostEquals(x, 3)

        x = interp.Reverse(4.5)
        self.assertAlmostEquals(x, 1.5)

        x = interp.Reverse(5.75)
        self.assertAlmostEquals(x, 2.75)

    def testTrim(self):
        t = range(100)
        random.shuffle(t)
        trimmed = thinkstats2.Trim(t, p=0.05)
        n = len(trimmed)
        self.assertEquals(n, 90)

    def testHist(self):
        hist = thinkstats2.Hist('allen')
        self.assertEquals(len(hist), 4)
        self.assertEquals(hist.Freq('l'), 2)

        hist = thinkstats2.Hist(Counter('allen'))
        self.assertEquals(len(hist), 4)
        self.assertEquals(hist.Freq('l'), 2)

        hist2 = thinkstats2.Hist('nella')
        self.assertEquals(hist, hist2)

    def testPmf(self):
        pmf = thinkstats2.Pmf('allen')
        self.assertEquals(len(pmf), 4)
        self.assertEquals(pmf.Prob('l'), 0.4)

        pmf = thinkstats2.Pmf(Counter('allen'))
        self.assertEquals(len(pmf), 4)
        self.assertEquals(pmf.Prob('l'), 0.4)

        pmf = thinkstats2.Pmf(pmf)
        self.assertEquals(len(pmf), 4)
        self.assertEquals(pmf.Prob('l'), 0.4)

        pmf = thinkstats2.Pmf(pmf.d.items())
        self.assertEquals(len(pmf), 4)
        self.assertEquals(pmf.Prob('l'), 0.4)

        pmf2 = pmf.Copy()
        self.assertEquals(pmf, pmf2)
        
    def testCdf(self):
        t = [1, 2, 2, 3, 5]
        pmf = thinkstats2.Pmf(t)

        cdf = thinkstats2.Cdf(pmf)
        self.assertEquals(len(cdf), 4)
        self.assertAlmostEquals(cdf.Prob(2), 0.6)
        self.assertAlmostEquals(cdf.Value(0.6), 2)

        cdf = thinkstats2.Cdf(pmf.Items())
        self.assertEquals(len(cdf), 4)
        self.assertAlmostEquals(cdf.Prob(2), 0.6)
        self.assertAlmostEquals(cdf.Value(0.6), 2)

        cdf = thinkstats2.Cdf(t)
        self.assertEquals(len(cdf), 4)
        self.assertAlmostEquals(cdf.Prob(2), 0.6)
        self.assertAlmostEquals(cdf.Value(0.6), 2)

        cdf = thinkstats2.Cdf(Counter(t))
        self.assertEquals(len(cdf), 4)
        self.assertAlmostEquals(cdf.Prob(2), 0.6)
        self.assertAlmostEquals(cdf.Value(0.6), 2)

        cdf2 = cdf.Copy()
        self.assertAlmostEquals(cdf2.Prob(2), 0.6)
        self.assertAlmostEquals(cdf2.Value(0.6), 2)
        

if __name__ == "__main__":
    unittest.main()
