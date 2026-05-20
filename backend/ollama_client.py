"""
Ollama LLM Client Wrapper
Handles communication with local Ollama instance for AI tutoring
"""

import requests
from flask import current_app


class OllamaClient:
    """Wrapper for Ollama HTTP API"""

    @staticmethod
    def get_url():
        return current_app.config.get('OLLAMA_API_URL', 'http://localhost:11434')

    @staticmethod
    def get_model():
        return current_app.config.get('OLLAMA_MODEL', 'mistral')

    @staticmethod
    def get_timeout():
        return current_app.config.get('OLLAMA_TIMEOUT', 30)

    @staticmethod
    def is_available():
        """Check if Ollama is running and reachable"""
        try:
            response = requests.get(
                f'{OllamaClient.get_url()}/api/tags',
                timeout=5
            )
            return response.status_code == 200
        except Exception:
            return False

    @staticmethod
    def list_models():
        """List available models in Ollama"""
        try:
            response = requests.get(
                f'{OllamaClient.get_url()}/api/tags',
                timeout=5
            )
            if response.status_code == 200:
                return response.json().get('models', [])
            return []
        except Exception:
            return []

    @staticmethod
    def generate(prompt, context=None, system=None):
        """
        Generate AI response for a question

        Args:
            prompt: The user's question or prompt
            context: Optional context (e.g., subject, grade level)
            system: Optional system prompt

        Returns:
            tuple: (response_text, error_message)
                - response_text is None if there's an error
                - error_message is None if successful
        """
        try:
            payload = {
                'model': OllamaClient.get_model(),
                'prompt': prompt,
                'stream': False,
                'options': {
                    'temperature': 0.7,
                    'top_p': 0.9,
                }
            }

            if system:
                payload['system'] = system

            response = requests.post(
                f'{OllamaClient.get_url()}/api/generate',
                json=payload,
                timeout=OllamaClient.get_timeout()
            )

            if response.status_code == 200:
                data = response.json()
                return data.get('response', '').strip(), None
            else:
                return None, f'Ollama returned status {response.status_code}'

        except requests.Timeout:
            return None, 'Ollama response timeout'
        except requests.ConnectionError:
            return None, 'Cannot connect to Ollama. Is it running?'
        except Exception as e:
            return None, f'Ollama error: {str(e)}'

    @staticmethod
    def answer_doubt(question, subject=None, grade_level=None):
        """
        Generate an educational AI response to a student's doubt

        Args:
            question: The student's question
            subject: Subject of the question (Math, Science, etc.)
            grade_level: Student's grade level (1-10)

        Returns:
            tuple: (response_text, error_message)
        """
        system_prompt = (
            "You are a friendly, patient AI tutor helping rural school students "
            "in India (grades 1-10). Provide clear, simple, age-appropriate "
            "explanations. Use examples that are relatable. Keep responses concise "
            "but thorough. If you don't know something, say so honestly."
        )

        context_parts = []
        if subject:
            context_parts.append(f"Subject: {subject}")
        if grade_level:
            context_parts.append(f"Student Grade Level: {grade_level}")

        context = "\n".join(context_parts) if context_parts else ""

        full_prompt = f"{context}\n\nStudent's Question: {question}\n\nAnswer:" if context else f"Student's Question: {question}\n\nAnswer:"

        return OllamaClient.generate(full_prompt, system=system_prompt)
