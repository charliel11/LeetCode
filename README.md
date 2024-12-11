# 環境安裝

執行 `uv sync`，安裝虛擬環境與 pytest

# 如何使用

- 在 `src/leetcode` 位置建立 `{name}.py` 檔，把 leetcode 網頁上的程式內容複製進來，檔名與 function 名稱相同
- 把測試資料與答案 (測項 1、答案 1、測試 2、答案 2、...) 加到 `test/data/{name}` 位置，檔名與 function 名稱相同
- 使用 pytest 執行測試
