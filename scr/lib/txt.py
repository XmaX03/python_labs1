import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('Ё','Е').replace('ё','е')
    text = text.replace('\n',' ').replace('\t',' ').replace('\r',' ')
    text = re.sub(r'\s+', ' ', text.strip())
    return text



def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)



def count_freq(tokens: list[str]) -> dict[str, int]:
    ans = {}
    for token in tokens:
        if token not in ans:
            ans[token] = 1
        else:
            ans[token] += 1
    return ans

def top_n(freq: dict[str, int], n: int | None = None) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items if n is None else sorted_items[:n]
