
def analyze_code(client, code_text):
    try:
        with open("prompts/prompt.txt", "r", encoding="utf-8") as f:
            base_prompt = f.read()
        full_prompt = base_prompt + "\n\n" + code_text

        for model in ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"]:
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a cybersecurity expert."},
                        {"role": "user", "content": full_prompt}
                    ]
                )
                return f"<p style='color:#58a6ff'><b> Model used:</b> {model}</p>\n\n" + response.choices[0].message.content.strip()
            except Exception as e:
                continue

        return "<span style='color:red'>❌ All models failed. Check API access.</span>"

    except Exception as e:
        return f"<span style='color:red'>❌ Error: {e}</span>"
