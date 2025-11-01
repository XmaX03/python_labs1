#Лабораторные работы

#Лабораторная работа №1
## Задание 1

```python
a = (input('Имя:'))
b = int(input('Возраст:'))
print('Привет,'+ str(a) + '! Через год тебе будет'+ str(b+1)+'.')
```
![Code](./images/lab01/01_greeting.png)

## Задание 2

```python
a = float(input("a: ").replace(',', '.'))
b = float(input("b: ").replace(',', '.'))
print('sum='+str(a+b)+'; avg='+str((a+b)/2))
```
![Code](./images/lab01/02_sum_avg.png)

## Задание 3

```python
price = int(input('Стоимость $:'))
discount = int(input('Скидка, %:'))
vat = int(input('НДС:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки:', base)
print('НДС:',vat_amount)
print('Итого к оплате:',total)
```
![Code](./images/lab01/03_discount_vat.png)

## Задание 4

```python
minutes_input = int(input('Минуты:'))
hour = 60
hours = minutes_input//hour
minutes = minutes_input-(hours*hour)
print(f'{hours}:{minutes:02d}')
```
![Code](./images/lab01/04_minutes_to_hhmm.png)

## Задание 5

```python
full_name = input()
cleaned_name = ' '.join(full_name.split())
x = full_name.split()
print(f'ФИО:{cleaned_name}')
print(f'Инициалы:{x[0][0]}{x[1][0]}{x[2][0]}.')
print(f'Длина (символов):{len(cleaned_name)}')
```
![Code](./images/lab01/05_initials_and_len.png)



#Лабораторная работа №2

# Задание A_min_max

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    try:
        return tuple([min(nums), max(nums)])
    except ValueError:
        return 'ValueError'
print('min_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, 9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```
![Code](./images/lab02/A_min_max.png)

# Задание A_flatten

```python
def flatten(mat: list[list | tuple]) -> list:
    spisok = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for j in mat[i]:
                spisok.append(j)
        else:
            return 'TypeError'
    return spisok
print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![code](./images/lab02/A_flatten.png)

# Задание A_unique_sorted

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    n = sorted(list(set(nums)))
    return n
print('unique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![code](./images/lab02/A_unique_sorted.png)

# Задание B_transpose
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
       return []
    
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'
    
    return [[mat[r][c] for r in range(len(mat))] for c in range(row_len)]
print('transpose')
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```
![code](./images/lab02/B_transpose.png)

# Задание B_row_sums
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'
        
    return [sum(i) for i in mat]

print('row_sum')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```
![code](./images/lab02/B_row_sums.png)

# Задание B_col_sums
```python


def col_sums(mat):
    if not mat:
        return [] 
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            return "ValueError"  
    res = []  
    for j in range(n):  
        k = 0  
        for i in range(len(mat)):  
            k += mat[i][j] 
        res.append(k)  
    return res 
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![code](./images/lab02/B_col_sums.png)

# Задание C_info

```python

def format_record(student: tuple[str, str, float]) -> str:
    if len(student) != 3: 
        return "ValueError"
    
    if not (isinstance(student[0], str) and isinstance(student[1], str) and isinstance(student[2], float)): 
        return "TypeError"

    fio_parts = student[0].split() 
    
    if len(fio_parts) < 2:
        return "ValueError: ФИО должно содержать фамилию и имя"
    
    fio_parts = [part.strip() for part in fio_parts if part.strip()]
    
    res = fio_parts[0].title() + " " + fio_parts[1][0].upper()  
   
    if len(fio_parts) == 3:
        res += "." + fio_parts[2][0].upper() + "., "  
        res += "., "  

    res += "гр. " + student[1] + ", GPA " + f"{round(student[2],2):.2f}" 
    return res 

print(format_record(("Иванов Иван Иванович","BIVT-25",4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("Иванов Иван Иванович","BIVT-25", 4.5))) 
```
![code](./images/lab02/C_info_format_record.png)
