import csv 

def main():
    word = []  
    with open('Wordle Answers.txt', 'r') as f:
        for line in f: 
            data = line.split()
            word.append(data[2]) 
    with open('Wordle_Answers_CSV.csv', 'w') as f:
        for x in word: 
            writer = csv.writer(f) 
            writer.writerows(word) 

if __name__ == "__main__":
   main() 
