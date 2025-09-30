import requests
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ChatMessage:
    role: str
    content: str

@dataclass
class ChatResponse:
    content: str
    usage: Optional[Dict[str, int]] = None

class OpenRouterClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://openrouter.ai/api/v1'
        self.model = 'x-ai/grok-4-fast:free'

    def chat(self, messages: List[ChatMessage]) -> ChatResponse:
        try:
            response = requests.post(
                f'{self.base_url}/chat/completions',
                headers={
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json',
                    'HTTP-Referer': os.getenv('APP_URL', 'http://localhost:7860'),
                    'X-Title': 'AI Research Assistant - Powered by DeepSeek V3'
                },
                json={
                    'model': self.model,
                    'messages': [{'role': msg.role, 'content': msg.content} for msg in messages],
                    'temperature': 0.2,
                    'max_tokens': 4000,
                    'stream': False,
                    'top_p': 0.9,
                    'frequency_penalty': 0.1,
                    'presence_penalty': 0.1
                }
            )

            if not response.ok:
                error_data = response.json() if response.content else {}
                error_message = error_data.get('error', {}).get('message', 'Unknown error occurred')
                raise Exception(f'AI service error: {response.status_code} - {error_message}')

            data = response.json()

            if not data.get('choices') or len(data['choices']) == 0:
                raise Exception('The AI model did not generate a response. This might be due to content filtering or a temporary service issue.')

            return ChatResponse(
                content=data['choices'][0]['message']['content'],
                usage=data.get('usage')
            )

        except requests.exceptions.RequestException as e:
            raise Exception(f'Network error while connecting to AI service: {str(e)}')
        except Exception as error:
            print(f'OpenRouter API error: {error}')
            raise error

    def synthesize_search_results(self, query: str, search_results: List[Any]) -> str:
        system_prompt = """You are an expert research assistant with a talent for synthesizing information from multiple sources into clear, comprehensive answers.

Your expertise includes:
- Reading and analyzing diverse sources quickly and accurately
- Identifying key insights and connecting related information
- Presenting complex topics in an accessible, engaging way
- Maintaining objectivity while acknowledging different perspectives
- Providing proper citations so readers can verify and explore further

When synthesizing information:
1. Lead with the most important insights that directly answer the question
2. Organize information logically with clear headings when helpful
3. Include relevant details and context that enhance understanding
4. Note any conflicting information and explain different viewpoints
5. Use citations [1], [2], etc. that correspond to the numbered sources
6. Write in a conversational but authoritative tone
7. Ensure accuracy while making the content engaging and readable

Remember: Your goal is to save the reader time while giving them confidence in the information and the ability to dive deeper if they want."""

        search_context = '\n'.join([
            f"[{index + 1}] {result.title}\nSource: {result.domain}\nURL: {result.url}\nContent: {result.snippet}\n"
            for index, result in enumerate(search_results)
        ])

        user_prompt = f"""Research Question: {query}

Sources Found:
{search_context}

Please provide a comprehensive, well-researched answer based on these sources. Structure your response to be informative and engaging, with proper citations using [1], [2], etc. format. If sources present different perspectives, acknowledge them. Focus on accuracy and clarity while maintaining a conversational tone."""

        messages = [
            ChatMessage(role='system', content=system_prompt),
            ChatMessage(role='user', content=user_prompt)
        ]

        response = self.chat(messages)
        return response.content

_openrouter_client = None

def get_openrouter_client() -> OpenRouterClient:
    global _openrouter_client

    if _openrouter_client is None:
        api_key = os.getenv('OPENROUTER_API_KEY')

        if not api_key:
            raise Exception(
                'OpenRouter API key not configured. '
                'Please add OPENROUTER_API_KEY to your .env file. '
                'Get your key at https://openrouter.ai'
            )

        _openrouter_client = OpenRouterClient(api_key)

    return _openrouter_client