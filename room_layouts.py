# Main:
# 0 - empty
# 1234 - wall corners (LR UP, LR DOWN)
# 5678 - walls (UP DOWN LEFT RIGHT)
# zxvbn - left opening, cv - right opening, bn - up or down opening
# qwer - stones (q hookable)
# tyui - water corners, @ - water middle, ghjk - water sides,
# <?> - river hor
# ,/. - river vert
# {}:; - LU RU LD RD corner connectors

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


# Intro - hook over water
LEVEL_INTRO_A = "155bfn5552\n" \
                "7[Ja000Kd8\n" \
                "7]G0KJ00#8\n" \
                "7tggggggy8\n" \
                "7uhhhhhhi8\n" \
                "7L0Q00K0R8\n" \
                "3666666664"

# Intro - Hook over water, take turns
LEVEL_INTRO_B = "1555555555\n" \
                "70[H0000R0\n" \
                "7R]wn55552\n" \
                "700tgy0E08\n" \
                "7<?{h}??>8\n" \
                "7L0e00KK08\n" \
                "366b0n6664"
# Intro - "secret" coin, info about rolling
LEVEL_INTRO_C = "5555555552\n" \
                "0KQ000000e\n" \
                "1555b0n552\n" \
                "7H00W00[s8\n" \
                "7[00e#r]L8\n" \
                "7]00KLa0q8\n" \
                "3bJn666664"
# Intro - Hook between rooms
LEVEL_INTRO_D = "1b0n555552\n" \
                "700Kr00008\n" \
                "7wE00#0#L8\n" \
                "70000w000c\n" \
                "7e[00K00tg\n" \
                "70]W00L0uh\n" \
                "3666666666"
# Intro - First enemy
LEVEL_INTRO_E = "1555555552\n" \
                "7[0Y00E0Kc\n" \
                "7]0w#00r0D\n" \
                "z0Q00H00n2\n" \
                "ggggggyLd8\n" \
                "hhhhhhi0a8\n" \
                "6666666664"
# Intro - Roll when hooking
LEVEL_INTRO_F = "1555555555\n" \
                "zwtyr00tgg\n" \
                "00jk0WLj@@\n" \
                "xejk0Q0j@@\n" \
                "7[uirs#uhh\n" \
                "7]H00000L0\n" \
                "3666666664"

LEVEL_INTRO_G = "5552001552\n" \
                "gyq80L70w8\n" \
                "@kG8K07dG8\n" \
                "@kn40J3bK8\n" \
                "hi00Q00[08\n" \
                "000#0L0]E8\n" \
                "3666666664"
LEVEL_INTRO_G_SECRET = "0000000000\n" \
                       "00s0000000\n" \
                       "0000000000\n" \
                       "0000000000\n" \
                       "0000000000\n" \
                       "0000000000\n" \
                       "0000000000"


# Intro - Pull Enemies to kill them
LEVEL_INTRO_H = "1b[0J0K#n2\n" \
                "7Q]r0[00K8\n" \
                "7e0Jw]r008\n" \
                "70000L00T8\n" \
                "70n555bfn2\n" \
                "700000aLs8\n" \
                "366400n664"

# Intro - some space before first main challenge
LEVEL_INTRO_I = "155b0Qn552\n" \
                "7w0K00qs[8\n" \
                "70K0[0#0]8\n" \
                "7H[0]0Ke08\n" \
                "70]0L0r[L8\n" \
                "7#0Q000]08\n" \
                "3bL00000n4"

# Level One - small labyrinth with simple enemies spread out
LEVEL_ONE_A = "1554003552\n" \
              "70w00W0ws8\n" \
              "700K000rq8\n" \
              "z0WaL00q0c\n" \
              "???>0<????\n" \
              "xK00000H0v\n" \
              "366b00n664"
LEVEL_ONE_B = "1555555552\n" \
              "zK00Y0H0d8\n" \
              "D000w00#08\n" \
              "x00J000E08\n" \
              "700e00q0K8\n" \
              "7KTK000R08\n" \
              "3662001664"
LEVEL_ONE_C = "1555555552\n" \
              "7K0L0e0E0c\n" \
              "7[00W0H00K\n" \
              "7]0n555552\n" \
              "70K0#0J008\n" \
              "7a00L00v08\n" \
              "3666b0n4K8"
LEVEL_ONE_D = "1555b0nb08\n" \
              "7d0q0K<>08\n" \
              "15555b0008\n" \
              "zK00HK000c\n" \
              "D0000000<?\n" \
              "x0E0T0H00v\n" \
              "3666666664"

# Level Two - Open sided meadows

LEVEL_TWO_A = "K000E0#008\n" \
              "00T00000R8\n" \
              "00tgggy008\n" \
              "0[uhhhi00c\n" \
              "0]00L00000\n" \
              "00J000H0av\n" \
              "6666666664"
LEVEL_TWO_B = "7QK00000e0\n" \
              "7K#J0H0[00\n" \
              "7LJKL00]K0\n" \
              "70G000G000\n" \
              "15555b00R0\n" \
              "7d0Y00E000\n" \
              "6666666666"
LEVEL_TWO_C = "15bfn55555\n" \
              "7H0T00E0G0\n" \
              "7000K00[00\n" \
              "700KL00]K0\n" \
              "700J000000\n" \
              "70#000J000\n" \
              "70000000#0"
LEVEL_TWO_D = "5555555552\n" \
              "000000q[s8\n" \
              "H00Y0E0]08\n" \
              "0000J0#0q8\n" \
              "0W00000008\n" \
              "L000w00L08\n" \
              "00000K0008"


# Level Three - 9 rooms, main challange, 2 secrets in there
LEVEL_THREE_A = "1555b0n552\n" \
                "700L00H008\n" \
                "zr00000[08\n" \
                "000[W00]J8\n" \
                "xK0]00aty8\n" \
                "7#0000Kui8\n" \
                "36b0n66664"
LEVEL_THREE_B = "1555b0n552\n" \
                "70J00000T8\n" \
                "zw00152008\n" \
                "?>007Y8008\n" \
                "x#00z0c0[8\n" \
                "7L000W00]8\n" \
                "3666b0n664"
LEVEL_THREE_C = "1555555552\n" \
                "Q00e0L0#08\n" \
                "0w000000d8\n" \
                "00KH0[YRw8\n" \
                "x0000]00#8\n" \
                "700r00JH08\n" \
                "3666b0n664"
LEVEL_THREE_D = "1555555525\n" \
                "z0HJ00Ks80\n" \
                "0000016640\n" \
                "Q00v07w0L0\n" \
                "00w8qz000v\n" \
                "xK0800[0E8\n" \
                "3664ty]n64"
LEVEL_THREE_E = "1555555552\n" \
                "7KW0r00[Kc\n" \
                "70w0000]a0\n" \
                "7#00L0W00L\n" \
                "70TJ0[0eJ0\n" \
                "70000]00Hv\n" \
                "366bfn6664"
LEVEL_THREE_F = "1552015552\n" \
                "7E080700L8\n" \
                "7J08036664\n" \
                "70G8T<????\n" \
                "7L08015552\n" \
                "7K0807KL08\n" \
                "7008f36664"
LEVEL_THREE_G = "15540n5552\n" \
                "7#0000He[8\n" \
                "7J[00#0Q]8\n" \
                "7[]r0W[0[8\n" \
                "7]R0#0]q]8\n" \
                "7w00000JL8\n" \
                "3666666664"
LEVEL_THREE_H = "155buin552\n" \
                "7sw0000[#8\n" \
                "7Kv00E0]0c\n" \
                "7Hc0[00K00\n" \
                "7[op]00w0v\n" \
                "7]+ld0J0K8\n" \
                "3666666664"
LEVEL_THREE_I = "155bjkn552\n" \
                "7t;?{}?:y8\n" \
                "zjkK00Wjkc\n" \
                "?(k0G00j)?\n" \
                "xjka0Lsjkv\n" \
                "7u}?:;?{i8\n" \
                "366bjkn664"

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
        "THE GARDEN",
        (1, -1),  # Location in the world
        [LEVEL_INTRO_C]  # All layouts for that level
    ),
    (
        "D",
        (1, 0),  # Location in the world
        [LEVEL_INTRO_D]  # All layouts for that level
    ),
    (
        "THE GATE",
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
        "THE ORCHARD",
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
        "RIVERSIDE",
        (4, -3),  # Location in the world
        [LEVEL_ONE_A]  # All layouts for that level
    ),
    (
        "LVL1_B",
        (4, -4),  # Location in the world
        [LEVEL_ONE_B]  # All layouts for that level
    ),
    (
        "WILLOW TREE",
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
        "LOWER LAKE",
        (1, -5),  # Location in the world
        [LEVEL_THREE_A]  # All layouts for that level
    ),
    (
        "LAKE",
        (1, -6),  # Location in the world
        [LEVEL_THREE_B]  # All layouts for that level
    ),
    (
        "LAKE",
        (1, -7),  # Location in the world
        [LEVEL_THREE_C]  # All layouts for that level
    ),
    (
        "UPPER LAKE",
        (0, -7),  # Location in the world
        [LEVEL_THREE_D]  # All layouts for that level
    ),
    (
        "LAKE",
        (-1, -7),  # Location in the world
        [LEVEL_THREE_E]  # All layouts for that level
    ),
    (
        "LAKE",
        (-1, -6),  # Location in the world
        [LEVEL_THREE_F]  # All layouts for that level
    ),
    (
        "LAKE",
        (-1, -5),  # Location in the world
        [LEVEL_THREE_G]  # All layouts for that level
    ),
    (
        "LAKE",
        (0, -5),  # Location in the world
        [LEVEL_THREE_H]  # All layouts for that level
    ),
    (
        "LAKE ISLAND",
        (0, -6),  # Location in the world
        [LEVEL_THREE_I]  # All layouts for that level
    ),
]
