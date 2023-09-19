# Main:
# 0 - empty
# 1234 - wall corners (LR UP, LR DOWN)
# 5678 - walls (UP DOWN LEFT RIGHT)
# zx - left opening, cv - right opening, bn - down opening (use up corners for up opening)
# qwer - stones (q hookable)

# O - Flying enemy, P - Walking enemy
# A - checkpoint, B - coin, C - key, D - door

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

ROOM_LAYOUT_TEST = "15555D5552\n" \
                   "7CO0000qB8\n" \
                   "7O00000w08\n" \
                   "z00000P0Oc\n" \
                   "0B00000000\n" \
                   "xA0e0000rv\n" \
                   "366b0n6664"

ROOM_DECOR_TEST = "0000000000\n" \
                  "000000R000\n" \
                  "000Q0W0000\n" \
                  "000000E000\n" \
                  "00FG000LW0\n" \
                  "0000HJK000\n" \
                  "0000000000"


LEVEL_A = "1555555552\n" \
          "7000000008\n" \
          "7000000008\n" \
          "7000000008\n" \
          "7000000008\n" \
          "7000000008\n" \
          "3666666664"

ALL_LEVELS = [
    (
        "ENTRANCE",
        (0, 0),  # Location in the world
        [LEVEL_A]  # All layouts for that level
    )
]
