import my_bloc
class Testbloc:

    def test_5(self):
        assert 25 == my_bloc.square(5)

    def test_10(self):
        assert 100 == my_bloc.square(10)