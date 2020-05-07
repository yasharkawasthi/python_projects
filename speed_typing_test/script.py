# Speed Typing Test - Python Project
from time import time

def typingSpeed(typed_text, start_time, end_time):
	global time
	global words
	
	words = typed_text.split()
	wordLen = len(words)
	speed = wordLen / (time / 60)
	
	return speed

def typingErrors(given_text):
        global given_words

        given_words = given_text.split()
        errors = 0
        
        for i in range(len(words)):
                if words[i]==given_words[i]:
                        continue
                else:
                        errors+=1
        return errors

        
given_text="The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters of the alphabet. It is commonly used for touch-typing practice, testing typewriters and computerkeyboards, displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired. Owing to its brevity and coherence, it has become widely known. In the age of computers, this pangram is commonly used to display font samples and for testing computer keyboards. In cryptography, it is commonly used as a test vector for hash and encryption algorithms to verify their implementation, as well as to ensure alphabetic character set compatibility."
                
print("Speed Typing Test")
print("Type this - :")
print(given_text)

input("Press Enter Key when you are ready")

start_time = time()

typed_text = input()

end_time = time()

time_taken =  end_time - start_time

time = round(time_taken, 2)
speed = round(typingSpeed(typed_text, start_time, end_time),2)
errors = typingErrors(given_text)

print("You took",time,"seconds with an Average Speed of",speed,"words per minute with",errors,"errors.")

input()
