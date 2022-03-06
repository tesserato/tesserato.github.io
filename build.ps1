$root = "./docs/"

Get-ChildItem -Path "./docs/" -Include *.html -Recurse | ForEach-Object { $_.Delete()}

$pages = Get-ChildItem -Path "./SOURCE/pages" | Where-Object { $_.Extension -in ".md" }
foreach ($post in $pages){
  $in = $post.FullName
  $out= $root + "/_" + $post.Name.Replace($post.Extension, ".html").Replace(" ", "_").ToLower()
  $edited = $post.LastWriteTime.ToString("dd/MM/yyyy")
  pandoc -s $in -o $out --template "templatePages.html" --metadata edited=$edited
}

$posts = Get-ChildItem -Path "./SOURCE/posts" | Where-Object { $_.Extension -in ".md" }
foreach ($post in $posts){
  $in = $post.FullName
  $out= $root + "/_" + $post.Name.Replace($post.Extension, ".html").Replace(" ", "_").ToLower()
  $edited = $post.LastWriteTime.ToString("dd/MM/yyyy")
  pandoc -s $in -o $out --template "templatePages.html" --metadata edited=$edited
}

python "./create_index.py"