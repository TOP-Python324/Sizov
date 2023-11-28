# Университет
from abc import ABC, abstractmethod
from datetime import date
from decimal import Decimal as dec
from dataclasses import dataclass
from enum import Enum


class ExamType(Enum):
    CHECK = 'зачет'
    DIFF_CHECK = 'дифзачет'
    EXAMEN = 'екзамен'
    PROJECT = 'научная работа'


class Degree(Enum):
    """Ученая степень"""
    CANDIDATE = 'кондидат'
    DOCTOR = 'доктор'


@dataclass
class Contact:
    """
    Описывает контактные данные.
    """
    mobile: str = None
    office: str = None
    email: str = None
    web: str = None
    telegram: str = None


class Person(ABC):
    """
    Описывает человека как персону.
    """
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: date,
            contact: Contact 
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.birthdate = birthdate
        self.contact = contact
    
    @abstractmethod
    def __repr__(self) -> str:
        pass   


class Gradebook(dict):
    """
    Описывает зачетную книжку
    """
    id: str = '1'
    
    @dataclass
    class GradeRecord:
        """Запись в зачетной книжке"""
        semester: int
        date: date
        type: ExamType
        grade: int
        scale: int
        examiner: 'Teacher'

    def __init__(self, *disciplines: str):
        super().__init__({})
        self.id = 1
        #keys = 'id', *disciplines
        #super().fromkeys(keys)
        #super()['id'] = id
                
    def avg_semester_grade()-> float:
        """Раситывает средний бал за семестр"""
        pass


class Student(Person):
    """
    Описывает студента.
    """
    
    class EducationForm(Enum):
        """Форма обучения"""        
        INTRAMURAL = 'очная'
        EXTRAMURAL = 'заочная'
        REMOTE = 'удаленная'

    class ContractForm(Enum):
        """Форма договора"""        
        BUDGET = 'бюджетный'
        COMPANY = 'целевой'
        PERSONAL = 'персональный'

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: date,
            contact: Contact, 
            id: str,
            form: EducationForm,
            contract: ContractForm,
            semestr: int,
    ):
        super().__init__(
                last_name = last_name,
                first_name = first_name,
                patr_name = patr_name,
                birthdate = date,
                contact = contact
        )
        self.id = id
        self.form = form
        self.contract = contract
        self.semestr = semestr
        self.gradebook = Gradebook()
        self.__stipendia: dec  = dec(0) 

    def __repr__(self):
        return f'Студент {self.last_name} {self.first_name[0]}.{self.patr_name[0]}.,id-{self.id}, семестр-{self.semestr}' 
        
    @property
    def stipendia(self) -> dec:
        return self.__stipendia

    @stipendia.setter
    def x(self, new_stipendia: dec):
        self.__stipendia: dec  = dec(new_stipendia)


class Employee(Person):
    """
    Сотрудник.
    """
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: date,
            contact: Contact, 
            position: str,
            income: dec,
    ):
        super().__init__(last_name, first_name, patr_name, birthdate, contact)
        self.position = position
        self.income = income

    @abstractmethod
    def calc_month_income()-> dec: #абстрактный метод
        """Расчитывает ежемесячные выплаты"""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass 


class Teacher(Employee):
    """
    Преподаватель.
    """
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: date,
            contact: Contact, 
            position: str,
            income: dec,
            courses: list[str],
            degree: Degree | None,
            professor: bool,
    ):
        super().__init__(last_name, first_name, patr_name, birthdate, contact, position, income)
        self.courses: courses
        self.degree = degree
        self.professor = professor

    def __repr__(self):
        return f'{self.last_name} {self.first_name[0]}.{self.patr_name[0]}., ученая степень - {self.degree.__dict__["_value_"]}' 

    def calc_month_income()-> dec:
        """Расчитывает ежемесячные выплаты"""
        return(dec(100500))

    def make_examination(students_book: Gradebook) -> 'GradeRecord':
        """Формирует запись о результате экзамена в зачетке студента"""
        pass


class Administrator(Employee):
    """Руководитель"""
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: date,
            contact: Contact, 
            position: str,
            income: dec,
            head: 'Administartor',
            subordinates: list[Employee]
    ):
        super().__init__(last_name,first_name,patr_name,birthdate,contact,position,income)
        self.head: head
        self.subordinates: subordinates
    
    def calc_month_income()-> dec:
        """Расчитывает ежемесячные выплаты"""
        return(dec(100500))


# >>> c1=Contact(
# ... 12345,
# ... 'Saratov',
# ... '1@ya.ru',
# ... 'www',
# ... '1t'
# ... )
# >>> print(c1)
# Contact(mobile=12345, office='Saratov', email='1@ya.ru', web='www', telegram='1t')
# >>>
# >>> t1 = Teacher('s','s','e',date(2023,11,28),Contact(),'1',10,['1','2'],Degree.DOCTOR,True)
# >>> print(t1)
# s s.e., ученая степень - доктор
# >>>
# >>>
# >>> st1 = Student(
# ... 'Иванов',
# ... 'Иван',
# ... 'Иванович',
# ... date(2000,5,15),
# ... Contact(),
# ... 123456,
# ... 1
# ... )
# >>> print(st1)
# Студент Иванов И.И.,id-123456, семестр-1
# >>>