def process_queries(phone_book):
    while True:
        try:
            query = input().strip()
            if query in phone_book:
                print(f"{query}={phone_book[query]}")
            else:
                print("Not found")
        except EOFError:
            break

if __name__ == "__main__":
    n = int(input())
    phone_book = {}
    for _ in range(n):
        name, number = input().split()
        phone_book[name] = number

    process_queries(phone_book)
