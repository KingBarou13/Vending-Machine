soda = 10
water = 10
lemonade = 10
potato = 10
choc = 10
ice = 10
profit = 0
while True:
    try:
        print('--------Vending Machine--------\n'
              '|Code:         |Items:        |\n'
              '|      1       |Soda          |\n'
              '|      2       |Water         |\n'
              '|      3       |Lemonade      |\n'
              '|      4       |Potato chips  |\n'
              '|      5       |Chocolate     |\n'
              '|      6       |Ice cream     |\n'
              '-------------------------------\n'
              '0- Exit\n'
              '1- Buy\n'
              '1234- Storage')
        op = int(input('-> '))
        if (op == 1234):
            while True:
                try:
                    print('---------STORAGE---------')
                    print('Items:      |Units: ')
                    print('Soda        |{}    '.format(soda))
                    print('Water       |{}    '.format(water))
                    print('Lemonade    |{}    '.format(lemonade))
                    print('Potato chips|{}    '.format(potato))
                    print('Chocolate   |{}    '.format(choc))
                    print('Ice cream   |{}    '.format(ice))
                    print('-' * 25)
                    print('0- Exit\n'
                          '1- Add\n'
                          '2- Profit')
                    stock = int(input('-> '))
                    if (stock == 1):
                        print('What do you want to add?\n'
                              '1- Soda\n'
                              '2- Water\n'
                              '3- Lemonade\n'
                              '4- Potato chips\n'
                              '5- Chocolate\n'
                              '6- Ice cream')
                        item = int(input('-> '))
                        if (item == 1):
                            print('How many units will be added?')
                            unit1 = int(input('-> '))
                            soda += unit1
                            print('Units successfully added!')
                        elif (item == 2):
                            print('How many units will be added?')
                            unit2 = int(input('-> '))
                            water += unit2
                            print('Units successfully added!')
                        elif (item == 3):
                            print('How many units will be added?')
                            unit3 = int(input('-> '))
                            lemonade += unit3
                            print('Units successfully added!')
                        elif (item == 4):
                            print('How many units will be added?')
                            unit4 = int(input('-> '))
                            potato += unit4
                            print('Units successfully added!')
                        elif (item == 5):
                            print('How many units will be added?')
                            unit5 = int(input('-> '))
                            choc += unit5
                            print('Units successfully added!')
                        elif (item == 6):
                            print('How many units will be added?')
                            unit6 = int(input('->'))
                            ice += unit6
                            print('Units successfully added!')
                        else:
                            print('Invalid value\n'
                                  'Try again...')
                            continue

                    elif (stock == 2):
                        print('The total profit is {}'.format(profit))

                    elif (stock == 0):
                        break

                    else:
                        print('Invalid value\n'
                              'Try again...')
                        continue

                except ValueError:
                    print('Invalid value\n'
                          'Try again...')

            print('Finishing...')

        elif (op == 1):
            print('What do you want to buy?')
            buy = int(input('-> '))
            if (buy == 1):
                if (soda != 0):
                    print('One Soda cost ??2.5')
                    print('Insert the money')
                    payment1 = float(input('-> '))
                    if (payment1 < 2.5):
                        print('PAY CORRECTLY!')
                    elif (payment1 == 2.5):
                        profit += 2.5
                        soda -= 1
                        print('Successfully payed!')
                    else:
                        profit += 2.5
                        soda -= 1
                        print('Successfully payed!')
                        print('Returning ??{}'.format(payment1 - 2.5))
                else:
                    print('Product unavailable!')

            elif (buy == 2):
                if (water != 0):
                    print('One bottle of water cost ??1')
                    print('Insert the money')
                    payment2 = float(input('-> '))
                    if (payment2 < 1):
                        print('PAY CORRECTLY!')
                    elif (payment2 == 1):
                        profit += 1
                        water -= 1
                        print('Successfully payed!')
                    else:
                        profit += 1
                        water -= 1
                        print('Successfully payed!')
                        print('Returning ??{}'.format(payment2 - 1))
                else:
                    print('Product unavailable!')

            elif (buy == 3):
                if (lemonade != 0):
                    print('One lemonade cost ??1.50')
                    print('Insert the money')
                    payment3 = int(input('-> '))
                    if (payment3 < 1.5):
                        print('PAY CORRECTLY!')
                    elif (payment3 == 1.5):
                        profit += 1.5
                        lemonade -= 1
                        print('Successfully payed!')
                    else:
                        profit += 1.5
                        lemonade -= 1
                        print('Successfully payed!')
                        print('Returning ??{}'.format(payment3 - 1.5))
                else:
                    print('Product unavailable!')

            elif (buy == 4):
                if (potato != 0):
                    print('One bag of potato chips cost ??4')
                    print('Insert the money')
                    payment4 = int(input('-> '))
                    if (payment4 < 4):
                        print('PAY CORRECTLY!')
                    elif (payment4 == 4):
                        profit += 4
                        potato -= 1
                        print('Successfully payed!')
                    else:
                        profit += 4
                        potato -= 1
                        print('Successfully payed!')
                        print('Returning ??{}'.format(payment4 - 4))
                else:
                    print('Product unavailable!')

            elif (buy == 5):
                if (choc != 0):
                    print('One chocolate bar cost ??2')
                    print('Insert the money')
                    payment5 = int(input('-> '))
                    if (payment5 < 2):
                        print('PAY CORRECTLY!')
                    elif (payment5 == 2):
                        profit += 2
                        choc -= 1
                        print('Successfully payed!')
                    else:
                        profit += 2
                        choc -= 1
                        print('Successfully payed!')
                        print('Returning ??{}'.format(payment5 - 2))
                else:
                    print('Product unavailable!')

            elif (buy == 6):
                if (ice != 0):
                    print('One ice cream cost ??0.50')
                    print('Insert the money')
                    payment6 = int(input('-> '))
                    if (payment6 < 0.50):
                        print('PAY CORRECTLY!')
                    elif (payment6 == 0.50):
                        profit += 0.50
                        ice -= 1
                        print('Successfully payed!')
                    else:
                        profit += 0.50
                        ice -= 1
                        print('Successfully payed!')
                        print('Returning ??{}'.format(payment6 - 0.50))
                else:
                    print('Product unavailable!')

            else:
                print('This product do not exist')

        else:
            break

    except ValueError:
        print('Invalid value\n'
              'Try again...')

print('finishing')