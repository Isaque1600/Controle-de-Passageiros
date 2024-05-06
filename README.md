Trabalho de Algoritmos

TEMA ------------------------------------------------------------------------------

Eficiência e otimização utilizando algoritmos

EQUIPE ----------------------------------------------------------------------------

Felipe Barbosa Soares de Souza Pereira

Isaque Batista Nobrega

Joel Feitosa da Silva

Jose Francisco Viana Dantas

Julio Cesar Morais Satyro

Julio Cesar Morais de Carvalho

Lucas Ferreira Siqueira Brito

Marcos Gustavo de Andrade Ferreira

Raimundo Nobrega de Sousa Segundo

Contextualização do Problema ------------------------------------------------------

Algoritmos na computação são pequenos pedaços de código utilizados em sua
grande maioria para resolver problemas, sendo esses problemas os mais diversos,
indo desde um sistema simples de loja, até um complexo sistema de gerencia-
mento de servidores em nuvem. Esses algoritmos são normalmente projetados
para não só solucionar o problema, mas também realizar isso da forma mais
eficiente e otimizada possível, e dentre esse meio existem diversos algoritmos e
programas que facilitam isso, assim como há muitos problemas para solucionar.
Um dos problemas que encontramos foi a falta de eficiência e otimização nas
listas de pessoas que utilizam de transporte municipal direcionado a estudantes
das universidades de Patos, onde as pessoas para se locomover de sua cidade
para estudar em outra, necessitam por meio de um grupo no Whatsapp colocar
o nome em uma lista para poder pegar o transporte no outro dia.

Justificativa ----------------------------------------------------------------------

A dependência das listas usadas no WhatsApp para organizar o transporte
escolar apresenta desafios significativos devido à sua falta de controle. Tanto os
motoristas quanto os alunos precisam se manter atentos às mudanças repentinas
nas paradas e nas listas de passageiros. Isso requer uma vigilância constante por
parte dos motoristas para ajustar seus percursos de acordo com as alterações
na lista, enquanto os alunos também precisam adaptar-se rapidamente para
garantir sua presença nas paradas corretas.
Alguns outros problemas encontrados são a superlotação dos ônibus para
faculdade, um problema que preocupa muito a segurança dos alunos, podendo
comprometer a segurança e o conforto deles, além de aumentar o risco de aciden-
tes, o fato dos ônibus não respeitar os horários da instituição de ensino, podendo
resultar em atrasos para os estudantes, afetando diretamente a produtividade
e o desempenho acadêmico, além de causar frustração e estresse nos envolvi-
dos, impactando negativamente o ambiente de aprendizado e o bem-estar geral
da comunidade acadêmica, a checagem da lista de alunos em ônibus escolares
apresenta falhas como a falta de monitores, lentidão na checagem e a distra-
ção do motorista, que podem comprometer a segurança dos alunos na estrada.
Paradas em locais não devidos, como por exemplo pessoas que não estudam
nas instituições e pegam carona nos ônibus apenas para passear pelo shopping,
sendo necessário um controle maior disso, e o problema das mudanças de ho-
rários, afetando tanto alunos quanto professores devido à redução no tempo de
estudo, podendo resultar na perda de partes essenciais do conteúdo e prejudicar
o andamento das aulas.

Solução Proposta ---------------------------------------------------------------------

Para solucionar este problema pensamos em realizar um programa que solicitasse
o nome do estudante, a sua instituição e o horário que ele iria e o da volta,
respeitando também os horários do ônibus (6h, 12h, 18h e 22h), otimizando
assim questões como consulta da quantidade de passageiros e horários.
4 Descrição da Aplicação
Dada a relativa simplicidade do problema em questão, iremos implementar
as seguintes funcionalidades no sistema proposto: a capacidade de marcar e
desmarcar viagens, a realização de consultas para determinar o total de alunos
transportados e sua distribuição por instituição, a visualização dos dados básicos
dos motoristas envolvidos, assim como a exibição dos horários de partida e
chegada dos ônibus, juntamente com as paradas correspondentes ao itinerário.
