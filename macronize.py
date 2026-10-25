import re
import shutil
import chardet
from pathlib import Path      
from latin_macronizer import Macronizer


macronizer = Macronizer(db_path="macronizer.db")

source_dir = Path("./text/")
dest_dir = Path("./macronized/")
shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)

for filepath in dest_dir.rglob("*"):
    if filepath.is_file():
        print(filepath)
        
        with open(filepath, "rb") as file:
            raw = file.read()

        try:
            text = raw.decode("utf-8")
            
        except UnicodeDecodeError:
            encoding = chardet.detect(raw)["encoding"] or "utf-8"
            text = raw.decode(encoding)

            if encoding != "utf-8":
                print("Unusual encoding:", encoding)

        # Normalize line endings and clean up
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = "\n".join([l for l in text.split("\n") if ".braille " not in l])
        text = re.sub(r'\n{2,}', '\n', text)
        
        # Macronize only text outside {...} blocks
        def macronize_outside_braces(s):
            parts = re.split(r'(\{[^}]*\})', s)
            result = []
            for part in parts:
                if part.startswith('{') and part.endswith('}'):
                    result.append(part)  # leave brace blocks untouched
                else:
                    macronizer.settext(part)
                    macronized = macronizer.gettext(performutov=True, performitoj=True)
                    macronized = (macronized
                        .replace("Ā", "Á").replace("Ē", "É").replace("Ī", "Í")
                        .replace("Ō", "Ó").replace("Ū", "Ú").replace("Ȳ", "Ý")
                        .replace("ā", "á").replace("ē", "é").replace("ī", "í")
                        .replace("ō", "ó").replace("ū", "ú").replace("ȳ", "ý")
                        .replace("áé", "{AE_}").replace("áe", "{AE_}").replace("aé", "{AE_}").replace("ae", "æ")
                        .replace("Áé", "{AE}").replace("Áe", "{AE}").replace("Aé", "{AE}").replace("ae", "Æ")
                        .replace("óé", "{OE_}").replace("óe", "{OE_}").replace("oé", "{OE_}").replace("oe", "œ")
                        .replace("Óé", "{OE}").replace("Óe", "{OE}").replace("Oé", "{OE}").replace("oe", "Œ")
                    )
                    #print(macronized)
                    result.append(macronized)
            return "".join(result)

        #print(text)
        text = macronize_outside_braces(text)
        text = text.replace("\"namé\":", "\"name\":")
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)

        