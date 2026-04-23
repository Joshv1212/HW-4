from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

experiments = [
    {
        "label": "Basic explanation",
        "prompt": "Explain neural networks in 2 sentences."
    },
    {
        "label": "Audience change",
        "prompt": "Explain neural networks to a 10-year-old in 2 sentences."
    },
    {
        "label": "Format constraint",
        "prompt": "Explain neural networks in exactly 3 bullet points."
    }
]

for exp in experiments:
    response = client.responses.create(
        model="gpt-5",
        input=exp["prompt"]
    )

    print("\n==============================")
    print("Experiment:", exp["label"])
    print("Prompt:", exp["prompt"])
    print("Output:")
    print(response.output_text)
