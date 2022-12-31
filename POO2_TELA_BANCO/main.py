import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from tela_deposite import tela_deposito
from tela_cadastro import tela_cadastro
from tela_inicial_banco import tela_inicial_banco
from tela_extrato import tela_extrato
from tela_transf import tela_transf
from tela_saque import tela_saque
from tela_usuario import tela_usuario
from BANK import *

conta_atual = ''
class UiMain(QtWidgets.QWidget):

    def setupUi(self,UiMain):
        UiMain.setObjectName("UiMain")
        UiMain.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_inicial = tela_inicial_banco()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_usuario = tela_usuario()
        self.tela_usuario.setupUi(self.stack2)

        self.tela_extrato = tela_extrato()
        self.tela_extrato.setupUi(self.stack3)

        self.tela_deposito = tela_deposito()
        self.tela_deposito.setupUi(self.stack4)

        self.tela_saque = tela_saque()
        self.tela_saque.setupUi(self.stack5)

        self.tela_transfere = tela_transf()
        self.tela_transfere.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, UiMain):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.b = Banco()
        # Interação tela inicial para tela de cadastro ou para a tela de usuario já cadastrado
        self.tela_inicial.pushButton.clicked.connect(self.botao_login)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_3.clicked.connect(self.sairTelaInicial)
        # Interação de voltar da tela de cadastro para tela inicial
        self.tela_cadastro.pushButton.clicked.connect(self.botao_cadastra)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltarTelaInicial)
        

        # Tela pós-login onde conecta para tela de  extrato, transferência, deposito, saque, e retorna para tela inicial
        self.tela_usuario.pushButton.clicked.connect(self.abrirTelaDeposito)
        self.tela_usuario.pushButton_2.clicked.connect(self.abrirTelaTransfere)
        self.tela_usuario.pushButton_3.clicked.connect(self.abrirTelaSaque)
        self.tela_usuario.pushButton_4.clicked.connect(self.abrirTelaExtrato)
        self.tela_usuario.pushButton_5.clicked.connect(self.voltarTelaInicial)
        self.tela_usuario.pushButton_6.clicked.connect(self.sairTelaUsuario)
        self.tela_usuario.Ocultar_button.clicked.connect(self.mostra_Saldo)
        # Tela de extrato que volta para tela de login ou para tela de usuario
        self.tela_extrato.pushButton.clicked.connect(self.voltarTelaUsuario)

        # Tela de transferência que volta para tela de login ou para tela de usuario
        self.tela_transfere.pushButton.clicked.connect(self.botao_transf)
        self.tela_transfere.pushButton_2.clicked.connect(self.voltarTelaUsuario)

        # Tela de saque que volta para tela de login ou para tela de usuario
        self.tela_saque.pushButton.clicked.connect(self.botao_saque)
        self.tela_saque.pushButton_2.clicked.connect(self.voltarTelaUsuario)        
        
		# Tela de deposito que volta para tela de login ou para tela de usuario
        self.tela_deposito.pushButton.clicked.connect(self.botao_deposito)
        self.tela_deposito.pushButton_2.clicked.connect(self.voltarTelaUsuario)
        
    def atualiza_tela_principal(self,l):             
        self.tela_usuario.Mensagem_user.setText(f'SEJA BEM-VINDO: {(self.b.contas[l].get_titular).get_nome}  Nº{self.b.contas[l].get_numero}')
        self.tela_usuario.Saldo_set.setText('******')

    def mostra_Saldo(self):
        if self.tela_usuario.Saldo_set.text() == '******':
            self.tela_usuario.Ocultar_button
            self.tela_usuario.Saldo_set.setText(f'{self.b.contas[conta_atual].saldo}')
        else:
            self.tela_usuario.Saldo_set.setText('******')
            self.tela_usuario.Ocultar_button
    
    def botao_saque(self):
        senha = self.tela_saque.lineEdit_2.text()
        valor = self.tela_saque.lineEdit.text()
        if not(senha == '' and valor == ''):
            if self.b.contas[conta_atual].saque(float(valor), senha):
                QMessageBox().information(None,'IgBank','Saque realizado com sucesso!')
                self.tela_saque.lineEdit.setText('')
                self.tela_saque.lineEdit_2.setText('')
                if not(self.tela_usuario.Saldo_set.text() == '******'):
                    self.tela_usuario.Saldo_set.setText(f'{self.b.contas[conta_atual].saldo}')
            else:
                QMessageBox().warning(None,'IgBank','Falha na operação!')
        else:
            QMessageBox().warning(None,'IgBank','Todos os dados devem ser preenchidos!')
    
    def botao_deposito(self):
        valor = self.tela_deposito.lineEdit.text()
        if not(valor == ''):
            if self.b.contas[conta_atual].deposita(float(valor)):
                QMessageBox().information(None,'IgBank','Depósito realizado com sucesso!')
                self.tela_deposito.lineEdit.setText('')
                if not(self.tela_usuario.Saldo_set.text() == '******'):
                    self.tela_usuario.Saldo_set.setText(f'{self.b.contas[conta_atual].saldo}')
            else:
                QMessageBox().warning(None,'IgBank','Falha na operação!')
        else:
            QMessageBox().warning(None,'IgBank','Todos os dados devem ser preenchidos!')
    
    def botao_transf(self):
        senha = self.tela_transfere.lineEdit_3.text()
        valor = self.tela_transfere.lineEdit_2.text()
        destino = self.tela_transfere.lineEdit.text()

        if not(senha == '' or valor == '' or destino == ''):
            if not(self.b.busca_conta(destino) == None):
                destino = self.b.busca_conta(destino)
                if self.b.contas[conta_atual].transfere(destino,float(valor),senha):
                    QMessageBox().information(None,'IgBank','Transferência realizada com sucesso!')
                    self.tela_transfere.lineEdit_3.setText('')
                    self.tela_transfere.lineEdit_2.setText('')
                    self.tela_transfere.lineEdit.setText('')
                    if not(self.tela_usuario.Saldo_set.text() == '******'):
                        self.tela_usuario.Saldo_set.setText(f'{self.b.contas[conta_atual].saldo}')
                else:
                    QMessageBox().information(None,'IgBank','Falha na operação!')
            else:
                QMessageBox().warning(None,'IgBank','Conta não encontrada!')
        else:
            QMessageBox().warning(None,'IgBank','Todos os dados devem ser preenchidos!')
     
    def botao_cadastra(self):
        nome = self.tela_cadastro.lineEdit_3.text()
        cpf = self.tela_cadastro.lineEdit_4.text()
        login = self.tela_cadastro.lineEdit.text()
        senha = self.tela_cadastro.lineEdit_2.text()

        if not(nome == '' or senha == '' or cpf == '' or login == ''):
            c = Cliente(nome,cpf)

            cc = Conta(gera_numero(self.b),c,senha,login)
            if self.b.adiciona_cliente(c,cpf) and self.b.adiciona_conta(cc,login):
                QMessageBox().information(None,'IgBank',f'Cadastro realizado com sucesso!\nSeu número da conta é: {cc.get_numero}')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
            else:
                QMessageBox().warning(None,'IgBank','CPF já cadastrado na base de dados!')
                    
        else:
            QMessageBox().warning(None,'IgBank','Todos os dados devem ser preenchidos!')
    
    def botao_login(self):
        login = self.tela_inicial.lineEdit.text()
        senha = self.tela_inicial.lineEdit_2.text()

        if not(login == '' or senha == ''):
            if confirma_login(login,senha,self.b):
                global conta_atual
                conta_atual = login
                QMessageBox().information(None,'IgBank','Login Realizado com Sucesso!')
                self.abrirTelaUsuario(login)
                
            else:
                QMessageBox().warning(None,'IgBank','Login/Senha incorreto!')    
        else:
            QMessageBox().warning(None,'IgBank','Todos os dados devem ser preenchidos!')
    
   
    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirTelaInicialBanco(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirTelaUsuario(self, l):
        self.QtStack.setCurrentIndex(2)
        self.atualiza_tela_principal(l)
    def abrirTelaExtrato(self):
        self.QtStack.setCurrentIndex(3)
        QMessageBox().information(None,'IgBank','Extrato gerado!')
        self.tela_extrato.Texto_extrato.setText((self.b.contas[conta_atual].get_historico).imprime())
    def abrirTelaDeposito(self):
        self.QtStack.setCurrentIndex(4)
    def abrirTelaSaque(self):
        self.QtStack.setCurrentIndex(5)
    def abrirTelaTransfere(self):
        self.QtStack.setCurrentIndex(6)
	
    def sairTelaUsuario(self):
        sys.exit(app.exec_())
    def sairTelaInicial(self):
        sys.exit(app.exec_())
    def voltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)
    def voltarTelaUsuario(self):
        self.QtStack.setCurrentIndex(2)
		
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    show_main = Main()
    
    sys.exit(app.exec_())        
