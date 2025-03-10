import re

ruta_log = r"C:\Users\306\Downloads\access.log"

regex_ip = re.compile(r"\b(?:\d{1,3}.){3}\d{1,3}\b")
regex_http_errors = re.compile(r"\b(4\d{2}|5\d{2})\b")

ips_unicas = set() errores_http = set()

LIMITE_RESULTADOS = 100

with open(ruta_log, "r", encoding="utf-8", errors="ignore") as f: for linea in f:

    if len(ips_unicas) < LIMITE_RESULTADOS:
        ips_unicas.update(regex_ip.findall(linea))

    if len(errores_http) < LIMITE_RESULTADOS:
        errores_http.update(regex_http_errors.findall(linea))

    if len(ips_unicas) >= LIMITE_RESULTADOS and len(errores_http) >= LIMITE_RESULTADOS:
        break
ips_mostradas = sorted(list(ips_unicas))[:LIMITE_RESULTADOS] errores_mostrados = sorted(list(errores_http))[:LIMITE_RESULTADOS]

print("IPs únicas encontradas:") print("\n".join(ips_mostradas))

print("\nCódigos de error HTTP encontrados:") print(", ".join(errores_mostrados))
