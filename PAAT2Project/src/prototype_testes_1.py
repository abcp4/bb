import CPUTimer
import prototype_case5

def teste_case5(endereco, nome_do_teste):
    timer = CPUTimer.CPUTimer(0)
    result = 0
    iteracoes = 0
    
    tempo_total = 0
    timer.reset()
    timer.start()
    #print (tempo_total)
    while (tempo_total < 5000):
        timer.start()
        result = prototype_case5.branch_and_bound(endereco)
        timer.stop()
        tempo_total += timer.get_time("last", "ms")
        iteracoes += 1  
        timer.lap()
    timer.stop()
    # Imprimindo resultados de diversas formas
    print("Teste " + nome_do_teste)
    print("Resultado " + str(result))
    print("Tempo Total: " + str( timer.get_time() ) +" s")
    print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
    print("Iteracoes: " + str(iteracoes))
    print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
    print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
    print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )
    print("--------------------------------------------")
    print()

teste_case5("../inputs/nl01-40.txt", "nl01-40")
teste_case5("../inputs/nl01-41.txt", "nl01-41")
teste_case5("../inputs/nl01-42.txt", "nl01-42")
teste_case5("../inputs/nl01-43.txt", "nl01-43")
teste_case5("../inputs/nl01-44.txt", "nl01-44")
teste_case5("../inputs/nl01-45.txt", "nl01-45")
teste_case5("../inputs/nl01-46.txt", "nl01-46")
teste_case5("../inputs/nl01-47.txt", "nl01-47")
teste_case5("../inputs/nl01-48.txt", "nl01-48")
teste_case5("../inputs/nl01-49.txt", "nl01-49")
teste_case5("../inputs/nl01-50.txt", "nl01-50")
teste_case5("../inputs/nl01-51.txt", "nl01-51")