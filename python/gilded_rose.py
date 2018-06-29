# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.decrease_sellin(item)

            if item.name == "Aged Brie":
                self.increase_quality(item)
                if item.sell_in < 0:
                    self.increase_quality(item)

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.increase_quality(item)
                if item.sell_in < 10:
                    self.increase_quality(item)
                if item.sell_in < 5:
                    self.increase_quality(item)
                if item.sell_in < 0:
                    item.quality = 0

            else:
                self.decrease_quality(item)
                if item.sell_in < 0:
                    self.decrease_quality(item)

    def decrease_quality(self, item):
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrease_sellin(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
