# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdateStrategy(ABC):
    @abstractmethod
    def update_quality(self, item):
        pass


class NormalItemUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
        if item.quality > 50:
            item.quality = 50


class BackstagePassUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

class SulfurasUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        pass


class ItemUpdateStrategyFactory:
    @staticmethod
    def get_strategy(item):
        if item.name == "Aged Brie":
            return AgedBrieUpdateStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdateStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdateStrategy()
        else:
            return NormalItemUpdateStrategy()


class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = ItemUpdateStrategyFactory.get_strategy(item)
            strategy.update_quality(item)