import os
from pygments.lexers import guess_lexer, get_lexer_for_filename
from pygments.token import Token

def programming_language_of(filepath: str, source_code: str):
    _, ext = os.path.splitext(filepath)
    if ext.lower() == '.txt':
        return guess_lexer(source_code)
    else:
        return get_lexer_for_filename(filepath)


class InputCleaner:
    def clean(self, filepath: str, source_code: str) -> str:
        try:
            lexer = programming_language_of(filepath, source_code)
            tokens = lexer.get_tokens(source_code)

            cleaned_code = ""
            for token_type, value in tokens:
                # Remove any comment or any docstring
                if token_type in Token.Comment or token_type in Token.Literal.String.Doc:
                    continue

                cleaned_code += value

            return cleaned_code
        except Exception:
            return source_code


class FunctionValidator:
    def has_function(self, filepath: str, source_code: str) -> bool:
        try:
            lexer = programming_language_of(filepath, source_code)
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