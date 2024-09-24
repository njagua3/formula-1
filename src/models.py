from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Team(Base):
    __tablename__ = "teams"  # Name of the database table

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the team
    name = Column(String, unique=True, nullable=False)  # Name of the team, must be unique and not null
    country = Column(String, nullable=False)  # Country the team represents
    drivers = relationship("Driver", back_populates="team")  # Relationship to Driver, allowing access to all drivers of the team


class Driver(Base):
    __tablename__ = "drivers"  # Name of the database table

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the driver
    name = Column(String, nullable=False)  # Name of the driver, must not be null
    age = Column(Integer, nullable=False)  # Age of the driver, must not be null
    team_id = Column(Integer, ForeignKey("teams.id"))  # Foreign key linking to the teams table
    team = relationship("Team", back_populates="drivers")  # Relationship to Team, allowing access to the team's details


class Race(Base):
    __tablename__ = "races"  # Name of the database table

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the race
    name = Column(String, nullable=False)  # Name of the race, must not be null
    location = Column(String, nullable=False)  # Location where the race is held, must not be null
    winner_id = Column(Integer, ForeignKey("drivers.id"))  # Foreign key linking to the drivers table, indicating the race winner
    winner = relationship("Driver")  # Relationship to Driver, allowing access to the winner's details
