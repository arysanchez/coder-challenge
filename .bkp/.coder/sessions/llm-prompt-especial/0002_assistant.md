To fix the error "Body has already been consumed" in the `saveSelectedPrompts` function, we need to ensure that the response body is not being consumed multiple times. This can be done by checking the response status before attempting to parse the JSON body.

Let's update the `saveSelectedPrompts` function in `frontend/src/api/endpoints.ts` to handle this correctly.

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

  const data = await response.json();
  return {
    success: response.ok,
    data: response.ok ? data : undefined,
    error: response.ok ? undefined : data.detail,
  };
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

This update ensures that the response body is only consumed once and the result is returned in a consistent format.