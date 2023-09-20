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
# a - checkpoint, s - coin, d - key, f - door

# Decor:
# QWE - flowers
# R - Little stone
# GH - Mushrooms
# HJKL - Grass
#

FRAME = "1555555552\n" \
        "70O0000008\n" \
        "7O00000008\n" \
        "70000000O8\n" \
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


LEVEL_A = "155bfn5552\n" \
          "7[0a000Kd8\n" \
          "7]00KJ00#8\n" \
          "7tggggggy8\n" \
          "7uhhhhhhi8\n" \
          "700Q0000R8\n" \
          "3666666664"

ALL_LEVELS = [
    (
        "ENTRANCE",
        (0, 0),  # Location in the world
        [LEVEL_A]  # All layouts for that level
    )
]
