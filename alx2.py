#Write a program that prints numbers from 0 to 99.
for i in range(0, 100):
    if i == 99:
        print(i)#to stop the comma
    else:
        print("{:0>2d}".format(i), end=", ")