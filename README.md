# todo-list-api-rest
Este projeto é uma API para TO-DO List, criada com o intuito de desenvolver conhecimentos sobre APIs REST, seus fundamentos e boas práticas.

## Tópicos
- [Anotações Teóricas](#anotacoes-dos-estudos)
    - [REST: Representational State Transfer](#rest-representational-state-transfer)
    - [Níveis de Maturidade](#niveis-de-maturidade)

## Anotações dos Estudos

### REST: Representational State Transfer
É um conjunto de restrições (constraints) de arquitetura basicamente leve por natureza, criado pelo Roy Fielding.

Logo, uma API RESTful significa que a API em questão está em conformidade com as constraints REST:
- Arquitetura cliente-servidor: Separação de responsabilidades entre cliente e servidor;
- Stateless server: Servidor não mantém estado de sessão entre requisições;
- Cacheable: Respostas podem ser temporariamente armazenadas para melhorar eficiência;
- Interface uniforme:
    - Identificação de rescursos (URI): cada recurso é identificado por uma URI única;
    - Manipulação de recursos a partir de suas representações: as operações (CRUD) são realizadas através da representação do recurso, como JSON ou XML;
    - Mensagem autodescritivas: as requisições devem conter informações suficientes para processamento;
    - Hypermedia as the engine of application state (HATEOAS): uso de hypermedia para descrever estado e relacionamentos;
- Sistema em camadas: Arquitetura composta por várias camadas (ex.: servidor, banco de dados, serviços externos), onde cada camada só precisa saber sobre a camada adjacente;
- Código sob demanda (opcional): O servidor pode fornecer funcionalidades executáveis (ex.: applets ou scripts) para serem executadas no cliente.

### Níveis de Maturidade
O RESTful representa o ápice da maturidade dentro da arquitetura REST, sendo considerado o nível mais avançado
- **Nível 0 - Pântano de XML:** Utilização de um único endpoint para todos os recursos, sem organização clara.
- **Nível 1 - Organização por Recursos:** Recursos são organizados com endpoints específicos para cada função, mas sem uma atenção dedicada ao uso adequado dos verbos HTTP.
- **Nível 2 - Uso de Verbos HTTP:** Introdução do uso apropriado dos verbos HTTP, melhorando a clareza e semântica das interações, com uma separação mais eficiente dos recursos.
- **Nível 3- HATEOAS:** Incorporação de controles de hypermedia (HATEOAS), permitindo que o documento descreva seu estado e relacionamentos, possibilitando uma interconexão dinâmica entre recursos, inclusive em estados futuros.