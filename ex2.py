def c_vs(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(1 for char in word if char in vowels)
def name(*args):
    for word in args:
        print(count_vs(word))
a = input().split()
name(*a)
