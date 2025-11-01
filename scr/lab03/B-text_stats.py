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

def text_stats(s, beautiful = False):
    s = tokenize(normalize(s))
    print(f'Всего слов: {len(s)}')
    print(f'Уникальных слов: {len(set(s))}')
    print('Топ-5:')
    s = count_freq(s)
    if beautiful:
        max_word_len = max([len(x) for x in s]) + 3
        print(f"{'слово':<{max_word_len}} | частота")
        print("-" * (max_word_len + 10))
        cnt = 0
        for word, freq in s.items():
            if cnt == 5: break
            print(f"{word:<{max_word_len}} | {freq}")
            cnt += 1
    else:
        cnt = 0
        for word, freq in s.items():
            if cnt == 5: break
            print(f"{word}:{freq}")
        cnt += 1

print(text_stats(input(),beautiful=True))