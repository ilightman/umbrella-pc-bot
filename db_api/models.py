from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100)
    first_name = fields.CharField(max_length=65, null=True)
    last_name = fields.CharField(max_length=65, null=True)

    admin = fields.BooleanField(default=False)
    manager = fields.BooleanField(default=False)
    pc_builder = fields.BooleanField(default=False)
    courier = fields.BooleanField(default=False)

    created_at = fields.DatetimeField(auto_now_add=True)

    @property
    def speciality(self):
        msg = ''
        if self.admin:
            msg = 'Администратор'
        if self.manager:
            msg = 'Менеджер'
        if self.pc_builder:
            msg = 'Сборщик ПК'
        if self.courier:
            msg = 'Курьер'
        return msg

    def __str__(self):
        return f'{self.id} - {self.username} - {self.first_name} - {self.speciality}'
