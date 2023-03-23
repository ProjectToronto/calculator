import tkinter as tk

def calculate_cylinder_surface_area():
    radius = float(radius_entry.get())
    height = float(height_entry.get())
    surface_area = 2 * 3.14159 * radius * (radius + height)
    surface_area_label.configure(text=f"Surface area: {surface_area:.2f}")

def calculate_prism_surface_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_prism_entry.get())
    surface_area = 2 * (length * width + length * height + width * height)
    surface_area_label.configure(text=f"Surface area: {surface_area:.2f}")

def calculate_cylinder_volume():
    radius = float(radius_entry.get())
    height = float(height_entry.get())
    volume = 3.14159 * radius ** 2 * height
    volume_label.configure(text=f"Volume: {volume:.2f}")

def calculate_prism_volume():
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_prism_entry.get())
    volume = length * width * height
    volume_label.configure(text=f"Volume: {volume:.2f}")

root = tk.Tk()
root.title("Shape Calculator")

# Cylindrical container
cylinder_frame = tk.Frame(root)
cylinder_frame.pack(padx=10, pady=10)
cylinder_label = tk.Label(cylinder_frame, text="Cylinder")
cylinder_label.pack()
radius_label = tk.Label(cylinder_frame, text="Radius:")
radius_label.pack()
radius_entry = tk.Entry(cylinder_frame)
radius_entry.pack()
height_label = tk.Label(cylinder_frame, text="Height:")
height_label.pack()
height_entry = tk.Entry(cylinder_frame)
height_entry.pack()
calculate_cylinder_surface_area_button = tk.Button(cylinder_frame, text="Calculate surface area", command=calculate_cylinder_surface_area)
calculate_cylinder_surface_area_button.pack()
calculate_cylinder_volume_button = tk.Button(cylinder_frame, text="Calculate volume", command=calculate_cylinder_volume)
calculate_cylinder_volume_button.pack()
surface_area_label = tk.Label(cylinder_frame, text="Surface area: ")
surface_area_label.pack()
volume_label = tk.Label(cylinder_frame, text="Volume: ")
volume_label.pack()
prism_frame = tk.Frame(root)
prism_frame.pack(padx=10, pady=10)
prism_label = tk.Label(prism_frame, text="Rectangular Prism")
prism_label.pack()
length_label = tk.Label(prism_frame, text="Length:")
length_label.pack()
length_entry = tk.Entry(prism_frame)
length_entry.pack()
width_label = tk.Label(prism_frame, text="Width:")
width_label.pack()
width_entry = tk.Entry(prism_frame)
width_entry.pack()
height_prism_label = tk.Label(prism_frame, text="Height:")
height_prism_label.pack()
height_prism_entry = tk.Entry(prism_frame)
height_prism_entry.pack()
calculate_prism_surface_area_button = tk.Button(prism_frame, text="Calculate surface area", command=calculate_prism_surface_area)
calculate_prism_surface_area_button.pack()
calculate_prism_volume_button = tk.Button(prism_frame, text="Calculate volume", command=calculate_prism_volume)
calculate_prism_volume_button.pack()
surface_area_label = tk.Label(prism_frame, text="Surface area: ")
surface_area_label.pack()
volume_label = tk.Label(prism_frame, text="Volume: ")
volume_label.pack()

root.mainloop()




