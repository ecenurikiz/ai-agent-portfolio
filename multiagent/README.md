# Multi-Agent Sistemi (Manager + Web Agent)

## Ne Yapar?
Birden fazla uzman agent'ın koordineli şekilde çalıştığı bir sistem. Bir **Manager Agent**, 
görevin araştırma gerektiren kısmını kendi yönettiği bir **Web Agent**'a devrediyor, 
gelen sonucu değerlendirip kendi tool'larıyla (calculator) işliyor.

## Mimari
## Kullanılan Teknolojiler
- Python
- smolagents (CodeAgent, `managed_agents` parametresi)
- Hugging Face Inference API (Qwen2.5-Coder-32B-Instruct)
- DuckDuckGo Search Tool

## Nasıl Çalıştırılır?
1. Bu klasörde bir `.env` dosyası oluşturup içine `HF_TOKEN=senin_tokenin` yaz
2. Gerekli kütüphaneleri yükle: `pip install smolagents huggingface_hub python-dotenv ddgs`
3. Çalıştır: `python agent.py`

## Nasıl Çalışıyor?
1. Manager, görevi alır ve araştırma gerektiren kısmı fark eder
2. Manager, `web_agent`'ı bir fonksiyon gibi çağırır: `web_agent(task="...")`
3. Web Agent, **kendi ayrı Thought-Action-Observation döngüsünde** arama yapar
4. Web Agent, sonucu standart 3 bölümlü bir rapor formatında (`short version`, 
   `detailed version`, `additional context`) Manager'a döndürür
5. Manager, bu özet raporu okuyup kendi `calculator` tool'uyla işlemi tamamlar

## Öğrenilen Ders
Multi-agent mimarisi, **context (hafıza) izolasyonu** sağlıyor: Manager, web_agent'ın 
ham arama loglarını hiç görmüyor, sadece yapılandırılmış özet raporu alıyor. Bu, tek 
bir agent'ın tüm süreci tek başına yönetmesine kıyasla **daha az token kullanımı ve 
daha odaklı çalışma** sağlıyor. Ayrıca, multi-agent yapısının **hallucination (uydurma 
veri) riskini otomatik olarak çözmediğini** de gözlemledim — web_agent, arama 
sonucundaki sayıyı yine yanlış aktardı, bu modelin temel bir zayıflığı.