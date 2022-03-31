
def get_words():
    array = [] 
    with open('Wordle Answers.txt','r') as file: 
        for line in file: 
            data = line.split()
            array.append(data[3])
    return array 

def main(): 
    how_many_letters = input("Enter how many letters you know: ")
    position = input("Enter the location of ")
    if how_many_letters >= 1 and how_many_letters <=4: 
        for i in range(0, how_many_letters): 
            input

if __name__ == "__main__":
   main()
