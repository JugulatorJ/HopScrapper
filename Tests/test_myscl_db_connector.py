from db_connector import ConnectToDB, ModifyDB


def test_ConnectToDB(mocker):
    mock_connect = mocker.patch('mysql.connector.connect')
    mock_connect.return_value.is_connected.return_value = True

    db = ConnectToDB()

    mock_connect.assert_called_once_with(user='root', password='PrestaSimcoe2018!',
                                         host='127.0.0.1', database='certificates',
                                         auth_plugin='mysql_native_password')
    assert db.connection.is_connected()
    assert db.cursor is not None


def test_ModifyDB_insert_data(mocker):
    mock_connect = mocker.patch('mysql.connector.connect')
    mock_connect.return_value.is_connected.return_value = True

    db = ModifyDB()
    mock_cursor = mocker.Mock()
    db.cursor = mock_cursor
    mock_connect.return_value.commit.return_value = None

    table_name = "test_table"
    certificate_dict = {
        "entry_id": 1,
        "lot_id": "lot1",
        "contract_number": "contract1",
        "hop_name": "hop1",
        "crop_year": 2023,
        "alpha_acid": 5.5,
        "beta_acid": 4.5,
        "total_oil": 1.5,
        "cohumulone": 30.5
    }

    db.insert_data(table_name, certificate_dict)

    mock_cursor.execute.assert_called_once()
    mock_connect.return_value.commit.assert_called_once()
