import exceptions
import hedy
import textwrap
from tests.Tester import HedyTester
from parameterized import parameterized


class TestsLevel16(HedyTester):
    level = 16

    def test_print_list_var(self):
        code = textwrap.dedent("""\
            dieren is ['Hond', 'Kat', 'Kangoeroe']
            print dieren[1]""")

        expected = textwrap.dedent("""\
            dieren = ['Hond', 'Kat', 'Kangoeroe']
            print(f'''{dieren[1-1]}''')""")

        check_in_list = (lambda x: HedyTester.run_code(x) == 'Hond')

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=check_in_list
        )
    
    def test_create_empty_list(self):
        code = "friends = []"
        expected = "friends = []"

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected
        )
    
    def test_create_with_single_item(self):
        code = "friends = ['Ashli']"
        expected = "friends = ['Ashli']"

        check_in_list = (lambda x: HedyTester.run_code(x) == 'Ashli')

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=check_in_list
        )
    
    def test_add_to_empty_list(self):
        code = textwrap.dedent("""\
                friends = []
                add 'Ashli' to friends
                print friends[1]""")
        
        expected = textwrap.dedent("""\
                friends = []
                friends.append('Ashli')
                print(f'''{friends[1-1]}''')""")
        
        check_in_list = (lambda x: HedyTester.run_code(x) == 'Ashli')

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=check_in_list
        )

    def test_print_list_var_arabic_number(self):
        code = textwrap.dedent("""\
            dieren is ['Hond', 'Kat', 'Kangoeroe']
            print dieren[١]""")

        expected = textwrap.dedent("""\
            dieren = ['Hond', 'Kat', 'Kangoeroe']
            print(f'''{dieren[1-1]}''')""")

        check_in_list = (lambda x: HedyTester.run_code(x) == 'Hond')

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=check_in_list
        )

    def test_print_list_commas(self):
        code = textwrap.dedent("""\
            szamok1 = ['1' , '2' , '3' , '4' , '5']
            szamok2 = ['6' , '7' , '8' , '9']
            print szamok1[random]""")

        expected = textwrap.dedent("""\
            szamok1 = ['1', '2', '3', '4', '5']
            szamok2 = ['6', '7', '8', '9']
            print(f'''{random.choice(szamok1)}''')""")

        szamok1 = ['1', '2', '3', '4', '5']
        check_in_list = (lambda x: HedyTester.run_code(x) in szamok1)

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=check_in_list
        )
    
    def test_list_access_space(self):
        code = textwrap.dedent("""\
            szamok1 = [ '1' , '2' , '3' , '4' , '5' ]
            print szamok1 [random]""")
        
        expected = textwrap.dedent("""\
            szamok1 = ['1', '2', '3', '4', '5']
            print(f'''{random.choice(szamok1)}''')""")
        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected
        )

    def test_print_list_access(self):
        code = textwrap.dedent("""\
            fruit is ['banaan', 'appel', 'kers']
            print fruit[1]""")
        expected = textwrap.dedent("""\
            fruit = ['banaan', 'appel', 'kers']
            print(f'''{fruit[1-1]}''')""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=self.is_not_turtle()
        )

    def test_print_list_access_non_latin(self):
        code = textwrap.dedent("""\
            vrienden = ['Ahmed', 'Ben', 'Cayden']
            geluksgetallen = [15, 18, 6]
            voor म in bereik 1 tot 3
               print 'het geluksgetal van ' vrienden[म]
               print 'is ' geluksgetallen[म]""")
        expected = textwrap.dedent("""\
        vrienden = ['Ahmed', 'Ben', 'Cayden']
        geluksgetallen = [15, 18, 6]
        step = 1 if 1 < 3 else -1
        for म in range(1, 3 + step, step):
          print(f'''het geluksgetal van {vrienden[म-1]}''')
          print(f'''is {geluksgetallen[म-1]}''')
          time.sleep(0.1)""")

        self.single_level_tester(
            code=code,
            expected=expected,
            lang='nl',
            extra_check_function=self.is_not_turtle()
        )

    def test_list_access_var(self):
        code = textwrap.dedent("""\
            fruit = ['banaan', 'appel', 'kers']
            eerstefruit = fruit[1]
            print eerstefruit""")
        expected = textwrap.dedent("""\
            fruit = ['banaan', 'appel', 'kers']
            eerstefruit = fruit[1-1]
            print(f'''{eerstefruit}''')""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=self.is_not_turtle()
        )

    def test_access_plus(self):
        code = textwrap.dedent("""\
            lijst is [1, 2, 3]
            optellen is lijst[1] + lijst[2]
            optellen is optellen + lijst[3]
            print optellen""")
        expected = textwrap.dedent("""\
            lijst = [1, 2, 3]
            optellen = lijst[1-1] + lijst[2-1]
            optellen = optellen + lijst[3-1]
            print(f'''{optellen}''')""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=self.is_not_turtle()
        )

    def test_list_access_random(self):
        code = textwrap.dedent("""\
            fruit is ['banaan', 'appel', 'kers']
            randomfruit is fruit[random]
            print randomfruit""")
        expected = textwrap.dedent("""\
            fruit = ['banaan', 'appel', 'kers']
            randomfruit = random.choice(fruit)
            print(f'''{randomfruit}''')""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=self.is_not_turtle()
        )

    def test_access_in_equality_check(self):
        code = textwrap.dedent("""\
            luiaard = 'luiaard'
            dieren is ['aap', 'goat', 'fish']
            if luiaard is dieren[1]
                print 'ja'""")

        expected = textwrap.dedent("""\
            luiaard = 'luiaard'
            dieren = ['aap', 'goat', 'fish']
            if convert_numerals('Latin', luiaard) == convert_numerals('Latin', dieren[1-1]):
              print(f'''ja''')""")

        self.single_level_tester(
            code=code,
            expected=expected,
            extra_check_function=self.is_not_turtle()
        )

    @parameterized.expand(HedyTester.comparison_commands)
    def test_access_smaller_check(self,comparison):
        code = textwrap.dedent(f"""\
            balletje = 0
            bingo_getallen is [11, 17, 21]
            if balletje {comparison} bingo_getallen[1]
                print 'ja'""")

        expected = textwrap.dedent(f"""\
            balletje = 0
            bingo_getallen = [11, 17, 21]
            if convert_numerals('Latin', balletje).zfill(100){comparison}convert_numerals('Latin', bingo_getallen[1-1]).zfill(100):
              print(f'''ja''')""")

        self.single_level_tester(
            code=code,
            expected=expected,
            extra_check_function=self.is_not_turtle()
        )

    # ask tests
    def test_ask_with_list_var(self):
        code = textwrap.dedent("""\
        colors is ['orange', 'blue', 'green']
        favorite is ask 'Is your fav color' colors[1]""")

        expected = textwrap.dedent("""\
        colors = ['orange', 'blue', 'green']
        favorite = input(f'''Is your fav color{colors[1-1]}''')
        try:
          favorite = int(favorite)
        except ValueError:
          try:
            favorite = float(favorite)
          except ValueError:
            pass""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            extra_check_function=self.is_not_turtle()
        )

    def test_ask_with_list(self):
        code = textwrap.dedent("""\
        colors is ['orange', 'blue', 'green']
        favorite is ask 'Is your fav color' colors""")

        expected = textwrap.dedent("""\
        colors = ['orange', 'blue', 'green']
        favorite = input(f'''Is your fav color{colors}''')
        try:
          favorite = int(favorite)
        except ValueError:
          try:
            favorite = float(favorite)
          except ValueError:
            pass""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected
        )

    #add/remove tests
    def test_add_to_list(self):
        code = textwrap.dedent("""\
        color is ask 'what is your favorite color? '
        colors is ['green', 'red', 'blue']
        add color to colors
        print colors[random]""")

        expected = textwrap.dedent("""\
        color = input(f'''what is your favorite color? ''')
        try:
          color = int(color)
        except ValueError:
          try:
            color = float(color)
          except ValueError:
            pass
        colors = ['green', 'red', 'blue']
        colors.append(color)
        print(f'''{random.choice(colors)}''')""")

        self.multi_level_tester(
          code=code,
          max_level=17,
          expected=expected
        )

    def test_add_list_access_to_list(self):
        code = textwrap.dedent("""\
        colors1 is ['green', 'red', 'blue']
        colors2 is ['yellow', 'purple']
        add colors1[2] to colors2
        print colors2[3]""")

        expected = textwrap.dedent("""\
        colors1 = ['green', 'red', 'blue']
        colors2 = ['yellow', 'purple']
        colors2.append(colors1[2-1])
        print(f'''{colors2[3-1]}''')""")

        check_in_list = (lambda x: HedyTester.run_code(x) == 'red') # check that 'red' was correctly appended 

        self.multi_level_tester(
          code=code,
          max_level=17,
          expected=expected,
          extra_check_function=check_in_list
        )

    def test_remove_from_list(self):
        code = textwrap.dedent("""\
        colors is ['green', 'red', 'blue']
        color is ask 'what color to remove?'
        remove color from colors
        print colors[random]""")

        expected = textwrap.dedent("""\
        colors = ['green', 'red', 'blue']
        color = input(f'''what color to remove?''')
        try:
          color = int(color)
        except ValueError:
          try:
            color = float(color)
          except ValueError:
            pass
        try:
          colors.remove(color)
        except:
          pass
        print(f'''{random.choice(colors)}''')""")

        self.multi_level_tester(
          code=code,
          max_level=17,
          expected=expected
        )

    def test_remove_list_access_from_list(self):
        code = textwrap.dedent("""\
        colors1 is ['green', 'red', 'blue']
        colors2 is ['red', 'purple']
        remove colors1[2] from colors2
        print colors2[1]""")

        expected = textwrap.dedent("""\
        colors1 = ['green', 'red', 'blue']
        colors2 = ['red', 'purple']
        try:
          colors2.remove(colors1[2-1])
        except:
          pass
        print(f'''{colors2[1-1]}''')""")

        check_removed_from_list = (lambda x: HedyTester.run_code(x) == 'purple') # check that 'red' was removed

        self.multi_level_tester(
          code=code,
          max_level=17,
          expected=expected,
          extra_check_function=check_removed_from_list
        )

    def test_equality_with_lists(self):
        code = textwrap.dedent("""\
        m is [1, 2]
        n is [1, 2]
        if m is n
            print 'success!'""")

        expected = textwrap.dedent("""\
        m = [1, 2]
        n = [1, 2]
        if convert_numerals('Latin', m) == convert_numerals('Latin', n):
          print(f'''success!''')""")

        self.single_level_tester(code=code, expected=expected)

    def test_equality_with_number_and_list_gives_error(self):
        code = textwrap.dedent("""\
        color is [5, 6, 7]
        if 1 is color
            print 'success!'""")

        with self.assertRaises(hedy.exceptions.InvalidTypeCombinationException):
            hedy.transpile(code, self.level)

    @parameterized.expand(["'text'", '1', '1.3', '[1, 2]'])
    def test_not_equal(self, arg):
        code = textwrap.dedent(f"""\
            a = {arg}
            b = {arg}
            if a != b
                b = 1""")

        expected = textwrap.dedent(f"""\
            a = {arg}
            b = {arg}
            if convert_numerals('Latin', a).zfill(100)!=convert_numerals('Latin', b).zfill(100):
              b = 1""")

        self.single_level_tester(code, expected=expected)

    @parameterized.expand([
        ('"text"', '1'),        # double-quoted text and number
        ("'text'", '1'),        # single-quoted text and number
        ('[1, 2]', '1'),        # list and number
        ('[1, 2]', "'text'")])  # list and text
    def test_not_equal_with_diff_types_gives_error(self, left, right):
        code = textwrap.dedent(f"""\
            a = {left}
            b = {right}
            if a != b
                b = 1""")

        self.single_level_tester(code, exception=exceptions.InvalidTypeCombinationException)

    def test_color_with_list_variable_gives_error(self):
        code = textwrap.dedent("""\
        c = ['red', 'green', 'blue']
        color c""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_color_with_list_access_random(self):
        code = textwrap.dedent("""\
        colors = ['red', 'green', 'blue']
        color colors[random]""")

        expected = HedyTester.dedent("""\
        colors = ['red', 'green', 'blue']""",
        HedyTester.turtle_color_command_transpiled('{random.choice(colors)}'))

        self.multi_level_tester(
            code=code,
            expected=expected,
            extra_check_function=self.is_turtle(),
        )

    #
    # forward tests
    #
    def test_forward_with_list_variable_gives_error(self):
        code = textwrap.dedent("""\
        a = [1, 2, 3]
        forward a""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_forward_with_list_access_random(self):
        code = textwrap.dedent("""\
        directions = [10, 100, 360]
        forward directions[random]""")

        expected = HedyTester.dedent("""\
        directions = [10, 100, 360]""",
        HedyTester.forward_transpiled('random.choice(directions)', self.level))

        self.multi_level_tester(
            code=code,
            expected=expected,
            extra_check_function=self.is_turtle(),
        )

    #
    # turn tests
    #
    def test_turn_with_list_variable_gives_error(self):
        code = textwrap.dedent("""\
        a = [45, 90, 180]
        turn a""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_turn_with_list_access_random(self):
        code = textwrap.dedent("""\
        directions = [10, 100, 360]
        turn directions[random]""")

        expected = HedyTester.dedent("""\
        directions = [10, 100, 360]""",
        HedyTester.turn_transpiled('random.choice(directions)', self.level))

        self.multi_level_tester(
            code=code,
            expected=expected,
            extra_check_function=self.is_turtle(),
        )
