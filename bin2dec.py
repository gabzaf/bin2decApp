#dec = 39
#b_n = bin(dec)                                      #pyfunction to convert decimal value to its corresponding binary value
#print(b_n)

string_to_iterate = input("Input a binary number until eight digits: ")
char_length = len(string_to_iterate)
#print(char_length)

if(char_length > 7):
    print("Number above eight digits is NOT allowed")
    quit()                  #quit should not be used in production code. this function should only be used in the interpreter

total = 0
char_index = char_length - 1
index_binary = 0

while (char_index >= 0 and index_binary < char_length):
    if((string_to_iterate[char_index]) != "0" and  (string_to_iterate[char_index]) != "1"):
        print("Not a binary number!")
        quit()
    bin_number = (int(string_to_iterate[char_index]))*(2**(index_binary))              # sum[(1or0)*2^(n)]. char_index iterate string backwards. index_binary to start countinng from right to left
    total = total + bin_number

    char_index -=1
    index_binary +=1      #teste

print(total)