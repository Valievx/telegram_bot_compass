import json


class DataStorage:
    def __init__(self):
        self.path = 'tgbot/data/data.json'
        self.storage = {}

    # Загружаем JSON
    def load(self):
        with open(self.path) as file:
            self.storage = json.load(file)
            return self

    # Сохраняем JSON
    def save(self):
        with open(self.path, 'w') as file:
            json.dump(self.storage, file, indent=4)
            return True

    # Возвращаем конфиги парсера
    async def get_pars_config(self):
        return (
            self.storage['pars'],
            self.storage['pars_id'],
            self.storage['pars_word'],
        )

    # Читаем все записанные сообщения в опредленном чате
    async def get_pars_data(self, channel):
        if not channel in self.storage['pars_data']:
            self.storage['pars_data'][channel] = []
        return self.storage['pars_data'][channel]
