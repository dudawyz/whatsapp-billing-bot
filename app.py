
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open("https://web.whatsapp.com/")
sleep(15)

workbook = openpyxl.load_workbook("clientes chat bot.xlsx")
pagina_clientes = workbook['Planilha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f"Olá {nome}, seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no pix: SEU-PIX-AQUI"


    try: 
        link_mensagem_whatsapp = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
        webbrowser.open(link_mensagem_whatsapp)
        sleep(15)          # aguarda o WhatsApp Web carregar
        pyautogui.press('enter')  # envia a mensagem
        sleep(3)
        pyautogui.hotkey('ctrl', 'w')  # fecha o tab
    except Exception as e:
        print(f"Erro real: {e}")
        print(f"Não foi possível enviar mensagem para {nome}")

