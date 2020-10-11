## EDA Notes

- Dùng matrix profile thì thấy đúng là có pattern lặp lại trong data
- Vấn đề là bây giờ mình thống kê các pattern đó như thế nào?
- Hiện pattern length = 24 nhưng thực ra trading session chỉ có 9h giờ
- Hướng thứ nhất: Tìm tất cả các pattern thông dụng trong toàn bộ dữ liệu 
và đưa vào hopfield network để train và retrieval
- Với lượng dữ liệu lớn như này thì chạy matrix profile để mà ra kết quả là ko khả thi. 
hưa kể mình còn phải test xem giá trị windows nào là hợp lý.
- Đổi sang hướng dùng knn để tìm pattern
- Cần xác đinh hướng dùng knn rõ ràng hơn
- Hoặc test matrix profile với từng đoạn dữ liệu nhỏ.