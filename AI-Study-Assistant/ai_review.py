from openai import OpenAI

client = OpenAI()

def review_code(code):

    prompt = f"""
    다음 코드를 분석해줘.

    1. 코드 설명
    2. 문제점
    3. 시간복잡도
    4. 개선 코드
    5. 더 좋은 알고리즘이 있으면 제안하기

    코드:
    {code}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output[0].content[0].text