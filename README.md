# Trình Cào Dữ Liệu Điểm Thi THPTQG 2024

Dự án này sử dụng framework Scrapy để cào dữ liệu điểm thi tốt nghiệp THPT quốc gia (THPTQG 2024) từ API của VTV.

## Cấu Trúc Dự Án
diemthi/
├── diemthi/
│ ├── pycache/
│ ├── spiders/
│ │ ├── pycache/
│ │ ├── init.py
│ │ ├── diem_spider.py      #Tập tin Scrapy spider chính dùng để cào dữ liệu.
│ ├── init.py
│ ├── items.py
│ ├── middlewares.py
│ ├── pipelines.py
│ ├── settings.py           #Thay đổi cấu hình cào dữ liệu
├── scrapy.cfg

## Cài Đặt

1. **Clone kho lưu trữ:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Tạo một môi trường ảo:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows, sử dụng `venv\Scripts\activate`
    ```

3. **Cài đặt các thư viện cần thiết:**

    ```bash
    pip install scrapy
    ```

## Sử Dụng

1. **Điều hướng đến thư mục dự án:**

    ```bash
    cd <repository_directory>
    ```

2. **Chạy Scrapy spider:**

    ```bash
    scrapy crawl diem_spider -o diemthi.json
    ```

    Lệnh này sẽ bắt đầu chạy spider và lưu dữ liệu cào được vào file `diemthi.json`.

## Chi Tiết Spider

### `diem_spider.py`

Tập tin này chứa Scrapy spider dùng để cào dữ liệu điểm thi từ API của VTV. Spider hoạt động như sau:

- **Tên**: `diem_spider`
- **Allowed Domains**: `vtvapi3.vtv.vn`
- **Start URLs**: `https://vtvapi3.vtv.vn`

### Các Hàm:

- `start_requests`: Tạo các yêu cầu ban đầu cho mỗi dải số báo danh.
- `parse`: Phân tích phản hồi từ API và trích xuất các trường dữ liệu như `SOBAODANH`, `TOAN`, `VAN`, `NGOAI_NGU`, `LY`, `HOA`, `SINH`, `SU`, `DIA`, `GIAO_DUC_CONG_DAN`, và `MA_MON_NGOAI_NGU`.

### Các Trường Dữ Liệu:

- `SOBAODANH`: Số báo danh
- `TOAN`: Điểm Toán
- `VAN`: Điểm Văn
- `NGOAI_NGU`: Điểm Ngoại ngữ
- `LY`: Điểm Lý
- `HOA`: Điểm Hóa
- `SINH`: Điểm Sinh
- `SU`: Điểm Sử
- `DIA`: Điểm Địa
- `GIAO_DUC_CONG_DAN`: Điểm Giáo dục công dân
- `MA_MON_NGOAI_NGU`: Mã môn Ngoại ngữ

## Ghi Chú

- Điều chỉnh dải số báo danh trong phương thức `start_requests` theo nhu cầu của bạn.
- Đảm bảo bạn có quyền cào dữ liệu từ API và tuân thủ các điều khoản dịch vụ của trang web.

## Giấy Phép

Dự án này được cấp phép theo Giấy phép MIT. Xem tệp LICENSE để biết thêm chi tiết.
