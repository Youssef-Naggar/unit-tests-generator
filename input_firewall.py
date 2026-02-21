import os
from pygments.lexers import guess_lexer
from pygments.token import Token


class InputCleaner:
    def clean(self, filepath: str, source_code: str) -> str:
        try:
            lexer = guess_lexer(filepath, source_code)
            tokens = lexer.get_tokens(source_code)

            cleaned_code = ""
            for token_type, value in tokens:
                # Remove any comment
                if token_type in Token.Comment:
                    continue

                cleaned_code += value

            return cleaned_code
        except Exception:
            return source_code


class FunctionValidator:
    def has_function(self, filepath: str, source_code: str) -> bool:
        try:
            lexer = guess_lexer(filepath, source_code)
            tokens = lexer.get_tokens(source_code)

            # Search for a function
            for token_type, value in tokens:
                if token_type in Token.Name.Function or (
                        token_type in Token.Keyword and value in ['def', 'define', 'function', 'fun', 'fn', 'proc', 'func']
                ):
                    return True
            return False
        except Exception:
            return False