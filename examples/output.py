#$14()         first_subtrahend = float(input("First subtrahend: "))
#$5()     print("4. Division")
#$15()         second_subtrahend = float(input("Second subtrahend: "))
#$18()     elif choice == "3":
#$9()         first_addend = float(input("First addend: "))
#$7()     choice = input("Your choice: ")
#$3()     print("2. Substraction")
#$1() while True:
#$12()         print(first_addend + second_addend)
#$25()         divider = float(input("Divider: "))
#$8()     if choice == "1":
#$28()     elif choice == "5":
#$6()     print("5. Exit")
#$23()     elif choice == "4":
#$22()         print(multiplier * multiplicand)
#$31()         print("Wrong choice!")
#$21()         print("Result: ", end="")
#$11()         print("Result: ", end="")
#$19()         multiplier = float(input("Multiplier: "))
#$2()     print("1. Addition")
#$26()         print("Result: ", end="")
#$13()     elif choice == "2":
#$16()         print("Result: ", end="")
#$10()         second_addend = float(input("Second addend: "))
#$4()     print("3. Multiplication")
#$29()         break
#$30()     else:
#$24()         dividend = float(input("Dividend: "))
#$20()         multiplicand = float(input("Multiplicand: "))
#$27()         print(dividend / divider)
#$17()         print(first_subtrahend - second_subtrahend)

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
