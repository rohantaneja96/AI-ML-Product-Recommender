import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# ✅ Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file")

def generate_creative_description(base_description: str, category: str):
    """
    Generate creative product descriptions using Google Gemini via LangChain.
    Compatible with Gemini 2.0+ models and v1beta API.
    """
    template = """
    You are an AI product marketing assistant.
    Write a short, catchy, and creative marketing-style description for a furniture product.
    Use a warm, human-like tone.
    Original details: {base_description}
    Category: {category}
    Keep it premium and engaging, within 2 lines.
    """

    prompt = PromptTemplate(template=template, input_variables=["base_description", "category"])

    try:
        # ✅ Use stable model compatible with LangChain (v1beta)
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",  # ✅ stable model your key supports
            temperature=0.8,
            google_api_key=GOOGLE_API_KEY
        )

        # Generate description
        response = llm.invoke(prompt.format(base_description=base_description, category=category))

        return response.content.strip() if hasattr(response, "content") else str(response)

    except Exception as e:
        # Handle and show readable GenAI error
        return f"[GenAI error: {str(e)}]"
