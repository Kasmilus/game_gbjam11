# Main:
# 0 - empty
# 1234 - wall corners (LR UP, LR DOWN)
# 5678 - walls (UP DOWN LEFT RIGHT)
# zxvbn - left opening, cv - right opening, bn - up or down opening
# qwer - stones (q hookable)
# tyui - water corners, @ - water middle, ghjk - water sides,

# [] - Large tree (top/bottom)
# # - small tree
# op+l - super large stone

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
                "70]wn55552\n" \
                "700tgy0008\n" \
                "7uhhhhhhh8\n" \
                "700e000008\n" \
                "366b0n6664"
# Intro - "secret" coin, info about rolling
LEVEL_INTRO_C = "1555555552\n" \
                "000000000e\n" \
                "1555b0n552\n" \
                "7000000[s8\n" \
                "7[00e#r]08\n" \
                "7]0000a0q8\n" \
                "3b0n666664"
# Intro - Hook between rooms
LEVEL_INTRO_D = "1b0n555552\n" \
                "7000r00008\n" \
                "7w000#0#08\n" \
                "70000w000c\n" \
                "7e[00000tg\n" \
                "70]00000uh\n" \
                "3666666666"
# Intro - First enemy
LEVEL_INTRO_E = "1555555552\n" \
                "7[000000Yc\n" \
                "7]0wq00q0D\n" \
                "z0000000ev\n" \
                "ggggggy0d8\n" \
                "hhhhhhi0a8\n" \
                "6666666664"
# Intro - Roll when hooking
LEVEL_INTRO_F = "1555555555\n" \
                "zwty000tgg\n" \
                "00jk00wj@@\n" \
                "xejk000j@@\n" \
                "7[uirs#uhh\n" \
                "7]00000000\n" \
                "3666666664"

LEVEL_INTRO_G = "5552001552\n" \
                "gyq80070w8\n" \
                "@k08007d08\n" \
                "@kn4003b08\n" \
                "hi00000[08\n" \
                "000#000]08\n" \
                "3666666664"
LEVEL_INTRO_G_SECRET = "0000000000\n" \
                       "00s0000000\n" \
                       "0000000000\n" \
                       "0000000000\n" \
                       "0000000000\n" \
                       "0000000000\n" \
                       "0000000000"


# Intro - Pull Enemies to kill them
LEVEL_INTRO_H = "1b000000n2\n" \
                "70[00[e#T8\n" \
                "70]00]0008\n" \
                "7r00000w08\n" \
                "1bfn555408\n" \
                "7s0ea00008\n" \
                "366400n664"

# Intro - some space before first main challenge
LEVEL_INTRO_I = "155b00n552\n" \
                "7w0000q0[8\n" \
                "7000[0#s]8\n" \
                "70[0]00e08\n" \
                "70]0000[08\n" \
                "7#00000]08\n" \
                "3b000000n4"

# Level One - small labyrinth(5 rooms?) with simple enemies spread out
LEVEL_ONE_A = "155b00n552\n" \
              "7a00000ws8\n" \
              "7000000rq8\n" \
              "z000000q08\n" \
              "@@@@0@@@@8\n" \
              "x000000008\n" \
              "366b00n664"
LEVEL_ONE_B = "1555555552\n" \
              "z0000000d8\n" \
              "D00w0Y00T8\n" \
              "x000000008\n" \
              "700e00#008\n" \
              "7000000008\n" \
              "366b00n664"
LEVEL_ONE_C = "1555555552\n" \
              "70000e00ac\n" \
              "7[00000000\n" \
              "7]0n555552\n" \
              "700w#00008\n" \
              "7000000r08\n" \
              "3666b0nb08"
LEVEL_ONE_D = "1555b0nb08\n" \
              "7dq000@@08\n" \
              "15555b0008\n" \
              "z00000000c\n" \
              "D000T000@@\n" \
              "x00000000v\n" \
              "3666666664"

# Level Two - Open sided meadows

LEVEL_TWO_A = "000000#008\n" \
              "00T0000008\n" \
              "00tgggy008\n" \
              "0[uhhhi00c\n" \
              "0]00000000\n" \
              "00000000av\n" \
              "6666666664"
LEVEL_TWO_B = "70000000e0\n" \
              "70#0000[00\n" \
              "7000000]00\n" \
              "7000000000\n" \
              "15555b0000\n" \
              "7d0Y000000\n" \
              "6666666666"
LEVEL_TWO_C = "15bfn55555\n" \
              "700T000000\n" \
              "7000000[00\n" \
              "7000000]00\n" \
              "700000000q\n" \
              "70#0000000\n" \
              "70000000#0"
LEVEL_TWO_D = "5555555552\n" \
              "000000q[s8\n" \
              "000Y000]08\n" \
              "000000#0q8\n" \
              "0000000008\n" \
              "0000w00008\n" \
              "0000000008"


# Level Three - 9 rooms, main challange, 2 secrets in there
LEVEL_THREE_A = "1555b0n552\n" \
                "7000000008\n" \
                "zr000a0[08\n" \
                "000[000]08\n" \
                "x00]000ty8\n" \
                "7#00000ui8\n" \
                "36b0n66664"
LEVEL_THREE_B = "1555b0n552\n" \
                "z0000000T8\n" \
                "@@00152008\n" \
                "@@007Y8008\n" \
                "@@00z0c0[8\n" \
                "x0000000]8\n" \
                "3666b0n664"
LEVEL_THREE_C = "1555555552\n" \
                "00e00000#8\n" \
                "0w0000Y0d8\n" \
                "00000[00w8\n" \
                "x0000]00#8\n" \
                "7000000r08\n" \
                "3666b0n664"
LEVEL_THREE_D = "1555555525\n" \
                "z000000s80\n" \
                "000v016640\n" \
                "000807w000\n" \
                "00w8qz000v\n" \
                "x00800[008\n" \
                "3664@@]n64"
LEVEL_THREE_E = "1555555552\n" \
                "7000r00[0c\n" \
                "70w0000]00\n" \
                "7#00000000\n" \
                "700T0[0e00\n" \
                "700a0]000v\n" \
                "366bfn6664"
LEVEL_THREE_F = "1552015552\n" \
                "7008070008\n" \
                "7008036668\n" \
                "7008T@@@@@\n" \
                "7008015552\n" \
                "7008070008\n" \
                "3664f36664"
LEVEL_THREE_G = "155b0n5552\n" \
                "7#00000e[8\n" \
                "7w[00#00]8\n" \
                "7[]000[0[8\n" \
                "7]r0#0]q]8\n" \
                "7000000008\n" \
                "3666666664"
LEVEL_THREE_H = "155b@@n552\n" \
                "7sw0000[#8\n" \
                "70v0000]0c\n" \
                "70c0[00000\n" \
                "7[op]00w0v\n" \
                "7]+ld00008\n" \
                "3666666664"
LEVEL_THREE_I = "155b@@n552\n" \
                "7@@@@@@@@8\n" \
                "z@@@@@@@@c\n" \
                "@@@0000@@@\n" \
                "x@@a00s@@v\n" \
                "7@@@@@@@@8\n" \
                "366b@@n664"

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
        [LEVEL_INTRO_G, LEVEL_INTRO_G_SECRET]  # All layouts for that level
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

    # Level 1
    (
        "LVL1",
        (4, -3),  # Location in the world
        [LEVEL_ONE_A]  # All layouts for that level
    ),
    (
        "LVL1_B",
        (4, -4),  # Location in the world
        [LEVEL_ONE_B]  # All layouts for that level
    ),
    (
        "LVL1_C",
        (3, -4),  # Location in the world
        [LEVEL_ONE_C]  # All layouts for that level
    ),
    (
        "LVL1_D",
        (3, -3),  # Location in the world
        [LEVEL_ONE_D]  # All layouts for that level
    ),

    # Level 2
    (
        "THE MEADOWS",
        (2, -3),  # Location in the world
        [LEVEL_TWO_A]  # All layouts for that level
    ),
    (
        "THE MEADOWS B",
        (1, -3),  # Location in the world
        [LEVEL_TWO_B]  # All layouts for that level
    ),
    (
        "THE MEADOWS C",
        (1, -4),  # Location in the world
        [LEVEL_TWO_C]  # All layouts for that level
    ),
    (
        "THE MEADOWS D",
        (2, -4),  # Location in the world
        [LEVEL_TWO_D]  # All layouts for that level
    ),

    # Level 3
    (
        "POND - ENTRANCE",
        (1, -5),  # Location in the world
        [LEVEL_THREE_A]  # All layouts for that level
    ),
    (
        "POND",
        (1, -6),  # Location in the world
        [LEVEL_THREE_B]  # All layouts for that level
    ),
    (
        "POND",
        (1, -7),  # Location in the world
        [LEVEL_THREE_C]  # All layouts for that level
    ),
    (
        "UPPER POND",
        (0, -7),  # Location in the world
        [LEVEL_THREE_D]  # All layouts for that level
    ),
    (
        "POND",
        (-1, -7),  # Location in the world
        [LEVEL_THREE_E]  # All layouts for that level
    ),
    (
        "POND",
        (-1, -6),  # Location in the world
        [LEVEL_THREE_F]  # All layouts for that level
    ),
    (
        "POND",
        (-1, -5),  # Location in the world
        [LEVEL_THREE_G]  # All layouts for that level
    ),
    (
        "POND",
        (0, -5),  # Location in the world
        [LEVEL_THREE_H]  # All layouts for that level
    ),
    (
        "POND ISLAND",
        (0, -6),  # Location in the world
        [LEVEL_THREE_I]  # All layouts for that level
    ),
]
