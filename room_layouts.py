# Main:
# 0 - empty
# 1234 - wall corners (LR UP, LR DOWN)
# 5678 - walls (UP DOWN LEFT RIGHT)
# zxvbn - left opening, cv - right opening, bn - up or down opening
# qwer - stones (q hookable)
# tyui - water corners, @ - water middle, ghjk - water sides,

# [] - Large tree (top/bottom)
# # - small tree
# opkl - super large stone

# T - Flying enemy, Y - Walking enemy
# a - checkpoint, s - coin, d - key, f - door, D - standalone door

# Decor:
# QWE - flowers
# R - Little stone
# GH - Mushrooms
# HJKL - Grass
#

FRAME = "1555555552\n" \
        "7000000008\n" \
        "7000000008\n" \
        "7000000008\n" \
        "7000000008\n" \
        "7000000008\n" \
        "3666666664"

ROOM_LAYOUT_TEST = "15555f5552\n" \
                   "7dT0000qs8\n" \
                   "7T00000w08\n" \
                   "z00000Y0Tc\n" \
                   "0s00000000\n" \
                   "xa0e0000rv\n" \
                   "366b0n6664"

ROOM_DECOR_TEST = "0000000000\n" \
                  "000000R000\n" \
                  "000Q0W0000\n" \
                  "000000E000\n" \
                  "00FG000LW0\n" \
                  "0000HJK000\n" \
                  "0000000000"


# Intro - hook over water
LEVEL_INTRO_A = "155bfn5552\n" \
          "7[0a000Kd8\n" \
          "7]00KJ00#8\n" \
          "7tggggggy8\n" \
          "7uhhhhhhi8\n" \
          "700Q0000R8\n" \
          "3666666664"

# Intro - Hook over water, take turns
LEVEL_INTRO_B = "1555555552\n" \
                "70[0000000\n" \
                "70]rrrrrrv\n" \
                "700tgy0008\n" \
                "7uhhhhhhh8\n" \
                "700e000008\n" \
                "366b0n6664"
# Intro - "secret" coin, info about rolling
LEVEL_INTRO_C = "1555555552\n" \
                "000000000e\n" \
                "1555b0n552\n" \
                "7000000[s8\n" \
                "70[0rrr]08\n" \
                "70]000a0q8\n" \
                "30n6666664"
# Intro - Hook between rooms
LEVEL_INTRO_D = "10n5555552\n" \
                "7000q00008\n" \
                "7q000q0qq8\n" \
                "70qq0q0q0c\n" \
                "7q000000tg\n" \
                "70q00000uh\n" \
                "3666666664"
# Intro - First enemy
LEVEL_INTRO_E = "1555555552\n" \
                "7[000000Yc\n" \
                "7]0wq00q0D\n" \
                "x0000000ev\n" \
                "ggggggy0d8\n" \
                "hhhhhhi0a8\n" \
                "3666666664"
# Intro - Roll when hooking
LEVEL_INTRO_F = "1555555552\n" \
                "zqty000w@8\n" \
                "00jk0000@8\n" \
                "xqjk000@@8\n" \
                "7[uiqsq@#c\n" \
                "7]00000000\n" \
                "3666666664"

LEVEL_INTRO_G = "1552001552\n" \
                "7008007008\n" \
                "7008007d08\n" \
                "70n4003b08\n" \
                "z000000008\n" \
                "000#000008\n" \
                "3666666664"


# Intro - Pull Enemies to kill them
LEVEL_INTRO_H = "1b000000n2\n" \
                "70[00[#qT8\n" \
                "70]00]0008\n" \
                "7000000b08\n" \
                "7Dr1555408\n" \
                "70sea00008\n" \
                "366400n664"

# Intro - some space before first main challenge
LEVEL_INTRO_I = "155b00n552\n" \
                "7w000000[8\n" \
                "7000[0#0]8\n" \
                "70[0]00008\n" \
                "70]0000[08\n" \
                "7#00000]08\n" \
                "3b000000n4"

# Level One - small labyrinth(5 rooms?) with simple enemies spread out
# TODO

# Level Two - 9 rooms, main challange, 2 secrets in there
# TODO

ALL_LEVELS = [
    (
        "ENTRANCE",
        (0, 0),  # Location in the world
        [LEVEL_INTRO_A]  # All layouts for that level
    ),
    (
        "B",
        (0, -1),  # Location in the world
        [LEVEL_INTRO_B]  # All layouts for that level
    ),
    (
        "C",
        (1, -1),  # Location in the world
        [LEVEL_INTRO_C]  # All layouts for that level
    ),
    (
        "D",
        (1, 0),  # Location in the world
        [LEVEL_INTRO_D]  # All layouts for that level
    ),
    (
        "E",
        (2, 0),  # Location in the world
        [LEVEL_INTRO_E]  # All layouts for that level
    ),
    (
        "F",
        (3, 0),  # Location in the world
        [LEVEL_INTRO_F]  # All layouts for that level
    ),
    (
        "G",
        (4, 0),  # Location in the world
        [LEVEL_INTRO_G]  # All layouts for that level
    ),
    (
        "H",
        (4, -1),  # Location in the world
        [LEVEL_INTRO_H]  # All layouts for that level
    ),
    (
        "I",
        (4, -2),  # Location in the world
        [LEVEL_INTRO_I]  # All layouts for that level
    ),
]
