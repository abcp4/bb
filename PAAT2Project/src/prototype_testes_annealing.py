import CPUTimer
import annealing

def teste_case_annealing(endereco, nome_do_teste):
    timer = CPUTimer.CPUTimer(0)
    result = 0
    iteracoes = 0
    
    tempo_total = 0
    timer.reset()
    timer.start()
    #print (tempo_total)
    while (tempo_total < 5000):
        timer.start()
        result = annealing.teste(endereco)
        timer.stop()
        tempo_total += timer.get_time("last", "ms")
        iteracoes += 1  
        timer.lap()
    timer.stop()
    # Imprimindo resultados de diversas formas
    print("Teste " + nome_do_teste)
    print("Resultado " + str(result))
    print("Tempo Total: " + str( timer.get_time() ) +" s")
    print("Iteracoes: " + str(iteracoes)) 
    print("Tempo Medio: " + str( timer.get_time() / iteracoes ) +" s")
    print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
    print("Estampa do total: " + str( timer.get_stamp("total","clock") ) )
    print("---------------------------------------------")
    print("Para tabela")
    print(nome_do_teste + ";" + str(result[1]) + ";" + str(timer.get_time()) + ";" + str(iteracoes) + ";" + str(timer.get_time()/iteracoes))
    print("--------------------------------------------")
    print()
'''
teste_case_annealing("../inputs/nl01-40.txt", "nl01-40")
teste_case_annealing("../inputs/nl01-41.txt", "nl01-41")
teste_case_annealing("../inputs/nl01-42.txt", "nl01-42")
teste_case_annealing("../inputs/nl01-43.txt", "nl01-43")
teste_case_annealing("../inputs/nl01-44.txt", "nl01-44")
teste_case_annealing("../inputs/nl01-45.txt", "nl01-45")
teste_case_annealing("../inputs/nl01-46.txt", "nl01-46")
teste_case_annealing("../inputs/nl01-47.txt", "nl01-47")
teste_case_annealing("../inputs/nl01-48.txt", "nl01-48")
teste_case_annealing("../inputs/nl01-49.txt", "nl01-49")
teste_case_annealing("../inputs/nl01-50.txt", "nl01-50")
teste_case_annealing("../inputs/nl01-51.txt", "nl01-51")

teste_case_annealing("../inputs/bqp50-1.txt", "bqp50-1")
teste_case_annealing("../inputs/bqp50-2.txt", "bqp50-2")
teste_case_annealing("../inputs/bqp50-3.txt", "bqp50-3")
teste_case_annealing("../inputs/bqp50-4.txt", "bqp50-4")
teste_case_annealing("../inputs/bqp50-5.txt", "bqp50-5")
teste_case_annealing("../inputs/bqp50-6.txt", "bqp50-6")
teste_case_annealing("../inputs/bqp50-7.txt", "bqp50-7")
teste_case_annealing("../inputs/bqp50-8.txt", "bqp50-8")
teste_case_annealing("../inputs/bqp50-9.txt", "bqp50-9")
teste_case_annealing("../inputs/bqp50-10.txt", "bqp50-10")

teste_case_annealing("../inputs/bqp100-1.txt", "bqp100-1")
teste_case_annealing("../inputs/bqp100-2.txt", "bqp100-2")
teste_case_annealing("../inputs/bqp100-3.txt", "bqp100-3")
teste_case_annealing("../inputs/bqp100-4.txt", "bqp100-4")
teste_case_annealing("../inputs/bqp100-5.txt", "bqp100-5")
teste_case_annealing("../inputs/bqp100-6.txt", "bqp100-6")
'''
teste_case_annealing("../inputs/bqp100-7.txt", "bqp100-7")
'''
teste_case_annealing("../inputs/bqp100-8.txt", "bqp100-8")
teste_case_annealing("../inputs/bqp100-9.txt", "bqp100-9")
teste_case_annealing("../inputs/bqp100-10.txt", "bqp100-10")

teste_case_annealing("../inputs/bqp250-1.txt", "bqp250-1")
teste_case_annealing("../inputs/bqp250-2.txt", "bqp250-2")
teste_case_annealing("../inputs/bqp250-3.txt", "bqp250-3")
teste_case_annealing("../inputs/bqp250-4.txt", "bqp250-4")
teste_case_annealing("../inputs/bqp250-5.txt", "bqp250-5")
teste_case_annealing("../inputs/bqp250-6.txt", "bqp250-6")
teste_case_annealing("../inputs/bqp250-7.txt", "bqp250-7")
teste_case_annealing("../inputs/bqp250-8.txt", "bqp250-8")
teste_case_annealing("../inputs/bqp250-9.txt", "bqp250-9")
teste_case_annealing("../inputs/bqp250-10.txt", "bqp250-10")

teste_case_annealing("../inputs/bqp500-1.txt", "bqp500-1")
teste_case_annealing("../inputs/bqp500-2.txt", "bqp500-2")
teste_case_annealing("../inputs/bqp500-3.txt", "bqp500-3")
teste_case_annealing("../inputs/bqp500-4.txt", "bqp500-4")
teste_case_annealing("../inputs/bqp500-5.txt", "bqp500-5")
teste_case_annealing("../inputs/bqp500-6.txt", "bqp500-6")
teste_case_annealing("../inputs/bqp500-7.txt", "bqp500-7")
teste_case_annealing("../inputs/bqp500-8.txt", "bqp500-8")
teste_case_annealing("../inputs/bqp500-9.txt", "bqp500-9")
teste_case_annealing("../inputs/bqp500-10.txt", "bqp500-10")
'''