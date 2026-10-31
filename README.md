# Publication list

Generate a PDF publication list from a BibTeX export.

Requires Python 3 and a LaTeX installation with `pdflatex` and BibTeX.

1. Save your BibTeX export as `bib_test.bib` in this folder. Keep a backup: the script modifies this file.
2. Run these commands from this folder:

   ```bash
   python3 organize_orcid.py
   pdflatex bibliography.tex
   bibtex bibliography
   pdflatex bibliography.tex
   pdflatex bibliography.tex
   ```

3. Open `bibliography.pdf`.

The script makes duplicate bibliography keys unique and creates `bib.bib`, shortening long author lists to collaboration names. All entries are included in the PDF.

Edit `bibliography.tex` to change the title, author, or affiliation.
