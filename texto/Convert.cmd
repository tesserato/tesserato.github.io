pandoc Dissert.md -o Dissert.docx ^
--filter pandoc-fignos ^
--filter pandoc-tablenos ^
--filter pandoc-eqnos ^
--bibliography=FINAL.bib ^
--reference-doc=reference.docx ^
--from=markdown-markdown_in_html_blocks-native_divs

pause