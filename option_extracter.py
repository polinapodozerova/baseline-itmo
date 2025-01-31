import os
from openai import AsyncOpenAI

from together import AsyncTogether

client = AsyncTogether()


async def get_option(query, correct_answer):
    # client = AsyncOpenAI(
    #     base_url="https://api.scaleway.ai/v1",
    #     api_key=os.environ['TOGETHER_API_KEY']
    # )

    completion = await client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content":
                  f"Напиши какой из вариантов ответов соответствует \
                данному правильному ответу:\n\
              Вопрос:{query}\n\
              Правильный ответ:{correct_answer}\n\
              напиши одно число - вариант ответа \
                  соответствующий правильному"}],
    )

    return completion.choices[0].message.content


def extract_sources(results):
    sources = []
    for res in results:
        if res["url"] and res["url"] not in sources:
            sources.append(res["url"])
    return sources

# import asyncio

# query = "В каком рейтинге (по состоянию на 2021 год) ИТМО впервые вошёл в топ-400 мировых университетов?\n1. ARWU (Shanghai Ranking)\n2. Times Higher Education (THE) World University Rankings\n3. QS World University Rankings\n4. U.S. News & World Report Best Global Universities"
# correct_answer = "ИТМО впервые вошло в топ-400 мировых университетов в QS World University Rankings в 2021 году, заняв 365-е место."

# async def main():
#     answer = await get_option(query, correct_answer)
#     print(answer)

# asyncio.run(main())