# Upskilling

This repository is a compendium for working on various skils that needs upskilling.

## Development containers

The default configuration, `.devcontainer/devcontainer.json`, uses the development
image directly for general work. In Positron, enable `dev.containers.enable` in
settings, then run **Dev Containers: Reopen in Container**.

For PostgreSQL work in VS Code, select **Upskilling with PostgreSQL** when reopening
in a container. Its configuration is
`.devcontainer/postgresql/devcontainer.json` and uses `.devcontainer/compose.yaml`
to start the development container and PostgreSQL 17. From that development
container, connect to host `db`, port `5432`, database `clinical_training`, user
`student`, and password `training_password`. These are local training credentials.
Database data persists in the Compose `postgres_data` volume.

Positron currently does not support Compose-based devcontainer configurations;
use the default configuration there.

## Contact

For more information, please contact:

- Miguel Rodo: miguel.rodo@outlook.com

## Links

- [URLs to data sources (e.g. OneDrive), GitHub repositories, publications, etc.]

## Details

[Methods, timeline, team, data sources, software/tools, etc.]
