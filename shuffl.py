import random

if __name__ == '__main__':
    input_file = 'input.py'   # Replace with the path to your input file
    output_file = 'output.py' # Replace with the desired output file path
    add_comments_and_shuffle(input_file, output_file)
    shuffle_lines(output_file, output_file)
    add_unshuffler(input_file, output_file)


def add_comments_and_shuffle(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        lines = f_in.readlines()
        comments = ['#${}()'.format(i + 1) for i in range(len(lines))]
        

        for comment, line in zip(comments, lines):
            shuffled_line = comment + " " + line
            f_out.write(shuffled_line)

def shuffle_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        random.shuffle(lines)

    with open(output_file, 'w') as f:
        f.writelines(lines)

def add_unshuffler(input_file, output_file):
    unshuffler = """
#$/&(&/)(/(/%))
import os
with open("temp.py", "+x") as f:
    unshuffler = '''import re, os

def unshuffle_lines():
    with open("unshuffled.py", 'r') as f_in, open("output.py", 'w') as f_out:
        lines = f_in.readlines()
        comments = []
        shuffled_lines = []

        for line in lines:
            match = re.match(r'#\$(\d+)\(\)', line)
            if match:
                comment_num = int(match.group(1))
                comments.append(comment_num)
                line = re.sub(r'#\$\d+\(\)\ ', '', line)  # Remove matching parts from the line
                shuffled_lines.append(line)
            else:
                f_out.write(line)

        unshuffled_lines = [line for _, line in sorted(zip(comments, shuffled_lines))]
        f_out.writelines(unshuffled_lines)

def delete_after_string(input_file, output_file):
    with open(input_file, 'r') as f_in:
        str = f_in.read()
        
    ch = '#$/&(&/)(/(/%))'
    # Remove all characters after the character '-' from string
    strValue = str.split(ch, 1)[0]
    with open(output_file, 'w') as f_out:
        f_out.write(strValue)



if __name__ == '__main__':
    input_file = 'output.py'  # Replace with the path to your shuffled output file
    output_file = 'unshuffled.py'  # Replace with the desired unshuffled output file path
    delete_after_string(input_file, output_file) 
    
    unshuffle_lines()
    os.remove("unshuffled.py")
    os.system("output.py")

'''
    f.write(unshuffler)

os.system("temp.py")
os.remove("temp.py")
"""

    with open(output_file, "a") as output_file:
        output_file.write(unshuffler)

