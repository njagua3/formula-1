# Formula 1 Manager CLI

## Overview

The Formula 1 Manager CLI is a command-line interface application built using Python that allows users to manage teams, drivers, and races in a Formula 1 context. The application leverages SQLAlchemy for object-relational mapping (ORM) and Alembic for database migrations.


## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Pipenv

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd formula-1

2. Install dependencies using Pipenv:
   pipenv install

3. Initialize the database:
   alembic upgrade head


CLI Usage

To run the CLI, use the following command:
  pipenv run python src/cli.py


Commands
1. Create a Team


pipenv run python src/cli.py create-team "Team Name" "Country"

Description: Creates a new F1 team with the specified name and country.

pipenv run python src/cli.py create-team "Mercedes" "Germany"

2. Create a Driver


pipenv run python src/cli.py create-driver <team_id> "Driver Name" <age>
Description: Creates a new driver associated with a specified team ID.
Parameters:
team_id: The ID of the team the driver belongs to.
Driver Name: The name of the driver.
age: The age of the driver.


pipenv run python src/cli.py create-driver 1 "Lewis Hamilton" 36
3. Create a Race

pipenv run python src/cli.py create-race "Race Name" "Location" <winner_id>
Description: Creates a new race and assigns a winner based on driver ID.
Parameters:
Race Name: The name of the race.
Location: The location where the race is held.
winner_id: The ID of the driver who won the race.

pipenv run python src/cli.py create-race "Monaco Grand Prix" "Monaco" 1
4. List Teams


pipenv run python src/cli.py list-teams
Description: Lists all teams in the database.
5. List Drivers


pipenv run python src/cli.py list-drivers
Description: Lists all drivers in the database.

6. List Races

pipenv run python src/cli.py list-races
Description: Lists all races in the database.


