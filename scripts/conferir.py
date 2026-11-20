#!/usr/bin/env python3
"""Lê uma ficha local; não abre rede nem executa o modelo. Python 3.10+."""
import argparse
import json
from pathlib import Path

CAMPOS = {
    "dados": ("sinteticos", "publicos", "confidenciais"),
    "execucao": ("local", "vps", "provedor"),
    "ferramentas": ("nenhuma", "leitura", "escrita"),
    "revisao": ("humana", "segundo-modelo", "nenhuma"),
    "acesso": ("somente-dispositivo", "rede-privada", "internet"),
}
EVIDENCIAS = ("sem_rede", "resultado_conferido", "permissoes_conferidas")

def conferir(ficha):
    erros, faltas, avisos = [], [], []
    if not isinstance(ficha, dict):
        return {"estado": "invalida", "erros": ["A ficha precisa ser um objeto JSON."], "faltas": [], "avisos": []}
    for campo, opcoes in CAMPOS.items():
        if ficha.get(campo) not in opcoes:
            erros.append(campo + ": escolha " + ", ".join(opcoes))
    for campo in ("objetivo", "modelo"):
        if not isinstance(ficha.get(campo), str) or not ficha[campo].strip() or ficha[campo].startswith("preencher"):
            erros.append(campo + ": preencha com o valor real.")
    if type(ficha.get("offline_necessario")) is not bool:
        erros.append("offline_necessario: use true ou false.")
    ev = ficha.get("evidencias")
    if not isinstance(ev, dict):
        erros.append("evidencias: objeto obrigatório.")
        ev = {}
    for nome in EVIDENCIAS:
        if type(ev.get(nome)) is not bool:
            erros.append("evidencias." + nome + ": use true ou false.")
    if erros:
        return {"estado": "invalida", "erros": erros, "faltas": [], "avisos": []}
    if ficha["offline_necessario"] and ficha["execucao"] != "local":
        faltas.append("Offline exige executar no próprio dispositivo, com modelo já baixado.")
    if ficha["offline_necessario"] and not ev["sem_rede"]:
        faltas.append("Falta registrar o teste com a rede desligada.")
    if not ev["resultado_conferido"]:
        faltas.append("Falta conferir o resultado contra dados ou testes de referência.")
    if not ev["permissoes_conferidas"]:
        faltas.append("Falta conferir ferramentas, arquivos e acessos concedidos.")
    if ficha["revisao"] == "nenhuma":
        faltas.append("Defina quem vai revisar o resultado.")
    if ficha["revisao"] == "segundo-modelo":
        avisos.append("Dois modelos podem repetir o mesmo erro; confira com dados ou testes independentes.")
    if ficha["dados"] == "confidenciais" and ficha["execucao"] != "local":
        avisos.append("Dados sairão do dispositivo. Confira retenção, região e contrato do serviço antes de enviar.")
    if ficha["acesso"] == "internet":
        avisos.append("Há acesso pela internet. Confira autenticação e exposição; rede privada restringe o acesso.")
    if ficha["ferramentas"] == "escrita":
        avisos.append("Permissão de escrita: use cópia de trabalho, limite de pasta e revisão das alterações.")
    if ficha["execucao"] == "vps":
        avisos.append("VPS mantém o serviço disponível enquanto o servidor funciona; exige manutenção e custo recorrente.")
    return {"estado": "revisar" if faltas else "ficha-conferida", "erros": [], "faltas": faltas, "avisos": avisos,
            "limite": "Verifica apenas a consistência da ficha declarada; não comprova a configuração real, privacidade ou qualidade do modelo."}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ficha", type=Path)
    args = ap.parse_args()
    try:
        resultado = conferir(json.loads(args.ficha.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        print(json.dumps({"estado": "invalida", "erros": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 2 if resultado["erros"] else (1 if resultado["faltas"] else 0)

if __name__ == "__main__":
    raise SystemExit(main())
