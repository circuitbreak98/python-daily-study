MENU = {'sandwich': 10,
        'tea': 7}

def restaurant():
    total = 0
    while(True):
        order = input("Order: ").strip()
        if not order:
            break
        elif order in MENU:
            price =MENU[order]
            total += price
            print(f'{order} costs {price}, total is {total}')
        else:
            print(f'Sorry, we are fresh out of {order} today.')

    print(f'Your total is {total}')
                
restaurant()
