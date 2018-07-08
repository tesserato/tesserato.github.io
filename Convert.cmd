pandoc -o Dissert.docx Dissert.md --filter pandoc-fignos --bibliography=bib.bib --reference-doc=reference.docx

pandoc -o index.html Dissert.md --filter pandoc-fignos --bibliography=bib.bib --mathjax --toc --standalone --css=style.css

REM pandoc -o AST.json Dissert.md --filter pandoc-fignos --bibliography=bib.bib

REM pandoc -o Dissert.pdf Dissert.md --bibliography=bib.bib --pdf-engine=xelatex

pause