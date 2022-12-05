import bank

def test_init():
    customer = bank.BankCustomer(5, 17, 150.23)
    assert hasattr(customer, 'customer_id'), "No instance variable named customer_id found"
    assert customer.customer_id == 5

    assert hasattr(customer, 'accounts'), "No instance variable named accounts found"
    assert customer.accounts == {17: 150.23}

    assert not hasattr(customer, 'account_id'), "Customer shouldn't have an instance variable for account_id"
    assert not hasattr(customer, 'initial_balance'), "Customer shouldn't have an instance variable for initial_balance"

    return customer

def test_add_account(customer):
    assert hasattr(customer, 'add_account'), "No method named add_account found."
    customer.add_account(526, 6687.22)
    assert customer.accounts == {17: 150.23, 526: 6687.22}

def test_get_total_balance(customer):
    assert hasattr(customer, 'get_total_balance'), "No method named add_account found."
    assert customer.get_total_balance() == 6837.45, "Did not correctly get total balance across all accounts"

def main():
    c = test_init()
    test_add_account(c)
    test_get_total_balance(c)

if __name__ == "__main__":
    main()
