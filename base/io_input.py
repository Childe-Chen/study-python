def reverse(text):
    return text[::-1]


def is_palindrome(text):
    text = text.lower()
    return text == reverse(text)


something = input("Enter text: ")
something = something.replace(" ", "").replace(",", "").replace(".", "")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")