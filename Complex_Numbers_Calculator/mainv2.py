list_of_complex_numbers = []

class Complex:
    def __init__(self, real, imag):
        """
        Initializează un număr complex.

        :param real: Partea reală a numărului complex (float).
        :param imag: Partea imaginară a numărului complex (float).
        """
        self.real = real
        self.imag = imag

    def __str__(self):
        """Returnează reprezentarea sub formă de string a numărului complex."""
        return f"{self.real} + {self.imag}i"

def read_complex_number():
    """
    Citește un număr complex de la utilizator.

    :return: Tuple conținând partea reală și partea imaginară (float, float).
    """
    real = float(input("Enter the real part: "))
    imag = float(input("Enter the imaginary part: "))
    return real, imag

def append_complex_number(complex_list, real, imag):
    """
    Adaugă un număr complex la listă.

    :param complex_list: Lista de numere complexe.
    :param real: Partea reală a numărului complex (float).
    :param imag: Partea imaginară a numărului complex (float).
    :return: Lista actualizată de numere complexe.
    """
    new_complex = Complex(real, imag)
    complex_list.append(new_complex)
    print(f"Added: {new_complex}")
    return complex_list

def insert_complex_number(complex_list, position, real, imag):
    """
    Inserează un număr complex într-o poziție specificată.

    :param complex_list: Lista de numere complexe.
    :param position: Poziția la care se va insera numărul complex (int).
    :param real: Partea reală a numărului complex (float).
    :param imag: Partea imaginară a numărului complex (float).
    :return: Lista actualizată de numere complexe.
    """
    new_complex = Complex(real, imag)
    complex_list.insert(position, new_complex)
    print(f"Inserted: {new_complex} at position {position}")
    return complex_list

def display_complex_numbers(complex_list):
    """
    Afișează toate numerele complexe din listă.

    :param complex_list: Lista de numere complexe.
    """
    for complex_number in complex_list:
        print(complex_number)

def delete_element_at_position(complex_list, position):
    """
    Șterge un element de la o poziție specificată.

    :param complex_list: Lista de numere complexe.
    :param position: Poziția elementului care va fi șters (int).
    :return: Lista actualizată de numere complexe.
    """
    del complex_list[position]
    print(f"Deleted element at position {position}")
    return complex_list

def delete_elements_from_range(complex_list, start, end):
    """
    Șterge elementele dintr-un interval specificat.

    :param complex_list: Lista de numere complexe.
    :param start: Poziția de început a intervalului (int).
    :param end: Poziția de sfârșit a intervalului (int).
    :return: Lista actualizată de numere complexe.
    """
    del complex_list[start:end]
    print(f"Deleted elements from position {start} to {end}")
    return complex_list

def replace_elements_with_another_value(complex_list, realval, compval, chrealval, chcompval):
    """
    Înlocuiește elementele din listă cu un alt număr complex.

    :param complex_list: Lista de numere complexe.
    :param realval: Partea reală a numărului complex de înlocuit (float).
    :param compval: Partea imaginară a numărului complex de înlocuit (float).
    :param chrealval: Noua parte reală (float).
    :param chcompval: Noua parte imaginară (float).
    :return: Lista actualizată de numere complexe.
    """
    for i in range(len(complex_list)):
        if complex_list[i].real == realval and complex_list[i].imag == compval:
            complex_list[i].real = chrealval
            complex_list[i].imag = chcompval
    return complex_list

def print_real_part(complex_list, start, end):
    """
    Afișează partea reală a fiecărui număr complex din listă.

    :param complex_list: Lista de numere complexe.
    """
    for complex_number in complex_list[start:end]:
        print(complex_number.real)

def calculate_module(complex_number):
    """
    Calculează modulul unui număr complex.

    :param complex_number: Numărul complex pentru care se calculează modulul.
    :return: Modulul numărului complex (float).
    """
    return (complex_number.real**2 + complex_number.imag**2)**0.5

def print_module_less_than_10(complex_list):
    """
    Afișează numerele complexe cu modulul mai mic decât 10.

    :param complex_list: Lista de numere complexe.
    """
    for complex_number in complex_list:
        if calculate_module(complex_number) < 10:
            print(complex_number)

def print_module_equal_to_10(complex_list):
    """
    Afișează numerele complexe cu modulul egal cu 10.

    :param complex_list: Lista de numere complexe.
    """
    for complex_number in complex_list:
        if calculate_module(complex_number) == 10:
            print(complex_number)

def print_imaginary_part(complex_list, start, end):
    """
    Afișează partea imaginară a fiecărui număr complex din listă.

    :param complex_list: Lista de numere complexe.
    :param start: Poziția de început a intervalului (int).
    :param end: Poziția de sfârșit a intervalului (int).
    """
    for complex_number in complex_list[start:end]:
        print(complex_number.imag)

def menu(complex_list):
    """
    Afișează meniul principal și gestionează interacțiunile utilizatorului.

    :param complex_list: Lista de numere complexe.
    """
    while True:
        print("\n------------MENU------------")
        print("[1] to add a complex number")
        print("[2] to modify a complex number")
        print("[3] to display complex numbers with a given property")
        print("[4] to display all complex numbers")
        print("[0] to exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n------------SUB-MENU------------")
            print("   [1] to append a complex number")
            print("   [2] to insert a complex number")
            schoice = int(input("Enter your secondary choice: "))
            real, imag = read_complex_number()
            if schoice == 1:
                complex_list = append_complex_number(complex_list, real, imag)
            elif schoice == 2:
                position = int(input("Enter the position: "))
                complex_list = insert_complex_number(complex_list, position, real, imag)
            else:
                print("Invalid choice")
        
        elif choice == 2:
            print("\n------------SUB-MENU------------")
            print("[1] to delete an element at a position from the list")
            print("[2] to delete elements from a range")
            print("[3] to replace elements value with another value")
            schoice = int(input("Enter your secondary choice: "))
            if schoice == 1:
                position = int(input("Enter the position: "))
                complex_list = delete_element_at_position(complex_list, position)
            elif schoice == 2:
                start = int(input("Enter the start position: "))
                end = int(input("Enter the end position: "))
                complex_list = delete_elements_from_range(complex_list, start, end)
            elif schoice == 3:
                print("Enter the complex number to replace:")
                old_real, old_imag = read_complex_number()
                print("Enter the new complex number:")
                new_real, new_imag = read_complex_number()
                complex_list = replace_elements_with_another_value(complex_list, old_real, old_imag, new_real, new_imag)
            else:
                print("Invalid choice")
        elif choice == 3:
            print("\n------------SUB-MENU------------")
            print("[1] to display only the imaginary part of the complex numbers")
            print("[2] to display the complex numbers with the module < 10")
            print("[3] to display the complex numbers with the module = 10")
            schoice = int(input("Enter your secondary choice: "))
            if schoice == 1:
                start = int(input("Enter the start position: "))
                end = int(input("Enter the end position: "))
                print_imaginary_part(complex_list, start, end)
            elif schoice == 2:
                print_module_less_than_10(complex_list)
            elif schoice == 3:
                print_module_equal_to_10(complex_list)
            else:
                print("Invalid choice")
        elif choice == 4:
            display_complex_numbers(complex_list)
        elif choice == 0:
            break

def test_append_complex_number():
    test_list = []
    test_list = append_complex_number(test_list, 3, 4)
    assert len(test_list) == 1
    assert str(test_list[0]) == "3 + 4i"
    print("test_append_complex_number passed")

def test_insert_complex_number():
    test_list = [Complex(1, 2), Complex(5, 6)]
    test_list = insert_complex_number(test_list, 1, 3, 4)
    assert len(test_list) == 3
    assert str(test_list[1]) == "3 + 4i"
    print("test_insert_complex_number passed")

def test_delete_element_at_position():
    test_list = [Complex(1, 2), Complex(3, 4), Complex(5, 6)]
    test_list = delete_element_at_position(test_list, 1)
    assert len(test_list) == 2
    assert str(test_list[1]) == "5 + 6i"
    print("test_delete_element_at_position passed")

def test_delete_elements_from_range():
    test_list = [Complex(1, 2), Complex(3, 4), Complex(5, 6), Complex(7, 8)]
    test_list = delete_elements_from_range(test_list, 1, 3)
    assert len(test_list) == 2
    assert str(test_list[1]) == "7 + 8i"
    print("test_delete_elements_from_range passed")

def test_replace_elements_with_another_value():
    test_list = [Complex(1, 2), Complex(3, 4), Complex(5, 6)]
    test_list = replace_elements_with_another_value(test_list, 3, 4, 9, 10)
    assert len(test_list) == 3
    assert str(test_list[0]) == "1 + 2i"
    assert str(test_list[1]) == "9 + 10i"
    assert str(test_list[2]) == "5 + 6i"
    print("test_replace_elements_with_another_value passed")

def test_calculate_module():
    # Test case 1: 3 + 4i (should be 5)
    complex1 = Complex(3, 4)
    assert calculate_module(complex1) == 5

    # Test case 2: 0 + 0i (should be 0)
    complex2 = Complex(0, 0)
    assert calculate_module(complex2) == 0

    # Test case 3: 1 + 1i (should be sqrt(2))
    complex3 = Complex(1, 1)
    assert calculate_module(complex3) == 2**0.5

    # Test case 4: 6 + 8i (should be 10)
    complex4 = Complex(6, 8)
    assert calculate_module(complex4) == 10


def run_tests():
    test_append_complex_number()
    test_insert_complex_number()
    test_delete_element_at_position()
    test_delete_elements_from_range()
    test_replace_elements_with_another_value()
    print("\nAll tests passed!")

def main():
    complex_list = []
    menu(complex_list)

if __name__ == "__main__":
    run_tests()  # Run tests before starting the main program
    main()
