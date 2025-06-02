import art
print(art.logo)

char_str = "abcdefghijklmnopqrstuvwxyz"

def encrypt(user_msg, no_of_shifts):
    encoded_str = ""
    for i in range(len(user_msg)):
        curr_char_pos = ord(user_msg[i]) - ord('a') + 1 
        new_char_pos = (curr_char_pos - 1 + no_of_shifts) % 26
        encoded_str += char_str[new_char_pos]
    return encoded_str

def decrypt(user_msg, no_of_shifts):
    decoded_str = ""
    for i in range(len(user_msg)):
        curr_char_pos = char_str.index(user_msg[i])
        prev_char_pos = (curr_char_pos - no_of_shifts) % 26
        decoded_str += char_str[prev_char_pos]
    return decoded_str

# if user_action == "encrypt":
#     print(encrypt(user_msg, no_of_shifts))
# else:
#     print(decrypt(user_msg, no_of_shifts))

# CHALLENGE - combine encrypt and decrypt into a single function caesar_cipher() and get rid of the last if-else
user_wants_to_continue = True

def caesar_cipher(user_msg, no_of_shifts, user_action):
    enc_dec_str = ""
    if user_action == "decrypt":
        no_of_shifts *= -1

    for i in range(len(user_msg)):
        if user_msg[i] in char_str:
            curr_char_pos = char_str.index(user_msg[i])
            new_char_pos = (curr_char_pos + no_of_shifts) % 26
            enc_dec_str += char_str[new_char_pos]
        else:
            enc_dec_str += user_msg[i]

    return enc_dec_str

while user_wants_to_continue:
    user_msg = input("What is your message? ").lower()
    user_action = input("What is your action? Do you want to encrypt or decrypt? ").lower()
    no_of_shifts = int(input("How many letters would you like to shift? "))
    
    print(f"The {user_action}ed message is: {caesar_cipher(user_msg, no_of_shifts, user_action)}")
    
    user_wish = input("Would you like to go again? (y/n) ").lower()
    if user_wish == "n":
        user_wants_to_continue = False
        print("Goodbye!")


