import datetime
from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


test_user = User(
    first_name='Test',
    last_name='Testov',
    email='test@test.com',
    phone='1234567890',
    address='Minsk',
    birthday=date(1999, 12, 12),
    gender='Male',
    subject='Computer Science',
    hobbies='Music',
    image='photo.png',
    state='NCR',
    city='Delhi')