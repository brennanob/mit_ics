def count_vowels(s: str):
    vowels = ["a", "e", "i", "o", "u"]
    nvowels = len([x for x in s if x in vowels])
    print("Number of vowels: " + str(nvowels))
