# Çok Araçlı Agent (Calculator + Word Counter)

## Ne Yapar?
Birden fazla tool'u aynı anda yönetebilen bir agent. Kullanıcı hem matematik işlemi 
hem de metin analizi isteyebilir, agent ihtiyaca göre doğru tool'u (veya tool'ları) seçer.

## Kullanılan Teknolojiler
- Python
- smolagents (CodeAgent, @tool decorator)
- Hugging Face Inference API (Qwen2.5-Coder-32B-Instruct)

## Tool'lar
- `calculator`: iki sayı ile temel matematik işlemleri (toplama, çıkarma, çarpma, bölme)
- `word_counter`: bir metindeki kelime sayısını hesaplar

## Nasıl Çalıştırılır?
1. Bu klasörde bir `.env` dosyası oluşturup içine `HF_TOKEN=senin_tokenin` yaz
2. Gerekli kütüphaneleri yükle: `pip install smolagents huggingface_hub python-dotenv ddgs`
3. Çalıştır: `python agent.py`

## Öğrenilen Ders
Code Agent'ın gücünü gözlemledim: model, **tek bir kod bloğunda birden fazla tool'u 
art arda çağırıp**, aralarında normal Python değişkenleriyle veri taşıyarak sonuçları 
birleştirebiliyor — bu, JSON Agent'a göre çok daha az adımda aynı işi yapmasını sağlıyor.