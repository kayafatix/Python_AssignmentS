"comfortable words"

left_hand = set("qwertasdfgzxcvb")
right_hand = set("yuıopğühjklşinmöç")
word = set(input("please TYPE a word: "))
comf_word = bool((word - left_hand) and (word - right_hand))
print(comf_word)
