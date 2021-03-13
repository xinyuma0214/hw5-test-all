import unittest
import hw5_cards_ec2

class TestHand(unittest.TestCase):

    def testRemovePairs(self):
        eq1 = hw5_cards_ec2.Hand([1,1,1,2,2,3,4,5])
        self.assertEqual(eq1.remove_pairs(),[1,3,4,5])

    def testDeal(self):
        eq2 = hw5_cards_ec2.Deck()
        # self.assertEqual(len(eq2.deal(2,3)), 2)
        self.assertEqual(len(eq2.deal(3,-1)[1]),17)
if __name__=="__main__":
    unittest.main()