# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_update_sellin(self):
        items = [Item("foo", 1, 0)]
        gilded_rose = GildedRose(items)
        expected_sellin = 0
        gilded_rose.update_quality()
        self.assertEquals(expected_sellin, items[0].sell_in)

    def test_update_quality(self):
        items = [Item("foo", 0, 1)]
        gilded_rose = GildedRose(items)
        expected_quality = 0
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_after_sellin(self):
        items = [Item("foo", -1, 2)]
        gilded_rose = GildedRose(items)
        expected_quality = 0
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_quality_not_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        expected_quality = 0
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_increase_brie_quality(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        expected_quality = 1
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_quality_under_50(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        expected_quality = 50
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_increase_brie_quality_after_date(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)
        expected_quality = 2
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)
    
    def test_sulfuras_sellin(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 0)]
        gilded_rose = GildedRose(items)
        expected_sell_in = 1
        gilded_rose.update_quality()
        self.assertEquals(expected_sell_in, items[0].sell_in)

    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 1)]
        gilded_rose = GildedRose(items)
        expected_quality = 1
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_backstage_passes_quality_under_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 0)]
        gilded_rose = GildedRose(items)
        expected_quality = 2
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_backstage_passes_quality_under_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 0)]
        gilded_rose = GildedRose(items)
        expected_quality = 3
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_backstage_passes_quality_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 3)]
        gilded_rose = GildedRose(items)
        expected_quality = 0
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

if __name__ == '__main__':
    unittest.main()
