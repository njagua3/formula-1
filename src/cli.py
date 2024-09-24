import click
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
from src.models import Team, Driver, Race, Base

# Create all tables in the database based on the defined models
Base.metadata.create_all(bind=engine)

@click.group()
def cli():
    """Formula 1 Manager CLI: Command-line interface for managing Formula 1 teams, drivers, and races."""
    pass

@cli.command()
@click.argument('name')
@click.argument('country')
def create_team(name, country):
    """Create a new F1 team with the specified NAME and COUNTRY."""
    db: Session = SessionLocal()  # Start a new database session
    team = Team(name=name, country=country)  # Create a new Team instance
    db.add(team)  # Add the new team to the session
    db.commit()  # Commit the session to save changes to the database
    db.refresh(team)  # Refresh the team instance to get the latest data
    click.echo(f"Team {team.name} from {team.country} created!")  # Print confirmation message

@cli.command()
@click.argument('team_id', type=int)
@click.argument('name')
@click.argument('age', type=int)
def create_driver(team_id, name, age):
    """Create a new driver for a team, identified by TEAM_ID, with the specified NAME and AGE."""
    db: Session = SessionLocal()  # Start a new database session
    driver = Driver(name=name, age=age, team_id=team_id)  # Create a new Driver instance
    db.add(driver)  # Add the new driver to the session
    db.commit()  # Commit the session to save changes to the database
    db.refresh(driver)  # Refresh the driver instance to get the latest data
    click.echo(f"Driver {driver.name} created for team {driver.team.name}!")  # Print confirmation message

@cli.command()
@click.argument('name')
@click.argument('location')
@click.argument('winner_id', type=int)
def create_race(name, location, winner_id):
    """Create a new race at the specified LOCATION, with the specified NAME and WINNER_ID."""
    db: Session = SessionLocal()  # Start a new database session
    race = Race(name=name, location=location, winner_id=winner_id)  # Create a new Race instance
    db.add(race)  # Add the new race to the session
    db.commit()  # Commit the session to save changes to the database
    db.refresh(race)  # Refresh the race instance to get the latest data
    click.echo(f"Race {race.name} at {race.location} won by {race.winner.name}!")  # Print confirmation message

@cli.command()
def list_teams():
    """List all F1 teams in the database."""
    db: Session = SessionLocal()  # Start a new database session
    teams = db.query(Team).all()  # Query all teams from the database
    for team in teams:
        click.echo(f"Team: {team.name}, Country: {team.country}")  # Print each team's name and country

@cli.command()
def list_drivers():
    """List all drivers in the database."""
    db: Session = SessionLocal()  # Start a new database session
    drivers = db.query(Driver).all()  # Query all drivers from the database
    for driver in drivers:
        click.echo(f"Driver: {driver.name}, Age: {driver.age}, Team: {driver.team.name}")  # Print each driver's details

@cli.command()
def list_races():
    """List all races in the database."""
    db: Session = SessionLocal()  # Start a new database session
    races = db.query(Race).all()  # Query all races from the database
    for race in races:
        click.echo(f"Race: {race.name}, Location: {race.location}, Winner: {race.winner.name}")  # Print each race's details

if __name__ == "__main__":
    cli()  # Run the CLI application
