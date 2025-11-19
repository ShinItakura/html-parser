from bs4 import BeautifulSoup

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
    
    matches = find_ramp_ref_value(html)

    urlmatch = ""

    for i, div in enumerate(matches, start=1):
        urlmatch = urlmatch + div

    print(urlmatch)