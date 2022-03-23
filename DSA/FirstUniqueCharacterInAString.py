"""
Basic question: return the first unique letter in a given string

example: firstUniqueChar("Jose Cabral") => "J" because j occurs first

T = O(N)
S = O(N) because of the letters hashmap that is being using, it's as long as the input

YouTube Link: https://www.youtube.com/watch?v=St47WCbQa9M
"""



def firstUniqueChar(string) -> str:
    letters = {}
    for i in range(0, len(string)):
        currentLetter = string[i]
        if currentLetter not in letters:
            letters[currentLetter] = i
        else:
            letters[currentLetter] = -1
            
    '''for occurence in letters:
        if letters[occurence] != -1:
            return occurence'''

    for letter, occurence in letters.items():
        if occurence is not -1:
            return letter

    return "no unique characters"




def main():
    print(firstUniqueChar("Jose Cabral"))
    print(firstUniqueChar("leetcode"))
    print(firstUniqueChar("loveleetcode"))
    print(firstUniqueChar("aaabbbcccddd"))



if __name__ == "__main__":
    main()