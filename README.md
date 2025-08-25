# 🎨 chromalogger

Um logger colorido, contextual e super fácil de usar para Python.  
Ideal para dar aquele toque profissional e visual no terminal, com timestamps configuráveis e logs gravados em arquivo.

---

## 🚀 Instalação

```bash
pip install git+https://github.com/GussApenas/chromalogger
```

---

## 💡 Por que usar `chromalogger`?

- Logs coloridos e fáceis de ler no terminal  
- Timestamp configurável (padrão para horário do Brasil UTC−3)  
- Suporte a contexto (dicionários, objetos JSON)  
- Fácil gravação de logs em arquivo  
- Métodos intuitivos: `info()`, `warn()`, `error()`, `debug()`, `success()`

---

## 🧰 Como usar

```python
from chromalogger import log

# Log simples com timestamp padrão (Brasil UTC-3)
log.info("Servidor iniciado")

# Log com contexto JSON
log.warn("Uso alto de CPU", context={"cpu": "92%"})

# Log com timestamp em UTC
log.debug("Debug em UTC", timezone=0)

# Log sem timestamp e sem cores
log.error("Erro crítico sem timestamp e sem cores", timestamp=False, colors=False)

# Grava log diretamente em arquivo (sem cores, timestamp padrão)
log.to_file("Mensagem salva no arquivo", file="logs/app.log", level="INFO")
```

---

## ⚙️ Parâmetros por método

| Parâmetro  | Tipo     | Padrão  | Descrição                                               |
|------------|----------|---------|---------------------------------------------------------|
| `msg`      | `str`    | —       | Mensagem a ser logada                                   |
| `context`  | `dict`   | `None`  | Informações adicionais (mostradas em JSON no log)       |
| `timestamp`| `bool`   | `True`  | Mostrar timestamp no log                                |
| `colors`   | `bool`   | `True`  | Usar cores no terminal                                  |
| `timezone` | `int`    | `-3`    | Offset de fuso horário para timestamp (ex: -3 = BR)   |

---

## 📚 Métodos disponíveis

| Método       | Descrição                         |
|--------------|----------------------------------|
| `log.info()` | Informações gerais                |
| `log.warn()` | Avisos                           |
| `log.error()`| Erros críticos                   |
| `log.debug()`| Mensagens de depuração           |
| `log.success()` | Mensagens de sucesso           |
| `log.to_file()` | Grava mensagens direto em arquivo|

---

## 🤝 Contribua!

Quer ajudar a melhorar o `chromalogger`?  
Sinta-se à vontade para abrir issues e pull requests no [GitHub](https://github.com/GussApenas/chromalogger)!

---

### Desenvolvido com 💜 por Guss

---
