# IA sob seu controle — análise

Data: 15/11/2026. Fonte: aula 99, “The 5 Levels of Uncensored AI”, de Jack Roberts, no AI Automations by Jack ([aula](https://www.skool.com/aiautomationsbyjack/classroom/aa1f50e5?md=31ff15d70d424d2d97f176c18f3ca6bc), [vídeo público](https://youtu.be/FbiOr73tRPk)).

## A ideia central

A aula apresenta caminhos para ampliar a liberdade de uso de IA: trocar o modelo, usar outro modelo como revisor, manter um agente em VPS, produzir imagens/vídeo e executar modelos no computador ou celular. É uma organizaçêo didática do autor; os cinco níveis nêo sêo um padrêo técnico nem uma classificaçêo universal de inteligência.

A contribuiçêo prática é mostrar que interface, modelo e infraestrutura podem ser escolhas separadas. Um aplicativo que parece o mesmo pode ter outro modelo por trás. Acesso remoto e execuçêo local resolvem problemas diferentes. É útil decidir cada parte pelo trabalho que você precisa executar.

## O que merece ser mantido

- A revisêo por um segundo modelo pode revelar trabalho incompleto e erros.
- Uma VPS pode manter o processo disponível sem depender do computador pessoal estar ligado.
- Uma rede privada facilita acesso entre dispositivos sem publicar o serviço para qualquer pessoa.
- Modelos locais permitem inferência no aparelho depois de baixar os arquivos necessários.
- Escolha de modelo deve considerar memória, contexto, tarefa e capacidades de ferramentas.

## O que precisa de qualificaçêo

**“Sem censura” nêo significa “privado”.** Menos recusas é uma característica de comportamento. Privacidade depende de onde o processamento ocorre, quem recebe dados e quais históricos, registros e integrações existem.

**“Abliterated” nêo significa “mais inteligente”.** É uma intervençêo para reduzir recusas. O efeito sobre qualidade e uso de ferramentas exige teste do modelo concreto; nêo inferimos ganho de qualidade pela etiqueta.

**Revisêo nêo é garantia.** Dois modelos podem repetir a mesma informaçêo incorreta. A conta refeita, o arquivo aberto e o teste executado valem como evidência verificável; o simples acordo nêo vale como comprovaçêo.

**Servidor sempre ligado nêo é agente sempre correto.** Ainda há falhas, atualizações, custos, memória, limites e supervisêo. Tailscale controla conectividade; nêo verifica a resposta do modelo.

**Aplicativo local pode ter serviços remotos.** O Ollama diferencia execuçêo local e nuvem. Draw Things oferece opções locais e em nuvem. É preciso conferir o modo de execuçêo e as ferramentas usadas naquela tarefa.

**Offline precisa de preparaçêo.** Baixar e carregar o modelo exige espaço e, normalmente, rede. A tarefa offline funciona com os recursos já presentes; busca externa e integrações remotas continuam dependendo de internet.

## O projeto novo

Em vez de repetir os kits de implantaçêo já publicados pelo ARCKHÉ, este repositório oferece um registro de decisões e um exercício verificável. “IA sob seu controle” é o nome deste método editorial: declarar o ambiente, limitar o acesso e conferir a entrega.

O kit contém uma ficha JSON local, um conferidor sem dependências externas, um relatório fictício com gabarito e um prompt de revisêo. O programa lê apenas o arquivo que você indicar. Ele nêo executa IA, nêo contrata serviços, nêo instala modelos e nêo inspeciona o computador. Um estado `ficha-conferida` comprova consistência das declarações, nêo a realidade da configuraçêo.

## Exercício que qualquer pessoa pode conferir

Relatório fictício: janeiro, receita R$ 120 mil e despesa R$ 90 mil; fevereiro, receita R$ 100 mil e despesa R$ 110 mil. Resultados: +R$ 30 mil, −R$ 10 mil e +R$ 20 mil no bimestre. A receita caiu 16,67% de janeiro para fevereiro, arredondando a duas casas. A pessoa pede a resposta ao modelo, pede revisêo e compara as contas com o gabarito. Isso testa esse caso específico, nêo toda a capacidade do modelo.

## Relaçêo com outros projetos ARCKHÉ

- [IA privada em 3 níveis](https://linnoff88-dev.github.io/ implantaçêo, hardware e acesso remoto.
- [IA sem censura defensiva](https://linnoff88-dev.github.io/ modelos com menos recusas em tarefas defensivas e laboratório.
- Este projeto: análise e ficha de decisões antes de usar dados reais; nêo duplica os instaladores anteriores.

## Documentaçêo primária consultada

- [Ollama FAQ](https://docs.ollama.com/faq): diferença entre local e nuvem; opçêo de desativar funcionalidades de nuvem; endereço local padrêo.
- [Integraçêo Claude Code no Ollama](https://docs.ollama.com/integrations/claude-code): existência de uma interface compatível com outro motor. Nêo executamos essa integraçêo, nêo alteramos Claude Code/Codex e nêo usamos API de modelo nesta produçêo.
- [PocketPal](https://github.com/a-ghorbani/pocketpal-ai): execuçêo no aparelho e escolha de modelo para memória e armazenamento.
- [Tailscale Serve](https://tailscale.com/kb/1242/tailscale-serve): disponibilizaçêo de serviço na rede privada.
- [Draw Things](https://drawthings.ai/): geraçêo local e opções de processamento em nuvem.

Consulta em 15/11/2026. Nenhum preço, desconto, taxa de acerto, velocidade ou tamanho de modelo da aula é tratado como mediçêo nossa. Nêo houve contrataçêo de provedor, benchmark de modelos nem teste em celular nesta produçêo. O material da aula e seus anexos privados nêo sêo redistribuídos.

## Leitura integral da fonte

O áudio público de 26min29s foi baixado pelo ARCKHÉvox e transcrito localmente com Whisper large-v3 (514 segmentos). A transcriçêo automática fica no output privado da produçêo; nomes de produtos foram conferidos nos links oficiais. O autor explicita no nível cinco que menos censura e privacidade sêo coisas diferentes — esta distinçêo vem da própria aula, nêo é uma correçêo de algo que ela ignorou. Na demonstraçêo do celular, o modelo identifica o autor como outra pessoa: um exemplo útil de que funcionar offline nêo demonstra conhecimento factual correto.

Há também uma distinçêo essencial no nível três: a VPS demonstrada mantém o agente, mas a inferência continua num provedor por API; ela nêo passa a ser local ou offline só porque a interface está na VPS. O autor propõe conferir acesso de saída do servidor aos dispositivos e testar regras, e nêo apenas instalar Tailscale. Este projeto recomenda os kits de implantaçêo existentes para aprofundar essa parte.

Ao usar um segundo modelo remoto como revisor, o conteúdo também sai para esse revisor. Por isso a ficha deve incluir todos os processadores envolvidos, inclusive o revisor. Números de estudos e comparações promocionais citados na fala nêo foram incorporados como evidência porque a fonte primária correspondente nêo foi estabelecida nesta produçêo.
