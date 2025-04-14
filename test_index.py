import unittest
from unittest.mock import patch, MagicMock, ANY
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys

from main import Login, MainApp

app = QApplication(sys.argv)

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = Login()

    @patch('index.MySQLdb.connect')
    def test_successful_login(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, 'user1', 'email@example.com', 'pass123')
        ]
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.login.lineEdit.setText('user1')
        self.login.lineEdit_2.setText('pass123')

        self.login.Handel_Login()

        self.assertTrue(hasattr(self.login, 'window2'))
        self.assertIsInstance(self.login.window2, MainApp)

    @patch('index.MySQLdb.connect')
    def test_failed_login(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, 'user1', 'email@example.com', 'pass123')
        ]
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.login.lineEdit.setText('user1')
        self.login.lineEdit_2.setText('wrongpass')

        self.login.Handel_Login()

        self.assertEqual(
            self.login.label.text(),
            'Make Sure You Enterd Your Username And Password Correctly'
        )

class TestMainAppFull(unittest.TestCase):
    def setUp(self):
        self.main = MainApp()

    @patch('index.MySQLdb.connect')
    def test_edit_books(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_8.setText("Edited Book")
        self.main.textEdit_2.setPlainText("New Desc")
        self.main.lineEdit_7.setText("EDIT123")
        self.main.comboBox_7.currentText = MagicMock(return_value="NewCat")
        self.main.comboBox_8.currentText = MagicMock(return_value="NewAuth")
        self.main.comboBox_6.currentText = MagicMock(return_value="NewPub")
        self.main.lineEdit_6.setText("99")
        self.main.lineEdit_5.setText("Test Book")
        self.main.Edit_Books()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.QMessageBox.warning', return_value=QMessageBox.Yes)
    @patch('index.MySQLdb.connect')
    def test_delete_books(self, mock_connect, mock_msgbox):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_5.setText("Book To Delete")
        self.main.Delete_Books()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.MySQLdb.connect')
    def test_add_new_client(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_22.setText("Client")
        self.main.lineEdit_23.setText("client@test.com")
        self.main.lineEdit_24.setText("12345")
        self.main.Add_New_Client()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.MySQLdb.connect')
    def test_edit_client(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_25.setText("12345")
        self.main.lineEdit_28.setText("Updated Name")
        self.main.lineEdit_27.setText("new@email.com")
        self.main.lineEdit_26.setText("54321")
        self.main.Edit_Client()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.QMessageBox.warning', return_value=QMessageBox.Yes)
    @patch('index.MySQLdb.connect')
    def test_delete_client(self, mock_connect, mock_msgbox):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_25.setText("54321")
        self.main.Delete_Client()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.MySQLdb.connect')
    def test_add_new_user(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_9.setText("newuser")
        self.main.lineEdit_10.setText("new@user.com")
        self.main.lineEdit_11.setText("123")
        self.main.lineEdit_12.setText("123")
        self.main.Add_New_User()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.MySQLdb.connect')
    def test_add_category(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_19.setText("NewCat")
        self.main.Add_Category()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.MySQLdb.connect')
    def test_add_author(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_20.setText("AuthorName")
        self.main.Add_Author()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.MySQLdb.connect')
    def test_add_publisher(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit_21.setText("PubName")
        self.main.Add_Publisher()
        mock_cursor.execute.assert_any_call(ANY, ANY)

    @patch('index.MySQLdb.connect')
    def test_day_operation_insert(self, mock_connect):
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        mock_db.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_db

        self.main.lineEdit.setText("Book")
        self.main.lineEdit_29.setText("Client")
        self.main.comboBox.currentText = MagicMock(return_value="Borrow")
        self.main.comboBox_2.currentIndex = MagicMock(return_value=2)

        self.main.Handel_Day_Operations()
        mock_cursor.execute.assert_any_call(ANY, ANY)
        mock_db.commit.assert_called_once()
