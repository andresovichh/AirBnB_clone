for key, value in my_dict.items():
                """this for loop utilise a key value pair to run
                    my_dict.items() and create a dictionary of key and value"""
                new_object = key.split('.')
                class_name = new_object[0]
                """new_object is equal to key.split('.')[0]
                    this split the key and take the first part of the key"""
                self.new(eval("{}".format(class_name))(**value))
                """this if statement is used to create a new object
                    with the class name of new_object and its value"""