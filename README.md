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
0. Download the [Decompilation Project](https://github.com/pret/pokeemerald) and follow the [installation instructions](https://github.com/pret/pokeemerald/blob/master/INSTALL.md) 
1. Download this project using `git clone https://github.com/krkpdf/pokeemerald-latin`
2. Translate the text and submit a pull request with your changes
3. Extract, translate and manually replace game graphics as needed
4. Change ABILITY_NAME_LENGTH in include/globals.h to 13 and ITEM_NAME_LENGTH to 15
5. Automatically replace text in the Decompilation Project folder and compile using `./make.sh` 


## DISCLAIMER

This project is an unofficial, fan-made translation of Pokémon Emerald into Latin and is intended for educational and linguistic purposes only. It is not affiliated with, endorsed by, or approved by Nintendo, Game Freak, The Pokémon Company, or any other official entity associated with the Pokémon franchise.

Pokémon and all related trademarks, logos, and intellectual property are the property of their respective owners. This project is a non-commercial effort, and no financial gain is derived from its distribution. If you represent Nintendo, Game Freak, or The Pokémon Company and have concerns regarding this project, please contact me, and I will promptly address the issue.
