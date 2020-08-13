from microstate.client import MicroStateWriter

# Creating a key is the first step to participation in the prediction network
# A key of difficulty 11 is recommended for using MicroStateWriter
# If you are impatient, you can use difficulty=10

if __name__ == "__main__":
    print('This may take hours. Come back later.')
    print('See https://www.microprediction.org/muids.html for explanation of MUIDs')
    write_key = MicroStateWriter.create_key(difficulty=11)
    print('Your private write_key is ' + write_key)
    print('Your spirit animal is ' + MicroStateWriter.animal_from_key(write_key))
    print('Do not lose the key!', flush=True)
