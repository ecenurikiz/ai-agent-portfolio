import os
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool

# .env dosyasındaki token'ı yükle
load_dotenv()

# Modeli tanımla (Hugging Face'in ücretsiz Inference API'si üzerinden)
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=os.getenv("HF_TOKEN")
)

# Agent'ı, web araması yapabilen bir tool ile kur
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model
)

# Agent'ı çalıştır
result = agent.run("Türkiye'nin nüfusu şu an ne kadar ve bu bilgiyi hangi kaynaktan aldın?")

print(result)