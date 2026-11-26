# IA sob seu controle

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Sua IA sob controle](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

Este êÂ© um kit gratuito de decisêÂ£o e verificaêÂ§êÂ£o para quem usa IA no trabalho. Ele separa duas escolhas: quem pode acessar os dados e quais pedidos o modelo aceita responder. O kit traz um exercêÂ­cio com resposta conhecida, uma ficha preenchêÂ­vel e um conferidor local para registrar suas decisêÂµes. Para entender o assunto, basta ler; para executar o conferidor, vocêÂª precisa de Python. Ele nêÂ£o instala nem configura modelos de IA.

Este repo entrega um kit de decisêÂ£o e verificaêÂ§êÂ£o. Ele ajuda vocêÂª a avaliar privacidade, liberdade de resposta e qualidade separadamente. NêÂ£o instala uma IA privada nem um modelo sem censura.

## Guia de uso

**https://linnoff88-dev.github.io/

## ComeêÂ§ar

Python 3.10+ e Git, sem dependêÂªncias externas.

```bash
git clone https://github.com/linnoff88-dev/ia-sob-seu-controle.git
cd ia-sob-seu-controle
python3 -m unittest discover -s tests -v
python3 scripts/conferir.py kit/exemplos/ficha.json
```

O exemplo comeêÂ§a incompleto e retorna `invalida` (cêÂ³digo 2). Abra `kit/exemplos/ficha.json` no editor: preencha o modelo e os campos e marque as evidêÂªncias somente apêÂ³s conferir. `revisar` (cêÂ³digo 1) indica pendêÂªncia; `ficha-conferida` (cêÂ³digo 0) indica consistêÂªncia declarada, nêÂ£o certificaêÂ§êÂ£o. Os avisos continuam exigindo leitura. No Windows, `py` pode substituir `python3`.

## O processo, do inêÂ­cio ao fim

1. Leia a [anêÂ¡lise](docs/ANALISE.md) e escolha sua necessidade.
2. Preencha a [ficha](kit/exemplos/ficha.json) com a configuraêÂ§êÂ£o que pretende usar.
3. Execute a tarefa com o [relatêÂ³rio fictêÂ­cio](kit/exemplos/relatorio-ficticio.md) no aplicativo de IA escolhido.
4. Entregue os dados e o resultado ao [revisor](kit/prompts/revisor.md), e confira com a referêÂªncia.
5. Se precisa de offline, teste com a rede desligada depois de baixar o modelo.
6. Registre as evidêÂªncias e execute o conferidor.

## Limites

O conferidor apenas lêÂª JSON local e valida as decisêÂµes declaradas. NêÂ£o inspeciona rede, modelo, hardware ou arquivos do usuêÂ¡rio. NêÂ£o mede qualidade da IA, nêÂ£o garante ausêÂªncia de vazamento e nêÂ£o instala software. O cêÂ³digo êÂ© independente do idioma do guia; os exemplos e mensagens do kit estêÂ£o em portuguêÂªs.


MIT para o cêÂ³digo e textos autorais deste projeto. Marcas e materiais externos pertencem aos respectivos autores.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>