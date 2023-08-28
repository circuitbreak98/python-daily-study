import sys
def get_final_line1(filename):
    with open(filename) as f:
        last_line = ''
        for current_line in f:
            last_line = current_line
        return last_line

def get_final_line2(filename):
    for current_line in open(filename):
        pass
    return current_line
                    

def get_final_line(filename):
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line        

def get_byte_length(filename):
    with open(filename) as f:
        while True:
            one_chunk = f.read(1000)
            if not one_chunk:
                break
            print(f'This chunk contains {len(one_chunk)} bytes')

print(get_final_line('./loremipsum.txt'))
get_byte_length('./loremipsum.txt')