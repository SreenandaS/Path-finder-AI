from pydantic import BaseModel
class StudentProfile(BaseModel):
    annual_income:int
    state:str
    year_of_study:int
    category:str
    interests:list[str]
    