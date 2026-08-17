import re


entry_key_pattern = re.compile(
    r"(@[A-Za-z][A-Za-z0-9_]*\s*\{\s*)([^,\s]+)(\s*,)"
)


def make_keys_unique(text):
    used_keys = set()

    def replace_key(match):
        prefix, key, suffix = match.groups()
        candidate = key
        counter = 2
        while candidate in used_keys:
            candidate = f"{key}{counter}"
            counter += 1
        used_keys.add(candidate)
        return f"{prefix}{candidate}{suffix}"

    return entry_key_pattern.sub(replace_key, text)


with open("bib_test.bib", "r", encoding="utf-8-sig") as file:
    file_string = file.read()

processed_string = make_keys_unique(file_string)

with open("bib_test.bib", "w", encoding="utf-8") as file:
    file.write(processed_string)

# Replace very long author lists with collaboration names so the generated
# bibliography remains manageable for both BibTeX and LaTeX.
to_write = []
with open("bib_test.bib", "r", encoding="utf-8") as file:
    for line in file:
        if len(line) > 10000:
            to_write.append("author={The CMS Collaboration},\n")
        elif 1000 < len(line) < 10000 and (
            "Accettura, Carlotta" not in line
            and "Black, K.M. and Jindariani, S." not in line
        ):
            to_write.append("author={The CMS GEM Group},\n")
        elif 1000 < len(line):
            to_write.append("author={The Muon Collider Collaboration},\n")
        else:
            to_write.append(line)

with open("bib.bib", "w", encoding="utf-8") as file:
    file.writelines(to_write)
