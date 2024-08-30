class HeroRepository:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_static_data(self):
        datas = [
            {
                'id': 1,
                'title': 'BT-001',
            },
            {
                'id': 2,
                'title': 'Zero Hawk Knight',
            },
            {
                'id': 3,
                'title': self.get_name(),
            },
        ]
        return datas