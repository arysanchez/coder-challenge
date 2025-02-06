Os erros que você está enfrentando no arquivo `endpoints.ts` são devido à falta de importações dos tipos `ApiResponse`, `Conversation`, `Message` e `Prompt`. Esses tipos estão definidos no arquivo `types.ts`, mas não foram importados no arquivo `endpoints.ts`.

Vamos corrigir isso importando os tipos necessários no início do arquivo `endpoints.ts`.

### frontend/src/api/endpoints.ts [coder:save]
```typescript
import { ApiResponse, Conversation, Message, Prompt } from '../types';

const API_BASE_URL = 'http://localhost:8000/api'; // Update this with your FastAPI server URL

export async function createNewChat(): Promise<ApiResponse<Conversation>> {
  const response = await fetch(`${API_BASE_URL}/chats`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
}

export async function sendMessage(content: string, conversationId: string): Promise<ApiResponse<Message>> {
  const response = await fetch(`${API_BASE_URL}/messages`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      content,
      conversation_id: conversationId,
    }),
  });
  return response.json();
}

export async function fetchPrompts(): Promise<ApiResponse<Prompt[]>> {
  const response = await fetch(`${API_BASE_URL}/v1/prompt-manager`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
}

export async function saveSelectedPrompts(promptIds: string[]): Promise<ApiResponse<void>> {
  const response = await fetch(`${API_BASE_URL}/prompts/save`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ prompt_ids: promptIds }),
  });
  return response.json();
}

export async function toggleFavorite(conversationId: string, isFavorite: boolean): Promise<ApiResponse<void>> {
  const response = await fetch(`${API_BASE_URL}/conversations/${conversationId}/favorite`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ is_favorite: isFavorite }),
  });
  return response.json();
}
```
[coder:end]

### Explicação

1. **Importações**: Adicionamos as importações dos tipos `ApiResponse`, `Conversation`, `Message` e `Prompt` do arquivo `types.ts`. Isso resolve os erros de "Cannot find name" que você estava enfrentando.

2. **Integração com o Backend**: Este arquivo `endpoints.ts` define funções assíncronas que fazem chamadas HTTP para o backend FastAPI. Cada função corresponde a uma rota específica no backend:
   - `createNewChat`: Cria um novo chat.
   - `sendMessage`: Envia uma mensagem para um chat específico.
   - `fetchPrompts`: Busca os prompts disponíveis.
   - `saveSelectedPrompts`: Salva os prompts selecionados.
   - `toggleFavorite`: Alterna o estado de favorito de uma conversa.

Essas funções utilizam a API Fetch para fazer requisições HTTP e retornam os dados no formato esperado, encapsulados em um tipo `ApiResponse`. Isso facilita a integração do frontend com o backend, permitindo que você chame essas funções diretamente nos componentes React para interagir com o backend FastAPI.