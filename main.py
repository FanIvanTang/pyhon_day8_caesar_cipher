alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


def encrypt(origin, key):
    encrypted = []
    length = len(alphabet)
    for letter in origin:
        try:
            idx = alphabet.index(letter)

            idx += key

            idx = idx % length

            encrypted.append(alphabet[idx])
        except ValueError:
            encrypted.append(letter)
    encrypted = "".join(encrypted)

    print(f"The encoded text is {encrypted}")
    return encrypted


def decode(encoded_text, shift_amount):
    decoded_text = []
    length = len(alphabet)

    for letter in encoded_text:
        try:
            idx = alphabet.index(letter)
            idx -= shift_amount
            idx = idx % length
            decoded_text.append(alphabet[idx])
        except ValueError:
            decoded_text.append(letter)

    decoded_text = "".join(decoded_text)
    print(f"The origin text is {decoded_text}")
    return decoded_text


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


def caesar(plain_text, shift_amount, direction):

    result = []
    length = len(alphabet)

    for letter in plain_text:
        try:
            idx = alphabet.index(letter)
            if direction == "encode":
                idx += shift_amount
            elif direction == "decode":
                idx -= shift_amount
            idx = idx % length
            result.append(alphabet[idx])
        except ValueError:
            result.append(letter)

    result = "".join(result)
    print(f"The {direction} text is {result}")
    return result


if __name__ == "__main__":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_amount=shift, direction=direction)
