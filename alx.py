#Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
#Print all the letters except q and e
#You can only use one print function with string format
for c in range(ord('a'), ord('z') + 1):
    if c != (ord('q') or ord('e')):
        print("{:c}".format(c), end=" ")