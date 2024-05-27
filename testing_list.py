class Chair:
    def __init__(self, pk: int, name: str, price: int):
        """
        سازنده کلاس صندلی میباشد و متغییر های زیر را به عنوان ویژگی های یک شی از کلاس صندلی میسازد
        :param pk:
        :param name:
        :param price:
        """
        self.pk = pk
        self.name = name
        self.price = price


class Database:
    def __init__(self):
        """
        سازنده کلاس دیتا بین میباشد و با اولین بار که یک شی از این کلاس ساخته میشود متغییری به نام chairs میسازند و به عنوان عضو شی کلاس در نظر میگیرد
        """
        self.chairs_table: list[Chair] = []

    def insert(self, instance: Chair):
        if len(self.chairs_table) <= 0:
            self.chairs_table.append(instance)
        else:
            for item in self.chairs_table:
                if item.pk == instance.pk:
                    raise Exception('Chair already exists')
                else:
                    self.chairs_table.append(instance)

    def delete(self, pk: int):
        pass


if __name__ == "__main__":
    pk = int(input('Please Input Primary Key:'))
    name = input('Please Input Name:')
    price = int(input('Please Input Price:'))
    chair = Chair(pk=pk, name=name, price=price)
    database_object = Database()

    database_object.insert(instance=chair)

    print("Exited")
