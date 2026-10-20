"""Pack the character animation strips into one sprite sheet per character.

Each strip goes on its own row of 16 tiles so the .tilesource files can address
animations by tile number (row 1 starts at tile 1, row 2 at tile 17, ...).
Run from the project root after changing anything in ASSETS/Homeless_*:

    python tools/build_character_sheets.py
"""
from PIL import Image

TILE = 128
COLUMNS = 16
# order matters: the .tilesource files refer to these rows by tile number
STRIPS = ["Run", "Jump", "Dead", "Idle", "Hurt", "Attack_1"]
CHARACTERS = {
    "Homeless_1": "hero/homeless_1_sheet.png",
    "Homeless_3": "killer/homeless_3_sheet.png",
}

for character, output in CHARACTERS.items():
    strips = [Image.open("ASSETS/%s/%s.png" % (character, name)).convert("RGBA") for name in STRIPS]
    sheet = Image.new("RGBA", (TILE * COLUMNS, TILE * len(strips)))
    print(character)
    for row, (name, strip) in enumerate(zip(STRIPS, strips)):
        frames = strip.width // TILE
        assert frames <= COLUMNS, name
        sheet.paste(strip, (0, row * TILE))
        first = row * COLUMNS + 1
        print("  %-8s tiles %d-%d" % (name, first, first + frames - 1))
    sheet.save(output)
