import math

fill_shapes = ["Solid Cone", "Solid Cube", "Solid Cylinder", "Solid Rectangular Prism", "Solid Sphere",
               "Solid Spiral Coil", "Solid Triangular Trough"]

hollow_shapes = ["Hollow Cone", "Hollow Cube", "Hollow Cylinder", "Hollow Rectangular Prism", "Hollow Sphere",
                 "Hollow Spiral Coil", "Triangular Trough w/ an opening",
                 "Hollow Tube w/ two openings"]

materialskgm3 = {
    "Aluminum": 2700, "Polyethylene": 960,
    "Concrete": 2500, "Borosilicate Glass": 2350,
    "Stainless Steel": 8000
}

materialsgcm3 = {
    "Aluminum": 2.70, "Polyethylene": 0.96,
    "Concrete": 2.50, "Borosilicate Glass": 2.35,
    "Stainless Steel": 8.00
}

print("\n{}".format("Materializer".center(100, "~")))


def figure_app():
    def menu():
        print("Solid Shapes:\n")
        for index, item in enumerate(fill_shapes, start=1):
            print(f"{index}: {item}")

        print("\nHollow Shapes:\n")
        for index, item in enumerate(hollow_shapes, start=8):
            print(f"{index}: {item}")

        try:
            selection = int(input("\nPlease select a 3D Object: ").strip())
            if 1 <= selection <= len(fill_shapes):
                selected_materials = select_material_units(fill_shapes[selection - 1])
                if selected_materials == '1':
                    density, used_mat = material_choice(materialskgm3, '1')  # Pass '1' for kg/m^3
                    if selection == 2:  # Solid Cube
                        solid_cube_prompt(density, 'm', used_mat)
                    elif selection == 3:  # Solid Cylinder
                        solid_cylinder_prompt(density, 'm', used_mat)
                    elif selection == 4:  # Solid Rectangular Prism
                        solid_rectangle_prompt(density, 'm', used_mat)
                    elif selection == 5:  # Solid Sphere
                        solid_sphere_prompt(density, 'm', used_mat)
                    elif selection == 6:  # Solid Spiral Coil
                        solid_coil_prompt(density, 'm', used_mat)
                    elif selection == 7:  # Solid Spiral Coil
                        solid_triangle_trough_prompt(density, 'm', used_mat)
                    else:
                        solid_cone_prompt(density, 'm', used_mat)
                elif selected_materials == '2':
                    density, used_mat = material_choice(materialsgcm3, '2')  # Pass '2' for g/cm^3
                    if selection == 2:  # Solid Cube
                        solid_cube_prompt(density, 'cm', used_mat)
                    elif selection == 3:  # Solid Cylinder
                        solid_cylinder_prompt(density, 'cm', used_mat)
                    elif selection == 4:  # Solid Rectangular Prism
                        solid_rectangle_prompt(density, 'cm', used_mat)
                    elif selection == 5:  # Solid Sphere
                        solid_sphere_prompt(density, 'cm', used_mat)
                    elif selection == 6:  # Solid Spiral Coil
                        solid_coil_prompt(density, 'cm', used_mat)
                    elif selection == 7:  # Solid Spiral Coil
                        solid_triangle_trough_prompt(density, 'cm', used_mat)
                    else:
                        solid_cone_prompt(density, 'cm', used_mat)
                else:
                    print("Invalid selection. Please choose 1 or 2.")
            else:
                print("Invalid selection.")

        except ValueError:
            print("\nPlease enter an appropriate value.")
            input("Press Enter to continue...")

    def solid_cone(radius, height, density, unit, used_mat, shape):

        volume_cone = (1 / 3) * math.pi * (radius ** 2) * height
        mass = volume_cone * density

        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))
        print(f"Radius: {radius} meters")
        print(f"Height: {height} meters")
        print(f"Material Density: {density}")
        print(f"Volume: {volume_cone:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_cone_prompt(density, unit, used_mat):
        shape = "Solid Cone"
        print("\n{}\n".format("Solid Cone".center(100, "~")))

        radius = 0.0
        height = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        unit_choice = input("Enter the unit for radius and height (ft, in, m, cm, mm): \n").lower()
        factor = get_factor(unit_choice)
        if unit == 'm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            radius = float(input(f"Enter the radius (in {unit_choice}): ")) * factor / 100  # convert to meters
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_cone(radius, height, density, unit, used_mat, shape)

        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed * 1000, 4), "grams")

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_cube(side_length, density, unit, used_mat, shape):

        volume_cube = side_length ** 3

        mass = volume_cube * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))
        print(f"Side Length: {side_length} meters")
        print(f"Material Density: {density}")
        print(f"Volume: {volume_cube:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_cube_prompt(density, unit, used_mat):
        shape = "Solid Cube"
        print("\n{}\n".format("Solid Cube".center(100, "~")))

        side_length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        unit_choice = input("Enter the unit for side length (ft, in, m, cm, mm): \n").lower()
        factor = get_factor(unit_choice)
        if unit == 'm':
            side_length = float(input(f"\nEnter the side length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            side_length = float(input(f"Enter the side length (in {unit_choice}): ")) * factor / 100  # convert to
            # meters

        mass_needed = solid_cube(side_length, density, unit, used_mat, shape)

        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed * 1000, 4), "grams")

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_cylinder(radius, height, density, unit, used_mat, shape):

        volume_cylinder = math.pi * (radius ** 2) * height

        mass = volume_cylinder * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))
        print(f"Radius: {radius} meters")
        print(f"Height: {height} meters")
        print(f"Material Density: {density}")
        print(f"Volume: {volume_cylinder:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_cylinder_prompt(density, unit, used_mat):
        shape = "Solid Cylinder"
        print("\n{}\n".format("Solid Cylinder".center(100, "~")))

        radius = 0.0
        height = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        unit_choice = input("Enter the unit for radius and height (ft, in, m, cm, mm): \n").lower()
        factor = get_factor(unit_choice)
        if unit == 'm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            radius = float(input(f"Enter the radius (in {unit_choice}): ")) * factor / 100  # convert to meters
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_cylinder(radius, height, density, unit, used_mat, shape)

        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed * 1000, 4), "grams")

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_rectangle(length, width, height, density, unit, used_mat, shape):

        volume_prism = length * width * height

        mass = volume_prism * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))
        print(f"Length: {length} meters")
        print(f"Width: {width} meters")
        print(f"Height: {height} meters")
        print(f"Material Density: {density}")
        print(f"Volume: {volume_prism:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_rectangle_prompt(density, unit, used_mat):
        shape = "Solid Rectangular Prism"
        print("\n{}\n".format("Solid Rectangular Prism".center(100, "~")))

        length = 0.0
        width = 0.0
        height = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        unit_choice = input("Enter the unit for radius and height (ft, in, m, cm, mm): \n").lower()
        factor = get_factor(unit_choice)
        if unit == 'm':
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
            width = float(input(f"Enter the width (in {unit_choice}): ")) * factor
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor / 100
            width = float(input(f"Enter the width (in {unit_choice}): ")) * factor / 100
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor / 100

        mass_needed = solid_rectangle(length, width, height, density, unit, used_mat, shape)

        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed * 1000, 4), "grams")

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_sphere(radius, density, unit, used_mat, shape):

        volume_sphere = (4 / 3) * math.pi * radius ** 3

        mass = volume_sphere * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))
        print(f"Radius: {radius} meters")
        print(f"Material Density: {density}")
        print(f"Volume: {volume_sphere:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_sphere_prompt(density, unit, used_mat):
        shape = "Solid Sphere"
        print("\n{}\n".format("Solid Sphere".center(100, "~")))

        radius = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        unit_choice = input("Enter the unit for radius and height (ft, in, m, cm, mm): \n").lower()
        factor = get_factor(unit_choice)
        if unit == 'm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            radius = float(input(f"Enter the radius (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_sphere(radius, density, unit, used_mat, shape)

        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed * 1000, 4), "grams")

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_spiral_coil(pitch, length, radius, density, unit, used_mat, shape):
        # length of coil based on pitch
        height = pitch * length / (2 * math.pi * radius)

        # volume of the coil (cylindrical)
        volume_coil = math.pi * radius ** 2 * height

        mass = volume_coil * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))
        print(f"Pitch: {pitch} meters")
        print(f"Length: {length} meters")
        print(f"Radius: {radius} meters")
        print(f"Material Density: {density}")
        print(f"Volume: {volume_coil:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_coil_prompt(density, unit, used_mat):
        shape = "Solid Spiral Coil"
        print("\n{}\n".format("Solid Spiral Coil".center(100, "~")))

        pitch = 0.0
        length = 0.0
        radius = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        unit_choice = input("Enter the unit for radius and height (ft, in, m, cm, mm): \n").lower()
        factor = get_factor(unit_choice)
        if unit == 'm':
            pitch = float(input(f"\nEnter the pitch (in {unit_choice}): ")) * factor
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            pitch = float(input(f"\nEnter the pitch (in {unit_choice}): ")) * factor / 100
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor / 100
            radius = float(input(f"Enter the radius (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_spiral_coil(pitch, length, radius, density, unit, used_mat, shape)

        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed * 1000, 4), "grams")

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_triangular_trough(base_length, height, length, density, unit, used_mat, shape):

        volume_triangle_trough = 0.5 * base_length * height * length

        mass = volume_triangle_trough * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))
        print(f"Base Length: {base_length} meters")
        print(f"Height: {height} meters")
        print(f"Length: {length} meters")
        print(f"Material Density: {density}")
        print(f"Volume: {volume_triangle_trough:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_triangle_trough_prompt(density, unit, used_mat):
        shape = "Solid Triangular Trough"
        print("\n{}\n".format("Solid Triangular Trough".center(100, "~")))

        base_length = 0.0
        height = 0.0
        length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        unit_choice = input("Enter the unit for radius and height (ft, in, m, cm, mm): \n").lower()
        factor = get_factor(unit_choice)
        if unit == 'm':
            base_length = float(input(f"\nEnter the base_length (in {unit_choice}): ")) * factor
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            base_length = float(input(f"\nEnter the base_length (in {unit_choice}): ")) * factor / 100
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor / 100
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor / 100

        mass_needed = solid_triangular_trough(base_length, height, length, density, unit, used_mat, shape)

        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:", round(mass_needed * 1000, 4), "grams")

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def get_factor(unit_choice):
        if unit_choice == 'ft':
            factor = 0.3048  # 1 foot = 0.3048 meters
        elif unit_choice == 'in':
            factor = 0.0254  # 1 inch = 0.0254 meters
        elif unit_choice == 'cm':
            factor = 0.01  # 1 centimeter = 0.01 meters
        elif unit_choice == 'mm':
            factor = 0.001  # 1 millimeter = 0.001 meters
        else:
            factor = 100  # Default to meters
        return factor

    def get_mass_unit(unit, mass):
        if unit == 'm':
            mass_unit = "kilograms"
            mass_formatted = mass
        elif unit == 'cm':
            mass_unit = "grams"
            mass_formatted = mass * 1000
        else:
            mass_unit = "units"  # pag wala nilagay si user magiging units lang
            mass_formatted = mass
        return mass_unit, mass_formatted

    def user_choice():
        choice = input(f"\nDo you want to solve for a 3D Figure again (Yes/No)?\n")
        if choice.lower() == "yes":
            menu()
        elif choice.lower() == "no":
            print("The Materializer will now exit.")
            exit()

    def material_choice(materials, unit):
        print("\n{}".format("Materials".center(70, "-")))
        print("\nMaterials:")
        for index, (material, density) in enumerate(materials.items(), start=1):
            if unit == '1':
                density_str = f"{density} kg/m^3"
                print(f"{index}: {material} - Density: {density_str}")
            elif unit == '2':
                density_str = f"{density} g/cm^3"
                print(f"{index}: {material} - Density: {density_str}")

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

    def select_material_units(shape):
        print("\n{}".format("Unit Selection".center(70, "-")))
        selected_materials = None
        while selected_materials not in ['1', '2']:
            selected_materials = input(f"\nSelect a unit for the material of the {shape}:\n"
                                       "1. kg/m^3 (for larger objects / answers in Kilograms)"
                                       "\n2. g/cm^3 (for smaller objects / answers in Grams)\nChoice: ")
        return selected_materials

    menu()


figure_app()
