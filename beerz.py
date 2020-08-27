# coding=utf8
import random
from datetime import datetime, timedelta

people = [
    "Magnus Hornef",
    "Joel Torkelsson",
    "Adam Ringhede",
    "Torsten Freyhall",
    "Ugur Atar",
    "Emelie Klemetz",
    "Matthew Holman",
    "Tasnim Reza",
    "Tuğrul Can Şöllü",
    "Anna Wannberg",
    "Märta Waldrop Bergman",
    "Lukas Jonson",
    "Sara Rösman",
    "Anders Andersson",
    "Benjamin Reece-Hamshere",
    "Amanda Gibson",
    "Hanna Bjärkvik",
    "Stefan Fridén",
    "Carolina Tarqui",
    "Anton Olsson",
    "Robert Draghici",
    "Serhat Can",
    "Emma Alexandersson",
    "Adam Halling",
    "Mikael Jerkstrand"
]
random.shuffle(people)
friday = datetime(2020, 8, 28)
for i in range(0, len(people), 3):
    print(f"{friday.strftime('%Y-%m-%d')}        {', '.join(people[i:i + 3])}")
    friday += timedelta(days=7)
