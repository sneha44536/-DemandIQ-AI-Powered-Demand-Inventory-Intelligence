import pandas as pd
import os

# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

OUTPUT_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# 2. FURNITURE PRODUCT CATALOG
# ============================================================

products = [

    # --------------------------------------------------------
    # OFFICE CHAIRS
    # --------------------------------------------------------

    ["P001", "Ergonomic Office Chair", "Chair", "Mesh", "Modern", "Black", 12500, 65, 115, 65],
    ["P002", "Executive Office Chair", "Chair", "Leather", "Executive", "Brown", 22000, 70, 120, 70],
    ["P011", "Visitor Chair", "Chair", "Fabric", "Modern", "Grey", 8500, 55, 90, 60],
    ["P015", "Lounge Chair", "Chair", "Leather", "Contemporary", "Black", 28000, 75, 90, 80],
    ["P016", "Task Chair", "Chair", "Mesh", "Modern", "Blue", 11000, 62, 110, 62],
    ["P017", "High Back Office Chair", "Chair", "Fabric", "Executive", "Black", 19500, 68, 118, 68],
    ["P018", "Conference Chair", "Chair", "Leather", "Executive", "Brown", 16500, 65, 100, 65],
    ["P019", "Stackable Visitor Chair", "Chair", "Plastic", "Modern", "Black", 5500, 52, 85, 55],
    ["P020", "Gaming Style Office Chair", "Chair", "Leather", "Contemporary", "Red", 24000, 70, 125, 70],
    ["P041", "Reception Lounge Chair", "Chair", "Fabric", "Contemporary", "Beige", 26000, 80, 90, 80],
    ["P042", "Conference Room Chair", "Chair", "Mesh", "Modern", "Black", 13500, 65, 105, 65],
    ["P043", "Bar Height Stool", "Chair", "Metal", "Industrial", "Black", 9000, 50, 105, 50],
    ["P044", "Breakout Area Chair", "Chair", "Fabric", "Modern", "Yellow", 12000, 60, 85, 60],
    ["P045", "Training Room Chair", "Chair", "Plastic", "Modern", "Blue", 7000, 55, 90, 55],

    # --------------------------------------------------------
    # DESKS
    # --------------------------------------------------------

    ["P003", "Adjustable Workstation", "Desk", "Wood", "Modern", "Oak", 35000, 150, 75, 75],
    ["P004", "Executive Office Desk", "Desk", "Wood", "Executive", "Walnut", 48000, 180, 75, 90],
    ["P012", "Reception Desk", "Desk", "Wood", "Contemporary", "White", 55000, 200, 110, 80],
    ["P014", "Adjustable Standing Desk", "Desk", "Wood", "Modern", "White", 45000, 160, 120, 75],
    ["P025", "Compact Work Desk", "Desk", "Wood", "Minimalist", "White", 26000, 120, 75, 60],
    ["P026", "L-Shaped Office Desk", "Desk", "Wood", "Modern", "Brown", 52000, 180, 75, 150],
    ["P027", "U-Shaped Executive Desk", "Desk", "Wood", "Executive", "Walnut", 78000, 240, 75, 180],
    ["P050", "Height Adjustable Desk", "Desk", "Wood", "Modern", "Oak", 48000, 160, 120, 80],

    # --------------------------------------------------------
    # WORKSTATIONS
    # --------------------------------------------------------

    ["P021", "Four-Person Workstation", "Workstation", "Wood", "Modern", "Oak", 62000, 240, 75, 120],
    ["P022", "Six-Person Workstation", "Workstation", "Wood", "Modern", "White", 90000, 360, 75, 120],
    ["P023", "Eight-Person Workstation", "Workstation", "Wood", "Contemporary", "Oak", 120000, 480, 75, 120],
    ["P024", "Manager Workstation", "Workstation", "Wood", "Executive", "Walnut", 72000, 180, 75, 90],

    # --------------------------------------------------------
    # SOFAS
    # --------------------------------------------------------

    ["P005", "Two-Seater Sofa", "Sofa", "Fabric", "Modern", "Grey", 42000, 160, 85, 85],
    ["P006", "Three-Seater Sofa", "Sofa", "Fabric", "Modern", "Blue", 58000, 220, 85, 90],
    ["P031", "Four-Seater Sofa", "Sofa", "Fabric", "Modern", "Grey", 68000, 260, 85, 95],
    ["P032", "Single Lounge Sofa", "Sofa", "Leather", "Executive", "Black", 32000, 90, 90, 85],
    ["P033", "Reception Sofa", "Sofa", "Fabric", "Contemporary", "Blue", 52000, 200, 85, 90],
    ["P034", "Modular Sofa", "Sofa", "Fabric", "Modern", "Beige", 75000, 280, 85, 100],
    ["P035", "Waiting Area Sofa", "Sofa", "Fabric", "Classic", "Brown", 46000, 190, 85, 90],

    # --------------------------------------------------------
    # TABLES
    # --------------------------------------------------------

    ["P009", "Conference Table", "Table", "Wood", "Modern", "Brown", 65000, 240, 75, 120],
    ["P010", "Round Meeting Table", "Table", "Wood", "Contemporary", "Oak", 38000, 120, 75, 120],
    ["P028", "Training Table", "Table", "Wood", "Modern", "Grey", 30000, 180, 75, 60],
    ["P029", "Collaborative Table", "Table", "Wood", "Contemporary", "Oak", 44000, 200, 75, 100],
    ["P030", "Coffee Table", "Table", "Glass", "Modern", "Black", 18000, 100, 45, 60],
    ["P046", "Large Conference Table", "Table", "Wood", "Executive", "Walnut", 85000, 300, 75, 130],
    ["P047", "Small Meeting Table", "Table", "Wood", "Modern", "White", 28000, 120, 75, 80],
    ["P048", "Reception Side Table", "Table", "Glass", "Contemporary", "Black", 14000, 70, 50, 50],

    # --------------------------------------------------------
    # STORAGE
    # --------------------------------------------------------

    ["P007", "Office Storage Cabinet", "Storage", "Wood", "Modern", "White", 18000, 90, 180, 45],
    ["P008", "Filing Cabinet", "Storage", "Metal", "Industrial", "Grey", 15000, 50, 120, 55],
    ["P013", "Bookshelf", "Storage", "Wood", "Classic", "Brown", 22000, 90, 180, 35],
    ["P036", "Mobile Storage Unit", "Storage", "Metal", "Modern", "Grey", 14000, 45, 100, 50],
    ["P037", "Personal Locker Unit", "Storage", "Metal", "Industrial", "Grey", 24000, 90, 180, 45],
    ["P038", "Open Storage Shelf", "Storage", "Wood", "Modern", "Oak", 16000, 80, 170, 35],
    ["P039", "Under Desk Pedestal", "Storage", "Metal", "Modern", "Black", 12000, 45, 65, 50],
    ["P040", "Tall Storage Cabinet", "Storage", "Wood", "Executive", "Walnut", 29000, 90, 200, 50],
    ["P049", "Office Bookshelf", "Storage", "Wood", "Modern", "White", 20000, 90, 180, 35],

    # --------------------------------------------------------
    # INDIAN TRADITIONAL
    # --------------------------------------------------------

    ["P051", "Teak Carved Accent Chair", "Chair", "Teak Wood", "Indian Traditional", "Natural", 32000, 70, 100, 75],
    ["P052", "Cane Lounge Chair", "Chair", "Cane", "Indian Traditional", "Honey", 24000, 75, 95, 80],
    ["P053", "Handcrafted Teak Study Desk", "Desk", "Teak Wood", "Indian Traditional", "Brown", 52000, 140, 75, 70],
    ["P054", "Indian Jali Storage Cabinet", "Storage", "Teak Wood", "Indian Traditional", "Walnut", 38000, 90, 180, 45],
    ["P055", "Traditional Low Coffee Table", "Table", "Sheesham Wood", "Indian Traditional", "Dark Brown", 28000, 110, 45, 70],

    # --------------------------------------------------------
    # INDIAN CONTEMPORARY
    # --------------------------------------------------------

    ["P056", "Cane and Wood Workstation", "Workstation", "Cane + Wood", "Indian Contemporary", "Natural", 58000, 160, 75, 75],
    ["P057", "Modern Indian Accent Chair", "Chair", "Fabric + Wood", "Indian Contemporary", "Terracotta", 26000, 70, 90, 75],
    ["P058", "Teak and Metal Executive Desk", "Desk", "Teak + Metal", "Indian Contemporary", "Walnut", 62000, 180, 75, 85],
    ["P059", "Contemporary Indian Sofa", "Sofa", "Cotton Fabric", "Indian Contemporary", "Mustard", 62000, 210, 85, 90],
    ["P060", "Cane Partition Storage", "Storage", "Cane + Wood", "Indian Contemporary", "Natural", 30000, 100, 180, 40],

    # --------------------------------------------------------
    # GEN Z / TRENDY
    # --------------------------------------------------------

    ["P061", "Modular Bean Bag Chair", "Chair", "Fabric", "Gen Z", "Purple", 9500, 80, 80, 80],
    ["P062", "Color Pop Study Desk", "Desk", "Engineered Wood", "Gen Z", "Yellow", 18000, 120, 75, 60],
    ["P063", "Modular Lounge Sofa", "Sofa", "Boucle Fabric", "Gen Z", "Pink", 48000, 180, 80, 85],
    ["P064", "Cloud Style Lounge Chair", "Chair", "Boucle Fabric", "Gen Z", "Cream", 22000, 85, 80, 85],
    ["P065", "Minimal Modular Side Table", "Table", "Engineered Wood", "Gen Z", "Green", 12000, 55, 50, 55],
]


# ============================================================
# 3. COLUMN NAMES
# ============================================================

columns = [
    "product_id",
    "product_name",
    "category",
    "material",
    "style",
    "color",
    "price",
    "width_cm",
    "height_cm",
    "depth_cm"
]


# ============================================================
# 4. CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(products, columns=columns)


# ============================================================
# 5. SAVE DATASET
# ============================================================

file_path = os.path.join(OUTPUT_DIR, "products.csv")

df.to_csv(file_path, index=False)


# ============================================================
# 6. OUTPUT INFORMATION
# ============================================================

print("=" * 60)
print("FURNITURE PRODUCT DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"File saved at: {file_path}")
print(f"Total products: {len(df)}")

print("\nProduct categories:")
print(df["category"].value_counts())

print("\nDesign styles:")
print(df["style"].value_counts())

print("\nFirst 10 products:")
print(df.head(10))

print("\nDataset shape:")
print(df.shape)