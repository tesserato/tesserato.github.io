from bs4 import BeautifulSoup
import copy
import os
import minify_html


path_to_input_html = "./site/source/thesis.html"
path_to_output_html = "./site/public/thesis.html"

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