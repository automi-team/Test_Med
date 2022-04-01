import my_bloc
class Testbloc:
    """ test bench for my_bloc """
    @staticmethod
    def test_5(self):
        """ simple test """
        assert 25 == my_bloc.square(5)
    @staticmethod
    def test_10(self):
        """ simple test """
        assert 100 == my_bloc.square(10)
