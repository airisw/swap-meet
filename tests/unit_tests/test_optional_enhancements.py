import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_newest_by_category():
    item_a = Clothing(age=1)
    item_b = Electronics(age=3)
    item_c = Electronics(age=2)

    vendor = Vendor(inventory=
                    [item_a, item_b, item_c])
    
    items = vendor.get_newest_by_category("Electronics")

    assert items == item_c

def test_same_age():
    item_a = Decor(age=6)
    item_b = Clothing(age=1)
    item_c = Electronics(age=3)
    item_d = Decor(age=6)

    vendor = Vendor(inventory=
                    [item_a, item_b, item_c, item_d])
    
    items = vendor.get_newest_by_category("Decor")

    assert items == item_a

def test_swap_by_newest_return_false():
    item_a = Clothing(age=1)
    item_b = Electronics(age=3)
    item_c = Electronics(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(age=6)
    item_e = Clothing(age=1)
    item_f = Electronics(age=3)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(other_vendor=jesse, my_priority="Electronics", their_priority="Decor")

    assert result == False
    assert item_a and item_b and item_c in tai.inventory
    assert item_d and item_e and item_f in jesse.inventory

def test_swap_by_newest():
    item_a = Clothing(age=1)
    item_b = Decor(age=3)
    item_c = Decor(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(age=6)
    item_e = Clothing(age=1)
    item_f = Electronics(age=3)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(other_vendor=jesse, my_priority="Electronics", their_priority="Decor")

    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a and item_b and item_f in tai.inventory
    assert item_d and item_e and item_c in jesse.inventory