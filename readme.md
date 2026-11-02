## Criar e ativar o ambiente virtual

Na raiz do projeto, crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative-o no Linux ou macOS:

```bash
source .venv/bin/activate
```

No Windows, usando PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```
```bash
pip3 install fastapi uvicorn sqlalchemy "passlib[bcrypt]" "python-jose[cryptography]" python-dotenv python-multipart
```
### Executar projeto
```bash
uvicorn main:app --reload
```
