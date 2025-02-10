# Context

All files complete source code.

## Project Structure

/
├── .bolt/
│   ├── config.json
│   └── prompt
├── .vscode/
│   ├── chatHistory.json
│   └── launch.json
├── backend/
│   ├── app/
│   │   ├── apis/
│   │   │   ├── __init__.py
│   │   │   └── prompts.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── prompt.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── endpoints.ts
│   │   ├── components/
│   │   │   ├── ChatInput.tsx
│   │   │   ├── ChatMessage.tsx
│   │   │   └── Sidebar.tsx
│   │   ├── App.tsx
│   │   ├── index.css
│   │   ├── main.tsx
│   │   ├── types.ts
│   │   └── vite-env.d.ts
│   ├── eslint.config.js
│   ├── favicon.ico
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── .env.local
└── README.md

## File Contents

### .bolt/config.json
```
{
  "template": "bolt-vite-react-ts"
}
```

### .bolt/prompt
```
For all designs I ask you to make, have them be beautiful, not cookie cutter. Make webpages that are fully featured and worthy for production.

By default, this template supports JSX syntax with Tailwind CSS classes, React hooks, and Lucide React for icons. Do not install other packages for UI themes, icons, etc unless absolutely necessary or I request them.

Use icons from lucide-react for logos.

Use stock photos from unsplash where appropriate, only valid URLs you know exist. Do not download the images, only link to them in image tags.
```

### .vscode/chatHistory.json
```
[
  {
    "content": "como iniciar um repositorio",
    "role": "user",
    "name": "coderExtensionChat"
  },
  {
    "content": "Para iniciar e configurar um repositório Git, você pode seguir os passos abaixo:\n\n1. **Instale o Git**: Se ainda não o fez, você precisa instalar o Git em sua máquina. Você pode baixar e instalar a versão mais recente do Git a partir do site oficial: [https://git-scm.com/](https://git-scm.com/).\n\n2. **Configurar o Git**: Depois de instalar o Git, é recomendável configurar seu nome de usuário e endereço de e-mail. Estes serão usados para identificar as suas alterações.\n\n   ```bash\n   git config --global user.name \"Seu Nome\"\n   git config --global user.email \"seu-email@example.com\"\n   ```\n\n3. **Iniciar um repositório**: Navegue até o diretório onde você quer criar o repositório e inicialize um novo repositório Git. Aqui estão os comandos:\n\n   ```bash\n   cd /caminho/para/seu/projeto\n   git init\n   ```\n\n4. **Adicionar arquivos e fazer o primeiro commit**:\n   - Adicione os arquivos que deseja monitorar (ou todos os arquivos do diretório) ao repositório e faça o primeiro commit:\n\n   ```bash\n   git add .\n   git commit -m \"Primeiro commit\"\n   ```\n\n5. **Conectar a um repositório remoto** (opcional, mas comum):\n   - Se você quiser conectar seu repositório local a um repositório remoto (por exemplo, no GitHub, GitLab ou Bitbucket), você pode usar o comando `git remote add` para adicionar o URL do repositório remoto:\n\n   ```bash\n   git remote add origin https://github.com/usuario/repositorio.git\n   git branch -M main\n   git push -u origin main\n   ```\n\nAgora você tem um repositório Git inicializado e conectado a um repositório remoto (se aplicável). Este é apenas o começo, mas cobre os fundamentos de iniciar e configurar um repositório Git.",
    "role": "assistant",
    "name": "coderExtensionChat"
  }
]
```

### .vscode/launch.json
```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Sidebar Component",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "webRoot": "${workspaceFolder}/frontend/src",
      "sourceMaps": true,
      "trace": true,
      "sourceMapPathOverrides": {
        "webpack:///src/*": "${webRoot}/*"
      }
    }
  ]
}
```

### backend/app/apis/__init__.py
```
from fastapi import APIRouter
from .prompts import router as prompts_router

router = APIRouter()
router.include_router(prompts_router, prefix="/v1/prompt-templates", tags=["prompts"])
```

### backend/app/apis/prompts.py
```
from fastapi import APIRouter, HTTPException, Depends
from typing import List
import httpx
import os
from ..models.prompt import Prompt, CreatePromptRequest, PromptResponse, prompts_db

router = APIRouter()

EXTERNAL_API_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IkM3Q3V4MXM4V0dfYWNRZE5VLWh3bG1YNGtTV1c5Uzl3dV9oaHVIZVA2TlEiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJmZGUwYzc5Yi1lZjA5LTQ1MGYtYTUwOS0zZDAzMmNlMjFlODUiLCJpc3MiOiJodHRwczovL2NpdGZsb3dkZXZiMmMuYjJjbG9naW4uY29tL2QxZGVhMWU1LThhZWItNDE3ZS1hMWIyLWQ4NDAyZmNmNGE4Zi92Mi4wLyIsImV4cCI6MTczODg4MTk1NCwibmJmIjoxNzM4Nzk1NTU0LCJzdWIiOiIwYzEwMDhhMi01YTIyLTRkODgtYTZlMS1hOGUxYmY0YzEwOGYiLCJlbWFpbCI6ImFyeXNhbmNoZXpAY2lhbmR0LmNvbSIsImdpdmVuX25hbWUiOiJBcnkiLCJmYW1pbHlfbmFtZSI6IkhlbnJpcXVlIGRhIEx1eiBTYW5jaGV6IiwibmFtZSI6IkFyeSBIZW5yaXF1ZSBkYSBMdXogU2FuY2hleiIsImlkcCI6Imdvb2dsZS5jb20iLCJjaGFubmVsIjoicG9ydGFsIiwidGVuYW50IjoiY2l0LWRldiIsInJvbGVzIjoiZmxvd2NvcmUudXNlcixiYWNrbG9ncmVmaW5lci51c2VyLGNoYXR3aXRoZG9jcy51c2VyLGdhbGF4eW9wcy51c2VyIiwidGlkIjoiZDFkZWExZTUtOGFlYi00MTdlLWExYjItZDg0MDJmY2Y0YThmIiwiYXpwIjoiZmRlMGM3OWItZWYwOS00NTBmLWE1MDktM2QwMzJjZTIxZTg1IiwidmVyIjoiMS4wIiwiaWF0IjoxNzM4Nzk1NTU0fQ.REOeDg3AGv4RVDDQ_Kv7WSP1c_0Gbyk4RHiZQwlfppQ59AKbUGQR3vYMACsGzyj0Vp4QNKcDCWpVNGQ8AevG9mHYfjtcNTlqvXqyWyNQ6yYHJxxykbOsIZJsLJ-JI95Mu9GmKpHDMaKKTpkJQ9sX_CZlxrA2OJbklCNtENY5B3jDoYetF_VLByI1zNawG-ij_cOPADAvXndfNzflgcO1t0qukOflV09NS1FnO7ogkUHFpfRy3Ly3sS5f1FFHBVBGiqduDoWEBOLzZdqMHBxL_bYVaFlO1gTyrDLzzn2MsY8gcpOs-CxhJlVPOj1QLeqnXhlLsclyz5HRUnYKsmb8Ew"

@router.get("/list-prompt", response_model=List[PromptResponse])
async def list_external_prompts():
    headers = {
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get("https://dev.flow.ciandt.com/channels-service/v1/prompt-templates", headers=headers)
        response.raise_for_status()
        external_prompts = response.json()
        if not isinstance(external_prompts, list):
            raise HTTPException(status_code=500, detail="Invalid response format from external API")
        return [PromptResponse(title=prompt["title"], description=prompt["description"], prompt=prompt["prompt"], id=prompt["id"]) for prompt in external_prompts]

@router.post("/create-prompt", response_model=PromptResponse)
async def create_external_prompt(request: CreatePromptRequest):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://dev.flow.ciandt.com/channels-service/v1/prompt-templates",
                json=request.dict(),
                headers=headers
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"Error from external API: {exc.response.text}")
        created_prompt = response.json()
        return PromptResponse(title=created_prompt["title"], description=created_prompt["description"], prompt=created_prompt["prompt"])
```

### backend/app/core/__init__.py
```
# This file can be left empty or used for initialization code for the core module
```

### backend/app/core/config.py
```
# Configuration settings can be added here
```

### backend/app/models/__init__.py
```
# This file can be left empty or used for initialization code for the models module
```

### backend/app/models/prompt.py
```
from pydantic import BaseModel
from typing import List
from datetime import datetime

class PromptVariable(BaseModel):
    name: str
    title: str

class Prompt(BaseModel):
    id: str
    title: str
    description: str
    prompt: str
    variables: List[PromptVariable] = []
    visibleTo: str
    visibleToGroups: List[str]
    categories: List[str]
    createdAt: datetime
    updatedAt: datetime
    isOwner: bool
    ownerId: str

class CreatePromptRequest(BaseModel):
    title: str
    description: str
    prompt: str
    visibleTo: str
    visibleToGroups: List[str]
    categories: List[str]
    ownerId: str

class PromptResponse(BaseModel):
    id: str
    title: str
    description: str

# In-memory storage for prompts
prompts_db = []
```

### backend/main.py
```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.apis.prompts import router as prompts_router

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:3000",  # Adicione o endereço do seu frontend aqui
    "http://127.0.0.1:3000",  # Adicione o endereço do seu frontend aqui
    "http://localhost:5173",  # Adicione o endereço do seu frontend aqui
    "http://127.0.0.1:5173",  # Adicione o endereço do seu frontend aqui
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prompts_router, prefix="/api")
```

### frontend/src/api/endpoints.ts
```
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

### frontend/src/components/ChatInput.tsx
```
import React, { useState } from 'react';
import { Send, Paperclip, Mic } from 'lucide-react';
import { sendMessage } from '../api/endpoints';

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  conversationId: string;
}

export function ChatInput({ onSendMessage, conversationId }: ChatInputProps) {
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim() && !isLoading) {
      try {
        setIsLoading(true);
        const response = await sendMessage(message, conversationId);
        if (response.success) {
          onSendMessage(message);
          setMessage('');
        } else {
          console.error('Failed to send message:', response.error);
        }
      } catch (error) {
        console.error('Error sending message:', error);
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="border-t border-gray-200 dark:border-gray-700 p-4">
      <div className="flex items-center gap-2">
        <button
          type="button"
          className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
        >
          <Paperclip className="w-5 h-5 text-gray-500 dark:text-gray-400" />
        </button>
        
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message..."
          disabled={isLoading}
          className="flex-1 bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white rounded-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
        />
        
        <button
          type="button"
          className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
        >
          <Mic className="w-5 h-5 text-gray-500 dark:text-gray-400" />
        </button>
        
        <button
          type="submit"
          disabled={isLoading || !message.trim()}
          className="p-2 bg-blue-600 rounded-full hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <Send className="w-5 h-5 text-white" />
        </button>
      </div>
    </form>
  );
}
```

### frontend/src/components/ChatMessage.tsx
```
import React from 'react';
import type { Message } from '../types';

interface ChatMessageProps {
  message: Message;
}

export function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.sender === 'user';
  
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div
        className={`max-w-[70%] rounded-2xl px-4 py-2 ${
          isUser
            ? 'bg-blue-600 text-white'
            : 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white'
        }`}
      >
        <p className="text-sm">{message.content}</p>
        <span className="text-xs opacity-70 mt-1 block">
          {new Date(message.timestamp).toLocaleTimeString()}
        </span>
      </div>
    </div>
  );
}
```

### frontend/src/components/Sidebar.tsx
```
import React, { useState, useEffect } from 'react';
import { MessageSquare, Settings, Star, Sun, Moon, List, ChevronDown, ChevronUp, Check, Save, User, Plus } from 'lucide-react';
import type { Conversation, Prompt } from '../types';
import { fetchPrompts, saveSelectedPrompts, createNewChat } from '../api/endpoints';

interface SidebarProps {
  conversations: Conversation[];
  isDarkMode: boolean;
  onToggleDarkMode: () => void;
  onNewChat?: (conversation: Conversation) => void;
  onToggleFavorite: (conversationId: string) => void;
  showFavoritesOnly: boolean;
  onToggleShowFavorites: () => void;
}

export function Sidebar({ 
  conversations, 
  isDarkMode, 
  onToggleDarkMode, 
  onNewChat,
  onToggleFavorite,
  showFavoritesOnly,
  onToggleShowFavorites
}: SidebarProps) {
  const [isPromptsOpen, setIsPromptsOpen] = useState(false);
  const [isPersonaOpen, setIsPersonaOpen] = useState(false);
  const [selectedPrompts, setSelectedPrompts] = useState<string[]>([]);
  const [selectedPersona, setSelectedPersona] = useState<string>('');
  const [prompts, setPrompts] = useState<Prompt[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const personas = [
    { id: '1', name: 'Developer' },
    { id: '2', name: 'Writer' },
    { id: '3', name: 'Analyst' },
    { id: '4', name: 'Teacher' },
  ];

  useEffect(() => {
    if (isPromptsOpen) {
      loadPrompts();
    }
  }, [isPromptsOpen]);

  const loadPrompts = async () => {
    try {
      setIsLoading(true);
      const response = await fetchPrompts();
      if (response.success) {
        setPrompts(response.data);
      } else {
        console.error('Failed to load prompts:', response.error);
      }
    } catch (error) {
      console.error('Error loading prompts:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleNewChat = async () => {
    try {
      setIsLoading(true);
      const response = await createNewChat();
      if (response.success && onNewChat) {
        onNewChat(response.data);
      } else {
        console.error('Failed to create new chat:', response.error);
      }
    } catch (error) {
      console.error('Error creating new chat:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handlePromptSelect = (promptId: string) => {
    setSelectedPrompts(prev => 
      prev.includes(promptId)
        ? prev.filter(id => id !== promptId)
        : [...prev, promptId]
    );
  };

  const handlePersonaSelect = (personaId: string) => {
    setSelectedPersona(personaId);
    handleSavePersona(personaId);
  };

  const handleSavePrompts = async () => {
    if (selectedPrompts.length > 0) {
      try {
        setIsLoading(true);
        const selectedPromptObjects = prompts.filter(prompt => selectedPrompts.includes(prompt.id));
        const response = await saveSelectedPrompts(selectedPromptObjects);
        if (response.success) {
          setIsPromptsOpen(false);
          setSelectedPrompts([]);
        } else {
          console.error('Failed to save prompts:', response.error);
        }
      } catch (error) {
        console.error('Error saving prompts:', error);
      } finally {
        setIsLoading(false);
      }
    }
  };

  const handleSavePersona = async (personaId: string) => {
    try {
      console.log('Selected persona:', personaId);
      setIsPersonaOpen(false);
    } catch (error) {
      console.error('Error saving persona:', error);
    }
  };

  return (
    <div className="w-64 h-screen bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-700 flex flex-col">
      <div className="p-4 border-b border-gray-200 dark:border-gray-700">
        <h1 className="text-xl font-semibold text-gray-800 dark:text-white">Conversations</h1>
      </div>
      
      <button
        onClick={handleNewChat}
        disabled={isLoading}
        className="mx-4 mt-4 p-2 flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <Plus className="w-5 h-5" />
        <span>New Chat</span>
      </button>
      
      <div className="flex-1 overflow-y-auto">
        {conversations.map((conversation) => (
          <div
            key={conversation.id}
            className="p-4 hover:bg-gray-100 dark:hover:bg-gray-800 cursor-pointer group"
          >
            <div className="flex items-center gap-3">
              <MessageSquare className="w-5 h-5 text-gray-500 dark:text-gray-400" />
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-gray-900 dark:text-white truncate">
                  {conversation.title}
                </p>
                <p className="text-sm text-gray-500 dark:text-gray-400 truncate">
                  {conversation.lastMessage}
                </p>
              </div>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  onToggleFavorite(conversation.id);
                }}
                className="opacity-0 group-hover:opacity-100 transition-opacity"
              >
                <Star
                  className={`w-5 h-5 ${
                    conversation.isFavorite
                      ? 'text-yellow-500 fill-yellow-500'
                      : 'text-gray-500 dark:text-gray-400'
                  }`}
                />
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="p-4 border-t border-gray-200 dark:border-gray-700">
        <button
          onClick={onToggleDarkMode}
          className="w-full flex items-center gap-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800"
        >
          {isDarkMode ? (
            <Sun className="w-5 h-5 text-gray-500 dark:text-gray-400" />
          ) : (
            <Moon className="w-5 h-5 text-gray-500 dark:text-gray-400" />
          )}
          <span className="text-sm text-gray-700 dark:text-gray-300">
            {isDarkMode ? 'Light Mode' : 'Dark Mode'}
          </span>
        </button>
        
        <button 
          onClick={onToggleShowFavorites}
          className={`w-full flex items-center gap-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 mt-2 ${
            showFavoritesOnly ? 'bg-gray-100 dark:bg-gray-800' : ''
          }`}
        >
          <Star className={`w-5 h-5 ${showFavoritesOnly ? 'text-yellow-500' : 'text-gray-500 dark:text-gray-400'}`} />
          <span className="text-sm text-gray-700 dark:text-gray-300">Favorites</span>
        </button>

        <div className="relative">
          <button 
            onClick={() => setIsPromptsOpen(!isPromptsOpen)}
            className="w-full flex items-center justify-between gap-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 mt-2"
          >
            <div className="flex items-center gap-2">
              <List className="w-5 h-5 text-gray-500 dark:text-gray-400" />
              <span className="text-sm text-gray-700 dark:text-gray-300">Prompts</span>
            </div>
            {isPromptsOpen ? (
              <ChevronUp className="w-4 h-4 text-gray-500 dark:text-gray-400" />
            ) : (
              <ChevronDown className="w-4 h-4 text-gray-500 dark:text-gray-400" />
            )}
          </button>

          {isPromptsOpen && (
            <div className="absolute bottom-full left-0 w-full bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 mb-1 max-h-[60vh] overflow-y-auto">
              {isLoading ? (
                <div className="p-4 text-center text-gray-500 dark:text-gray-400">
                  Loading prompts...
                </div>
              ) : (
                <>
                  {prompts.map((prompt) => (
                    <button
                      key={prompt.id}
                      type="button" 
                      onClick={() => handlePromptSelect(prompt.id)}
                      className="w-full text-left px-4 py-3 text-sm hover:bg-gray-100 dark:hover:bg-gray-700 first:rounded-t-lg last:rounded-b-lg flex items-start justify-between border-b border-gray-200 dark:border-gray-700 last:border-0"
                    >
                      <div className="flex-1 pr-4">
                        <div className="flex items-center justify-between">
                          <span className="font-medium text-gray-900 dark:text-white">
                            {prompt.title}
                          </span>
                          {selectedPrompts.includes(prompt.id) && (
                            <Check className="w-4 h-4 text-blue-500 ml-2 flex-shrink-0" />
                          )}
                        </div>
                        {prompt.description && (
                          <p className="text-gray-500 dark:text-gray-400 mt-1 text-xs line-clamp-2">
                            {prompt.description}
                          </p>
                        )}
                      </div>
                    </button>
                  ))}
                  <div className="border-t border-gray-200 dark:border-gray-700 p-2 sticky bottom-0 bg-white dark:bg-gray-800">
                    <button
                      onClick={handleSavePrompts}
                      disabled={selectedPrompts.length === 0 || isLoading}
                      className={`w-full flex items-center justify-center gap-2 p-2 rounded-lg ${
                        selectedPrompts.length > 0 && !isLoading
                          ? 'bg-blue-500 hover:bg-blue-600 text-white'
                          : 'bg-gray-200 dark:bg-gray-700 text-gray-500 dark:text-gray-400 cursor-not-allowed'
                      } transition-colors duration-200`}
                    >
                      <Save className="w-4 h-4" />
                      <span className="text-sm">
                        {isLoading ? 'Saving...' : `Save Selected (${selectedPrompts.length})`}
                      </span>
                    </button>
                  </div>
                </>
              )}
            </div>
          )}
        </div>

        <div className="relative">
          <button 
            onClick={() => setIsPersonaOpen(!isPersonaOpen)}
            className="w-full flex items-center justify-between gap-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 mt-2"
          >
            <div className="flex items-center gap-2">
              <User className="w-5 h-5 text-gray-500 dark:text-gray-400" />
              <span className="text-sm text-gray-700 dark:text-gray-300">
                Persona
                {selectedPersona && ` (${personas.find(p => p.id === selectedPersona)?.name})`}
              </span>
            </div>
            {isPersonaOpen ? (
              <ChevronUp className="w-4 h-4 text-gray-500 dark:text-gray-400" />
            ) : (
              <ChevronDown className="w-4 h-4 text-gray-500 dark:text-gray-400" />
            )}
          </button>

          {isPersonaOpen && (
            <div className="absolute bottom-full left-0 w-full bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 mb-1">
              {personas.map((persona) => (
                <button
                  key={persona.id}
                  onClick={() => handlePersonaSelect(persona.id)}
                  className="w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 first:rounded-t-lg last:rounded-b-lg flex items-center justify-between"
                >
                  <span>{persona.name}</span>
                  {selectedPersona === persona.id && (
                    <Check className="w-4 h-4 text-blue-500" />
                  )}
                </button>
              ))}
            </div>
          )}
        </div>
        
        <button className="w-full flex items-center gap-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 mt-2">
          <Settings className="w-5 h-5 text-gray-500 dark:text-gray-400" />
          <span className="text-sm text-gray-700 dark:text-gray-300">Settings</span>
        </button>
      </div>
    </div>
  );
}
```

### frontend/src/App.tsx
```
import React, { useState } from 'react';
import { Sidebar } from './components/Sidebar';
import { ChatMessage } from './components/ChatMessage';
import { ChatInput } from './components/ChatInput';
import { Activity } from 'lucide-react';
import type { Message, Conversation } from './types';
import { toggleFavorite } from './api/endpoints';

const initialConversations: Conversation[] = [
  {
    id: '1',
    title: 'Project Discussion',
    lastMessage: 'Let\'s review the requirements',
    timestamp: new Date(),
    isFavorite: false,
  },
  {
    id: '2',
    title: 'Technical Support',
    lastMessage: 'How can I help you today?',
    timestamp: new Date(),
    isFavorite: false,
  },
];

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [conversations, setConversations] = useState<Conversation[]>(initialConversations);
  const [currentConversationId, setCurrentConversationId] = useState<string | null>(null);
  const [showFavoritesOnly, setShowFavoritesOnly] = useState(false);

  const handleSendMessage = (content: string) => {
    if (!currentConversationId) return;

    const newMessage: Message = {
      id: Date.now().toString(),
      content,
      sender: 'user',
      timestamp: new Date(),
    };
    
    setMessages([...messages, newMessage]);
    
    // Update last message in conversation
    setConversations(prevConversations =>
      prevConversations.map(conv =>
        conv.id === currentConversationId
          ? { ...conv, lastMessage: content, timestamp: new Date() }
          : conv
      )
    );
  };

  const handleNewChat = (conversation: Conversation) => {
    setConversations(prev => [conversation, ...prev]);
    setCurrentConversationId(conversation.id);
    setMessages([]);
  };

  const handleToggleFavorite = async (conversationId: string) => {
    const conversation = conversations.find(c => c.id === conversationId);
    if (!conversation) return;

    const newIsFavorite = !conversation.isFavorite;
    
    try {
      const response = await toggleFavorite(conversationId, newIsFavorite);
      if (response.success) {
        setConversations(prevConversations =>
          prevConversations.map(conv =>
            conv.id === conversationId
              ? { ...conv, isFavorite: newIsFavorite }
              : conv
          )
        );
      }
    } catch (error) {
      console.error('Error toggling favorite:', error);
    }
  };

  const handleSelectConversation = (conversationId: string) => {
    setCurrentConversationId(conversationId);
    setMessages([]); // Clear messages when switching conversations
  };

  const filteredConversations = showFavoritesOnly
    ? conversations.filter(conv => conv.isFavorite)
    : conversations;

  return (
    <div className={isDarkMode ? 'dark' : ''}>
      <div className="flex h-screen bg-gray-50 dark:bg-gray-900">
        <Sidebar
          conversations={filteredConversations}
          isDarkMode={isDarkMode}
          onToggleDarkMode={() => setIsDarkMode(!isDarkMode)}
          onNewChat={handleNewChat}
          onToggleFavorite={handleToggleFavorite}
          showFavoritesOnly={showFavoritesOnly}
          onToggleShowFavorites={() => setShowFavoritesOnly(!showFavoritesOnly)}
        />
        
        <main className="flex-1 flex flex-col">
          <div className="p-4 border-b border-gray-200 dark:border-gray-700 flex items-center justify-between">
            <h1 className="text-xl font-semibold text-gray-800 dark:text-white">Chat</h1>
            <div className="flex items-center gap-2">
              <Activity className="w-4 h-4 text-green-500 animate-pulse" />
              <span className="text-sm text-gray-500 dark:text-gray-400">Online</span>
            </div>
          </div>
          
          <div className="flex-1 overflow-y-auto p-4">
            {messages.map((message) => (
              <ChatMessage key={message.id} message={message} />
            ))}
          </div>
          
          <ChatInput 
            onSendMessage={handleSendMessage} 
            conversationId={currentConversationId || ''}
          />
        </main>
      </div>
    </div>
  );
}

export default App;
```

### frontend/src/index.css
```
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply antialiased;
  }
}

/* Smooth scrolling */
* {
  scroll-behavior: smooth;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  @apply bg-transparent;
}

::-webkit-scrollbar-thumb {
  @apply bg-gray-400 dark:bg-gray-600 rounded-full;
}

/* Transitions */
.dark {
  color-scheme: dark;
}
```

### frontend/src/main.tsx
```
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.tsx';
import './index.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

### frontend/src/types.ts
```
export interface Message {
  id: string;
  content: string;
  sender: 'user' | 'ai';
  timestamp: Date;
}

export interface Conversation {
  id: string;
  title: string;
  lastMessage: string;
  timestamp: Date;
  isFavorite?: boolean;
}

export interface PromptVariable {
  name: string;
  title: string;
}

export interface Prompt {
  id: string;
  title: string;
  description: string;
  prompt: string;
  visibleTo: string;
  visibleToGroups: string[];
  categories: string[];
  ownerId: string;
  variables: PromptVariable[];
  createdAt: string;
}

// API response types
export interface ApiResponse<T> {
  success: boolean;
  data: T;
  error?: string;
}
```

### frontend/src/vite-env.d.ts
```
/// <reference types="vite/client" />
```

### frontend/eslint.config.js
```
import js from '@eslint/js';
import globals from 'globals';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
    },
  }
);
```

### frontend/favicon.ico (binary)

### frontend/index.html
```
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

### frontend/package.json
```
{
  "name": "vite-react-typescript-starter",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "lucide-react": "^0.344.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.9.1",
    "@types/react": "^18.3.5",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "autoprefixer": "^10.4.18",
    "eslint": "^9.9.1",
    "eslint-plugin-react-hooks": "^5.1.0-rc.0",
    "eslint-plugin-react-refresh": "^0.4.11",
    "globals": "^15.9.0",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "typescript": "^5.5.3",
    "typescript-eslint": "^8.3.0",
    "vite": "^5.4.2"
  }
}
```

### frontend/postcss.config.js
```
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

### frontend/tailwind.config.js
```
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.2s ease-in-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};
```

### frontend/tsconfig.app.json
```
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"]
}
```

### frontend/tsconfig.json
```
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
```

### frontend/tsconfig.node.json
```
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2023"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["vite.config.ts"]
}
```

### frontend/vite.config.ts
```
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    exclude: ['lucide-react'],
  },
});
```

### .env.local
```
# Environment variables for local development
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
EXTERNAL_API_TOKEN=eyJhbGciOiJSUzI1NiIsImtpZCI6IkM3Q3V4MXM4V0dfYWNRZE5VLWh3bG1YNGtTV1c5Uzl3dV9oaHVIZVA2TlEiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJmZGUwYzc5Yi1lZjA5LTQ1MGYtYTUwOS0zZDAzMmNlMjFlODUiLCJpc3MiOiJodHRwczovL2NpdGZsb3dkZXZiMmMuYjJjbG9naW4uY29tL2QxZGVhMWU1LThhZWItNDE3ZS1hMWIyLWQ4NDAyZmNmNGE4Zi92Mi4wLyIsImV4cCI6MTczODg4MTk1NCwibmJmIjoxNzM4Nzk1NTU0LCJzdWIiOiIwYzEwMDhhMi01YTIyLTRkODgtYTZlMS1hOGUxYmY0YzEwOGYiLCJlbWFpbCI6ImFyeXNhbmNoZXpAY2lhbmR0LmNvbSIsImdpdmVuX25hbWUiOiJBcnkiLCJmYW1pbHlfbmFtZSI6IkhlbnJpcXVlIGRhIEx1eiBTYW5jaGV6IiwibmFtZSI6IkFyeSBIZW5yaXF1ZSBkYSBMdXogU2FuY2hleiIsImlkcCI6Imdvb2dsZS5jb20iLCJjaGFubmVsIjoicG9ydGFsIiwidGVuYW50IjoiY2l0LWRldiIsInJvbGVzIjoiZmxvd2NvcmUudXNlcixiYWNrbG9ncmVmaW5lci51c2VyLGNoYXR3aXRoZG9jcy51c2VyLGdhbGF4eW9wcy51c2VyIiwidGlkIjoiZDFkZWExZTUtOGFlYi00MTdlLWExYjItZDg0MDJmY2Y0YThmIiwiYXpwIjoiZmRlMGM3OWItZWYwOS00NTBmLWE1MDktM2QwMzJjZTIxZTg1IiwidmVyIjoiMS4wIiwiaWF0IjoxNzM4Nzk1NTU0fQ.REOeDg3AGv4RVDDQ_Kv7WSP1c_0Gbyk4RHiZQwlfppQ59AKbUGQR3vYMACsGzyj0Vp4QNKcDCWpVNGQ8AevG9mHYfjtcNTlqvXqyWyNQ6yYHJxxykbOsIZJsLJ-JI95Mu9GmKpHDMaKKTpkJQ9sX_CZlxrA2OJbklCNtENY5B3jDoYetF_VLByI1zNawG-ij_cOPADAvXndfNzflgcO1t0qukOflV09NS1FnO7ogkUHFpfRy3Ly3sS5f1FFHBVBGiqduDoWEBOLzZdqMHBxL_bYVaFlO1gTyrDLzzn2MsY8gcpOs-CxhJlVPOj1QLeqnXhlLsclyz5HRUnYKsmb8Ew
EXTERNAL_API_URL=https://dev.flow.ciandt.com/
```

### README.md
```
# Project Name

This project is a web application that includes both a backend and a frontend. The backend is built with FastAPI, and the frontend is built with React.

## Backend Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/project-name.git
   cd project-name
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:

   Create a `.env.local` file in the root directory and add the following environment variables:

   ```env
   DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=your_secret_key
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   EXTERNAL_API_URL=https://dev.flow.ciandt.com/channels-service/v1
   EXTERNAL_API_TOKEN=your_external_api_token
   ```

### Running the Server

1. Navigate to the backend directory:

   ```bash
   cd backend/app
   ```

2. Start the FastAPI server using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   The `--reload` flag will auto-reload the server on code changes. The server will be running at `http://localhost:8000`.

### API Documentation

Once the server is running, you can access the API documentation at `http://localhost:8000/docs` for the interactive Swagger UI or `http://localhost:8000/redoc` for ReDoc.

## Frontend Setup

Refer to the frontend README for instructions on setting up and running the frontend.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

# Instructions

No need to analyze anything right now. 
Just wait for questions.
