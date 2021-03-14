import unittest
import hw5_cards_ec1

class TestHand(unittest.TestCase):

    def test_ec1_q1(self):
        eq1 = hw5_cards_ec1.Hand([1,2,3,4,5])
        self.assertIsInstance(eq1,hw5_cards_ec1.Hand)
        self.assertEqual(eq1.init_card, [1,2,3,4,5])


    def testAddAndRemove(self):
        eq2 = hw5_cards_ec1.Hand([1,2,3,4,5])
        eq2.add_card(6)
        self.assertEqual(eq2.init_card, [1,2,3,4,5,6])
        eq2.remove_card(3)
        self.assertEqual(eq2.init_card, [1,2,4,5,6])

    def testDraw(self):
        deck = hw5_cards_ec1.Deck()
        self.assertEqual(len(deck.cards),52)
        eq3 = hw5_cards_ec1.Hand([1,2,3,4,5])
        num1 = len(eq3.init_card)
        eq3.draw(deck)
        num2 = len(eq3.init_card)
        self.assertEqual(num1,5)
        self.assertEqual(num2,6)
        self.assertEqual(len(deck.cards),51)

if __name__=="__main__":
    unittest.main()