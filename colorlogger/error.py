from difflib import get_close_matches

class InvalidLogMethod(Exception):
    def __init__(self, method, valid_methods):
        suggestion = get_close_matches(method.upper(), valid_methods, n=1)
        hint = f"Você quis dizer: 'log.{suggestion[0].lower()}()'?" if suggestion else ""
        super().__init__(
            f"Erro: '{method}' não é um método válido.\n"
            f"{hint}\nMétodos disponíveis: {', '.join(m.lower() for m in valid_methods)}"
        )