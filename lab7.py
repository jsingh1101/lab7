def test_a_instantiate_class_1(self):
    """Test for Creating object - should fail with string arguments"""
    try:
        import lab7a as lab7aStudent
        student = lab7aStudent.Student('John', '12345')
    except Exception as e:
        print("Caught Exception (Debug):", e)
        return  # Pass the test if exception is caught
    self.fail("Exception not raised for string arguments")

