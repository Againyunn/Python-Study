EMPLOYEE_csv = 'Fname,Minit,Lname,Ssn,Bdate,Address,Sex,Salary,Superssn,Dno\r\nJohn,B,Smith,123456789,1965-01-09,731-Fondren-Houston-TX,M,30000.00,333445555,5\r\nFranklin,T,Wong,333445555,1955-12-08,638-Voss-Houston-TX,M,40000.00,888665555,5\r\nJoyce,A,English,453453453,1972-07-31,5631-Rice-Houston-TX,F,25000.00,333445555,5\r\nRamesh,K,Narayan,666884444,1962-09-15,975-Fire-Oak-Humble-TX,M,38000.00,333445555,5\r\nJames,E,Borg,888665555,1937-11-10,450-Stone-Houston-TX,M,55000.00,,1\r\nJennifer,S,Wallace,987654321,1941-06-20,291-Berry-Bellaire-TX,F,43000.00,888665555,4\r\nAhmad,V,Jabbar,987987987,1969-03-29,980-Dallas-Houston-TX,M,25000.00,987654321,4\r\nAlicia,J,Zelaya,999887777,1968-01-19,3321-Castle-Spring-TX,F,25000.00,987654321,4\r\n'
DEPARTMENT_csv = 'Dname,Dnumber,Mgrssn,Mgrstartdate\r\nHeadquarters,1,888665555,1981-06-19\r\nAdministration,4,987654321,1995-01-01\r\nResearch,5,333445555,1988-05-22\r\n'
DEPT_LOCATIONS_csv = 'Dnumber,Dlocation\r\n1,Houston\r\n4,Stafford\r\n5,Bellaire\r\n5,Houston\r\n5,Sugarland\r\n'
PROJECT_csv = 'Pname,Pnumber,Plocation,Dnum\r\nProductX,1,Bellaire,5\r\nProductY,2,Sugarland,5\r\nProductZ,3,Houston,5\r\nComputerization,10,Stafford,4\r\nReorganization,20,Houston,1\r\nNewbenefits,30,Stafford,4\r\n'
WORKS_ON_csv = 'Essn,Pno,Hours\r\n123456789,1,32.5\r\n123456789,2,7.5\r\n333445555,2,10.0\r\n333445555,3,10.0\r\n333445555,10,10.0\r\n333445555,20,10.0\r\n453453453,1,20.0\r\n453453453,2,20.0\r\n666884444,3,40.0\r\n888665555,20,\r\n987654321,20,15.0\r\n987654321,30,20.0\r\n987987987,10,35.0\r\n987987987,30,5.0\r\n999887777,10,10.0\r\n999887777,30,30.0\r\n'
DEPENDENT_csv = 'Essn,Dependent_name,Sex,Bdate,Relationship\r\n123456789,Alice,F,1988-12-30,Daughter\r\n123456789,Elizabeth,F,1967-05-05,Spouse\r\n123456789,Michael,M,1988-01-04,Son\r\n333445555,Alice,F,1986-04-05,Daughter\r\n333445555,Joy,F,1958-05-03,Spouse\r\n333445555,Theodore,M,1983-10-25,Son\r\n987654321,Abner,M,1942-02-28,Spouse\r\n'

# import packages

import pandas as pd
from io import StringIO
import re

# Tables
EMPLOYEE = pd.read_csv(StringIO(EMPLOYEE_csv))
DEPARTMENT = pd.read_csv(StringIO(DEPARTMENT_csv))
DEPT_LOCATIONS = pd.read_csv(StringIO(DEPT_LOCATIONS_csv))
PROJECT = pd.read_csv(StringIO(PROJECT_csv))
WORKS_ON = pd.read_csv(StringIO(WORKS_ON_csv))
DEPENDENT = pd.read_csv(StringIO(DEPENDENT_csv))

# short_names for Tables
E = EMPLOYEE
D = DEPARTMENT
DL = DEPT_LOCATIONS
P = PROJECT
WO = WORKS_ON
DE = DEPENDENT

def rename(R, C):
    return R.rename(columns=C)

def select(R, C):
    # The following substitution may NOT work
    # when column name is equal to a string value in C
    tokens = re.split(r'(\W+)', C)
    new_tokens = ["R." + token  if token in R.columns else token \
                  for token in tokens]
    selected = eval(''.join(new_tokens))
    return R[selected].reset_index(drop=True)

def project(R, C):
    return R[C].drop_duplicates().reset_index(drop=True)

def union(R, S):
    S.columns = R.columns
    T = pd.concat([R, S], ignore_index=True)
    T = T.drop_duplicates().reset_index(drop=True)
    return T

def intersect(R, S):
    S.columns = R.columns
    return R.merge(S).reset_index(drop=True)

def minus(R, S):
    S.columns = R.columns
    return pd.concat([R, S, S]).drop_duplicates(keep=False).reset_index(drop=True)

def product(R, S):
    """Determine Cartesian product of two data frames."""
    key = 'key'
    while key in R.columns or key in S.columns:
        key = '_' + key
    key_d = {key: 0}
    return pd.merge(R.assign(**key_d), S.assign(**key_d), on=key)\
           .drop(key, axis=1).reset_index(drop=True)

def natural_join(R, S):
    return pd.merge(R, S).reset_index(drop=True)

def natural_join2(R, S, keys_R, keys_S):
    return pd.merge(R, S, left_on=keys_R, right_on=keys_S)\
           .drop(keys_S, axis=1).reset_index(drop=True)

def division(R, S):
    Z = set(R.columns)
    X = set(S.columns)
    assert X <= Z
    Y = pd.Index(Z - X)
    T1 = project(R, Y)
    T2 = project(minus(product(T1, S), R), Y)
    T = minus(T1, T2)
    return T.reset_index(drop=True)