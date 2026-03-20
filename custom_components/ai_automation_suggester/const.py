"""Constants for the AI Automation Suggester integration."""

# ─────────────────────────────────────────────────────────────
# Core
# ─────────────────────────────────────────────────────────────
DOMAIN           = "ai_automation_suggester"
PLATFORMS        = ["sensor"]
CONFIG_VERSION   = 2  # config‑entry version (used by async_migrate_entry)
INTEGRATION_NAME = "AI Automation Suggester"

# ─────────────────────────────────────────────────────────────
# Token budgeting
# ─────────────────────────────────────────────────────────────
# Single legacy knob (kept for backward compatibility)
CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 500  # legacy default – used for both budgets if new keys absent

# New, separate knobs (Issue #91)
CONF_MAX_INPUT_TOKENS = "max_input_tokens"  # how much of the prompt we keep
CONF_MAX_OUTPUT_TOKENS = "max_output_tokens"  # how long the AI response may be

DEFAULT_MAX_INPUT_TOKENS = DEFAULT_MAX_TOKENS
DEFAULT_MAX_OUTPUT_TOKENS = DEFAULT_MAX_TOKENS

DEFAULT_TEMPERATURE = 0.7

# ─────────────────────────────────────────────────────────────
# Provider‑selection key
# ─────────────────────────────────────────────────────────────
CONF_PROVIDER = "provider"

# ─────────────────────────────────────────────────────────────
# Provider‑specific keys
# ─────────────────────────────────────────────────────────────
# OpenAI
CONF_OPENAI_API_KEY = "openai_api_key"
CONF_OPENAI_MODEL = "openai_model"
CONF_OPENAI_TEMPERATURE = "openai_temperature"

# OpenAI Azure
CONF_OPENAI_AZURE_API_KEY = "openai_azure_api_key"
CONF_OPENAI_AZURE_DEPLOYMENT_ID = "openai_azure_deployment_id"
CONF_OPENAI_AZURE_API_VERSION = "openai_azure_api_version"
CONF_OPENAI_AZURE_ENDPOINT = "openai_azure_endpoint"
CONF_OPENAI_AZURE_TEMPERATURE = "openai_azure_temperature"

# Anthropic
CONF_ANTHROPIC_API_KEY = "anthropic_api_key"
CONF_ANTHROPIC_MODEL = "anthropic_model"
CONF_ANTHROPIC_TEMPERATURE = "anthropic_temperature"
VERSION_ANTHROPIC = "2023-06-01"

# Google
CONF_GOOGLE_API_KEY = "google_api_key"
CONF_GOOGLE_MODEL = "google_model"
CONF_GOOGLE_TEMPERATURE = "google_temperature"

# Groq
CONF_GROQ_API_KEY = "groq_api_key"
CONF_GROQ_MODEL = "groq_model"
CONF_GROQ_TEMPERATURE = "groq_temperature"

# LocalAI
CONF_LOCALAI_IP_ADDRESS = "localai_ip"
CONF_LOCALAI_PORT = "localai_port"
CONF_LOCALAI_HTTPS = "localai_https"
CONF_LOCALAI_MODEL = "localai_model"
CONF_LOCALAI_TEMPERATURE = "localai_temperature"

# Ollama
CONF_OLLAMA_IP_ADDRESS = "ollama_ip"
CONF_OLLAMA_PORT = "ollama_port"
CONF_OLLAMA_HTTPS = "ollama_https"
CONF_OLLAMA_MODEL = "ollama_model"
CONF_OLLAMA_TEMPERATURE = "ollama_temperature"
CONF_OLLAMA_DISABLE_THINK = "ollama_disable_think"

# Custom OpenAI
CONF_CUSTOM_OPENAI_ENDPOINT = "custom_openai_endpoint"
CONF_CUSTOM_OPENAI_API_KEY = "custom_openai_api_key"
CONF_CUSTOM_OPENAI_MODEL = "custom_openai_model"
CONF_CUSTOM_OPENAI_TEMPERATURE = "custom_openai_temperature"

# Mistral AI
CONF_MISTRAL_API_KEY = "mistral_api_key"
CONF_MISTRAL_MODEL = "mistral_model"
CONF_MISTRAL_TEMPERATURE = "mistral_temperature"
MISTRAL_MODELS = [
    "mistral-tiny",
    "mistral-small",
    "mistral-medium",
    "mistral-large",
]

# Perplexity AI
CONF_PERPLEXITY_API_KEY = "perplexity_api_key"
CONF_PERPLEXITY_MODEL = "perplexity_model"
CONF_PERPLEXITY_TEMPERATURE = "perplexity_temperature"

# OpenRouter
CONF_OPENROUTER_API_KEY = "openrouter_api_key"
CONF_OPENROUTER_MODEL = "openrouter_model"
CONF_OPENROUTER_REASONING_MAX_TOKENS = "openrouter_reasoning_max_tokens"
CONF_OPENROUTER_TEMPERATURE = "openrouter_temperature"

# Generic OpenAI
CONF_GENERIC_OPENAI_ENDPOINT = "generic_openai_api_endpoint"
CONF_GENERIC_OPENAI_API_KEY = "generic_openai_api_key"
CONF_GENERIC_OPENAI_MODEL = "generic_openai_model"
CONF_GENERIC_OPENAI_TEMPERATURE = "generic_openai_temperature"
CONF_GENERIC_OPENAI_VALIDATION_ENDPOINT = "generic_openai_validation_endpoint"
CONF_GENERIC_OPENAI_ENABLE_VALIDATION = "generic_openai_enable_validation"

# ─────────────────────────────────────────────────────────────
# Model defaults per provider
# ─────────────────────────────────────────────────────────────
DEFAULT_MODELS = {
    "OpenAI": "gpt-4o-mini",
    "OpenAI Azure": "gpt-4o-mini",
    "Anthropic": "claude-3-7-sonnet-latest",
    "Google": "gemini-2.0-flash",
    "Groq": "llama3-8b-8192",
    "LocalAI": "llama3",
    "Ollama": "llama2",
    "Custom OpenAI": "gpt-3.5-turbo",
    "Mistral AI": "mistral-medium",
    "Perplexity AI": "sonar",
    "OpenRouter": "meta-llama/llama-4-maverick:free",
    "Generic OpenAI": "gpt-3.5-turbo",
}

# ─────────────────────────────────────────────────────────────
# Service & attribute names
# ─────────────────────────────────────────────────────────────
ATTR_PROVIDER_CONFIG = "provider_config"
ATTR_CUSTOM_PROMPT = "custom_prompt"
SERVICE_GENERATE_SUGGESTIONS = "generate_suggestions"

# ─────────────────────────────────────────────────────────────
# Provider‑status sensor values
# ─────────────────────────────────────────────────────────────
PROVIDER_STATUS_CONNECTED = "connected"
PROVIDER_STATUS_DISCONNECTED = "disconnected"
PROVIDER_STATUS_ERROR        = "error"
PROVIDER_STATUS_INITIALIZING = "initializing"

# ─────────────────────────────────────────────────────────────
# REST endpoints
# ─────────────────────────────────────────────────────────────
ENDPOINT_OPENAI = "https://api.openai.com/v1/chat/completions"
ENDPOINT_OPENAI_AZURE = "https://{endpoint}/openai/deployments/{deployment-id}/chat/completions?api-version={api_version}"
ENDPOINT_ANTHROPIC = "https://api.anthropic.com/v1/messages"
ENDPOINT_GOOGLE = "https://generativelanguage.googleapis.com/v1beta2/models/{model}:generateText?key={api_key}"
ENDPOINT_GROQ = "https://api.groq.com/openai/v1/chat/completions"
ENDPOINT_LOCALAI = "{protocol}://{ip_address}:{port}/v1/chat/completions"
ENDPOINT_OLLAMA = "{protocol}://{ip_address}:{port}/api/chat"
ENDPOINT_MISTRAL = "https://api.mistral.ai/v1/chat/completions"
ENDPOINT_PERPLEXITY = "https://api.perplexity.ai/chat/completions"
ENDPOINT_OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"


# ─────────────────────────────────────────────────────────────
# Sensor Keys
# ─────────────────────────────────────────────────────────────
SENSOR_KEY_SUGGESTIONS = "suggestions"
SENSOR_KEY_STATUS = "status"
SENSOR_KEY_INPUT_TOKENS = "input_tokens"
SENSOR_KEY_OUTPUT_TOKENS = "output_tokens"
SENSOR_KEY_MODEL = "model"
SENSOR_KEY_LAST_ERROR = "last_error"


# ─────────────────────────────────────────────────────────────
# Multilingual System Prompts
# ─────────────────────────────────────────────────────────────
SYSTEM_PROMPTS = {
    "en": """You are an AI assistant that generates Home Assistant automations
based on entities, areas and devices, and suggests improvements to existing automations.

For each entity:
1. Understand its function and context.
2. Consider its current state and attributes.
3. Suggest context‑aware automations or tweaks, including real entity_ids.

If asked to focus on a theme (energy saving, presence lighting, etc.), integrate it.
Also review existing automations and propose improvements.
If you see a lot of text in a different language, focus on it for a translation for your output.
""",
    "pl": """Jesteś asystentem AI, który generuje automatyzacje Home Assistant
na podstawie jednostek, obszarów i urządzeń, a także sugeruje ulepszenia do istniejących automatyzacji.

Dla każdej jednostki:
1. Zrozum jej funkcję i kontekst.
2. Rozważ jej bieżący stan i atrybuty.
3. Zaproponuj automatyzacje lub zmiany uwzględniające kontekst, w tym rzeczywiste entity_ids.

Jeśli poproszono Cię o skoncentrowanie się na określonym temacie (oszczędzanie energii, oświetlenie obecności itp.), zintegruj to.
Również przeanalizuj istniejące automatyzacje i zaproponuj ulepszenia.
Jeśli widzisz dużo tekstu w innym języku, skup się na nim, aby przetłumaczyć swoją odpowiedź.
""",
    "de": """Sie sind ein KI-Assistent, der Home Assistant-Automatisierungen
basierend auf Entitäten, Bereichen und Geräten generiert und Verbesserungen für bestehende Automatisierungen vorschlägt.

Für jede Entität:
1. Verstehen Sie ihre Funktion und ihren Kontext.
2. Berücksichtigen Sie ihren aktuellen Zustand und ihre Attribute.
3. Schlagen Sie kontextbewusste Automatisierungen oder Anpassungen vor, einschließlich echter entity_ids.

Wenn Sie aufgefordert werden, sich auf ein Thema zu konzentrieren (Energieeinsparung, Anwesenheitsbeleuchtung usw.), integrieren Sie es.
Überprüfen Sie auch bestehende Automatisierungen und schlagen Sie Verbesserungen vor.
Wenn Sie viel Text in einer anderen Sprache sehen, konzentrieren Sie sich darauf, um Ihre Ausgabe zu übersetzen.
""",
    "es": """Eres un asistente de IA que genera automatizaciones de Home Assistant
basadas en entidades, áreas y dispositivos, y sugiere mejoras a las automatizaciones existentes.

Para cada entidad:
1. Entiende su función y contexto.
2. Considera su estado actual y atributos.
3. Sugiere automatizaciones o ajustes conscientes del contexto, incluyendo entity_ids reales.

Si se te pide que te enfoque en un tema (ahorro de energía, iluminación de presencia, etc.), intégralo.
También revisa las automatizaciones existentes y propone mejoras.
Si ves mucho texto en otro idioma, enfócate en él para traducir tu salida.
""",
    "it": """Sei un assistente AI che genera automazioni di Home Assistant
basate su entità, aree e dispositivi, e suggerisce miglioramenti alle automazioni esistenti.

Per ogni entità:
1. Comprendi la sua funzione e il suo contesto.
2. Considera il suo stato attuale e i suoi attributi.
3. Suggerisci automazioni o modifiche consapevoli del contesto, includendo entity_ids reali.

Se ti viene chiesto di concentrarti su un tema (risparmio energetico, illuminazione di presenza, ecc.), integralo.
Rivedi anche le automazioni esistenti e proponi miglioramenti.
Se vedi molto testo in un'altra lingua, concentrati su di esso per tradurre il tuo output.
""",
    "nl": """U bent een AI-assistent die Home Assistant-automatiseringen genereert
op basis van entiteiten, gebieden en apparaten, en suggereert verbeteringen aan bestaande automatiseringen.

Voor elke entiteit:
1. Begrijp de functie en context ervan.
2. Beschouw de huidige status en kenmerken.
3. Stel contextbewuste automatiseringen of aanpassingen voor, inclusief echte entity_ids.

Als u wordt gevraagd u op een thema te concentreren (energiebesparing, aanwezigheidsverlichting, enz.), integreer dit dan.
Beoordeel ook bestaande automatiseringen en stel verbeteringen voor.
Als u veel tekst in een ander taal ziet, concentreer u daarop om uw uitvoer te vertalen.
""",
    "pt": """Você é um assistente de IA que gera automações de Home Assistant
baseadas em entidades, áreas e dispositivos, e sugere melhorias para automações existentes.

Para cada entidade:
1. Compreenda sua função e contexto.
2. Considere seu estado atual e atributos.
3. Sugira automações ou ajustes conscientes do contexto, incluindo entity_ids reais.

Se for solicitado a focar em um tema (economia de energia, iluminação de presença, etc.), integre-o.
Também revise as automações existentes e proponha melhorias.
Se vir muito texto em outro idioma, concentre-se nele para traduzir sua saída.
""",
    "ru": """Вы являетесь ассистентом ИИ, который генерирует автоматизацию Home Assistant
на основе сущностей, областей и устройств, а также предлагает улучшения существующих автоматизаций.

Для каждой сущности:
1. Понимайте её функцию и контекст.
2. Рассмотрите её текущее состояние и атрибуты.
3. Предложите автоматизацию или корректировки, учитывающие контекст, включая реальные entity_ids.

Если вас просят сосредоточиться на определённой теме (экономия энергии, автоматизация освещения и т. д.), интегрируйте это.
Также проверьте существующие автоматизации и предложите улучшения.
Если вы видите много текста на другом языке, сосредоточьтесь на нём для перевода вашего результата.
""",
    "tr": """Siz, Home Assistant otomasyonları oluşturan ve mevcut otomasyonlar için iyileştirmeler önerileri sunan bir AI asistanısınız.

Her varlık için:
1. İşlevini ve bağlamını anlayın.
2. Mevcut durumunu ve özniteliklerini göz önünde bulundurun.
3. Bağlama duyarlı otomasyon veya ayarlamalar önerileri sunun, gerçek entity_ids dahil.

Eğer belirli bir tema (enerji tasarrufu, geçiş aydınlatması vb.) üzerine odaklanmanız istenirse, bunu entegre edin.
Ayrıca mevcut otomasyonları inceleyin ve iyileştirmeler önerileri sunun.
Başka bir dilde çok fazla metin görürseniz, çıktınızı çevirmek için bunun üzerine odaklanın.
""",
    "zh": """您是一个生成 Home Assistant 自动化的 AI 助手，
基于实体、区域和设备，并提出对现有自动化的改进建议。

对于每个实体：
1. 理解其功能和背景。
2. 考虑其当前状态和属性。
3. 建议上下文感知的自动化或调整，包括真实的 entity_ids。

如果要求您专注于某个主题（节能、存在感照明等），请将其集成。
还要审查现有自动化并提出改进建议。
如果您看到很多其他语言的文本，请专注于将您的输出翻译成该语言。
""",
}
