import re

class OutputFormatter:
    def _strip_comments(self, code: str) -> str:
        code = re.sub(r'/\*.*?\*/', '', code)
        code = re.sub(r'(//|#).*?$', '', code)
        return re.sub(r'\n\s*\n', '\n', code)


    def format(self, raw_output: str) -> str:
        cleaned = raw_output.strip()

        # Remove opening markdown fences
        cleaned = re.sub(r'^```[a-zA-Z]*\n', '', cleaned)

        # Remove closing markdown
        cleaned = re.sub(r'\n```$', '', cleaned)
        cleaned = re.sub(r'```$', '', cleaned)

        # Extract pure code
        if '```' in cleaned:
            match = re.search(r'```[a-zA-Z]*\n(.*?)```', cleaned, re.DOTALL)
            if match:
                cleaned = match.group(1).strip()
            else:
                # If there's an unmatched backtick block, remove it manually
                cleaned = cleaned.replace('```', '')
        # Remove comments
        cleaned = self._strip_comments(cleaned)
        return cleaned.strip()