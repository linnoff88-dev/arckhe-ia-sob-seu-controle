# IA sob seu controle — análise

Data: 15/11/2026. Fonte: aula 99, “The 5 Levels of Uncensored AI”, de Jack Roberts, no AI Automations by Jack ([aula](https://www.skool.com/aiautomationsbyjack/classroom/aa1f50e5?md=31ff15d70d424d2d97f176c18f3ca6bc), [vídeo público](https://youtu.be/FbiOr73tRPk)).

## A ideia central

A aula apresenta caminhos para ampliar a liberdade de uso de IA: trocar o modelo, usar outro modelo como revisor, manter um agente em VPS, produzir imagens/vídeo e executar modelos no computador ou celular. É uma organização didática do autor; os cinco níveis não são um padrão técnico nem uma classificação universal de inteligência.

A contribuição prática é mostrar que interface, modelo e infraestrutura podem ser escolhas separadas. Um aplicativo que parece o mesmo pode ter outro modelo por trás. Acesso remoto e execução local resolvem problemas diferentes. É útil decidir cada parte pelo trabalho que você precisa executar.

## O que merece ser mantido

- A revisão por um segundo modelo pode revelar trabalho incompleto e erros.
- Uma VPS pode manter o processo disponível sem depender do computador pessoal estar ligado.
- Uma rede privada facilita acesso entre dispositivos sem publicar o serviço para qualquer pessoa.
- Modelos locais permitem inferência no aparelho depois de baixar os arquivos necessários.
- Escolha de modelo deve considerar memória, contexto, tarefa e capacidades de ferramentas.

## O que precisa de qualificação

**“Sem censura” não significa “privado”.** Menos recusas é uma característica de comportamento. Privacidade depende de onde o processamento ocorre, quem recebe dados e quais históricos, registros e integrações existem.

**“Abliterated” não significa “mais inteligente”.** É uma intervenção para reduzir recusas. O efeito sobre qualidade e uso de ferramentas exige teste do modelo concreto; não inferimos ganho de qualidade pela etiqueta.

**Revisão não é garantia.** Dois modelos podem repetir a mesma informação incorreta. A conta refeita, o arquivo aberto e o teste executado valem como evidência verificável; o simples acordo não vale como comprovação.

**Servidor sempre ligado não é agente sempre correto.** Ainda há falhas, atualizações, custos, memória, limites e supervisão. Tailscale controla conectividade; não verifica a resposta do modelo.

**Aplicativo local pode ter serviços remotos.** O Ollama diferencia execução local e nuvem. Draw Things oferece opções locais e em nuvem. É preciso conferir o modo de execução e as ferramentas usadas naquela tarefa.

**Offline precisa de preparação.** Baixar e carregar o modelo exige espaço e, normalmente, rede. A tarefa offline funciona com os recursos já presentes; busca externa e integrações remotas continuam dependendo de internet.

## O projeto novo

Em vez de repetir os kits de implantação já publicados pelo INEMA, este repositório oferece um registro de decisões e um exercício verificável. “IA sob seu controle” é o nome deste método editorial: declarar o ambiente, limitar o acesso e conferir a entrega.

O kit contém uma ficha JSON local, um conferidor sem dependências externas, um relatório fictício com gabarito e um prompt de revisão. O programa lê apenas o arquivo que você indicar. Ele não executa IA, não contrata serviços, não instala modelos e não inspeciona o computador. Um estado `ficha-conferida` comprova consistência das declarações, não a realidade da configuração.

## Exercício que qualquer pessoa pode conferir

Relatório fictício: janeiro, receita R$ 120 mil e despesa R$ 90 mil; fevereiro, receita R$ 100 mil e despesa R$ 110 mil. Resultados: +R$ 30 mil, −R$ 10 mil e +R$ 20 mil no bimestre. A receita caiu 16,67% de janeiro para fevereiro, arredondando a duas casas. A pessoa pede a resposta ao modelo, pede revisão e compara as contas com o gabarito. Isso testa esse caso específico, não toda a capacidade do modelo.

## Relação com outros projetos INEMA

- [IA privada em 3 níveis](https://inematds.github.io/ia-privada-3-niveis/guia/): implantação, hardware e acesso remoto.
- [IA sem censura defensiva](https://inematds.github.io/ia-sem-censura-defensiva/guia/): modelos com menos recusas em tarefas defensivas e laboratório.
- Este projeto: análise e ficha de decisões antes de usar dados reais; não duplica os instaladores anteriores.

## Documentação primária consultada

- [Ollama FAQ](https://docs.ollama.com/faq): diferença entre local e nuvem; opção de desativar funcionalidades de nuvem; endereço local padrão.
- [Integração Claude Code no Ollama](https://docs.ollama.com/integrations/claude-code): existência de uma interface compatível com outro motor. Não executamos essa integração, não alteramos Claude Code/Codex e não usamos API de modelo nesta produção.
- [PocketPal](https://github.com/a-ghorbani/pocketpal-ai): execução no aparelho e escolha de modelo para memória e armazenamento.
- [Tailscale Serve](https://tailscale.com/kb/1242/tailscale-serve): disponibilização de serviço na rede privada.
- [Draw Things](https://drawthings.ai/): geração local e opções de processamento em nuvem.

Consulta em 15/11/2026. Nenhum preço, desconto, taxa de acerto, velocidade ou tamanho de modelo da aula é tratado como medição nossa. Não houve contratação de provedor, benchmark de modelos nem teste em celular nesta produção. O material da aula e seus anexos privados não são redistribuídos.

## Leitura integral da fonte

O áudio público de 26min29s foi baixado pelo inemavox e transcrito localmente com Whisper large-v3 (514 segmentos). A transcrição automática fica no output privado da produção; nomes de produtos foram conferidos nos links oficiais. O autor explicita no nível cinco que menos censura e privacidade são coisas diferentes — esta distinção vem da própria aula, não é uma correção de algo que ela ignorou. Na demonstração do celular, o modelo identifica o autor como outra pessoa: um exemplo útil de que funcionar offline não demonstra conhecimento factual correto.

Há também uma distinção essencial no nível três: a VPS demonstrada mantém o agente, mas a inferência continua num provedor por API; ela não passa a ser local ou offline só porque a interface está na VPS. O autor propõe conferir acesso de saída do servidor aos dispositivos e testar regras, e não apenas instalar Tailscale. Este projeto recomenda os kits de implantação existentes para aprofundar essa parte.

Ao usar um segundo modelo remoto como revisor, o conteúdo também sai para esse revisor. Por isso a ficha deve incluir todos os processadores envolvidos, inclusive o revisor. Números de estudos e comparações promocionais citados na fala não foram incorporados como evidência porque a fonte primária correspondente não foi estabelecida nesta produção.
