import os

def count_words(directory):
    words = {}
    for file in os.listdir(directory):
        with open(os.path.join(directory, file)) as f:
            for word in f.read().split():
                words[word] = words.get(word, 0) + 1
    return words

if __name__ == "__main__":
    while True:
        directory = input("Nhập đường dẫn thư mục: ")
        try:
            words = count_words(directory)
            with open(os.path.join(directory, "Output.txt"), "w") as f:
                for word, count in words.items():
                    f.write(f"{word}: {count}\n")
            print("Output.txt đã được tạo thành công!")
            break  # Thoát khỏi vòng lặp nếu thư mục hợp lệ và xử lý đã hoàn thành
        except FileNotFoundError:
            print("Thư mục không tìm thấy. Vui lòng nhập một đường dẫn thư mục hợp lệ.")
    
    # In kết quả ra màn hình để kiểm tra
    print("Kết quả của file Output.txt:")
    with open(os.path.join(directory, "Output.txt")) as f:
        print(f.read())
