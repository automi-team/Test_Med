import my_bloc
class Testbloc:
    """ test bench for my_bloc """
    def test_5(self):
        """ simple test """
        assert 25 == my_bloc.square(5)
    def test_10(self):
        """ simple test """
        assert 100 == my_bloc.square(10)
