import pytest
from modules.common.database import DataBase

@pytest.mark.database
def test_database_connection():
    db = DataBase()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = DataBase()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = DataBase()
    user = db.get_user_address('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = DataBase()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = DataBase()
    db.insert_product(4, 'cookies', 'sweet', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = DataBase()
    db.insert_product(99, 'test', 'info', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = DataBase()
    orders = db.get_detailed_orders()
    print("Orders", orders)
    #check quantity of orders equal to 1

    #check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'