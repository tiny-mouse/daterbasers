from __future__ import absolute_import

import random

from playtime.models import db_session
from playtime.models.color_family import ColorFamily
from playtime.models.hex_color import HexColor
from playtime.models.item_type import ItemType

# This isn't the most efficent way of doing this, but unless you're a wizard
# these hex colors don't make a ton of sense. Intentionally suboptimal.
ALL_COLORS = {
    "red": [ "FF0000", "8E2323", "EE2C2C", "8C1717", "EE0000", "E3170D", "FC1501" ],
    "orange": [ "E04006", "EE4000", "FF7F24", "FF6103", "EE8833", "FF4500", "FF6600" ],
    "yellow": [ "0000FF", "EEAD0E", "CDAB2D", "FFCC11", "FFC125", "FCDC3B", "FFD700" ],
    "green": [ "00FF00", "7FFF00", "3F6826", "55AE3A", "228B22", "0AC92B", "43CD80" ],
    "blues": [ "0000FF", "388E8E", "37FDFC", "0D4F8B", "5D7B93", "0276FD", "000080" ],
    "purple": [ "7F00FF", "2E0854", "A020F0", "68228B", "9932CC", "AA00FF", "CC99CC" ],
    "pink": [ "FF33CC", "FF1CAE", "CD1076", "FF00AA", "FF6EB4", "FF0066", "CD6889" ],
}

ALL_TYPES = [ "books", "shirts", "pants", "shoes", "bags", "dishes", "electronics" ]

def get_rando_name():
    names = ["my", "joe", "jane", "jesse", "bob", "mom", "brophia", "nicola", "marfa"]
    modifiers = ["favorite", "newest", "oldest", "borrowed", "found"]
    return "{0}'s {1}".format(random.choice(names), random.choice(modifiers))

def make_data():
    pass

