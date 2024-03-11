
with open("./frankenstein.txt") as f:
    content = f.read()

def count_words(text: str) -> int:
    text_list: list = text.split()
    return len(text_list)

def count_chars(text: str) -> dict:
    lower_text: str = text.lower()
    char_dict: dict = dict()
    for ch in lower_text:
        if ch not in char_dict.keys():
            char_dict[ch] = lower_text.count(ch)
    return char_dict

def sort_on(dict):
    return dict["num"]

num_chars: dict = count_chars(content)
num_chars.pop(' ')
result_list: list = [{"char": key, "num":value} for key, value in num_chars.items()]
result_list.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(count_words(content), "words found in the document")
for num in result_list:
    print(f"The '{num["char"]}' character was found {num["num"]} times")
print("--- End report ---")

