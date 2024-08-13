import subprocess

# Comando para ejecutar el servidor
server_process = subprocess.Popen(['python3', 'server.py'])

# Comando para ejecutar la app
app_process = subprocess.Popen(['python3', 'app.py'])

# Esperar a que ambos procesos terminen
server_process.wait()
app_process.wait()
