import random

def guessing_game():
    answer = random.randint(0,100)
    is_equal = False
    while True:
        try: 
            num = int(input('Input guessing number: '))
        except:
            continue
        if(num > answer):
            print('Too high')
        elif(num < answer):
            print('Too low')
        else:
            print('Just right')
            break

if __name__ == '__main__':
    guessing_game()
	
