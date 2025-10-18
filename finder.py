import time
import string

letters = list(string.ascii_lowercase + string.ascii_uppercase + ' +')
target ="I am an MCA student"
current_str =""
while current_str != target :
    for letter in letters:
        print(current_str + letter)
        time.sleep(0.01)

        if current_str + letter == target[:len(current_str)+1]:
            current_str += letter
            break