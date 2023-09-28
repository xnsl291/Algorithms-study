def Solution(phone_book):
    phone_book.sort()
    
    for num in range(len(phone_book)-1):
        if phone_book[num+1].startswith(phone_book[num]):
            return False
    return True