# Phân tích kết quả đánh giá RAGAS (V1 vs V2)
**Học viên:** Trịnh Quốc Trọng (2A202601779)



Dựa trên quá trình đánh giá bằng framework RAGAS cho 50 cặp câu hỏi, chúng ta có thể rút ra một số nhận xét chuyên sâu về hiệu suất của hai phiên bản Prompt:

1. **Prompt V1 (Ngắn gọn, trực tiếp):**
   - Đạt điểm số `faithfulness` rất cao do tính chất trả lời trực tiếp vào trọng tâm, bám sát context được cung cấp.
   - Thích hợp cho các ứng dụng chatbot thông thường nơi người dùng cần câu trả lời nhanh chóng, dễ hiểu và không chứa quá nhiều thông tin rườm rà.

2. **Prompt V2 (Chi tiết, có trích dẫn nguồn):**
   - Hướng dẫn LLM phải tóm tắt, trích dẫn nguồn và đánh giá mức độ chắc chắn. 
   - Điều này giúp tăng độ tin cậy và minh bạch (transparency) của câu trả lời, tuy nhiên có thể khiến `answer_relevancy` bị ảnh hưởng đôi chút do câu trả lời chứa nhiều thông tin phụ trợ (metadata) hơn mức cần thiết so với câu hỏi gốc.

**Kết luận:** Prompt V2 phù hợp cho các hệ thống đòi hỏi tính chính xác và tra cứu cao (như Legal, Medical, Research), trong khi Prompt V1 tối ưu hơn cho trải nghiệm người dùng cuối thông thường (B2C).
