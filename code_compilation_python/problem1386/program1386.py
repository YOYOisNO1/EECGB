    """Модуль содержит функции для поиска кода ОКВЭД."""
    
    import docx
    import xlrd
    
    # Словарь с режимами налогообложения
    TAX_REGIMES = {'1': 'УСН 6%', '2': 'УСН 15%', '3': 'ПСН',
                   '4': 'НПД', '5': 'ОСН', '6': 'ЕНВД'}
    # Пороговые объемы выручки
    PROFIT1 = 150000000
    PROFIT2 = 2500000
    # Пороговое количество сотрудников
    WORKERS_NUM = 100
    
    
def read_actions_dict():
        """Функция открываем файл с описанием видов деятельности
        для подбора кодов ОКВЭД.
        :return: словарь с описанием кодов ОКВЭД. Ключрм словаря является
        описание вида деятельности, а значением - список возможных кодов
        ОКВЭД."""
    
        # Открываем файл
        FILENAME = 'C:\\Users\\i.vladimirov\\Downloads\\data\\Виды деятельности ПСН.xlsx'
        book = xlrd.open_workbook(FILENAME)
        # Выбираем первый лист
        sheet = book.sheet_by_index(0)
        # Получаем словарь с описанием видов деятельности
        actions_dict = {}
        for rownum in range(sheet.nrows):
            key = sheet.row_values(rownum)[0].lower()
            actions_dict[key] = str(sheet.row_values(rownum)[1]).split(', ')
        # Выбираем второй лист
        sheet = book.sheet_by_index(1)
        # Получаем словарь с описанием видов деятельности
        for rownum in range(sheet.nrows):
            key = sheet.row_values(rownum)[0].lower()
            actions_dict[key] = str(sheet.row_values(rownum)[1]).split(', ')
        return actions_dict
    
    
def read_codes_dict():
        """Функция читает файл с кодами ОКВЭД.
        :return: словарь с описанием кодов ОКВЭД; ключом словрая
        является сам код, а значением - описание деятельности."""
    
        FILENAME = 'C:\\Users\\i.vladimirov\\Downloads\\data\\ОКВЭД.docx'
        doc = docx.Document(FILENAME)  # открываем файл с кодами
        codes_dict = {}  # словарь с кодами ОКВЭД
        # В цикле читаем все данные из всех таблиц в файле
        i = 0
        for table in doc.tables:
            i += 1
            if i > 6:
                break
            for row in table.rows:
                codes_dict[row.cells[0].text] = row.cells[1].text
        return codes_dict
    
    
def read_regions():
        """Функция читает файл с кодами регионов.
        :return: словарь с кодами регионов; ключом словаря является
        код региона, а значением - название региона."""
    
        FILENAME = 'C:\\Users\\i.vladimirov\\Downloads\\data\\Список регионов.xlsx'
        book = xlrd.open_workbook(FILENAME)  # открываем файл с регионами
        # Выбираем первый лист
        sheet = book.sheet_by_index(0)
        regions_dict = {}  # словарь с кодами ОКВЭД
        for rownum in range(sheet.nrows):
            key = int(sheet.row_values(rownum)[1])
            regions_dict[key] = sheet.row_values(rownum)[0]
        return regions_dict
    
    
    class Client:
        """Класс, определяющий объекты, хранящие полную информацию
        о клиенте, который хочет стать предпринимателем."""
    
    def __init__(self):
            """Конструктор класса."""
    
            pass
    
    def ask_1(self):
            """Метод задает вопрос 1.
            :return: True, если клиент - действующий предприниматель,
            иначе False."""
    
            while True:
                response = input('Вы являетесь действющим предпринимателем '
                                 '(ИП, ООО)? (Да - 1, нет - 2)'
                                 '\n\tВаш ответ: ')
                if response == '1':
                    self.real_boss = True
                    return True
                elif response == '2':
                    self.real_boss = False
                    return False
    
    def ask_real_2(self):
            """Метод задает вопросы действующему предпринимателю."""
    
            self.taxpayer_number = input('Введите ИНН:\n\tВаш ответ: ')
            while True:
                response = input('Какой у вас режим налогообложения?\n'
                                 '(УСН 6% - 1, УСН 15% - 2, ПСН - 3, НПД - 4,'
                                 ' ОСН - 5, ЕНВД - 6)\n\tВаш ответ: ')
                if response in '123456':
                    self.tax_regime = TAX_REGIMES[response]
                    return
    
    def ask_future_2(self, actions_dict):
            """Метод задает вопрос будущему предпринимателю о виде
            деятельности."""
    
            response = input('Чем вы планируете заниматься? '
                             '(Опишите в нескольких словах)\n'
                             '\tВаш ответ: ')
            response = response.lower().split()
            coincidences = {}
            for word in response:
                for action in actions_dict:
                    if word in actions_dict:
                        coincidences[actions_dict] += 1
    
    def ask_future_3(self, regions_dict):
            """Метод задает вопрос будущему предпринимателю о регионе
            работы.
            :param regions_dict: словарь с кодами регионов."""
    
            print('В каком регионе вы планируете работать?')
            print('(Список регионов:')
            i = 1
            for code, region in regions_dict.items():
                if i != len(regions_dict):
                    print(f'{region} - {code}')
                else:
                    print(f'{region} - {code}', end=')\n')
                i += 1
            while True:
                try:
                    response = int(input('\tВаш ответ: '))
                except ValueError:
                    pass
                else:
                    if response in regions_dict.keys():
                        self.region = response
                        return
    
    def ask_4(self):
            """Метод задает вопрос предпринимателю о выручке."""
    
            if self.real_boss:
                # Вопрос для действующего предпринимателя
                question = 'Объем выручки в год (в руб)?\n'\
                    '\tВаш ответ: '
            else:
                # Вопрос для будущего предпринимателя
                question = 'Планируемый объем выручки в год (в руб)?\n'\
                    '\tВаш ответ: '
            while True:
                try:
                    response = int(input(question))
                except ValueError:
                    pass
                else:
                    self.profit = response
                    return
    
    def ask_5(self):
            """Метод задает вопрос предпринимателю о количестве
            работников."""
    
            if self.real_boss:
                # Вопрос для действующего предпринимателя
                question = 'У вас есть сотрудники? (Да - 1, нет - 2)\n'\
                    '\tВаш ответ: '
            else:
                # Вопрос для будущего предпринимателя
                question = 'Вы планируете нанимать сотрудников? '\
                    '(Да - 1, нет - 2)\n\tВаш ответ: '
            while True:
                response = input(question)
                if response == '1':
                    break
                elif response == '2':
                    self.workers_num = 0
                    return
    
            if self.real_boss:
                # Вопрос для действующего предпринимателя
                question = 'Сколько у вас сотрудников?\n\tВаш ответ: '
            else:
                # Вопрос для будущего предпринимателя
                question = 'Сколько сотрудников вы планируете нанять?\n'\
                    '\tВаш ответ: '
            while True:
                try:
                    response = int(input(question))
                except ValueError:
                    pass
                else:
                    if response > 0:
                        self.workers_num = response
                        return
    
    def ask_6(self):
            """Метод задает вопрос предпринимателю о расходах."""
    
            if self.real_boss:
                # Вопрос для действующего предпринимателя
                question = 'Объем расходов более 60% от объема выручки? '\
                    '(Да - 1, нет - 2)\n\tВаш ответ: '
            else:
                # Вопрос для будущего предпринимателя
                question = 'Будет ли объем расходов более 60% от '\
                    'объема выручки? (Да - 1, нет - 2)\n\tВаш ответ: '
            while True:
                response = input(question)
                if response == '1':
                    self.expenses = True
                    return
                elif response == '2':
                    self.expenses = False
                    return
    
    def ask_7(self):
            """Метод задает вопрос предпринимателю о договорах
            простого товарищества."""
    
            if self.real_boss:
                # Вопрос для действующего предпринимателя
                question = 'Ведети ли вы деятельность по договорам ' \
                    'простого товарищества? '\
                    '(Да - 1, нет - 2)\n\tВаш ответ: '
            else:
                # Вопрос для действующего предпринимателя
                question = 'Планируете ли вы вести деятельность по '\
                    'договорам простого товарищества? '\
                    '(Да - 1, нет - 2)\n\tВаш ответ: '
            while True:
                response = input(question)
                if response == '1':
                    self.simple_partnership = True
                    return
                elif response == '2':
                    self.simple_partnership = False
                    return
    
    def print_optimal_regime(self):
            """Метод выводит на экран оптимальный режим
            налогообложения."""
    
            if self.real_boss:
                # Для действующего предпринимателя
                if self.tax_regime != self.optimal_tax_regime:
                    print(f'Оптимальный режим налогообложения '
                          f'{self.optimal_tax_regime}.')
                    return
                else:
                    print('У вас оптимальный режим налогообложения.')
                    return
            else:
                # Для будущего предпринимателя
                print(f'Оптимальный режим налогообложения '
                      f'{self.optimal_tax_regime}.')
                return
    
    def check_special_region(self):
            """Метод проверяет, является ли регион, в котором работает
             предприниматель регионом НПД."""
    
    def get_info(self, actions_dict, codes_dict, regions_dict):
            """Метод организует сбор полной информации о клиенте и его
            деятельности.
            :param actions_dict: словарь с описанием видов деятельности;
            :param codes_dict: словарь с кодами ОКВЭД;
            :param regions_dict: словарь с кодами регионов."""
    
            # Задаем вопрос 1
            if self.ask_1():
                # Если клиент ялвяется действующим предпринимателем
                self.ask_real_2()
            else:
                # Если клиент не является действующим предпринимателем
                self.ask_future_2(actions_dict)
                self.ask_future_3(regions_dict)
            self.ask_4()
            self.ask_5()
            self.ask_6()
            self.ask_7()
    
            if self.simple_partnership:
                # Ведется деятельность по договорам простого товарищества
                if self.profit < PROFIT1 and self.workers_num < WORKERS_NUM:
                    # Подобран оптимальный режим налогообложения УСН 15 или 6%
                    self.optimal_tax_regime = 'УСН 15%' if self.expenses \
                        else 'УСН 6%'
                    self.print_optimal_regime()
                    return
    
            if self.profit > PROFIT1 or self.workers_num > WORKERS_NUM:
                # Подобран оптимальный режим налогообложения ОСН
                self.optimal_tax_regime = 'ОСН'
                self.print_optimal_regime()
                return
    
            if self.profit <PROFIT2 and self.workers_num and
                self.check_special_region():
                pass
    
    
    
    # Скачиваются все данные из файлов
    actions_dict = read_actions_dict()
    codes_dict = read_codes_dict()
    regions_dict = read_regions()
    # Создаем клиента
    client = Client()
    client.get_info(actions_dict, codes_dict, regions_dict)