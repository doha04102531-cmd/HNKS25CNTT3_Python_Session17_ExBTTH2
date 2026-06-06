import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


def display_labels():
    """
    Hiển thị tem nhãn sản phẩm.
    """
    print("\n--- DANH SÁCH TEM NHÃN ---")

    template = "Mã: {code} | Tên: {name} | Giá: {price} | Rating: {rating}*"

    for product in product_list:
        parts = product.split("-")

        if len(parts) != 4:
            print(f"Bỏ qua sản phẩm {parts[0]} do sai cấu trúc dữ liệu")
            continue

        code = parts[0]
        name = parts[1]

        if not parts[2].isdigit():
            print(f"Bỏ qua sản phẩm {code} do giá không hợp lệ")
            continue

        price = int(parts[2])
        rating = parts[3]

        data = {
            "code": f"{code:<10}",
            "name": f"{name:<20}",
            "price": f"{price:,} VND",
            "rating": rating
        }

        print(template.format_map(data))


def get_sort_key(product):
    """
    Tạo key để sắp xếp:
    Rating giảm dần,
    Giá tăng dần.
    """
    parts = product.split("-")

    if len(parts) != 4:
        return (999, 999999999)

    if not parts[2].isdigit():
        return (999, 999999999)

    rating = float(parts[3])
    price = int(parts[2])

    return (-rating, price)


def sort_products():
    """
    Sắp xếp sản phẩm theo rating và giá.
    """
    product_list.sort(key=get_sort_key)

    print("\n--- SẮP XẾP SẢN PHẨM ---")

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product}")


def calculate_inventory_value():
    """
    Tính tổng giá trị kho bằng reduce().
    """
    prices = []

    for product in product_list:
        parts = product.split("-")

        if len(parts) != 4:
            print(f"Bỏ qua sản phẩm {parts[0]} do sai cấu trúc dữ liệu")
            continue

        if not parts[2].isdigit():
            print(f"Bỏ qua sản phẩm {parts[0]} do giá không hợp lệ")
            continue

        prices.append(int(parts[2]))

    total = functools.reduce(
        lambda acc, x: acc + x,
        prices,
        0
    )

    return total


def show_total_inventory():
    """
    Hiển thị tổng giá trị kho.
    """
    total = calculate_inventory_value()

    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND")


def main():
    """
    Chương trình chính.
    """
    while True:

        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm")
        print("2. Sắp xếp sản phẩm thông minh")
        print("3. Tính tổng giá trị kho hàng")
        print("4. Đóng hệ thống")
        print("================================================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            display_labels()

        elif choice == "2":
            sort_products()

        elif choice == "3":
            show_total_inventory()

        elif choice == "4":
            print("Đóng hệ thống...")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()