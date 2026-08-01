# Web Arama Yapabilen Agent

## Ne Yapar?
Kullanıcının sorusuna cevap vermek için gerçek zamanlı web araması yapan bir AI agent. 
`smolagents` kütüphanesinin `CodeAgent` yapısını ve `DuckDuckGoSearchTool`'u kullanır.

## Kullanılan Teknolojiler
- Python
- smolagents (CodeAgent)
- Hugging Face Inference API (Qwen2.5-Coder-32B-Instruct)
- DuckDuckGo Search Tool

## Nasıl Çalıştırılır?
1. Bu klasörde bir `.env` dosyası oluşturup içine `HF_TOKEN=senin_tokenin` yaz
2. Gerekli kütüphaneleri yükle: `pip install smolagents huggingface_hub python-dotenv ddgs`
3. Çalıştır: `python agent.py`

## Öğrenilen Ders
Bu proje sırasında, modelin web'den doğru veriyi bulmasına rağmen **sayıyı aktarırken 
hata yaptığını** (hallucination) gözlemledim — LLM'lerin uzun sayıları kopyalarken 
hata yapabileceğini gösteren gerçek bir örnek.