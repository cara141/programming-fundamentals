from Domain.entities import  Tractor
from Repository.repository import TractorRepository
from Controller.controller import TractorController
from UI.ui import UI

UI = UI("tractor.txt")
UI.run()