import pyautogui as robo
import time

def envio():
    try:
        
        print('Iniciando envio...')
        links = [] # https://wa.me/554399999999
        msg = 'Mensagens a ser enviada'
        arq = '' # Arquivo a ser enviado
        for x in range(len(links)):
            print(x)
            robo.moveTo(27, 1046) 
            robo.click()
            robo.write('executar') 
            robo.press('enter')
            time.sleep(2)            
            robo.write(links[x]) 
            # time.sleep(2)
            robo.press('enter')
            time.sleep(3)
            x_erro = valida_imagem()
            if(not x_erro):
                if(len(arq) > 0):
                    robo.moveTo(1779, 1002)#Seleciona Documentos            
                    time.sleep(1)
                    robo.click()
                    time.sleep(2)    
                    robo.press('tab')
                    robo.press('down', presses=2)
                    robo.press('enter')
                    time.sleep(2)
                    robo.write(arq,interval=0.25) #Informa o arquivo
                    time.sleep(1)
                    robo.press('enter')
                    time.sleep(1)
                    robo.write(msg,interval=0.10) #Digita msg e envia
                    robo.press('enter')
                    time.sleep(2)
                    robo.hotkey('esc')
                else:
                    robo.write(msg,interval=0.10) #Digita msg e envia
                    robo.press('enter')
                    time.sleep(2)
                    robo.hotkey('esc')

            else:
                robo.moveTo(2044,549)
                robo.click()

                
        print('Fim Envio')
    except Exception as err:
        print(err)


def posicao_mouse():
    time.sleep(3)
    x, y = robo.position()
    print(x, y)
# Valida se há uma mensagem informando que o número não é WhastApp
def valida_imagem():
    try:
        robo.locateOnScreen('img/numero_errado.png',region=(1701,446,190, 100))           
        robo.moveTo(2044,549)
        robo.click()
        return True
    except Exception as err:
        print(err)
        return False

if __name__ == "__main__":
    # Start processo
    envio()

