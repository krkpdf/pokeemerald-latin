# POKEMON EMERALD LATIN TRANSLATION

![](header.png)

This project aims to translate Pokémon Emerald into Latin. 
Currently, only the translation text files are hosted here. 
These files are intended to be integrated with the [Emerald Decompilation Project](https://github.com/pret/pokeemerald) for compilation. 
The base English text used for translation is also extracted from the Decompilation Project.

*WIKI:* https://github.com/krkpdf/pokeemerald-latin/wiki

*DISCORD:* https://discord.gg/ShA8rfBDwM

## INSTALLATION
1. Download the latest [Release](https://github.com/krkpdf/pokeemerald-latin/releases)
2. Use Rom Patching Software, such as [RomPatcher.js](https://www.marcrobledo.com/RomPatcher.js/), to create a working ROM file
3. Flash the ROM to a cartridge or use an emulator to play the game


## COMPILATION WORKFLOW
### Prerequisites
- Download the [Decompilation Project](https://github.com/pret/pokeemerald) and follow the [installation instructions](https://github.com/pret/pokeemerald/blob/master/INSTALL.md)

### Steps
1. Download this project using `git clone https://github.com/krkpdf/pokeemerald-latin`
2. Translate the text and submit a pull request with your changes
3. Extract, translate and manually replace game graphics as needed
4. In `include/constants/global.h`, set `ABILITY_NAME_LENGTH` to `13` and `ITEM_NAME_LENGTH` to `15`
5. Run `./make.sh` to automatically replace text in the Decompilation Project folder and compile


### Macronizer (Optional)
Generates a build with automatically added vowel-length accents. Values can be manually edited after the first run-through (manually edited text will be overwritten if the `macronize.py` script is executed again). 

#### Prerequisites:
- Complete the main workflow above first.
- Download the [Latin Macronizer](https://github.com/Alatius/latin-macronizer) and follow the [installation instructions](https://github.com/Alatius/latin-macronizer/blob/master/INSTALL.txt) (see also [Macronizer Installation](https://github.com/krkpdf/pokeemerald-latin/wiki/Tips#macronizer-installation))
- Install the latin-macronizer package with `pip install -e .` from the `latin-macronizer-master/` folder. 

1. Copy the `pokeemerald-master-translated/` folder and rename the copy to `pokeemerald-master-translated-marked/`
2. Add the following entries to `charmap.txt`:
   ```
   Ý = 0A
   ý = 1F
   ```
3. Edit all Latin font sprites under `graphics/fonts/`, adding `Ý` and `ý` to the right of `Ì` and `ì` glyphs respectively
4. Update glyph widths in `src/font.c` for all Latin font tables:
   - Find the top row and replace the **6th number from the right** with the first width value (the default should be 3)
   - Find the second row and replace the **1st number from the right** with the second width value (the default should be 3)
   - Use these widths depending on your font type:

   | Font type | Top row (6th from right) | Second row (1st from right) |
   |---|---|---|
   | Narrow / Small | 4 | 5 |
   | Normal / Short | 6 | 6 |

#### Steps:
1. Run `python3 macronize.py` to macronize the text *(this may take several hours)*
2. Run `./make.sh` to compile

## DISCLAIMER

This project is an unofficial, fan-made translation of Pokémon Emerald into Latin and is intended for educational and linguistic purposes only. It is not affiliated with, endorsed by, or approved by Nintendo, Game Freak, The Pokémon Company, or any other official entity associated with the Pokémon franchise.

Pokémon and all related trademarks, logos, and intellectual property are the property of their respective owners. This project is a non-commercial effort, and no financial gain is derived from its distribution. If you represent Nintendo, Game Freak, or The Pokémon Company and have concerns regarding this project, please contact me, and I will promptly address the issue.
