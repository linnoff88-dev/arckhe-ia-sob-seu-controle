# IA bajo tu control

[![Tu IA bajo control](guia/assets/banner-es.jpg)](https://inematds.github.io/ia-sob-seu-controle/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Este es un kit gratuito de decisión y verificación para quienes usan IA en el trabajo. Separa dos decisiones: quién puede acceder a los datos y qué solicitudes acepta responder el modelo. El kit incluye un ejercicio con una respuesta conocida, una ficha para completar y un verificador local para registrar tus decisiones. Para entender el tema, basta con leer; para ejecutar el verificador, necesitas Python. No instala ni configura modelos de IA.

Este repo ofrece un kit de decisión y verificación. Te ayuda a evaluar por separado la privacidad, la libertad de respuesta y la calidad. No instala una IA privada ni un modelo sin censura.

## Guía de uso

**https://inematds.github.io/ia-sob-seu-controle/guia/es/**

## Empezar

Python 3.10+ y Git, sin dependencias externas.

```bash
git clone https://github.com/inematds/ia-sob-seu-controle.git
cd ia-sob-seu-controle
python3 -m unittest discover -s tests -v
python3 scripts/conferir.py kit/exemplos/ficha.json
```

El ejemplo empieza incompleto y devuelve `invalida` (código 2). Abre `kit/exemplos/ficha.json` en un editor: completa el modelo y los campos, y marca las evidencias solo después de verificarlas. `revisar` (código 1) indica que hay algo pendiente; `ficha-conferida` (código 0) indica coherencia declarada, no una certificación. Aún hay que leer los avisos. En Windows, `py` puede sustituir a `python3`.

## El proceso, de principio a fin

1. Lee el [análisis](../../docs/ANALISE.md) y elige lo que necesitas.
2. Completa la [ficha](../../kit/exemplos/ficha.json) con la configuración que pretendes usar.
3. Ejecuta la tarea con el [informe ficticio](../../kit/exemplos/relatorio-ficticio.md) en la aplicación de IA que hayas elegido.
4. Entrega los datos y el resultado al [revisor](../../kit/prompts/revisor.md) y compáralos con la referencia.
5. Si necesitas trabajar sin conexión, haz la prueba con la red desconectada después de descargar el modelo.
6. Registra las evidencias y ejecuta el verificador.

## Límites

El verificador solo lee JSON local y valida las decisiones declaradas. No inspecciona la red, el modelo, el hardware ni los archivos del usuario. No mide la calidad de la IA, no garantiza que no haya filtraciones y no instala software. El código es independiente del idioma de la guía; los archivos del kit y sus mensajes están en portugués (en portugués).


MIT para el código y los textos originales de este proyecto. Las marcas y los materiales externos pertenecen a sus respectivos autores.
