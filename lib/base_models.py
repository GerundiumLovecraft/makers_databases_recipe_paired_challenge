class Model:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        kv_strs = [f"{k}: {v}" for k, v in self.__dict__.items()]
        joined_kv_str = ", ".join(kv_strs)
        return f"{self.__class__.__name__}({joined_kv_str})"


class Repository:
    def __init__(self, db_connection):
        self._connection = db_connection