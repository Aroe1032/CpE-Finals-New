import math

fill_shapes = ["Solid Cone", "Solid Cube", "Solid Cylinder", "Solid Rectangular Prism", "Solid Sphere",
               "Solid Spiral Coil", "Solid Triangular Trough", ]

hollow_shapes = ["Hollow Cone", "Hollow Cube", "Hollow Cylinder", "Hollow Rectangular Prism", "Hollow Sphere",
                 "Hollow Spiral Coil", "Triangular Trough w/ an opening",
                 "Hollow Tube w/ two openings"]

materials = {"Aluminum": 2700, "Polyethylene": 960, "Concrete": 2500,
             "Borosilicate Glass": 2350, "Stainless Steel": 8000}


def figure_app():
    def menu():
        while True:
            print("\n{}".format("Materializer".center(100, "~")))

            print("Solid Shapes:\n")
            for index, item in enumerate(fill_shapes, start=1):
                print(f"{index}: {item}")

            print("\nHollow Shapes:\n")
            for index, item in enumerate(hollow_shapes, start=len(fill_shapes) + 1):
                print(f"{index}: {item}")

            try:
                selection = int(input("\nPlease select a 3D Object: ").strip())
                if 1 <= selection <= len(fill_shapes) + len(hollow_shapes):  # Check if selection is within the valid
                    # range
                    if selection <= len(fill_shapes):
                        density, used_mat = material_choice(fill_shapes[selection - 1])
                        # Call the function corresponding to the selected solid shape
                        match selection:
                            case 1:
                                solid_cone_display(density, used_mat)
                            case 2:
                                solid_cube_display(density, used_mat)
                            case 3:
                                solid_cylinder_display(density, used_mat)
                            case 4:
                                solid_rectangle_display(density, used_mat)
                            case 5:
                                solid_sphere_display(density, used_mat)
                            case 6:
                                solid_coil_display(density, used_mat)
                            case 7:
                                solid_trough_display(density, used_mat)
                    else:
                        density, used_mat = material_choice(hollow_shapes[selection - len(fill_shapes) - 1])
                        # Call the function corresponding to the selected hollow shape
                        match selection:
                            case 8:
                                hollow_cone_display(density, used_mat)
                            case 9:
                                hollow_cube_display(density, used_mat)
                            case 10:
                                hollow_cylinder_display(density, used_mat)
                            case 11:
                                hollow_prism_display(density, used_mat)
                            case 12:
                                hollow_sphere_display(density, used_mat)
                            case 13:
                                hollow_coil_display(density, used_mat)
                            case 14:
                                hollow_trough_display(density, used_mat)
                            case 15:
                                hollow_tube_display(density, used_mat)
                else:
                    print("Invalid selection. Please enter a number between 1 and",
                          len(fill_shapes) + len(hollow_shapes))
            except ValueError:
                print("\nPlease enter an appropriate value.")
                input("Press Enter to continue...")

    def solid_cone(radius, height, density):
        # Calculate volume of the cone
        volume_cone = (1 / 3) * math.pi * radius ** 2 * height

        # Calculate mass of aluminum
        mass_aluminum = volume_cone * density

        return mass_aluminum

    def solid_cone_display(density, used_mat):
        shape = "Solid Cone"
        print("\n{}\n".format("Solid Cone".center(100, "~")))

        print(f"{used_mat} {shape}\n")
        radius = float(input("wat radius: "))
        height = float(input("wat height: "))  # meters

        mass_needed = solid_cone(radius, height, density)
        print(f"Mass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def solid_cube(side_length, density):
        # Calculate volume of the cube
        volume_cube = side_length ** 3

        # Calculate mass of aluminum
        mass_aluminum = volume_cube * density

        return mass_aluminum

    def solid_cube_display(density, used_mat):
        shape = "Solid Cube"
        print("\n{}\n".format("Solid Cube".center(100, "~")))

        print(f"{used_mat} {shape}\n")
        side_length = float(input("What is your side length?\n"))  # meters

        mass_needed = solid_cube(side_length, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def solid_cylinder(radius, height, density):
        # Calculate volume of the cylinder
        volume_cylinder = math.pi * (radius ** 2) * height

        # Calculate mass of aluminum
        mass_aluminum = volume_cylinder * density

        return mass_aluminum

    def solid_cylinder_display(density, used_mat):
        shape = "Solid Cylinder"
        print("\n{}\n".format("Solid Cylinder".center(100, "~")))

        print(f"{used_mat} {shape}\n")
        radius = float(input("wat radius: "))  # meters
        height = float(input("wat height: "))  # meters

        mass_needed = solid_cylinder(radius, height, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def solid_rectangle(length, width, height, density):
        # Calculate volume of the prism
        volume_prism = length * width * height

        # Calculate mass of aluminum
        mass_aluminum = volume_prism * density

        return mass_aluminum

    def solid_rectangle_display(density, used_mat):
        # Example usage
        shape = "Solid Rectangular Prism"
        print("\n{}".format("Solid Rectangular Prism".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        length = float(input("wat length: "))  # meters
        width = float(input("wat width: "))  # meters
        height = float(input("wat height: "))  # meters

        mass_needed = solid_rectangle(length, width, height, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def solid_sphere(radius, density):
        # Calculate volume of the sphere
        volume_sphere = (4 / 3) * math.pi * radius ** 3

        # Calculate mass of aluminum
        mass_aluminum = volume_sphere * density

        return mass_aluminum

    def solid_sphere_display(density, used_mat):
        shape = "Solid Sphere"
        print("\n{}".format("Solid Sphere".center(70, "-")))

        # Example usage
        print(f"{used_mat} {shape}\n")
        radius = float(input("wat radius: "))  # meters

        mass_needed = solid_sphere(radius, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def solid_spiral_coil(radius, pitch, length, density):
        # Calculate the height (or length) of the coil based on the pitch
        height = pitch * length / (2 * math.pi * radius)

        # Calculate the volume of the coil (cylindrical shape)
        volume_coil = math.pi * radius ** 2 * height

        # Calculate mass of aluminum
        mass_aluminum = volume_coil * density

        return mass_aluminum

    def solid_coil_display(density, used_mat):
        shape = "Solid Spiral Coil"
        print("\n{}".format("Solid Spiral Coil".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        # Example usage
        radius = float(input("wat radius: "))  # meters (outer radius minus thickness)
        pitch = float(input("wat pitch: "))  # meters (distance between each turn)
        length = float(input("wat length: "))

        mass_needed = solid_spiral_coil(radius, pitch, length, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")

        user_choice()

    def solid_triangular_trough(base_length, height, length, density):
        # Calculate volume of the triangular trough (prism with a triangular base)
        volume_trough = 0.5 * base_length * height * length

        # Calculate mass of aluminum
        mass_aluminum = volume_trough * density

        return mass_aluminum

    def solid_trough_display(density, used_mat):
        shape = "Solid Triangular Trough"
        print("\n{}".format("Solid Triangular Trough".center(70, "-")))
        # Example usage

        print(f"{used_mat} {shape}\n")
        base_length = float(input("wat base: "))  # meters
        height = float(input("wat height: "))  # meters
        length = float(input("wat length: "))  # meters

        mass_needed = solid_triangular_trough(base_length, height, length, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_cone(outer_radius, inner_radius, height, density):
        # Calculate volume of the outer cone
        volume_outer_cone = (1 / 3) * math.pi * outer_radius ** 2 * height

        # Calculate volume of the inner cone
        volume_inner_cone = (1 / 3) * math.pi * inner_radius ** 2 * height

        # Calculate volume of the aluminum shell
        volume_aluminum_shell = volume_outer_cone - volume_inner_cone

        # Calculate mass of aluminum
        mass_aluminum = volume_aluminum_shell * density

        return mass_aluminum

    def hollow_cone_display(density, used_mat):
        shape = "Hollow Cone"
        print("\n{}".format("Hollow Cone".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        outer_radius = float(input("wat outer radius: "))  # meters (outer radius)
        inner_radius = float(input("wat inner radius: "))  # meters (inner radius)
        height = float(input("wat height: "))  # meters

        mass_needed = hollow_cone(outer_radius, inner_radius, height, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_cube(outer_side_length, inner_side_length, density):
        # Calculate volume of the outer cube
        volume_outer_cube = outer_side_length ** 3

        # Calculate volume of the inner cube
        volume_inner_cube = inner_side_length ** 3

        # Calculate volume of the aluminum shell
        volume_aluminum_shell = volume_outer_cube - volume_inner_cube

        # Calculate mass of aluminum
        mass_aluminum = volume_aluminum_shell * density

        return mass_aluminum

    def hollow_cube_display(density, used_mat):
        shape = "Hollow Cube"
        print("\n{}".format("Hollow Cube".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        # Example usage
        outer_side_length = float(input("wat outer side length: "))  # meters (outer side length)
        inner_side_length = float(input("wat inner side length: "))  # meters (inner side length)

        mass_needed = hollow_cube(outer_side_length, inner_side_length, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_cylinder(outer_radius, inner_radius, height, density):
        # Calculate volume of the outer cylinder
        volume_outer_cylinder = math.pi * outer_radius ** 2 * height

        # Calculate volume of the inner cylinder
        volume_inner_cylinder = math.pi * inner_radius ** 2 * height

        # Calculate volume of the aluminum shell
        volume_aluminum_shell = volume_outer_cylinder - volume_inner_cylinder

        # Calculate mass of aluminum
        mass_aluminum = volume_aluminum_shell * density

        return mass_aluminum

    def hollow_cylinder_display(density, used_mat):
        shape = "Hollow Cylinder"
        print("\n{}".format("Hollow Cylinder".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        outer_radius = float(input("wat outer radius: "))  # meters
        inner_radius = float(input("wat inner radius: "))  # meters
        height = float(input("wat height: "))  # meters

        mass_needed = hollow_cylinder(outer_radius, inner_radius, height, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_rectangular_prism(length, width, height, thickness, density):
        # Calculate inner dimensions
        inner_length = length - 2 * thickness
        inner_width = width - 2 * thickness
        inner_height = height - 2 * thickness

        # Calculate volume of the outer prism
        volume_outer_prism = length * width * height

        # Calculate volume of the inner prism
        volume_inner_prism = inner_length * inner_width * inner_height

        # Calculate volume of the aluminum shell
        volume_aluminum_shell = volume_outer_prism - volume_inner_prism

        # Calculate mass of aluminum
        mass_aluminum = volume_aluminum_shell * density

        return mass_aluminum

    def hollow_prism_display(density, used_mat):
        shape = "Hollow Rectangular Prism"
        print("\n{}".format("Hollow Rectangular Prism".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        # Example usage
        length = float(input("wat length: "))  # meters
        width = float(input("wat width: "))  # meters
        height = float(input("wat height: "))  # meters
        thickness = float(input("wat thickness: "))  # meters (5 mm)

        mass_needed = hollow_rectangular_prism(length, width, height, thickness, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_sphere(outer_radius, thickness, density):
        # Calculate inner radius
        inner_radius = outer_radius - thickness

        # Calculate volume of the outer sphere
        volume_outer_sphere = (4 / 3) * math.pi * outer_radius ** 3

        # Calculate volume of the inner sphere
        volume_inner_sphere = (4 / 3) * math.pi * inner_radius ** 3

        # Calculate volume of the aluminum shell
        volume_aluminum_shell = volume_outer_sphere - volume_inner_sphere

        # Calculate mass of aluminum
        mass_aluminum = volume_aluminum_shell * density

        return mass_aluminum

    def hollow_sphere_display(density, used_mat):
        shape = "Hollow Sphere"
        print("\n{}".format("Hollow Sphere".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        outer_radius = float(input("wat outer radius: "))  # meters
        thickness = float(input("wat thickness: "))  # meters (5 cm)

        mass_needed = hollow_sphere(outer_radius, thickness, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_spiral_coil(outer_radius, inner_radius, thickness, pitch, length):
        # Calculate the total height (or length) of the coil
        total_height = pitch * length

        # Calculate the volume of one coil turn (cylindrical shell)
        volume_one_turn = math.pi * (outer_radius ** 2 - inner_radius ** 2) * thickness

        # Calculate the number of turns
        num_turns = math.ceil(total_height / thickness)

        # Calculate the volume of all coil turns
        volume_all_turns = volume_one_turn * num_turns

        return volume_all_turns

    def hollow_coil_display(density, used_mat):
        shape = "Hollow Spiral Coil"
        print("\n{}".format("Hollow Spiral Coil".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        outer_radius = float(input("wat outer radius: "))  # meters
        inner_radius = float(input("wat inner radius: "))  # meters (outer radius minus thickness)
        thickness = float(input("wat thickness: "))  # meters (thickness of the coil)
        pitch = float(input("wat pitch: "))  # meters (distance between each turn)
        length = float(input("wat length: "))  # meters (length of the coil)

        volume_needed = hollow_spiral_coil(outer_radius, inner_radius, thickness, pitch, length)
        mass_needed = volume_needed * density
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_triangular_trough(base_length, height, length, thickness, density):
        # Calculate inner dimensions
        inner_base_length = base_length - 2 * thickness
        inner_height = height - 2 * thickness
        inner_length = length - 2 * thickness

        # Calculate volume of the outer triangular trough (prism with a triangular base)
        volume_outer_trough = 0.5 * base_length * height * length

        # Calculate volume of the inner triangular trough (prism with a triangular base)
        volume_inner_trough = 0.5 * inner_base_length * inner_height * inner_length

        # Calculate volume of the aluminum shell
        volume_aluminum_shell = volume_outer_trough - volume_inner_trough

        # Calculate mass of aluminum
        mass_aluminum = volume_aluminum_shell * density

        return mass_aluminum

    def hollow_trough_display(density, used_mat):
        shape = "Hollow Triangular Trough"
        print("\n{}".format("Hollow Triangular Trough w/ base opening".center(70, "-")))
        # Example usage

        print(f"{used_mat} {shape}\n")
        base_length = float(input("wat base length: "))  # meters
        height = float(input("wat height: "))  # meters
        length = float(input("wat length: "))  # meters
        thickness = float(input("wat thickness: "))  # meters

        mass_needed = hollow_triangular_trough(base_length, height, length, thickness,
                                               density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def hollow_tube(outer_radius, inner_radius, length, thickness, density):
        # Calculate volume of the outer cylinder
        volume_outer_cylinder = math.pi * outer_radius ** 2 * length

        # Calculate volume of the inner cylinder (excluding the openings)
        volume_inner_cylinder = math.pi * inner_radius ** 2 * length

        # Calculate volume of the aluminum shell (excluding the openings)
        volume_aluminum_shell = volume_outer_cylinder - volume_inner_cylinder

        # Subtract the volume of the openings
        volume_openings = 2 * math.pi * inner_radius ** 2 * thickness
        volume_aluminum_shell -= volume_openings

        # Calculate mass of aluminum
        mass_aluminum = volume_aluminum_shell * density

        return mass_aluminum

    def hollow_tube_display(density, used_mat):
        shape = "Hollow Tube"
        print("\n{}".format("Hollow Tube w/ end openings".center(70, "-")))

        print(f"{used_mat} {shape}\n")
        outer_radius = float(input("wat outer radius: "))  # meters
        inner_radius = float(input("wat inner radius: "))  # meters
        length = float(input("wat length: "))  # meters
        thickness = float(input("wat thickness: "))  # meters (5 cm)

        mass_needed = hollow_tube(outer_radius, inner_radius, length, thickness, density)
        print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 2), "kg")
        print("{}".format("-".center(70, "-")))

        user_choice()

    def user_choice():
        choice = input(f"\nDo you want to solve for another shape again (Yes/No)?\n")
        if choice.lower() == "yes":
            print("{}".format("-".center(70, "-")))
            menu()
        elif choice.lower() == "no":
            print("The program will now exit.")
            exit()
        else:
            input("Please enter an appropriate value.\n Press Enter to continue...")

    def material_choice(shape):
        print("\n{}\n".format(f"{shape}".center(100, "~")))
        print("\nPlease select a Material:\n")
        for index, (key, value) in enumerate(materials.items(), start=1):
            # Using items() to iterate over key-value pairs
            print(f"{index}. {key}: {value} kg/m3")

        while True:
            try:
                selection = int(input("\nSelect a material: "))
                if 1 <= selection <= len(materials):
                    material = list(materials.keys())[selection - 1]
                    density = materials[material]
                    used_mat = material
                    return density, used_mat
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    menu()


figure_app()
