import msvcrt
import time

def wait_for_input(timeout):
    print("Please enter input within", timeout, "seconds:")
    start_time = time.time()
    input_text = ''
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch()
            char_decoded = char.decode('utf-8')
            if char_decoded == '\r':  # Enter key pressed
                return input_text.strip()
            input_text += char_decoded
        if time.time() - start_time > timeout:
            return None
        time.sleep(0.1)

# Wait for input for 10 seconds
user_input = wait_for_input(10)

if user_input is None:
    print("No input received. Proceeding with the code...")
else:
    print("Input received:", user_input)
    # Proceed with the code using the received input
