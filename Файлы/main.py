from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import sqlite3
from datetime import date
import random

from enter import Ui_Enter
from register import Ui_Reg
from menu import Ui_Menu
from client import Ui_Client
from coo import Ui_Coo
from oper import Ui_Oper
from bills import Ui_Bills
from clients import Ui_Clients
from coos import Ui_Coos
from Delete_Client import Ui_Delete_Client
from Delete_Coo import Ui_Delete_Coo
from Main_Oper import Ui_Main_Oper

db = sqlite3.connect('base.db')
sql = db.cursor()

app = QtWidgets.QApplication(sys.argv)
Enter = QtWidgets.QWidget()
ui = Ui_Enter()
ui.setupUi(Enter)
Enter.show()

def check():
	mail = ui.mail.text()
	pwd = ui.pwd.text()

	if len(mail.replace(' ','')) == 0:
		print()
	else:
		sql.execute(f'SELECT Login FROM Admins WHERE Login = "{mail}"')
		if sql.fetchone() is None:
			reg()
		else:
			for i in sql.execute(f'SELECT Password FROM Admins WHERE Login = "{mail}"'):
				_pwd = i[0]
			if str(_pwd) == pwd:
				Enter.close()
				menu()
			
def reg():
	global Reg
	Reg = QtWidgets.QWidget()
	ui = Ui_Reg()
	ui.setupUi(Reg)
	Enter.close()
	Reg.show()

	def enter():
		global Enter
		Enter = QtWidgets.QWidget()
		ui = Ui_Enter()
		ui.setupUi(Enter)
		Reg.close()
		Enter.show()

		def q():
			mail = ui.mail.text()
			pwd = ui.pwd.text()

			if len(mail.replace(' ','')) == 0:
				print()
			else:
				sql.execute(f'SELECT Login FROM Admins WHERE Login = "{mail}"')
				if sql.fetchone() is None:
					reg()
				else:
					for i in sql.execute(f'SELECT Password FROM Admins WHERE Login = "{mail}"'):
						_pwd = i[0]
					if str(_pwd) == pwd:
						Enter.close()
						menu()
		ui.mail.returnPressed.connect(q)
		ui.pwd.returnPressed.connect(q)
		ui.enter.clicked.connect(q)
		ui.reg.clicked.connect(reg)

	def check_reg():
		login = ui.login.text()
		pwd = ui.pwd.text()
		r_pwd = ui.pwd_rep.text()

		sql.execute(f'SELECT Login FROM Admins WHERE Login = "{login}"')
		if sql.fetchone() is None:
			if str(pwd) == str(r_pwd):
				sql.execute(f'INSERT INTO Admins VALUES(?, ?)', (login, pwd))
				db.commit()
				Reg.close()
				menu()
			else:
				ui.login.setText('')
				ui.pwd.setText('')
				ui.pwd_rep.setText('')
		else:
			enter()

	def looks_pwd():
		if ui.look_pwd.isChecked() == True:
			ui.pwd.setEchoMode(QtWidgets.QLineEdit.Normal)
		elif ui.look_pwd.isChecked() == False:
			ui.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
	def looks_pwd_rep():
		if ui.look_pwd_rep.isChecked() == True:
			ui.pwd_rep.setEchoMode(QtWidgets.QLineEdit.Normal)
		elif ui.look_pwd_rep.isChecked() == False:
			ui.pwd_rep.setEchoMode(QtWidgets.QLineEdit.Password)

	ui.login.returnPressed.connect(check_reg)
	ui.pwd.returnPressed.connect(check_reg)
	ui.pwd_rep.returnPressed.connect(check_reg)
	ui.reg.clicked.connect(check_reg)
	ui.look_pwd.clicked.connect(looks_pwd)
	ui.look_pwd_rep.clicked.connect(looks_pwd_rep)

def add_clients():
	global Client
	Client = QtWidgets.QWidget()
	ui = Ui_Client()
	ui.setupUi(Client)
	Menu.close()
	Client.show()
	ui.logs.setReadOnly(True)

	def add():
		fio = ui.fio.text()
		num = ui.num.text()
		adress = ui.adress.text()
		data_roz = ui.data_roz.text()
		data_pass = ui.data_pass.text()

		if len(fio.replace(' ','')) == 0:
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT Client_Name FROM Clients WHERE Client_Name = "{fio}"')
			if sql.fetchone() is None:
				for i in sql.execute('SELECT COUNT(Client_ID) from Clients'):
					_len = i[0]
				for i in sql.execute('SELECT COUNT(Account_ID) from Accounts'):
					_len1 = i[0]
				sql.execute(f'INSERT INTO Clients VALUES(?, ?, ?, ?, ?, ?)', (_len+1, fio, num, adress, data_roz, data_pass))
				sql.execute(f'INSERT INTO Accounts VALUES(?, ?, ?, ?)', (_len+1, _len1+1, random.randint(10000, 99999999), 0))
				db.commit()

				ui.fio.setText('')
				ui.num.setText('')
				ui.adress.setText('')
				ui.data_roz.setText('')
				ui.data_pass.setText('')
				ui.logs.setText('База данных обновлена!')
			else:
				ui.fio.setText('')
				ui.num.setText('')
				ui.adress.setText('')
				ui.data_roz.setText('')
				ui.data_pass.setText('')
				ui.logs.setText('')

	def back():
		Client.close()
		menu()

	ui.fio.returnPressed.connect(add)
	ui.num.returnPressed.connect(add)
	ui.adress.returnPressed.connect(add)
	ui.data_roz.returnPressed.connect(add)
	ui.data_pass.returnPressed.connect(add)
	ui.add_client.clicked.connect(add)
	ui.back.clicked.connect(back)

def add_coos():
	global Coo
	Coo = QtWidgets.QWidget()
	ui = Ui_Coo()
	ui.setupUi(Coo)
	Menu.close()
	Coo.show()
	ui.logs.setReadOnly(True)

	def add():
		fio = ui.fio.text()
		num = ui.num.text()
		func = ui.func.text()
		pwd = ui.pwd.text()
		pwd_rep = ui.pwd_rep.text()
		mail = ui.mail.text()

		if len(fio.replace(' ','')) == 0:
			ui.logs.setText('Ошибка')
		else:
			sql.execute(f'SELECT Employee_Name FROM Employees WHERE Employee_Name = "{fio}"')
			if sql.fetchone() is None:
				if pwd == pwd_rep:
					for i in sql.execute('SELECT COUNT(Employee_ID) from Employees'):
						_len = i[0]
					sql.execute(f'INSERT INTO Employees VALUES(?, ?, ?, ?, ?, ?)', (_len+1, fio, func, num, mail, pwd))
					db.commit()

					ui.fio.setText('')
					ui.num.setText('')
					ui.func.setText('')
					ui.pwd.setText('')
					ui.pwd_rep.setText('')
					ui.pwd_rep.setText('')
					ui.mail.setText('')
					ui.logs.setText('База данных обновлена!')
				else:
					ui.fio.setText('')
					ui.num.setText('')
					ui.func.setText('')
					ui.pwd.setText('')
					ui.pwd_rep.setText('')
					ui.pwd_rep.setText('')
					ui.mail.setText('')
					ui.logs.setText('Ошибка')
			else:
				ui.fio.setText('')
				ui.num.setText('')
				ui.func.setText('')
				ui.pwd.setText('')
				ui.pwd_rep.setText('')
				ui.pwd_rep.setText('')
				ui.mail.setText('')

	def back():
		Coo.close()
		menu()

	ui.fio.returnPressed.connect(add)
	ui.num.returnPressed.connect(add)
	ui.func.returnPressed.connect(add)
	ui.pwd.returnPressed.connect(add)
	ui.pwd_rep.returnPressed.connect(add)
	ui.mail.returnPressed.connect(add)
	ui.add.clicked.connect(add)
	ui.back.clicked.connect(back)

def check_oper():
	global Oper
	Oper = QtWidgets.QWidget()
	ui = Ui_Oper()
	ui.setupUi(Oper)
	Menu.close()
	Oper.show()
	ui.logs.setReadOnly(True)

	logs = 'ID операции | ID счета | Дата операции | Тип операции | Сумма операции'
	sql.execute('''SELECT * from Transactions''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}'

	ui.logs.setText(logs)

	def back():
		Oper.close()
		menu()

	ui.back.clicked.connect(back)

def bills():
	global Bills
	Bills = QtWidgets.QWidget()
	ui = Ui_Bills()
	ui.setupUi(Bills)
	Menu.close()
	Bills.show()
	ui.logs.setReadOnly(True)

	logs = 'ID счета | ID клиента | Номер счёта | Баланс'
	sql.execute('''SELECT * from Accounts''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]}'

	ui.logs.setText(logs)

	def back():
		Bills.close()
		menu()

	ui.back.clicked.connect(back)

def info_clients():
	global Clients
	Clients = QtWidgets.QWidget()
	ui = Ui_Clients()
	ui.setupUi(Clients)
	Menu.close()
	Clients.show()
	ui.logs.setReadOnly(True)

	logs = 'ID клиента | ФИО | Номер телефона | Адрес | Дата рождения | Пасспортные данные'
	sql.execute('''SELECT * from Clients''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}'

	ui.logs.setText(logs)

	def back():
		Clients.close()
		menu()

	ui.back.clicked.connect(back)

def info_coos():
	global Coos
	Coos = QtWidgets.QWidget()
	ui = Ui_Coos()
	ui.setupUi(Coos)
	Menu.close()
	Coos.show()
	ui.logs.setReadOnly(True)

	logs = 'ID сотрудника | ФИО | Должность | Номер телефона | Email | Пароль'
	sql.execute('''SELECT * from Employees''')
	for i in sql.fetchall():
		logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}'

	ui.logs.setText(logs)

	def back():
		Coos.close()
		menu()

	ui.back.clicked.connect(back)

def del_client():
	global Delete_Client
	Delete_Client = QtWidgets.QWidget()
	ui = Ui_Delete_Client()
	ui.setupUi(Delete_Client)
	Menu.close()
	Delete_Client.show()
	ui.logs.setReadOnly(True)

	def search():
		fio = ui.fio.text()

		if len(fio.replace(' ','')) == 0:
			ui.logs.setText('Ошибка')
		else:
			logs = 'ID клиента | ФИО | Номер телефона | Адрес | Дата рождения | Пасспортные данные'
			for i in sql.execute(f'SELECT * FROM Clients WHERE Client_Name = "{fio}"'):
				logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}'
			ui.logs.setText(logs)

	def delete():
		fio = ui.fio.text()

		if len(fio.replace(' ','')) == 0:
			ui.logs.setText('Ошибка')
		else:
			for i in sql.execute('SELECT COUNT(Client_ID) from Clients'):
				_len = i[0]
			for i in sql.execute(f'SELECT Client_ID FROM Clients WHERE Client_Name = "{fio}"'):
				_id = i[0]
			if _id == _len:
				sql.execute('''DELETE FROM Clients WHERE Client_Name = ?''', (fio,))
				db.commit()
			else:
				for i in range(_id, _len+1):
					sql.execute(f'UPDATE Clients SET Client_ID = {i-1} WHERE Client_ID = {i}')
					sql.execute('''DELETE FROM Clients WHERE Client_Name = ?''', (fio,))
					db.commit()

			ui.fio.setText('')
			ui.logs.setText('База данных обновлена')

	def back():
		Delete_Client.close()
		menu()

	ui.exit.clicked.connect(back)
	ui.fio.returnPressed.connect(search)
	ui.search.clicked.connect(search)
	ui.delete_client.clicked.connect(delete)

def del_coo():
	global Delete_Coo
	Delete_Coo = QtWidgets.QWidget()
	ui = Ui_Delete_Coo()
	ui.setupUi(Delete_Coo)
	Menu.close()
	Delete_Coo.show()
	ui.logs.setReadOnly(True)

	def search():
		fio = ui.lineFIO.text()

		if len(fio.replace(' ','')) == 0:
			ui.logs.setText('Ошибка')
		else:
			logs = 'ID сотрудника | ФИО | Должность | Номер телефона | Email | Пароль'
			for i in sql.execute(f'SELECT * FROM Employees WHERE Employee_Name = "{fio}"'):
				logs += f'\n{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}'
			ui.logs.setText(logs)

	def delete():
		fio = ui.lineFIO.text()

		if len(fio.replace(' ','')) == 0:
			ui.logs.setText('Ошибка')
		else:
			for i in sql.execute('SELECT COUNT(Employee_ID) from Employees'):
				_len = i[0]
			for i in sql.execute(f'SELECT Employee_ID FROM Employees WHERE Employee_Name = "{fio}"'):
				_id = i[0]
			if _id == _len:
				sql.execute('''DELETE FROM Employees WHERE Employee_Name = ?''', (fio,))
				db.commit()
			else:
				for i in range(_id, _len+1):
					sql.execute(f'UPDATE Employees SET Employee_ID = {i-1} WHERE Employee_ID = {i}')
					sql.execute('''DELETE FROM Employees WHERE Employee_Name = ?''', (fio,))
					db.commit()

			ui.lineFIO.setText('')
			ui.logs.setText('База данных обновлена')

	def back():
		Delete_Coo.close()
		menu()

	ui.back.clicked.connect(back)
	ui.lineFIO.returnPressed.connect(search)
	ui.search.clicked.connect(search)
	ui.delete_coo.clicked.connect(delete)

def main_oper():
	global Main_Oper
	Main_Oper = QtWidgets.QWidget()
	ui = Ui_Main_Oper()
	ui.setupUi(Main_Oper)
	Menu.close()
	Main_Oper.show()
	ui.tab_oper.setReadOnly(True)
	ui.tab_bill.setReadOnly(True)

	def make():
		id_client = ui.id_client.text()
		num_bill = ui.num_bill.text()
		type_oper = ui.type_oper.text()
		summa = ui.summa.text()
		logs = ui.tab_oper.toPlainText()

		if len(id_client.replace(' ','')) == 0:
			ui.tab_oper.setText('Ошибка')
		else:
			if int(type_oper) > 3:
				ui.tab_oper.setText('Ошибка')
			else:
				if int(type_oper) == 1:
					for i in sql.execute('SELECT COUNT(Transaction_ID) from Transactions'):
						_len = i[0]
					for i in sql.execute(f'SELECT Category_Name from Transaction_Categories WHERE Category_ID = {type_oper}'):
						_type = i[0]
					sql.execute(f'UPDATE Accounts SET Balance = Balance + {summa} WHERE Client_ID = "{id_client}"')
					sql.execute(f'INSERT INTO Transactions VALUES(?, ?, ?, ?, ?)', (_len+1, id_client, date.today(), _type, summa))
					db.commit()
					for i in sql.execute(f'SELECT Balance FROM Accounts WHERE Client_ID = "{id_client}"'):
						bal = i[0]
					logs += f'\nПополнение счета на {summa}'
					ui.tab_bill.setText(str(bal))
					ui.tab_oper.setText(logs)
					ui.id_client.setText('')
					ui.num_bill.setText('')
					ui.type_oper.setText('')
					ui.summa.setText('')
				elif int(type_oper) == 2: 
					for i in sql.execute('SELECT COUNT(Transaction_ID) from Transactions'):
						_len = i[0]
					for i in sql.execute(f'SELECT Category_Name from Transaction_Categories WHERE Category_ID = {type_oper}'):
						_type = i[0]
					sql.execute(f'UPDATE Accounts SET Balance = Balance - {summa} WHERE Client_ID = "{id_client}"')
					sql.execute(f'INSERT INTO Transactions VALUES(?, ?, ?, ?, ?)', (_len+1, id_client, date.today(), _type, summa))
					db.commit()
					for i in sql.execute(f'SELECT Balance FROM Accounts WHERE Client_ID = "{id_client}"'):
						bal = i[0]
					logs += f'\nСнятие счета на {summa}'
					ui.tab_bill.setText(str(bal))
					ui.tab_oper.setText(logs)
					ui.id_client.setText('')
					ui.num_bill.setText('')
					ui.type_oper.setText('')
					ui.summa.setText('')
				elif int(type_oper) == 3:
					for i in sql.execute('SELECT COUNT(Transaction_ID) from Transactions'):
						_len = i[0]
					for i in sql.execute(f'SELECT Category_Name from Transaction_Categories WHERE Category_ID = {type_oper}'):
						_type = i[0]
					sql.execute(f'UPDATE Accounts SET Balance = Balance - {summa} WHERE Client_ID = "{id_client}"')
					sql.execute(f'UPDATE Accounts SET Balance = Balance + {summa} WHERE Client_ID = "{num_bill}"')
					sql.execute(f'INSERT INTO Transactions VALUES(?, ?, ?, ?, ?)', (_len+1, id_client, date.today(), _type, summa))
					db.commit()
					for i in sql.execute(f'SELECT Balance FROM Accounts WHERE Client_ID = "{id_client}"'):
						bal = i[0]
					logs += f'\nПеревод на другой счет на {summa}'
					ui.tab_bill.setText(str(bal))
					ui.tab_oper.setText(logs)
					ui.id_client.setText('')
					ui.num_bill.setText('')
					ui.type_oper.setText('')
					ui.summa.setText('')

	def back():
		Main_Oper.close()
		menu()

	ui.back.clicked.connect(back)
	ui.id_client.returnPressed.connect(make)
	ui.num_bill.returnPressed.connect(make)
	ui.type_oper.returnPressed.connect(make)
	ui.summa.returnPressed.connect(make)
	ui.accept.clicked.connect(make)

def looks():
	if ui.look.isChecked() == True:
		ui.pwd.setEchoMode(QtWidgets.QLineEdit.Normal)
	elif ui.look.isChecked() == False:
		ui.pwd.setEchoMode(QtWidgets.QLineEdit.Password)

def exit():
	sys.exit(app.exec_())


def menu():
	global Menu
	Menu = QtWidgets.QWidget()
	ui = Ui_Menu()
	ui.setupUi(Menu)
	Menu.show()

	ui.add_client.clicked.connect(add_clients)
	ui.add_coo.clicked.connect(add_coos)
	ui.check_oper.clicked.connect(check_oper)
	ui.bills.clicked.connect(bills)
	ui.clients.clicked.connect(info_clients)
	ui.coos.clicked.connect(info_coos)
	ui.del_client.clicked.connect(del_client)
	ui.del_coo.clicked.connect(del_coo)
	ui.oper.clicked.connect(main_oper)
	ui.exit.clicked.connect(exit)
	ui.exit_2.clicked.connect(exit)



ui.mail.returnPressed.connect(check)
ui.pwd.returnPressed.connect(check)
ui.enter.clicked.connect(check)
ui.reg.clicked.connect(reg)
ui.look.clicked.connect(looks)


sys.exit(app.exec_())