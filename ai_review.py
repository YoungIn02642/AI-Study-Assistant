from openai import OpenAI

client = OpenAI()

def review_code(code):

    prompt = f"""
    다음 코드를 분석해 주세요.

    언어를 먼저 판단하고 아래를 설명하세요.

    1. 코드 설명
    2. 문제점
    3. 시간복잡도
    4. 개선 코드

    코드:
    {code}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output[0].content[0].text