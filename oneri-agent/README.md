# Kitap/Film Öneri Agent'ı

## Ne Yapar?
Kullanıcının kişisel kitap/film kütüphanesinde (yerel bir JSON dosyası) arama yapabilen, 
kütüphanedeki tüm kayıtları listeleyebilen ve kütüphaneye yeni kayıt ekleyebilen bir 
`smolagents` `CodeAgent`'ı. Kütüphanede uygun bir sonuç bulunamazsa web'den araştırma 
yapabilir, gerektiğinde kullanıcıya ek soru sorabilir.

## Mimari
Üç özel tool, smolagents'ın iki farklı tool tanımlama yönteminde yazıldı:
- **Class-based** (`Tool`'dan türetme): `oneri_retriever` — `tools.py` içinde
- **Decorator-based** (`@tool`): `get_library` ve `add_item` — `agent.py` içinde

`oneri_retriever`, sorgudaki **tüm kelimelerin** eşleştiği kayıtları arar (AND mantığı); 
`add_item`, eklediği kaydı hem bellekte hem `data/library.json` dosyasında kalıcı hale getirir.

## Kullanılan Teknolojiler
- Python
- smolagents (`CodeAgent`, `Tool` base class, `@tool` decorator)
- Hugging Face Inference API (Qwen2.5-Coder-32B-Instruct)
- `DuckDuckGoSearchTool`, `UserInputTool`
- JSON tabanlı yerel veri deposu (`data/library.json`)

## Nasıl Çalıştırılır?
1. Bu klasörde bir `.env` dosyası oluşturup içine `HF_TOKEN=senin_tokenin` yaz
2. Gerekli kütüphaneleri yükle: `pip install smolagents huggingface_hub python-dotenv ddgs`
3. Çalıştır: `python agent.py`
4. Terminalde görevini yazman istenecek (örn. "Bana bir bilim kurgu filmi öner")

## Nasıl Çalışıyor?
1. `oneri_retriever`, kullanıcının sorgusunu kelimelere böler ve `baslik`/`tur`/`aciklama`/`puan` 
   alanlarının tamamında bu kelimelerin geçtiği kayıtları döndürür
2. `get_library`, filtresiz olarak kütüphanedeki tüm kayıtları numaralı liste halinde döndürür
3. `add_item`, yeni bir kitap/film kaydını `data/library.json`'a kalıcı olarak yazar 
   (`ensure_ascii=False` ile Türkçe karakterler bozulmadan)
4. Kütüphanede uygun sonuç yoksa agent, `DuckDuckGoSearchTool` ile web'den araştırma yapabilir
5. Ek bilgiye ihtiyaç duyulursa `UserInputTool` ile kullanıcıya soru sorulur (interaktif bir 
   terminal gerektirir)

## Öğrenilen Ders
Tool'ları tanımlamak, modelin onları kullanacağı anlamına gelmiyor. İlk testimde, kütüphanede 
gerçek veriler olmasına rağmen model `oneri_retriever`'ı hiç çağırmadan kendi uydurduğu 
rastgele bir film listesinden seçim yaptı. Bu, tool `description`'larının ve göreve verilen 
talimatın, modelin doğru tool'u seçmesi için ne kadar belirleyici olduğunu gösterdi — sadece 
tool'un var olması yeterli değil, modelin onu tercih etmesi için açıkça yönlendirilmesi gerekiyor.
