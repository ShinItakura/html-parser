from bs4 import BeautifulSoup

# def find_nested_pattern(html: str):
#     soup = BeautifulSoup(html, "html.parser")
#     results = []

#     for section in soup.find_all("section", attrs={"data-id": True}):
#         if not str(section["data-id"]).startswith("92"):
#             continue
        
#         for article in section.find_all("article", attrs={"data-class": True}):
#             if not str(section["data-class"]).endswith("45"):
#                 continue
            
#             for div in article.find_all("div", attrs={"data-tag": True}):
#                 if "78" in str(div["data-tag"]):
#                     results.append(div)
    
#     return results

# def find_special_divs(html: str):
#     soup = BeautifulSoup(html, "html.parser")

#     selector = 'section[data-id^="92"] article[data-class$="45"] div[data-tag*="78"]'
#     return soup.select(selector)

def find_ramp_ref_value(html: str):
    soup = BeautifulSoup(html, "html.parser")

    selector = 'section[data-id^="92"] article[data-class$="45"] div[data-tag*="78"]'
    divs = soup.select(selector)

    results = []

    for div in divs:
        ref_value = None

        for tag in div.find_all():
            classes = tag.get("class", [])
            # if "ramp" in classes and ("ref" in classes or "ref0" in classes):
            if "ramp" in classes and  "ref" in classes:
                ref_value = tag.get("value")
                break

        results.append(ref_value)

    return results        

if __name__ == "__main__":
    with open("input.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # matches = find_nested_pattern(html)

    # matches = find_special_divs(html)

    matches = find_ramp_ref_value(html)

    urlmatch = ""

    for i, div in enumerate(matches, start=1):
        urlmatch = urlmatch + div

    print(urlmatch)