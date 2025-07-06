🌿 1️⃣ ¿Qué es Arquitectura Hexagonal?
La arquitectura hexagonal (o Ports and Adapters) divide la aplicación en capas independientes:

Dominio: Reglas de negocio puras.

Aplicación: Casos de uso.

Infraestructura: Adaptadores (DB, APIs externas, etc.).

Interfaz: Entrada/salida (FastAPI, CLI, etc.).

Esto permite aislar el dominio de cualquier tecnología.

🗂️ Estructura de carpetas en proyecto hexagonal basico

modules/
├── users/                       # Módulo usuarios
│   ├── domain/
│   │   ├── models.py
│   │   └── repositories.py
│   ├── application/
│   │   └── use_cases.py
│   ├── infrastructure/
│   │   ├── postgres_repo.py
│   │   └── dynamo_repo.py
│   └── interfaces/
│       └── api/
│           └── routes.py
├── products/                    # Módulo productos
│   ├── domain/
│   │   ├── models.py
│   │   └── repositories.py
│   ├── application/
│   │   └── use_cases.py
│   ├── infrastructure/
│   │   └── postgres_repo.py
│   └── interfaces/
│       └── api/
│           └── routes.py
├── shared/                      # Código compartido
│   └── utils.py
├── config.py
└── main.py


extra: 
¿Compartir Infraestructura o no?
Depende:

🚧 Infraestructura Compartida
Si varios módulos usan la misma base de datos, puedes tener un paquete común de infraestructura en shared/:

bash
Copiar
Editar
shared/
├── database.py       # Conexión DB común
├── dynamodb.py       # Conexión DynamoDB común
└── utils.py
Cada módulo implementa su repositorio pero reutiliza las conexiones.
Ejemplo:

users.infrastructure.postgres_repo.py importa shared.database

products.infrastructure.postgres_repo.py igual

Así evitas duplicar la conexión.

🧩 Infraestructura Independiente
Si cada módulo tiene su propia tabla o su propia forma de almacenamiento, entonces cada uno puede tener su propia infraestructura.