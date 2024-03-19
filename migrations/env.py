
from database.base import Base
from app.models.actor import Actor
from app.models.defendant import Defendant
from app.models.details import Detail
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Esta es la configuración de Alembic que proporciona acceso a los valores dentro del archivo .ini en uso.
config = context.config

# No necesitamos configurar el registro, así que eliminamos estas líneas.
#fileConfig(config.config_file_name)

# Agrega aquí el objeto MetaData de tus modelos para soporte de 'autogenerate'.
target_metadata = Base.metadata  # Establece target_metadata a tu Base.metadata

# Las funciones run_migrations_offline y run_migrations_online son proporcionadas por Alembic para ejecutar las migraciones.

def run_migrations_offline() -> None:
    """Ejecuta las migraciones en modo 'offline'.

    Esto configura el contexto solo con una URL y no un Engine, aunque un Engine también es aceptable
    aquí. Al omitir la creación del Engine, ni siquiera necesitamos que esté disponible un DBAPI.

    Las llamadas a context.execute() aquí emiten la cadena dada en la salida del script.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta las migraciones en modo 'online'.

    En este escenario, necesitamos crear un Engine y asociar una conexión con el contexto.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
