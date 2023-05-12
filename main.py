import csv

class Test:
    def __init__(self, test_num, test_name, test_date, test_time, test_result):
        self.test_num = test_num
        self.test_name = test_name
        self.test_date = test_date
        self.test_time = test_time
        self.test_result = test_result

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

def read_csv_file(file_name):
    tests = Queue()
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip header row
        for row in csv_reader:
            test_num = int(row[0])
            test_name = row[1]
            test_date = row[2]
            test_time = row[3]
            test_result = row[4]
            test = Test(test_num, test_name, test_date, test_time, test_result)
            tests.enqueue(test)
    return tests

def print_tests(tests):
    if tests.is_empty():
        print("No tests to display.")
    else:
        print("Tests:")
        for test in tests.items:
            print(f"Test number: {test.test_num}")
            print(f"Test name: {test.test_name}")
            print(f"Test date: {test.test_date}")
            print(f"Test time: {test.test_time}")
            print(f"Test result: {test.test_result}")
            print("")

def search_test(tests, test_num):
    if tests.is_empty():
        return None
    else:
        for test in tests.items:
            if test.test_num == test_num:
                return test
        return None

def insert_test(tests, test_num, test_name, test_date, test_time, test_result):
    test = Test(test_num, test_name, test_date, test_time, test_result)
    tests.enqueue(test)

def remove_test(tests, test_num):
    if tests.is_empty():
        return False
    else:
        for i in range(tests.size()):
            test = tests.dequeue()
            if test.test_num != test_num:
                tests.enqueue(test)
            else:
                return True
        return False
    
# чтение данных из CSV-файла
tests = read_csv_file("lab_1_read.csv")

# вывод содержимого очереди тестов
print_tests(tests)

# поиск теста по номеру
test_num = 2
test = search_test(tests, test_num)
if test:
    print(f"Found test: {test.test_name}")
else:
    print(f"Test {test_num} not found")

# добавление нового теста
insert_test(tests, 5, "New Test", "2023-05-08", "10:00:00", "SUCCESS")

# удаление теста по номеру
test_num = 1
if remove_test(tests, test_num):
    print(f"Test {test_num} removed")
else:
    print(f"Test {test_num} not found")