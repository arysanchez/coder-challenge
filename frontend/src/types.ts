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