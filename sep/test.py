def main():
    state = ['My', 'name', 'is', 'john']
    print('従来の表示')
    print(state)
    print('改行した表示')
    print(*state, sep='\n')
    print('*の挙動')
    print(*state)


if __name__ == '__main__':
    main()
