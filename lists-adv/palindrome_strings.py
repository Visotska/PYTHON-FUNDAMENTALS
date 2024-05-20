strings = input().split(" ")
searched_palindrome = input()
palindrome = []

for word in strings:
    if word == "".join(reversed(word)):
        palindrome.append(word)


print(f"{palindrome}")
print(f"Found palindrome {palindrome.count(searched_palindrome)} times")