# latexmk -lualatex -f -interaction=nonstopmode THESIS.tex

$name = "THESIS"
# $name = "000"

$genPDF = $true
$genHTML = $false
$clean = $false

if ($genPDF) {
  Write-Output ">>> lualatex 1:"
  lualatex -interaction=nonstopmode -file-line-error $name

  Write-Output ">>> biber 1:"
  biber $name --nodieonerror

  Write-Output ">>> makeglossaries 1:"
  makeglossaries $name

  Write-Output ">>> lualatex 2:"
  lualatex -interaction=nonstopmode -file-line-error $name

  $words = pdftotext ($name + ".pdf") - | Measure-Object -Word | Select-Object -ExpandProperty Words 
  $words | Out-File -FilePath .\Words.txt

  Write-Host "Current number of words = "$words -ForegroundColor White -BackgroundColor DarkGray
}

if ($genHTML) {
  # -F pandoc-crossref
  pandoc -s --toc ($name + ".tex") --bibliography="THESIS.bib" --bibliography="ENVELOPE.bib" --bibliography="SEGMENTATION.bib" -o "site/source/thesis.html" -c "thesis.css" --mathjax --citeproc --metadata-file="meta.yaml"

  $source = "./site/source/images/"
  $public = "./site/public/images/"


  Get-ChildItem -Path "./site/public/" -Include *.* -Recurse | ForEach-Object { $_.Delete()}

  # python .\00_ParseHtml.py
  node .\00_ParseHtml.js

  gswin64c.exe -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o ($name + "_o.pdf") ($name + ".pdf")
  Copy-Item ($name + "_o.pdf") -Destination "./site/public/thesis.pdf" -Force

  $items = Get-ChildItem -Path $source | Where-Object { $_.Extension -in ".svg" }
  foreach ($item in $items) {
    $in = $source + $item.name
    $out = $public + $item.name
    scour -i $in -o $out --enable-viewboxing --enable-id-stripping --enable-comment-stripping --shorten-ids --indent=none
  }

  $items = Get-ChildItem -Path $source | Where-Object { $_.Extension -in ".html" }
  foreach ($item in $items) {
    $in = $source + $item.name
    $out = $public + $item.name
    html-minifier $in -o $out
  }

Robocopy /xc /xn /xo /s "site/source/" "site/public/"
}

if ($clean) {
  Remove-Item *.bcf, *.xml, *.aux, *.fls, *.log, *.fdb_latexmk, *.glsdefs, *.bak, *.sav, *.ist, *.bbl, *.blg, *.glo, *.out, *.glg, *.gls, *.toc, *.lof, *.lot, *.tmp, *.loa
}




