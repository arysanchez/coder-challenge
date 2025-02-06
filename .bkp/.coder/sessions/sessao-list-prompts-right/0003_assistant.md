### frontend/index.html [coder:save]
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coder & Furious</title>
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
</head>
<body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
</body>
</html>
```
[coder:end]

### frontend/src/api/endpoints.ts [coder:save]
```typescript
import { ApiResponse, Conversation, Message, Prompt } from '../types';

const API_BASE_URL = 'http://127.0.0.1:8000/api'; // Update this with your FastAPI server URL

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
  const response = await fetch(`${API_BASE_URL}/list-prompt`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  const data = await response.json();
  return {
    success: response.ok,
    data: response.ok ? data : undefined,
    error: response.ok ? undefined : data.detail,
  };
}

export async function saveSelectedPrompts(prompts: Prompt[]): Promise<ApiResponse<Prompt>> {
  const response = await fetch(`${API_BASE_URL}/create-prompt`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(prompts),
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