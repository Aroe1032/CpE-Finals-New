import math

SHAPES = ["Solid Cone",
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
          "Hollow Trapezoid Trough w/ Base Opening"]

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
        print("3-Dimensional Figures:\n")
        for index, item in enumerate(SHAPES, start=1):
            print(f"{index}: {item}")

        try:
            selection = int(input("\nPlease select a 3D Object: ").strip())
            if 1 <= selection <= len(SHAPES):
                selected_materials = select_material_units(SHAPES[selection - 1])
                if selected_materials == '1':
                    density, used_mat, density_unit = material_choice(materialskgm3, '1')  # Pass '1' for kg/m^3
                    if selection == 1:  # Solid Cube
                        solid_cone_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 2:  # Solid Cube
                        solid_cube_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 3:  # Solid Cylinder
                        solid_cylinder_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 4:  # Solid Rectangular Prism
                        solid_rectangle_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 5:  # Solid Sphere
                        solid_sphere_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 6:  # Solid Triangular Trough
                        solid_triangle_trough_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 7:  # Solid Octahedron
                        solid_octahedron_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 8:  # Solid Rings
                        solid_ring_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 9:  # Solid Spiral Coil
                        solid_spiral_coil_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 10:  # Hollow Tube w/ two openings
                        hollow_tube_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 11:  # Hollow Hexagonal Strut
                        hollow_hexagonal_strut_prompt(density, 'm', used_mat, density_unit)
                    elif selection == 12:  # Hollow Trapezoid Trough
                        hollow_trapezoid_trough_with_base_opening_prompt(density, 'm', used_mat, density_unit)
                    else:
                        menu()
                elif selected_materials == '2':
                    density, used_mat, density_unit = material_choice(materialsgcm3, '2')  # Pass '2' for g/cm^3
                    if selection == 1:
                        solid_cone_prompt(density, "cm", used_mat, density_unit)
                    elif selection == 2:  # Solid Cube
                        solid_cube_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 3:  # Solid Cylinder
                        solid_cylinder_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 4:  # Solid Rectangular Prism
                        solid_rectangle_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 5:  # Solid Sphere
                        solid_sphere_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 6:  # Solid Spiral Coil
                        solid_triangle_trough_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 7:  # Solid Octahedron
                        solid_octahedron_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 8:  # Solid Rings
                        solid_ring_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 9:  # Solid Spiral Coil
                        solid_spiral_coil_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 10:  # Hollow Tube
                        hollow_tube_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 11:  # Hollow Hexagonal Strut
                        hollow_hexagonal_strut_prompt(density, 'cm', used_mat, density_unit)
                    elif selection == 12:  # Hollow Trapezoid Trough w/ Base Openings
                        hollow_trapezoid_trough_with_base_opening_prompt(density, 'cm', used_mat, density_unit)
                    else:
                        menu()
                else:
                    print("Invalid selection. Please choose 1 or 2.")
            else:
                print("Invalid selection.")

        except ValueError:
            print("\nPlease enter an appropriate value.")
            input("Press Enter to continue...")

    def solid_cone(radius, height, density, unit, used_mat, shape, density_unit):

        volume_cone = (1 / 3) * math.pi * (radius ** 2) * height
        mass = volume_cone * density

        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius} meters")
        print(f"Height: {height} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_cone:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_cone_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Cone"
        print("\n{}\n".format("Solid Cone".center(100, "~")))

        radius = 0.0
        height = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            radius = float(input(f"Enter the radius (in {unit_choice}): ")) * factor / 100  # convert to meters
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_cone(radius, height, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_cube(side_length, density, unit, used_mat, shape, density_unit):

        volume_cube = side_length ** 3

        mass = volume_cube * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Side Length: {side_length} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_cube:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_cube_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Cube"
        print("\n{}\n".format("Solid Cube".center(100, "~")))

        side_length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            side_length = float(input(f"\nEnter the side length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            side_length = float(input(f"Enter the side length (in {unit_choice}): ")) * factor / 100  # convert to
            # meters

        mass_needed = solid_cube(side_length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_cylinder(radius, height, density, unit, used_mat, shape, density_unit):

        volume_cylinder = math.pi * (radius ** 2) * height

        mass = volume_cylinder * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius} meters")
        print(f"Height: {height} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_cylinder:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_cylinder_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Cylinder"
        print("\n{}\n".format("Solid Cylinder".center(100, "~")))

        radius = 0.0
        height = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            radius = float(input(f"Enter the radius (in {unit_choice}): ")) * factor / 100  # convert to meters
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_cylinder(radius, height, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_rectangle(length, width, height, density, unit, used_mat, shape, density_unit):

        volume_prism = length * width * height

        mass = volume_prism * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Length: {length} meters")
        print(f"Width: {width} meters")
        print(f"Height: {height} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_prism:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_rectangle_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Rectangular Prism"
        print("\n{}\n".format("Solid Rectangular Prism".center(100, "~")))

        length = 0.0
        width = 0.0
        height = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
            width = float(input(f"Enter the width (in {unit_choice}): ")) * factor
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor / 100
            width = float(input(f"Enter the width (in {unit_choice}): ")) * factor / 100
            height = float(input(f"Enter the height (in {unit_choice}): ")) * factor / 100

        mass_needed = solid_rectangle(length, width, height, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_sphere(radius, density, unit, used_mat, shape, density_unit):

        volume_sphere = (4 / 3) * math.pi * radius ** 3

        mass = volume_sphere * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_sphere:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_sphere_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Sphere"
        print("\n{}\n".format("Solid Sphere".center(100, "~")))

        radius = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            radius = float(input(f"Enter the radius (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_sphere(radius, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_triangular_trough(base_length, height, length, density, unit, used_mat, shape, density_unit):

        volume_triangle_trough = 0.5 * base_length * height * length

        mass = volume_triangle_trough * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Base Length: {base_length} meters")
        print(f"Height: {height} meters")
        print(f"Length: {length} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_triangle_trough:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_triangle_trough_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Triangular Trough"
        print("\n{}\n".format("Solid Triangular Trough".center(100, "~")))

        base_length = 0.0
        height = 0.0
        length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            base_length = float(input(f"\nEnter the base_length (in {unit_choice}): ")) * factor
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            base_length = float(input(f"\nEnter the base_length (in {unit_choice}): ")) * factor / 100
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor / 100
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor / 100

        mass_needed = solid_triangular_trough(base_length, height, length, density,
                                              unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_octahedron(side_length, density, unit, used_mat, shape, density_unit):
        volume_octahedron = (side_length ** 3) / (3 * math.sqrt(2))

        mass = volume_octahedron * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Side Length: {side_length} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_octahedron:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_octahedron_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Octahedron"
        print("\n{}\n".format("Solid Octahedron".center(100, "~")))

        side_length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            side_length = float(input(f"\nEnter the side length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            side_length = float(input(f"\nEnter the side length (in {unit_choice}): ")) * factor / 100

        mass_needed = solid_octahedron(side_length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_ring(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit):

        volume_ring = math.pi * height * (outer_radius ** 2 - inner_radius ** 2)
        mass = volume_ring * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Height: {height} meters")
        print(f"Outer Radius: {outer_radius} meters")
        print(f"Inner Radius: {inner_radius} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_ring:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_ring_prompt(density, unit, used_mat, density_unit):
        shape = "Ring"
        print("\n{}\n".format("Ring".center(100, "~")))

        height = 0.0
        outer_radius = 0.0
        inner_radius = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
            outer_radius = float(input(f"\nEnter the outer radius (in {unit_choice}): ")) * factor
            inner_radius = float(input(f"\nEnter the inner radius (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor / 100
            outer_radius = float(input(f"\nEnter the outer radius (in {unit_choice}): ")) * factor / 100
            inner_radius = float(input(f"\nEnter the inner radius (in {unit_choice}): ")) * factor / 100

        mass_needed = solid_ring(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def solid_spiral_coil(radius, pitch, length, density, unit, used_mat, shape, density_unit):

        cross_sectional_area = math.pi * radius ** 2
        coil_length = math.sqrt(radius ** 2 + pitch ** 2) / (2 * math.pi)
        volume_spiral_coil = cross_sectional_area * coil_length * length

        mass = volume_spiral_coil * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Radius: {radius} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_spiral_coil:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def solid_spiral_coil_prompt(density, unit, used_mat, density_unit):
        shape = "Solid Spiral Coil"
        print("\n{}\n".format("Solid Spiral Coil".center(100, "~")))

        radius = 0.0
        pitch = 0.0
        length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor
            pitch = float(input(f"\nEnter the pitch (in {unit_choice}): ")) * factor
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            radius = float(input(f"\nEnter the radius (in {unit_choice}): ")) * factor / 100
            pitch = float(input(f"\nEnter the pitch (in {unit_choice}): ")) * factor / 100
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = solid_spiral_coil(radius, pitch, length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def hollow_tube(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit):
        volume_hollow_tube = math.pi * height * (outer_radius ** 2 - inner_radius ** 2)

        mass = volume_hollow_tube * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Inner Radius: {inner_radius} meters")
        print(f"Outer Radius: {outer_radius} meters")
        print(f"Height: {height} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_hollow_tube:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def hollow_tube_prompt(density, unit, used_mat, density_unit):
        shape = "Hollow Tube w/ Two Openings"
        print("\n{}\n".format("Hollow Tube w/ Two Openings".center(100, "~")))

        height = 0.0
        outer_radius = 0.0
        inner_radius = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
            outer_radius = float(input(f"\nEnter the outer radius (in {unit_choice}): ")) * factor
            inner_radius = float(input(f"\nEnter the inner_radius (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor / 100
            outer_radius = float(input(f"\nEnter the outer radius (in {unit_choice}): ")) * factor / 100
            inner_radius = float(input(f"\nEnter the inner_radius (in {unit_choice}): ")) * factor / 100

        mass_needed = hollow_tube(height, outer_radius, inner_radius, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def hollow_hexagonal_strut(outer_side_length, inner_side_length, length,
                               density, unit, used_mat, shape, density_unit):

        outer_area = 3 * math.sqrt(3) * (outer_side_length ** 2) / 2

        inner_area = 3 * math.sqrt(3) * (inner_side_length ** 2) / 2

        cross_sectional_area = outer_area - inner_area

        volume_sphere = cross_sectional_area * length

        mass = volume_sphere * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Outer Side Length: {outer_side_length} meters")
        print(f"Inner Side Length: {inner_side_length} meters")
        print(f"Length: {length} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_sphere:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def hollow_hexagonal_strut_prompt(density, unit, used_mat, density_unit):
        shape = "Hollow Hexagonal Strut"
        print("\n{}\n".format("Hollow Hexagonal Strut".center(100, "~")))

        outer_side_length = 0.0
        inner_side_length = 0.0
        length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            outer_side_length = float(input(f"\nEnter the outer side length (in {unit_choice}): ")) * factor
            inner_side_length = float(input(f"\nEnter the inner side length (in {unit_choice}): ")) * factor
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            outer_side_length = float(input(f"\nEnter the outer side length (in {unit_choice}): ")) * factor / 100
            inner_side_length = float(input(f"\nEnter the inner side length (in {unit_choice}): ")) * factor / 100
            length = float(input(f"\nEnter the length (in {unit_choice}): ")) * factor / 100  # convert to meters

        mass_needed = hollow_hexagonal_strut(outer_side_length, inner_side_length,
                                             length, density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def hollow_trapezoid_trough_with_base_opening(height, outer_bottom_base_length, inner_bottom_base_length,
                                                  inner_top_base_length, outer_top_base_length,
                                                  density, unit, used_mat, shape, density_unit):

        volume_outer = height * (outer_bottom_base_length + outer_top_base_length) / 2
        volume_inner = height * (inner_bottom_base_length + inner_top_base_length) / 2
        volume_hollow_trapezoid_trough_with_base_opening = volume_outer - volume_inner

        mass = volume_hollow_trapezoid_trough_with_base_opening * density
        mass_unit, mass_formatted = get_mass_unit(unit, mass)

        result_header(used_mat, shape)
        print(f"Height: {height} meters")
        print(f"Outer Bottom Base Length: {outer_bottom_base_length} meters")
        print(f"Inner Bottom Base Length: {inner_bottom_base_length} meters")
        print(f"Outer Top Base Length: {outer_top_base_length} meters")
        print(f"Inner Top Base Length: {inner_top_base_length} meters")
        print(f"Material Density: {density} {density_unit}")
        print(f"Volume: {volume_hollow_trapezoid_trough_with_base_opening:10f} m^3")
        print(f"Required Mass of {used_mat}: {mass_formatted:10f} {mass_unit}")

        return mass

    def hollow_trapezoid_trough_with_base_opening_prompt(density, unit, used_mat, density_unit):
        shape = "Hollow Trapezoid Trough w/ Base Opening"
        print("\n{}\n".format("Hollow Trapezoid Trough w/ Base Opening".center(100, "~")))

        height = 0.0
        outer_bottom_base_length = 0.0
        inner_bottom_base_length = 0.0
        outer_top_base_length = 0.0
        inner_top_base_length = 0.0

        print(f"{used_mat} {shape}\n")

        # Pag pipili unit
        factor, unit_choice = get_factor()
        if unit == 'm':
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor
            outer_bottom_base_length = float(input(
                f"\nEnter the outer bottom base length (in {unit_choice}): ")) * factor
            inner_bottom_base_length = float(input(
                f"\nEnter the inner bottom base length (in {unit_choice}): ")) * factor
            outer_top_base_length = float(input(f"\nEnter the outer top base length (in {unit_choice}): ")) * factor
            inner_top_base_length = float(input(f"\nEnter the inner top base length (in {unit_choice}): ")) * factor
        elif unit == 'cm':
            height = float(input(f"\nEnter the height (in {unit_choice}): ")) * factor / 100
            outer_bottom_base_length = float(input(
                f"\nEnter the outer bottom base length (in {unit_choice}): ")) * factor / 100
            inner_bottom_base_length = float(input(
                f"\nEnter the inner bottom base length (in {unit_choice}): ")) * factor / 100
            outer_top_base_length = float(input(
                f"\nEnter the outer top base length (in {unit_choice}): ")) * factor / 100
            inner_top_base_length = float(input(
                f"\nEnter the inner top base length (in {unit_choice}): ")) * factor / 100

        mass_needed = hollow_trapezoid_trough_with_base_opening(height, outer_bottom_base_length,
                                                                inner_bottom_base_length,
                                                                inner_top_base_length, outer_top_base_length,
                                                                density, unit, used_mat, shape, density_unit)
        print_mass_needed(mass_needed, used_mat, shape, unit)

        print("\n{}".format("-".center(70, "-")))

        user_choice()

    def result_header(used_mat, shape):
        print("{}\n".format("-".center(70, "-")))
        print("{}\n".format(f"{used_mat} {shape}".center(70)))

    def print_mass_needed(mass_needed, used_mat, shape, unit):
        if unit == 'm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:\n", round(mass_needed, 4), "kilograms")
        elif unit == 'cm':
            print(f"\nMass of {used_mat} needed for the {used_mat} {shape}:\n", round(mass_needed * 1000, 4), "grams")

    def get_factor():
        while True:
            try:
                unit_choice = input("Enter the unit for radius and height (ft, in, m, cm, mm): \n").lower()
                if unit_choice in ['ft', 'in', 'cm', 'mm']:
                    break  # Exit the loop if the input is valid
                else:
                    print("Invalid unit choice. Please enter one of the following: ft, in, m, cm, mm.")
            except KeyboardInterrupt:
                print("\nProgram interrupted by user. Exiting...")
                exit()  # Exit the program if the user interrupts it with Ctrl+C
        if unit_choice == 'ft':
            factor = 0.3048  # 1 foot = 0.3048 meters
        elif unit_choice == 'in':
            factor = 0.0254  # 1 inch = 0.0254 meters
        elif unit_choice == 'cm':
            factor = 0.01  # 1 centimeter = 0.01 meters
        elif unit_choice == 'mm':
            factor = 0.001  # 1 millimeter = 0.001 meters
        elif unit_choice == 'mm':
            factor = 1
        else:
            factor = 1  # Default to meters

        return factor, unit_choice

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
                density_unit = ""
                if 1 <= selection <= len(materials):
                    if unit == '1':
                        density_unit = "kg/m^3"
                    elif unit == '2':
                        density_unit = 'g/cm^3'
                    material = list(materials.keys())[selection - 1]
                    density = materials[material]
                    used_mat = material
                    return density, used_mat, density_unit
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
