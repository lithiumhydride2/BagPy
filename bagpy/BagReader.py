from bagreader import bagreader


def add_method(cls):  # 装饰器函数
    def show_items(self):
        print("old item is:")
        for item in self.items:
            print(item)

    # 绑定
    cls.show_items = show_items
    return cls


@add_method
class bagreader(bagreader):
    pass
