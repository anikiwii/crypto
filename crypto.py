import random

# Message to hide
original_message = "This is just a test"

# Function to hide the message by XORing with a random mask
def hide_message(message):
    mask = random.randint(0, 255)  # Random 8-bit mask
    hidden_message = "".join(chr(ord(char) ^ mask) for char in message)
    return hidden_message, mask

# Hide the message
hidden_message, mask_used = hide_message(original_message)

# Display the hidden message and the mask used
print("Hidden Message:", hidden_message)
print("Mask Used:", mask_used)

# Function to reveal the hidden message by XORing with the same mask
def reveal_message(hidden_message, mask):
    revealed_message = "".join(chr(ord(char) ^ mask) for char in hidden_message)
    return revealed_message

# Reveal the hidden message
revealed_message = reveal_message(hidden_message, mask_used)

# Display the revealed message
print("Revealed Message:", revealed_message)