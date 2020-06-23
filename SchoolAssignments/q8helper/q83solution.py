from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle,random.randint

#random.shuffle(alist) mutates its alist argument to be a random permutation
#random.randint(1,10)  returns a random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
    def test_len(self):
        initialv = 7
        while initialv >= 0:
            self.assertEqual(self.bag.__len__(), initialv, 'unexpected len')
            random.shuffle(self.alist)
            if initialv > 0:
                toremove = self.alist[0]
                self.bag.remove(toremove)
                self.alist.remove(toremove)
            initialv -= 1
    def test_unique(self):
        initialv = 4
        while initialv >= 0:
            uniquevals = list(self.bag.counts)
            random.shuffle(uniquevals)
            self.assertEqual(self.bag.unique(), initialv, 'unexpected unique val')
            self.assertEqual(self.bag.unique(), len(self.bag.counts), 'unexpected unique val')
            if initialv > 0:
                toremove = uniquevals[0]
                del self.bag.counts[toremove]
            initialv -= 1
    def test_contains(self):
        for value in ['a','b', 'c', 'd']:
            self.assertTrue(self.bag.__contains__(value), 'unexpected contains')
        self.assertFalse(self.bag.__contains__('x'), 'bag contains x')
    def test_count(self):
        masterdict = {'a':1,'b':2,'c':1,'d':3,'x':0}
        totcount = 7
        for value in masterdict:
                self.assertEqual(self.bag.count(value), masterdict[value],'unexpected count')
        masterdict = {'a':1,'b':2,'c':1,'d':3,}
        while totcount >= 0:
            totalvalue = 0
            for value in self.bag.counts:
                totalvalue += self.bag.counts[value]
            self.assertEqual(totalvalue, totcount)
            listkeys = list(masterdict)
            random.shuffle(listkeys)
            if totcount > 0:
                toremove = listkeys[0]
                self.bag.remove(toremove)
                masterdict[toremove] -= 1
                if masterdict[toremove] == 0:
                    del masterdict[toremove]
            totcount -= 1
    def test_equals(self):
        listone = []
        listtwo = []
        for x in range(1000):
            c = random.randint(1,10)
            listone.append(c)
            listtwo.append(c)
        random.shuffle(listone)
        b1 = Bag(listone)
        b2 = Bag(listtwo)
        self.assertTrue(b1 == b2)
    def test_add(self):
        listone = []
        listtwo = []
        for x in range(1000):
            c = random.randint(1,10)
            listone.append(c)
            listtwo.append(c)
        random.shuffle(listone)
        b1 = Bag(listone)
        b2 = Bag()
        for item in listtwo:
            b2.add(item)
        self.assertTrue(b1==b2)
    def test_remove(self):
        listone = []
        listtwo = []
        for x in range(1000):
            c = random.randint(1,10)
            listone.append(c)
            listtwo.append(c)
        random.shuffle(listtwo)
        b1 = Bag(listone)
        b2 = Bag(listone)
        self.assertRaises(ValueError, b1.remove, 53)
        for item in listtwo:
            b2.add(item)
        for item in listtwo:
            b2.remove(item)
        self.assertTrue(b1 == b2)
