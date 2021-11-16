from portfolio import Portfolio

def test_empty_portfolio():
    p=Portfolio()
    assert p.cost()== 0.0

def test_buy_one_stock():
    p=Portfolio()
    p.buy("IBM",100,176.48)
    assert p.cost() == 17648.0

def tes_buy_two_stocks():
    p = Portfolio()
    p.buy("",100,176.48)
    p.buy("",100,36.15)
    assert p.cost() == 21263.00

