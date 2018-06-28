pandoc -o Dissert.docx Dissert.md --bibliography=bib.bib --reference-doc=reference.docx

pandoc -o index.html Dissert.md --bibliography=bib.bib --mathjax --toc --standalone

REM pandoc -o Dissert.pdf Dissert.md --bibliography=bib.bib --pdf-engine=xelatex