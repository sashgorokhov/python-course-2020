def divide(user_input):
    # your code here

    try:
        a, b = user_input.strip().split(' ')
        return int(a) / int(b)
    except Exception as e:
        return f'Error code: {e}'
    pass


if __name__ == '__main__':
    while True:
        print(divide(input()))
