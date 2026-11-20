# AI under your control

[![Your AI under your control](guia/assets/banner-en.jpg)](https://inematds.github.io/ia-sob-seu-controle/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

This is a free decision and verification kit for people who use AI at work. It separates two choices: who can access the data and which requests the model agrees to answer. The kit includes an exercise with a known answer, a fillable form, and a local checker for recording your decisions. You only need to read to understand the subject; to run the checker, you need Python. It does not install or configure AI models.

This repo provides a decision and verification kit. It helps you assess privacy, freedom of response, and quality separately. It does not install a private AI or an uncensored model.

## User guide

**https://inematds.github.io/ia-sob-seu-controle/guia/en/**

## Getting started

Python 3.10+ and Git, with no external dependencies.

```bash
git clone https://github.com/inematds/ia-sob-seu-controle.git
cd ia-sob-seu-controle
python3 -m unittest discover -s tests -v
python3 scripts/conferir.py kit/exemplos/ficha.json
```

The example starts incomplete and returns `invalida` (code 2). Open `kit/exemplos/ficha.json` in an editor: fill in the model and fields, and mark evidence only after checking it. `revisar` (code 1) indicates something is pending; `ficha-conferida` (code 0) indicates declared consistency, not certification. The warnings still need to be read. On Windows, `py` can replace `python3`.

## The process from start to finish

1. Read the [analysis](../../docs/ANALISE.md) and choose what you need.
2. Fill in the [form](../../kit/exemplos/ficha.json) with the configuration you plan to use.
3. Run the task with the [fictional report](../../kit/exemplos/relatorio-ficticio.md) in your chosen AI app.
4. Give the data and result to the [reviewer](../../kit/prompts/revisor.md), then check against the reference.
5. If you need offline use, test with the network disconnected after downloading the model.
6. Record the evidence and run the checker.

## Limitations

The checker reads local JSON only and validates the decisions you declare. It does not inspect the network, model, hardware, or user files. It does not measure AI quality, guarantee there are no leaks, or install software. The code is independent of the guide language; the kit examples and messages are in Portuguese.


MIT license for the code and original texts in this project. Trademarks and external materials belong to their respective authors.
