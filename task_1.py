if __name__ == "__main__":
        class Robot:
            """
            Базовый класс для всех роботов.
            """

            def __init__(self, name: str, model: str):
                """
                Конструктор базового класса Robot.

                :param name: Имя робота (например, "R2D2").
                :param model: Модель робота (например, "X100").
                """
                self._name = name
                self._model = model

            @property
            def name(self) -> str:
                """
                Getter для имени робота.
                """
                return self._name

            @name.setter
            def name(self, new_name: str):
                """
                Setter для имени робота. Проверяет, что новое имя не пустое.
                """
                if not new_name.strip():
                    raise ValueError("Имя робота не может быть пустым.")
                self._name = new_name

            @property
            def model(self) -> str:
                """
                Getter для модели робота.
                """
                return self._model

            @model.setter
            def model(self, new_model: str):
                """
                Setter для модели робота. Проверяет, что новая модель не пустая.
                """
                if not new_model.strip():
                    raise ValueError("Модель робота не может быть пустой.")
                self._model = new_model

            def introduce(self) -> str:
                """
                Метод для представления робота.
                """
                return f"Привет! Я робот {self._name}, модель {self._model}."

            def perform_task(self) -> str:
                """
                Метод для выполнения задачи. Должен быть переопределен в дочерних классах.
                """
                raise NotImplementedError("Метод perform_task должен быть переопределен.")

            def __str__(self) -> str:
                return f"Робот {self._name} ({self._model})"

            def __repr__(self) -> str:
                return f"Robot(name={self._name}, model={self._model})"


        class CleaningRobot(Robot):
            """
            Класс для роботов, предназначенных для уборки.
            """

            def __init__(self, name: str, model: str, cleaning_area: float):
                """
                Конструктор класса CleaningRobot.

                :param name: Имя робота.
                :param model: Модель робота.
                :param cleaning_area: Площадь, которую может убрать робот за один цикл (в квадратных метрах).
                """
                super().__init__(name, model)  # Вызываем конструктор базового класса.
                self._cleaning_area = cleaning_area  # Инкапсулируем площадь уборки.

            @property
            def cleaning_area(self) -> float:
                """
                Getter для площади уборки.
                """
                return self._cleaning_area

            @cleaning_area.setter
            def cleaning_area(self, new_cleaning_area: float):
                """
                Setter для площади уборки. Проверяет, что новая площадь положительна.
                """
                if new_cleaning_area <= 0:
                    raise ValueError("Площадь уборки должна быть положительной.")
                self._cleaning_area = new_cleaning_area

            def perform_task(self) -> str:
                """
                Переопределяем метод для выполнения задачи.
                Описывает процесс уборки.
                """
                return f"{self.name} убирает площадь {self._cleaning_area} кв.м."

            def __str__(self) -> str:
                return f"Робот-уборщик {self.name} ({self.model}), способный убирать {self._cleaning_area} кв.м."

            def __repr__(self) -> str:
                return f"CleaningRobot(name={self.name}, model={self.model}, cleaning_area={self._cleaning_area})"


        class DeliveryRobot(Robot):
            """
            Класс для роботов, предназначенных для доставки.
            """

            def __init__(self, name: str, model: str, max_load: float):
                """
                Конструктор класса DeliveryRobot.

                :param name: Имя робота.
                :param model: Модель робота.
                :param max_load: Максимальная грузоподъемность робота (в килограммах).
                """
                super().__init__(name, model)  # Вызываем конструктор базового класса.
                self._max_load = max_load  # Инкапсулируем максимальную грузоподъемность.

            @property
            def max_load(self) -> float:
                """
                Getter для максимальной грузоподъемности.
                """
                return self._max_load

            @max_load.setter
            def max_load(self, new_max_load: float):
                """
                Setter для максимальной грузоподъемности. Проверяет, что новая грузоподъемность положительна.
                """
                if new_max_load <= 0:
                    raise ValueError("Грузоподъемность должна быть положительной.")
                self._max_load = new_max_load

            def perform_task(self) -> str:
                """
                Переопределяем метод для выполнения задачи.
                Описывает процесс доставки.
                """
                return f"{self.name} доставляет груз весом до {self._max_load} кг."

            def __str__(self) -> str:
                return f"Робот-доставщик {self.name} ({self.model}), способный переносить {self._max_load} кг."

            def __repr__(self) -> str:
                return f"DeliveryRobot(name={self.name}, model={self.model}, max_load={self._max_load})"
pass
