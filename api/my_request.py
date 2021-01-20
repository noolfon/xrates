from  main.controllers import UpdateRates
xrates = UpdateRates().call(from_currency=None, to_currency=None)

if __name__ == '__main__':
    print(xrates)