def main():
  path_to_file="books/frankenstein.txt"
  text = get_book_text(path_to_file)
  words = get_num_words(text)
  chars_dict = get_chars_dict(text)
  chars_sorted_list = get_sorted_chars(chars_dict)

  print(f"--- Begin report of books/frankenstein.txt ---")
  print(f"{words} words found in the document\n")
  for item in chars_sorted_list:
    if not item["char"].isalpha():
      continue
    print(f"The '{item['char']}' character was fount {item['num']} times")
  print("--- End report ---")


def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
  words = text.split()
  return len(words)

def get_chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_on(chars):
  return chars["num"]

def get_sorted_chars(chars):
  sorted_chars=[]
  for i in chars:
    sorted_chars.append({"char": i,"num": chars[i]})
  sorted_chars.sort(reverse=True, key=sort_on)
  return sorted_chars

main()
