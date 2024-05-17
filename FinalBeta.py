import math

SHAPES = [
    "Solid Cone",
    "Solid Cube",
    "Solid Cylinder",
    "Solid Rectangular Prism",
    "Solid Sphere",
    "Solid Triangular Trough",
    "Solid Octahedron",
    "Solid Ring",
    "Solid Spiral Coil",
    "Hollow Tube w/ Two Openings",
    "Hollow Hexagonal Strut",
    "Hollow Trapezoid Trough w/ Base Opening",
]

materialskgm3 = {
    "Aluminum": 2700,
    "Polyethylene": 960,
    "Concrete": 2500,
    "Borosilicate Glass": 2350,
    "Stainless Steel": 8000,
}

materialsgcm3 = {
    "Aluminum": 2.70,
    "Polyethylene": 0.96,
    "Concrete": 2.50,
    "Borosilicate Glass": 2.35,
    "Stainless Steel": 8.00,
}


def figure_app():
    def menu():
        print("\n{}".format("MatFabricator".center(100, "~")))
        print("3-Dimensional Figures:\n")
        for index, item in enumerate(SHAPES, start=1):
            print(f"{index}: {item}")

        try:
            selection = input("\nPlease select a 3D Object [1-12]\n(type EXIT to exit): ").strip()
            if selection.lower() == "exit":
                print("\nThe MatFabricator will now exit.\nThank you for using the app made by Accenorix.")
                exit()
            elif 1 <= int(selection) <= len(SHAPES):
                selected_materials = select_material_units(SHAPES[int(selection) - 1])
                materials = materialskgm3 if selected_materials == '1' else materialsgcm3
                density, used_mat, density_unit = material_choice(materials, selected_materials)
                unit = 'm' if selected_materials == '1' else 'cm'

                prompt_functions = {
                    1: solid_cone_prompt,
                    2: solid_cube_prompt,
                    3: solid_cylinder_prompt,
                    4: solid_rectangle_prompt,
                    5: solid_sphere_prompt,
                    6: solid_triangle_trough_prompt,
                    7: solid_octahedron_prompt,
                    8: solid_ring_prompt,
                    9: solid_spiral_coil_prompt,
                    10: hollow_tube_prompt,
                    11: hollow_hexagonal_strut_prompt,
                    12: hollow_trapezoid_trough_with_base_opening_prompt
                }

                if int(selection) in prompt_functions:
                    prompt_functions[int(selection)](density, unit, used_mat, density_unit)
                else:
                    menu()

            else:
                input("Invalid selection. Please select a shape from the list.\nPress Enter to continue...")
                menu()

        except ValueError:
            input("Invalid selection. Please input a proper value.\n"
                  "Returning to the Menu to ensure accuracy. Press Enter to continue...")
            menu()

    def solid_cone(radius, height, density, unit, used_mat, shape, density_unit):

        volume_cone = (1 / 3) * math.pi * (radius ** 2) * height
        mass = volume_cone * density

        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius:,.8f} meters")
        print(f"Height: {height:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_cone:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_cone_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Cone"
        print("\n{}\n".format("Solid Cone".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
        height = float(input(f"Enter the height (in {unit_choice}): ")) * factor

        mass_needed = solid_cone(radius, height, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_cube(side_length, density, unit, used_mat, shape, density_unit):

        volume_cube = side_length ** 3

        mass = volume_cube * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Side Length: {side_length:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_cube:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_cube_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Cube"
        print("\n{}\n".format("Solid Cube".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        side_length = (float(input(f"Enter the side length (in {unit_choice}): ")) * factor)

        mass_needed = solid_cube(side_length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_cylinder(radius, height, density, unit, used_mat, shape, density_unit):

        volume_cylinder = math.pi * (radius ** 2) * height

        mass = volume_cylinder * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius:,.8f} meters")
        print(f"Height: {height:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_cylinder:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_cylinder_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Cylinder"
        print("\n{}\n".format("Solid Cylinder".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
        height = float(input(f"Enter the height (in {unit_choice}): ")) * factor

        mass_needed = solid_cylinder(radius, height, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_rectangle(length, width, height, density, unit, used_mat, shape, density_unit):

        volume_prism = length * width * height

        mass = volume_prism * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Length: {length:,.8f} meters")
        print(f"Width: {width:,.8f} meters")
        print(f"Height: {height:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_prism:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_rectangle_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Rectangular Prism"
        print("\n{}\n".format("Solid Rectangular Prism".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
        width = float(input(f"Enter the width (in {unit_choice}): ")) * factor
        height = float(input(f"Enter the height (in {unit_choice}): ")) * factor

        mass_needed = solid_rectangle(length, width, height, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_sphere(radius, density, unit, used_mat, shape, density_unit):

        volume_sphere = (4 / 3) * math.pi * radius ** 3

        mass = volume_sphere * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_sphere:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_sphere_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Sphere"
        print("\n{}\n".format("Solid Sphere".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        radius = (float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor)

        mass_needed = solid_sphere(radius, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_triangular_trough(base_length, height, length, density, unit, used_mat, shape, density_unit):

        volume_triangle_trough = 0.5 * base_length * height * length

        mass = volume_triangle_trough * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Base Length: {base_length:,.8f} meters")
        print(f"Height: {height:,.8f} meters")
        print(f"Length: {length:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_triangle_trough:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_triangle_trough_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Triangular Trough"
        print("\n{}\n".format("Solid Triangular Trough".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        base_length = (float(input(f"\nEnter the base_length (in {unit_choice}): ")) * factor)
        height = float(input(f"Enter the height (in {unit_choice}): ")) * factor
        length = float(input(f"Enter the length (in {unit_choice}): ")) * factor

        mass_needed = solid_triangular_trough(base_length, height, length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_octahedron(side_length, density, unit, used_mat, shape, density_unit):
        volume_octahedron = (side_length ** 3) / (3 * math.sqrt(2))

        mass = volume_octahedron * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Side Length: {side_length:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_octahedron:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_octahedron_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Octahedron"
        print("\n{}\n".format("Solid Octahedron".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        side_length = (float(input(f"\nEnter the side length (in {unit_choice}): ")) * factor)

        mass_needed = solid_octahedron(side_length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_ring(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit):

        volume_ring = math.pi * height * (outer_radius ** 2 - inner_radius ** 2)
        mass = volume_ring * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Height: {height:,.8f} meters")
        print(f"Outer Radius: {outer_radius:,.8f} meters")
        print(f"Inner Radius: {inner_radius:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_ring:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_ring_prompt(density, unit, used_mat, density_unit):
        shape = "Ring"
        print("\n{}\n".format("Ring".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
        outer_radius = (float(input(f"Enter the outer radius (in {unit_choice}): ")) * factor)
        inner_radius = (float(input(f"Enter the inner radius (in {unit_choice}): ")) * factor)

        mass_needed = solid_ring(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def solid_spiral_coil(radius, pitch, length, density, unit, used_mat, shape, density_unit):

        cross_sectional_area = math.pi * radius ** 2
        coil_length = math.sqrt(radius ** 2 + pitch ** 2) / (2 * math.pi)
        volume_spiral_coil = cross_sectional_area * coil_length * length

        mass = volume_spiral_coil * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius:,.8f} meters")
        print(f"Pitch: {pitch:,.8f} meters")
        print(f"Length: {length:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_spiral_coil:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def solid_spiral_coil_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Spiral Coil"
        print("\n{}\n".format("Solid Spiral Coil".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
        pitch = float(input(f"Enter the pitch (in {unit_choice}): ")) * factor
        length = float(input(f"Enter the length (in {unit_choice}): ")) * factor

        mass_needed = solid_spiral_coil(radius, pitch, length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def hollow_tube(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit):
        volume_hollow_tube = math.pi * height * (outer_radius ** 2 - inner_radius ** 2)

        mass = volume_hollow_tube * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Inner Radius: {inner_radius:,.8f} meters")
        print(f"Outer Radius: {outer_radius:,.8f} meters")
        print(f"Height: {height:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_hollow_tube:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def hollow_tube_prompt(density, unit, used_mat, density_unit):
        shape = "Hollow Tube w/ Two Openings"
        print("\n{}\n".format("Hollow Tube w/ Two Openings".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
        outer_radius = (float(input(f"Enter the outer radius (in {unit_choice}): ")) * factor)
        inner_radius = (float(input(f"Enter the inner_radius (in {unit_choice}): ")) * factor)

        mass_needed = hollow_tube(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def hollow_hexagonal_strut(outer_side_length, inner_side_length, length, density, unit, used_mat, shape,
                               density_unit):

        outer_area = 3 * math.sqrt(3) * (outer_side_length ** 2) / 2
        inner_area = 3 * math.sqrt(3) * (inner_side_length ** 2) / 2
        cross_sectional_area = outer_area - inner_area
        volume_sphere = cross_sectional_area * length

        mass = volume_sphere * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Outer Side Length: {outer_side_length:,.8f} meters")
        print(f"Inner Side Length: {inner_side_length:,.8f} meters")
        print(f"Length: {length:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_sphere:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def hollow_hexagonal_strut_prompt(density, unit, used_mat, density_unit):
        shape = "Hollow Hexagonal Strut"
        print("\n{}\n".format("Hollow Hexagonal Strut".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        outer_side_length = (float(input(f"\nEnter the outer side length (in {unit_choice}): ")) * factor)
        inner_side_length = (float(input(f"Enter the inner side length (in {unit_choice}): ")) * factor)
        length = float(input(f"Enter the length (in {unit_choice}): ")) * factor

        mass_needed = hollow_hexagonal_strut(outer_side_length, inner_side_length, length, density, unit, used_mat,
                                             shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def hollow_trapezoid_trough_with_base_opening(
            height,
            outer_bottom_base_length,
            inner_bottom_base_length,
            inner_top_base_length,
            outer_top_base_length,
            density,
            unit,
            used_mat,
            shape,
            density_unit,
    ):

        volume_outer = height * (outer_bottom_base_length + outer_top_base_length) / 2
        volume_inner = height * (inner_bottom_base_length + inner_top_base_length) / 2
        volume_hollow_trapezoid_trough_with_base_opening = volume_outer - volume_inner

        mass = volume_hollow_trapezoid_trough_with_base_opening * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Height: {height:,.8f} meters")
        print(f"Outer Bottom Base Length: {outer_bottom_base_length:10f} meters")
        print(f"Inner Bottom Base Length: {inner_bottom_base_length:,.8f} meters")
        print(f"Outer Top Base Length: {outer_top_base_length:,.8f} meters")
        print(f"Inner Top Base Length: {inner_top_base_length:,.8f} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_hollow_trapezoid_trough_with_base_opening:,.8f} m^3")
        initial_result(used_mat, mass_formatted)

        return mass

    def hollow_trapezoid_trough_with_base_opening_prompt(density, unit, used_mat, density_unit):
        shape = "Hollow Trapezoid Trough w/ Base Opening"
        print("\n{}\n".format("Hollow Trapezoid Trough w/ Base Opening".center(100, "~")))

        print(f"{used_mat} {shape}")

        factor, unit_choice = get_factor()
        height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
        outer_bottom_base_length = (float(input(f"Enter the outer bottom base length (in {unit_choice}): ")) * factor)
        inner_bottom_base_length = (float(input(f"Enter the inner bottom base length (in {unit_choice}): ")) * factor)
        outer_top_base_length = (float(input(f"Enter the outer top base length (in {unit_choice}): ")) * factor)
        inner_top_base_length = (float(input(f"Enter the inner top base length (in {unit_choice}): ")) * factor)

        mass_needed = hollow_trapezoid_trough_with_base_opening(
            height,
            outer_bottom_base_length,
            inner_bottom_base_length,
            inner_top_base_length,
            outer_top_base_length,
            density,
            unit,
            used_mat,
            shape,
            density_unit,
        )
        print_mass_needed(mass_needed, used_mat, shape, unit)

        user_choice()

    def result_header(used_mat, shape):
        print("{}\n".format("-".center(100, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(100)))

    def initial_result(used_mat, mass_formatted):
        print(f"Required Mass of {used_mat} (in kg): {mass_formatted:,.8f} kilograms")

    def print_mass_needed(mass_needed, used_mat, shape, unit):
        if unit == "m":
            mass_unit = "kilograms"
            mass_formatted = f"{mass_needed:,.4f}"
        elif unit == "cm":
            mass_unit = "grams"
            mass_needed *= 1000000
            mass_formatted = f"{mass_needed:,.4f}"
        else:
            return

        print(f"\nMass of {used_mat} needed for:\n{used_mat} {shape} = {mass_formatted} {mass_unit}")
        print("{}\n".format("-".center(100, "-")))

    def get_factor():
        while True:
            try:
                unit_choice = input("\nEnter the unit for the shape parameters (ft, in, m, cm, mm)"
                                    "\n(type MENU/EXIT to go back/exit): ").lower()
                if unit_choice.lower() == "menu":
                    menu()
                elif unit_choice.lower() == "exit":
                    print("\nThe MatFabricator will now exit.\nThank you for using the app made by Accenorix.")
                    exit()
                elif unit_choice in ["ft", "in", "cm", "mm", "m"]:
                    break
                else:
                    input("Invalid unit choice. Please enter one of the following: ft, in, m, cm, mm."
                          "\nPress Enter to continue...\n")
            except ValueError:
                input("\nPlease select a proper value. Press Enter to continue...\n")
                get_factor()

        if unit_choice == "ft":
            factor = 0.3048
        elif unit_choice == "in":
            factor = 0.0254
        elif unit_choice == "cm":
            factor = 0.01
        elif unit_choice == "mm":
            factor = 0.001
        else:
            factor = 1

        return factor, unit_choice

    def get_mass_unit(unit, mass):
        if unit == "m":
            mass_unit = "kilograms"
            mass_formatted = mass
        elif unit == "cm":
            mass_unit = "grams"
            mass_formatted = mass * 1000
        else:
            mass_unit = "units"
            mass_formatted = mass
        return mass_unit, mass_formatted

    def user_choice():
        choice = input(f"Do you want to solve for a 3D Figure again (Yes/No)?\n")
        if choice.lower() == "yes":
            menu()
        elif choice.lower() == "no":
            print("\nThe MatFabricator will now exit.\nThank you for using the app made by Accenorix.")
            exit()
        else:
            input("Select from the choices (yes/no). Press Enter to continue...\n")
            user_choice()

    def material_choice(materials, unit):
        while True:
            try:
                print("\n{}".format("Materials".center(100, "-")))
                print("\nMaterials:")
                for index, (material, density) in enumerate(materials.items(), start=1):
                    if unit == "1":
                        density_str = f"{density} kg/m^3"
                        print(f"{index}: {material} - Density: {density_str}")
                    elif unit == "2":
                        density_str = f"{density} g/cm^3"
                        print(f"{index}: {material} - Density: {density_str}")
                        
                selection = input("\nSelect a material (type MENU/EXIT to go back/exit): ")
                density_unit = ""
                if selection.lower() == "menu":
                    menu()
                if selection.lower() == "exit":
                    print("\nThe MatFabricator will now exit.\nThank you for using the app made by Accenorix.")
                    exit()
                elif 1 <= int(selection) <= len(materials):
                    if unit == "1":
                        density_unit = "kg/m^3"
                    elif unit == "2":
                        density_unit = "g/cm^3"
                    material = list(materials.keys())[int(selection) - 1]
                    density = materials[material]
                    used_mat = material
                    return density, used_mat, density_unit
                else:
                    input("Invalid selection. Please select a number.\nPress Enter to continue...")
            except ValueError:
                input("Invalid input. Please select from the list.\nPress Enter to continue...")

    def select_material_units(shape):
        print("\n{}".format("Unit Selection".center(100, "-")))
        selected_materials = None
        while selected_materials not in ["1", "2"]:
            selected_materials = input(
                f"\nSelect a unit for the material of the {shape}:\n"
                "1. kg/m^3 (for larger objects / answers in Kilograms)"
                "\n2. g/cm^3 (for smaller objects / answers in Grams)\n\nChoice (type MENU/EXIT to go back/exit): "
            )
            if selected_materials.lower() == "menu":
                menu()
            elif selected_materials.lower() == "exit":
                print("\nThe MatFabricator will now exit.\nThank you for using the app made by Accenorix.")
                exit()
            elif selected_materials not in ["1", "2"]:
                input("Please select a unit from the list. Press Enter to continue...")
                print("\n{}".format("Unit Selection".center(70, "-")))
        return selected_materials

    menu()


figure_app()
