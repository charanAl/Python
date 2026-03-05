def main():
    yell("This " "is " "charan" )
def yell(*words):
    uppercased = map(str.upper, words)
    # uppercased =[]
    # for word in words:
    #     uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()