pandoc Dissert.md -o Dissert.docx ^
--filter pandoc-fignos ^
--filter pandoc-tablenos ^
--filter pandoc-eqnos ^
--bibliography=bib.bib ^
--reference-doc=reference.docx ^
--from=markdown-markdown_in_html_blocks-native_divs

pandoc Dissert.md -o index.html ^
--filter pandoc-fignos ^
--filter pandoc-tablenos ^
--filter pandoc-eqnos ^
--bibliography=bib.bib ^
--reference-doc=reference.docx ^
--css=style.css ^
--mathjax --toc --standalone

pause