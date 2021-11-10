from bot.bitcoin import Bitcoin

bitcoin = Bitcoin()
use_option = int(input('Deseja usar o programa: \n1. Sim\n2. Não\n'))
while use_option == 1:
    user_option = int(input('Digite a opção desejada:\n1. Grafico completo\n2. Grafico Simples\n3. Retorno percentual\n'))

    if user_option == 1:
        bitcoin._see_completed_data()
    elif user_option == 2:
        bitcoin._see_smaller_data()
    elif user_option == 3:
        bitcoin._see_percentual_return()
    
    use_option = int(input('Deseja usar o programa: \n1. Sim\n2. Não\n'))