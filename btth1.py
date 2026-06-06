raw_logs = []
processed_logs = []


def clean_logs():
    """
    Nhập log thô, loại bỏ ký tự đặc biệt
    và lưu vào danh sách raw_logs.
    """
    global raw_logs

    print("\n--- NẠP DỮ LIỆU LOG ---")

    log_text = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")

    table = str.maketrans("", "", "!@#$")

    clean_text = log_text.translate(table)

    raw_logs = [log.strip() for log in clean_text.split(";") if log.strip()]

    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")


def filter_danger_logs():
    """
    Lọc các log chứa ERROR hoặc CRITICAL
    bằng List Comprehension.
    """
    global processed_logs

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    print("\n--- LỌC CẢNH BÁO ---")

    processed_logs = [
        log for log in raw_logs
        if "ERROR" in log.upper()
        or "CRITICAL" in log.upper()
    ]

    if processed_logs:
        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
        for log in processed_logs:
            print("-", log)
    else:
        print("Không tìm thấy cảnh báo nguy hiểm.")


def mask_ip(log):
    """
    Mã hóa địa chỉ IP:
    192.168.1.1 -> 192.168.*.*
    """

    words = log.split()

    for i in range(len(words)):
        if "." in words[i]:

            parts = words[i].split(".")

            if len(parts) == 4:
                parts[2] = "*"
                parts[3] = "*"

                words[i] = ".".join(parts)

    return " ".join(words)


def generate_safe_report():
    """
    Tạo báo cáo log an toàn
    bằng cách che giấu IP.
    """

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    if not processed_logs:
        print("Chưa có dữ liệu log nguy hiểm để mã hóa.")
        return

    print("\n--- MÃ HÓA IP ---")

    safe_logs = [mask_ip(log) for log in processed_logs]

    print("Báo cáo log an toàn:")

    for index, log in enumerate(safe_logs, start=1):
        print(f"{index}. {log}")

    return safe_logs


def main():


    while True:

        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            clean_logs()

        elif choice == "2":
            filter_danger_logs()

        elif choice == "3":
            generate_safe_report()

        elif choice == "4":
            print("Đóng hệ thống...")
            break

        else:
            print("Lựa chọn không hợp lệ.")


main()