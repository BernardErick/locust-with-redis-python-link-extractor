import subprocess
import time
import os
import argparse

# Crie um analisador de argumentos para lidar com os parâmetros -type e --cache
parser = argparse.ArgumentParser()
parser.add_argument("-type", type=str, default="none")  # Valor padrão para -type
parser.add_argument("--cache", action="store_true", default=False)  # Parâmetro --cache, padrão False
args = parser.parse_args()

# Comando base
base_command = "locust -f locustfile.py --csv=results --headless --run-time 180"

# Configurações de usuários (-u), taxa de spawn (-r) e tempo de execução (--run-time)
# Aviso: Colocar o spawn rate sempre em FLOAT
user_rates = [(100, 10.0, 240), (1000, 10.0, 240), (10000, 10.0, 240)]

# Loop iterativo
for step in range(1, 4):
    print(f"Iniciando cenário de testes {step}")
    num_users, spawn_rate, run_time = user_rates[step - 1]
    
    # Construir o comando completo com as configurações atuais e o parâmetro -type
    command = f"{base_command} -u {num_users} -r {spawn_rate} --run-time {run_time}"
    
    try:
        # Executa o comando
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Lidar com erros se o comando não puder ser executado
        print(f"Erro ao executar o comando: {e}")

    # Determina o sufixo do nome do arquivo com base na presença ou ausência do parâmetro --cache
    cache_suffix = "cache" if args.cache else "nocache"
    csv_name = f"{num_users}_users_for_spawn_rate_{spawn_rate}_run_time_{run_time}_results_stats.csv"
    
    if os.path.exists(csv_name):
        csv_name_with_type = f"{cache_suffix}_{args.type}_{csv_name}"
        os.rename(csv_name, csv_name_with_type)
    
    print("Intervalo de 1 minuto acontecendo..")
    time.sleep(60)
