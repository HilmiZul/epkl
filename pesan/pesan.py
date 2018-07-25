class pesan:
    def __init__(self):
        self.success_add = "Berhasil ditambahkan. Yey!"
        self.success_update = "Berhasil diperbaharui. Yey!"
        self.success_delete = "Berhasil dihapus."

    def add(self):
        return self.success_add

    def update(self):
        return self.success_update

    def delete(self):
        return self.success_delete
