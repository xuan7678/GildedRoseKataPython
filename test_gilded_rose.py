# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_should_less_than_50(self):
        # Aged Brie with sell_in = -1 and quality = 47
        items = [Item(name="Aged Brie", sell_in=-1, quality=49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # The quality should less than 50
        self.assertLess(items[0].quality, 50, "item quantity should be less than 50")

    def test_Sulfuras_should_never_be_sold(self):
        """Aged Brie should increase in quality over time"""
        items = [Item(name="Sulfuras", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 10, "Sulfuras should never be sold")

    def test_backstage_passes_3x_within_5_days(self):
        """Backstage passes should be 0"""
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 30, "Backstage passes should by 3 if within 5 days")

    def test_sytax_error(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.non_existing_function()

if __name__ == '__main__':
    unittest.main()
