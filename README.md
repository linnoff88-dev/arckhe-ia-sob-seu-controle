# IA sob seu controle

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Sua IA sob controle](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

Este Ã© um kit gratuito de decisÃ£o e verificaÃ§Ã£o para quem usa IA no trabalho. Ele separa duas escolhas: quem pode acessar os dados e quais pedidos o modelo aceita responder. O kit traz um exercÃ­cio com resposta conhecida, uma ficha preenchÃ­vel e um conferidor local para registrar suas decisÃµes. Para entender o assunto, basta ler; para executar o conferidor, vocÃª precisa de Python. Ele nÃ£o instala nem configura modelos de IA.

Este repo entrega um kit de decisÃ£o e verificaÃ§Ã£o. Ele ajuda vocÃª a avaliar privacidade, liberdade de resposta e qualidade separadamente. NÃ£o instala uma IA privada nem um modelo sem censura.

## Guia de uso

**https://linnoff88-dev.github.io/

## ComeÃ§ar

Python 3.10+ e Git, sem dependÃªncias externas.

```bash
git clone https://github.com/linnoff88-dev/ia-sob-seu-controle.git
cd ia-sob-seu-controle
python3 -m unittest discover -s tests -v
python3 scripts/conferir.py kit/exemplos/ficha.json
```

O exemplo comeÃ§a incompleto e retorna `invalida` (cÃ³digo 2). Abra `kit/exemplos/ficha.json` no editor: preencha o modelo e os campos e marque as evidÃªncias somente apÃ³s conferir. `revisar` (cÃ³digo 1) indica pendÃªncia; `ficha-conferida` (cÃ³digo 0) indica consistÃªncia declarada, nÃ£o certificaÃ§Ã£o. Os avisos continuam exigindo leitura. No Windows, `py` pode substituir `python3`.

## O processo, do inÃ­cio ao fim

1. Leia a [anÃ¡lise](docs/ANALISE.md) e escolha sua necessidade.
2. Preencha a [ficha](kit/exemplos/ficha.json) com a configuraÃ§Ã£o que pretende usar.
3. Execute a tarefa com o [relatÃ³rio fictÃ­cio](kit/exemplos/relatorio-ficticio.md) no aplicativo de IA escolhido.
4. Entregue os dados e o resultado ao [revisor](kit/prompts/revisor.md), e confira com a referÃªncia.
5. Se precisa de offline, teste com a rede desligada depois de baixar o modelo.
6. Registre as evidÃªncias e execute o conferidor.

## Limites

O conferidor apenas lÃª JSON local e valida as decisÃµes declaradas. NÃ£o inspeciona rede, modelo, hardware ou arquivos do usuÃ¡rio. NÃ£o mede qualidade da IA, nÃ£o garante ausÃªncia de vazamento e nÃ£o instala software. O cÃ³digo Ã© independente do idioma do guia; os exemplos e mensagens do kit estÃ£o em portuguÃªs.


MIT para o cÃ³digo e textos autorais deste projeto. Marcas e materiais externos pertencem aos respectivos autores.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>