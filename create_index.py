from bs4 import BeautifulSoup
import os
import glob
import json

path_to_template_html = "./templatePages.html"
path_to_info_json = "./Info.json"
path_to_output_html = "./docs/index.html"
path_to_pages = "./docs/_20**.html"

soup = BeautifulSoup("", "html5lib")

main = soup.new_tag('main')
all_keywords = []

for file in glob.glob(path_to_pages):
  
  with open(file, encoding="utf-8") as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt, "html5lib")

  url = file.split("\\")[-1]
  print(f"\nAdding {url} to index.html")

  title = soup.find_all("title")[0].string.replace("\n", "")
  author = soup.find_all("meta", {"name": "author"})[0]["content"]
  keywords = soup.find_all("meta", {"name": "keywords"})[0]["content"].split(",")
  keywords = [k.strip() for k in keywords]
  all_keywords += keywords
  description = soup.find_all("meta", {"name": "description"})[0]["content"].replace("\n", " ")

  created = soup.find_all("time", {"class": "created"})[0].string
  edited = soup.find_all("time", {"class": "edited"})[0].string

  article = soup.new_tag('article')
  div = soup.new_tag('div')
  div["class"] = "postPreview"
  h3 = soup.new_tag('h3')
  h3.string = title
  p = soup.new_tag('p')
  p["class"] = "postInfo"
  p.string = f"Created: {created}, Last edited: {edited}, {author}"

  div.append(h3)
  div.append(p)

  article.append(div)

  a = soup.new_tag('a', href=url)
  a.string = description
  article.append(a)
  main.append(article)

with open(path_to_info_json, "r") as read_file:
  info = json.load(read_file)

with open(path_to_template_html, encoding="utf-8") as inf:
  txt = inf.read()
  soup = BeautifulSoup(txt, "html5lib")


title = soup.find_all("title")[0]
title.string = info["title"]
author = soup.find_all("meta", {"name": "author"})[0]
author["content"] = info["author"]
description = soup.find_all("meta", {"name": "description"})[0]
description["content"] = info["description"]
keywords = soup.find_all("meta", {"name": "keywords"})[0]
print(all_keywords)
keywords["content"] = ",".join(set([k for k in all_keywords if k != ""]))

oldMain = soup.find_all("main")[0]
oldMain.replace_with(main)

with open(path_to_output_html, "w", encoding="utf-8") as outf:
  out = str(soup.prettify())
  # out = minify_html.minify(out)
  outf.write(out)

exit()
with open(path_to_input_html, encoding="utf-8") as inf:
  txt = inf.read()
  soup = BeautifulSoup(txt, "html5lib")

for e in soup.find_all('embed'):
  name = e["src"].split("/")[-1].replace(".pdf", "")
  if os.path.isfile(f"./images/{name}.py"):
    pre_link = e["src"].replace(".pdf", "")
    im = soup.new_tag('img', src=pre_link + ".webp")
    try:
      im["id"] = e["id"]
    except:
      print("Error: no id found for ", e)
    a = soup.new_tag('a', href=pre_link + ".html", target="_blank")
    a.append(im)
    e.replace_with(a)
    # print(e)
    # exit()
    
  else:
    try:
      # with open(f"./images/{name}.svg", encoding="utf-8") as inf:
        # txt = inf.read()
        # svg = BeautifulSoup(txt, features="lxml").find("svg")
        # del svg["height"]
        # del svg["width"]
        # with open(f"./site/source/images/{name}.svg", "w", encoding="utf-8") as outf:
        #   out = str(svg)
        #   outf.write(out)
      e["src"] = e["src"].replace(".pdf", ".svg")
      e.name = "img"
    except:
      print(f"./images/{name}.svg")
    # exit()
  
  
IDS = {}
ctr = 1
for e in soup.find_all("span", {"class": "math display"}):
  lines = [l.replace("\\", "").replace("[", "").strip() for l in e.text.split("\n") if "label" in l]
  if len(lines) > 0:
    id = lines[0].replace("label", "").replace("{", "").replace("}", "")

    new_div = soup.new_tag('div', id=id)
    new_div['class'] = "equation"

    new_spn = soup.new_tag("span")
    new_spn['class'] = "math display"
    new_spn.string = e.string

    new_par = soup.new_tag("p")
    new_par['class'] = "numbering"
    new_par.string = f"({ctr})"

    new_div.contents = [new_spn, new_par]
    # soup.smooth()

    # new_div.append(copy.copy(e))
    # new_div.append(new_par)
    # print(new_div.prettify())

    # exit()
    e.replace_with(new_div)


    print(e.prettify())
    # exit()
    IDS[id] = ctr
    ctr += 1

for key in IDS.keys():
  for e in soup.find_all("a", {"data-reference": key}):
    e.string = f"{IDS[key]}"
    # print(e)
    # exit()

for e in soup.find_all("h1", {"id":"glossary"}):
  e.extract()

# for e in soup.find_all("div", {"class":"csl-entry"}):
#   new_div = soup.new_tag('div')
#   new_div['class'] = "csl-entry"

#   p = soup.new_tag("p")
#   print(new_div.text)
#   p.string = new_div.text
#   new_div.append(p)
#   for c in e.findChildren():
#     new_div.append(c)
#   e.replace_with(new_div)
#   print(e)
#   exit()
# 
with open(path_to_output_html, "w", encoding="utf-8") as outf:
  out = str(soup)
  out = minify_html.minify(out)
  outf.write(out)