vowels = ["a", "e", "i", "o", "u"]

word = input("introduce la palabra: ")

v_freq = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letter in word:
    if letter in vowels:
        v_freq[letter] += 1

print("Frecuencia de las vocales en {word}: \n {v-freq}", word, v_freq)
