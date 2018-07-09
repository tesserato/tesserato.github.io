pandoc Dissert.md -o 02_text.docx ^
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

REM pandoc 01_pre_textuais.docx 02_text.docx 03_pos_textuais.docx -o 04_FINAL.docx

pause

REM  --toc --toc-depth=4